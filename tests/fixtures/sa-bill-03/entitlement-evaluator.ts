export type EntitlementSource =
  | "free"
  | "subscription"
  | "sponsored-month"
  | "campaign-premium-grant";

export type EntitlementCapability =
  | "official-content"
  | "subscriber-ability-tiers"
  | "campaign-premium-content";

export interface SubscriptionRecord {
  readonly subscriptionId: string;
  readonly subjectId: string;
  readonly status: "active" | "cancelled" | "expired";
  readonly startsAt: string;
  readonly endsAt?: string;
}

export interface SponsoredMonthRecord {
  readonly sponsoredMonthId: string;
  readonly campaignId: string;
  readonly subjectId: string;
  readonly status: "active" | "cancelled" | "expired";
  readonly grantedAt: string;
  readonly expiresAt: string;
}

export interface CampaignPremiumGrantRecord {
  readonly grantId: string;
  readonly campaignId: string;
  readonly subjectId: string;
  readonly startsAt: string;
  readonly endsAt?: string;
  readonly revokedAt?: string;
}

export interface EntitlementEvaluationInput {
  readonly subjectId: string;
  readonly campaignId?: string;
  readonly evaluatedAt: string;
  readonly subscriptions: readonly SubscriptionRecord[];
  readonly sponsoredMonths: readonly SponsoredMonthRecord[];
  readonly campaignGrants: readonly CampaignPremiumGrantRecord[];
}

export interface EvaluatedEntitlement {
  readonly subjectId: string;
  readonly tier: "free" | "subscriber";
  readonly sources: readonly EntitlementSource[];
  readonly capabilities: readonly EntitlementCapability[];
  readonly abilityTreeTierCap: 2 | null;
  readonly activeRecordIds: readonly string[];
  readonly nextChangeAt?: string;
}

const activeWindow = (startsAt: string, endsAt: string | undefined, at: string) =>
  startsAt <= at && (endsAt === undefined || at < endsAt);

export function evaluateEntitlements(input: EntitlementEvaluationInput): EvaluatedEntitlement {
  const activeSubscriptions = input.subscriptions.filter(
    (record) =>
      record.subjectId === input.subjectId &&
      record.status === "active" &&
      activeWindow(record.startsAt, record.endsAt, input.evaluatedAt),
  );

  const activeSponsoredMonths = input.sponsoredMonths.filter(
    (record) =>
      record.subjectId === input.subjectId &&
      record.status === "active" &&
      record.grantedAt <= input.evaluatedAt &&
      input.evaluatedAt < record.expiresAt &&
      (input.campaignId === undefined || record.campaignId === input.campaignId),
  );

  const activeCampaignGrants = input.campaignGrants.filter(
    (record) =>
      record.subjectId === input.subjectId &&
      record.revokedAt === undefined &&
      activeWindow(record.startsAt, record.endsAt, input.evaluatedAt) &&
      input.campaignId !== undefined &&
      record.campaignId === input.campaignId,
  );

  const subscriber = activeSubscriptions.length > 0 || activeSponsoredMonths.length > 0;
  const sources: EntitlementSource[] = ["free"];
  if (activeSubscriptions.length > 0) sources.push("subscription");
  if (activeSponsoredMonths.length > 0) sources.push("sponsored-month");
  if (activeCampaignGrants.length > 0) sources.push("campaign-premium-grant");

  const capabilities: EntitlementCapability[] = ["official-content"];
  if (subscriber) capabilities.push("subscriber-ability-tiers");
  if (activeSponsoredMonths.length > 0 || activeCampaignGrants.length > 0) {
    capabilities.push("campaign-premium-content");
  }

  const activeRecordIds = [
    ...activeSubscriptions.map((record) => record.subscriptionId),
    ...activeSponsoredMonths.map((record) => record.sponsoredMonthId),
    ...activeCampaignGrants.map((record) => record.grantId),
  ].sort();

  const futureChanges = [
    ...activeSubscriptions.flatMap((record) => (record.endsAt ? [record.endsAt] : [])),
    ...activeSponsoredMonths.map((record) => record.expiresAt),
    ...activeCampaignGrants.flatMap((record) => (record.endsAt ? [record.endsAt] : [])),
  ].filter((value) => input.evaluatedAt < value).sort();

  return {
    subjectId: input.subjectId,
    tier: subscriber ? "subscriber" : "free",
    sources,
    capabilities,
    abilityTreeTierCap: subscriber ? null : 2,
    activeRecordIds,
    ...(futureChanges[0] ? { nextChangeAt: futureChanges[0] } : {}),
  };
}
