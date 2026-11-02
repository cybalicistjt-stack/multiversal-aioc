import { authorizeCampaignRequest, type CampaignMembership } from "../authorization/campaign-authorization-policy";
import type { CommandReceipt, SessionCommand, SessionEvent } from "../realtime-session";

export interface AuthoritativeSessionState {
  readonly sessionId: string;
  readonly campaignId: string;
  readonly campaignOwnerSubjectId: string;
  readonly revision: number;
  readonly lastSequence: number;
  readonly processedCommandIds: readonly string[];
}

export interface AuthoritativeCommandContext {
  readonly membership?: CampaignMembership;
  readonly existingReceipt?: CommandReceipt;
}

export type AuthoritativeCommandRejectionReason =
  | "wrong-session"
  | "unauthorized"
  | "duplicate-without-receipt"
  | "stale-revision"
  | "invalid-command";

export type AuthoritativeCommandDecision =
  | {
      readonly accepted: true;
      readonly receipt: CommandReceipt;
      readonly nextState: AuthoritativeSessionState;
      readonly events: readonly SessionEvent[];
      readonly replayed: boolean;
    }
  | {
      readonly accepted: false;
      readonly reason: AuthoritativeCommandRejectionReason;
      readonly resultingRevision: number;
    };

const validCommand = (command: SessionCommand) =>
  command.commandId.length > 0 &&
  command.sessionId.length > 0 &&
  command.actorId.length > 0 &&
  command.type.length > 0 &&
  Number.isInteger(command.expectedRevision) &&
  command.expectedRevision >= 0;

/**
 * Deterministic provider-neutral server-authority boundary.
 *
 * This function does not trust client-side revision, campaign role, replay, or
 * event sequence assertions. A command is accepted only after campaign
 * authorization, idempotency, and exact revision checks pass against the
 * authoritative state supplied by the server-side caller.
 */
export function handleAuthoritativeSessionCommand(
  state: AuthoritativeSessionState,
  command: SessionCommand,
  context: AuthoritativeCommandContext,
): AuthoritativeCommandDecision {
  if (!validCommand(command)) {
    return { accepted: false, reason: "invalid-command", resultingRevision: state.revision };
  }

  if (command.sessionId !== state.sessionId) {
    return { accepted: false, reason: "wrong-session", resultingRevision: state.revision };
  }

  const processed = state.processedCommandIds.includes(command.commandId);
  if (processed) {
    if (!context.existingReceipt) {
      return {
        accepted: false,
        reason: "duplicate-without-receipt",
        resultingRevision: state.revision,
      };
    }
    return {
      accepted: true,
      receipt: context.existingReceipt,
      nextState: state,
      events: [],
      replayed: true,
    };
  }

  const authorization = authorizeCampaignRequest({
    subjectId: command.actorId,
    action: "session.command",
    resource: {
      campaignId: state.campaignId,
      ownerSubjectId: state.campaignOwnerSubjectId,
    },
    membership: context.membership,
  });
  if (!authorization.allowed) {
    return { accepted: false, reason: "unauthorized", resultingRevision: state.revision };
  }

  if (command.expectedRevision !== state.revision) {
    return { accepted: false, reason: "stale-revision", resultingRevision: state.revision };
  }

  const nextRevision = state.revision + 1;
  const nextSequence = state.lastSequence + 1;
  const eventId = `evt:${state.sessionId}:${nextSequence}:${command.commandId}`;
  const event: SessionEvent = {
    eventId,
    sessionId: state.sessionId,
    sequence: nextSequence,
    revision: nextRevision,
    type: `command.accepted:${command.type}`,
    payload: {
      commandId: command.commandId,
      actorId: command.actorId,
      commandType: command.type,
      commandPayload: command.payload,
    },
    visibility: { kind: "public" },
    occurredAt: command.submittedAt,
  };
  const receipt: CommandReceipt = {
    commandId: command.commandId,
    accepted: true,
    resultingRevision: nextRevision,
    emittedEventIds: [eventId],
  };
  return {
    accepted: true,
    receipt,
    events: [event],
    replayed: false,
    nextState: {
      ...state,
      revision: nextRevision,
      lastSequence: nextSequence,
      processedCommandIds: [...state.processedCommandIds, command.commandId],
    },
  };
}

/**
 * A9 wrapper over the generic Session command seam.
 *
 * The generic handler remains authoritative and may retain an internal accepted
 * command payload for lower-level composition. A9 surfaces must never forward
 * that raw payload into role-safe Investigation/Social projections, search,
 * exports, diagnostics, notifications, or optional AI context.
 */
export interface A9AcceptedCommandProjection {
  readonly commandId: string;
  readonly resultingRevision: number;
  readonly replayed: boolean;
  readonly events: readonly {
    readonly eventId: string;
    readonly sessionId: string;
    readonly sequence: number;
    readonly revision: number;
    readonly type: string;
    readonly occurredAt: string;
  }[];
  readonly rawCommandPayload?: never;
}

export function projectAcceptedSessionCommandForA9(
  decision: AuthoritativeCommandDecision,
): A9AcceptedCommandProjection | undefined {
  if (!decision.accepted) return undefined;
  return {
    commandId: decision.receipt.commandId,
    resultingRevision: decision.receipt.resultingRevision,
    replayed: decision.replayed,
    events: decision.events.map((event) => ({
      eventId: event.eventId,
      sessionId: event.sessionId,
      sequence: event.sequence,
      revision: event.revision,
      type: event.type,
      occurredAt: event.occurredAt,
    })),
  };
}
