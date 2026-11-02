import type { CampaignMembership, CampaignResourceContext } from "../authorization/campaign-authorization-policy";
import { authorizeCampaignRequest } from "../authorization/campaign-authorization-policy";
import type { SessionEvent, SessionResult } from "../realtime-session";

export interface ViewerProjectionContext {
  readonly viewerSubjectId: string;
  readonly sessionId: string;
  readonly campaign: CampaignResourceContext;
  readonly membership?: CampaignMembership;
}

export interface FilteredSessionProjection {
  readonly sessionId: string;
  readonly viewerSubjectId: string;
  readonly visibleEvents: readonly SessionEvent[];
  readonly hiddenEventCount: number;
}

function canViewEvent(
  event: SessionEvent,
  context: ViewerProjectionContext,
  effectiveRole: "owner" | "gm" | "player" | "observer",
): boolean {
  if (event.visibility.kind === "public") return true;
  if (event.visibility.kind === "gm_only") {
    return effectiveRole === "owner" || effectiveRole === "gm";
  }
  return event.visibility.participantIds.includes(context.viewerSubjectId);
}

/**
 * Provider-neutral hidden-information projection boundary.
 *
 * Authorization is evaluated before any event payload is projected. Events
 * from another session are rejected rather than filtered, preventing a caller
 * from using this function to probe cross-session data. GM-only payloads are
 * visible only to campaign owners/GMs. Participant-scoped payloads are visible
 * only to explicitly named canonical subjects. Public events remain visible to
 * any authorized campaign viewer.
 */
export function filterSessionEventsForViewer(
  events: readonly SessionEvent[],
  context: ViewerProjectionContext,
): SessionResult<FilteredSessionProjection> {
  const decision = authorizeCampaignRequest({
    subjectId: context.viewerSubjectId,
    action: "session.read",
    resource: context.campaign,
    membership: context.membership,
  });

  if (!decision.allowed || decision.effectiveRole === undefined) {
    return {
      ok: false,
      error: { code: "unauthorized", message: "viewer is not authorized for this campaign session", retryable: false },
    };
  }

  if (events.some((event) => event.sessionId !== context.sessionId)) {
    return {
      ok: false,
      error: { code: "not_found", message: "event batch contains another session", retryable: false },
    };
  }

  const visibleEvents = events.filter((event) => canViewEvent(event, context, decision.effectiveRole!));

  return {
    ok: true,
    value: {
      sessionId: context.sessionId,
      viewerSubjectId: context.viewerSubjectId,
      visibleEvents,
      hiddenEventCount: events.length - visibleEvents.length,
    },
  };
}

/**
 * A9 wrapper: hidden/missing equivalence is required for protected
 * Investigation and Social state, so A9 never projects hidden-event counts.
 */
export interface A9FilteredSessionProjection {
  readonly sessionId: string;
  readonly viewerSubjectId: string;
  readonly visibleEvents: readonly SessionEvent[];
  readonly hiddenEventCount?: never;
}

export function filterSessionEventsForA9(
  events: readonly SessionEvent[],
  context: ViewerProjectionContext,
): SessionResult<A9FilteredSessionProjection> {
  const result = filterSessionEventsForViewer(events, context);
  if (!result.ok) return result;
  return {
    ok: true,
    value: {
      sessionId: result.value.sessionId,
      viewerSubjectId: result.value.viewerSubjectId,
      visibleEvents: result.value.visibleEvents,
    },
  };
}
