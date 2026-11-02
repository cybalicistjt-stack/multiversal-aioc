/**
 * SA-BILL-09 bounded SECURITY RESEARCH PATCH on throwaway copies of pinned
 * actual Multiversal-app source. Not a production patch, deployed mitigation
 * or implicit implementation authority. Every edit has an EXACT anchor;
 * drift fails instead of silently applying a broad or partial transformation.
 */
const replaceOnce=(source,before,after,tag)=>{
 const first=source.indexOf(before);
 if(first<0||source.indexOf(before,first+before.length)>=0)
   throw Error("SA09_ANCHOR_MISMATCH:"+tag);
 return source.slice(0,first)+after+source.slice(first+before.length);
};
export function patchSource(path,raw){
 if(path==="authorization/campaign-authorization-policy.ts")return raw;
 if(path==="session/hidden-information-response-filter.ts"){
   let code=replaceOnce(raw,
     "  readonly hiddenEventCount: number;",
     "  /** Hidden cardinality must never be returned to an ordinary viewer. */\n  readonly hiddenEventCount?: never;",
     "hidden-count-type");
   code=replaceOnce(code,
     "      hiddenEventCount: events.length - visibleEvents.length,\n",
     "",
     "hidden-count-runtime");
   return code;
 }
 if(path==="session/authoritative-session-command-handler.ts"){
   let code=replaceOnce(raw,
     "  readonly existingReceipt?: CommandReceipt;",
     [
       "  readonly existingReceipt?: CommandReceipt;",
       "  /** Trusted persisted original accepted command, NEVER supplied by client. */",
       "  readonly originalAcceptedCommand?: SessionCommand;"
     ].join("\n"),
     "canonical-command-binding");
   const auth=[
     '  const authorization = authorizeCampaignRequest({',
     '    subjectId: command.actorId,',
     '    action: "session.command",',
     '    resource: {',
     '      campaignId: state.campaignId,',
     '      ownerSubjectId: state.campaignOwnerSubjectId,',
     '    },',
     '    membership: context.membership,',
     '  });',
     '  if (!authorization.allowed) {',
     '    return { accepted: false, reason: "unauthorized", resultingRevision: state.revision };',
     '  }',
     '',
     ''
   ].join("\n");
   code=replaceOnce(code,auth,"","remove-late-auth");
   code=replaceOnce(code,
     "  const processed = state.processedCommandIds.includes(command.commandId);",
     auth+"  const processed = state.processedCommandIds.includes(command.commandId);",
     "move-auth-before-replay");
   code=replaceOnce(code,
     "    if (!context.existingReceipt) {",
     [
       "    if (",
       "      !context.existingReceipt ||",
       "      !context.originalAcceptedCommand ||",
       "      context.existingReceipt.commandId !== command.commandId ||",
       "      context.existingReceipt.accepted !== true ||",
       "      context.existingReceipt.resultingRevision > state.revision ||",
       "      // Intentional exact JSON command fidelity, fail closed. Real backend",
       "      // needs canonical persisted request hashes and authenticated owners.",
       "      JSON.stringify(context.originalAcceptedCommand) !== JSON.stringify(command)",
       "    ) {"
     ].join("\n"),
     "replay-evidence-bound");
   code=replaceOnce(code,
     "      commandPayload: command.payload,\n",
     "",
     "public-command-payload");
   return code;
 }
 throw Error("SA09_UNKNOWN_PINNED_FILE:"+path);
}
