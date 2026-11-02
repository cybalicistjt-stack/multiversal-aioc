export type CampaignRole = "owner" | "gm" | "player" | "observer";
export type CampaignAction =
  | "campaign.read"
  | "campaign.manage"
  | "member.read"
  | "member.manage"
  | "session.read"
  | "session.command"
  | "session.manage"
  | "private-gm.read";

export interface CampaignMembership {
  readonly campaignId: string;
  readonly subjectId: string;
  readonly role: CampaignRole;
}

export interface CampaignResourceContext {
  readonly campaignId: string;
  readonly ownerSubjectId: string;
}

export interface AuthorizationRequest {
  readonly subjectId: string;
  readonly action: CampaignAction;
  readonly resource: CampaignResourceContext;
  readonly membership?: CampaignMembership;
}

export type AuthorizationReason =
  | "campaign-owner"
  | "role-allowed"
  | "not-a-member"
  | "campaign-mismatch"
  | "role-denied"
  | "invalid-membership";

export interface AuthorizationDecision {
  readonly allowed: boolean;
  readonly reason: AuthorizationReason;
  readonly effectiveRole?: CampaignRole;
}

const ROLE_ACTIONS: Readonly<Record<CampaignRole, ReadonlySet<CampaignAction>>> = {
  owner: new Set([
    "campaign.read",
    "campaign.manage",
    "member.read",
    "member.manage",
    "session.read",
    "session.command",
    "session.manage",
    "private-gm.read",
  ]),
  gm: new Set([
    "campaign.read",
    "member.read",
    "member.manage",
    "session.read",
    "session.command",
    "session.manage",
    "private-gm.read",
  ]),
  player: new Set([
    "campaign.read",
    "member.read",
    "session.read",
    "session.command",
  ]),
  observer: new Set([
    "campaign.read",
    "member.read",
    "session.read",
  ]),
};

/**
 * Provider-neutral campaign authorization policy.
 *
 * Canonical subject identity is the only actor identifier. Access is bounded
 * to the resource campaign and an explicit campaign membership role. No
 * external identity-provider claims or SDK types are accepted here.
 */
export function authorizeCampaignRequest(request: AuthorizationRequest): AuthorizationDecision {
  const { subjectId, action, resource, membership } = request;

  if (subjectId === resource.ownerSubjectId) {
    return { allowed: true, reason: "campaign-owner", effectiveRole: "owner" };
  }

  if (!membership) {
    return { allowed: false, reason: "not-a-member" };
  }

  if (membership.subjectId !== subjectId) {
    return { allowed: false, reason: "invalid-membership" };
  }

  if (membership.campaignId !== resource.campaignId) {
    return { allowed: false, reason: "campaign-mismatch" };
  }

  const allowed = ROLE_ACTIONS[membership.role].has(action);
  return {
    allowed,
    reason: allowed ? "role-allowed" : "role-denied",
    effectiveRole: membership.role,
  };
}
