// MVAC-02 design oracle only. No storage, auth, pack resolution or owner mutation.
export function evaluate(o, overrides={}) {
 const c={actualRevision:o.nativeRevision,objectFound:true,packAvailable:true,actualPackVersion:o.packVersion,representationFound:true,unsupportedFeature:false,ownerResolved:true,requiresDistance:false,actualCoordinateSpace:o.coordinateSpace,finiteCoordinates:true,capabilityState:'allowed',action:'preview',byteState:'byte-present',redistribution:'allowed',audience:'gm',policyReceipt:true,expectedOwnerVersion:1,actualOwnerVersion:1,ownerReceipt:null,...overrides};
 const end=status=>({status,ownerMutationPerformed:false,runtimeAuthorizationProved:false});
 if(c.actualRevision!==o.nativeRevision)return end('stale-document');
 if(!c.objectFound)return end('missing-native-object');
 if(c.unsupportedFeature)return end('incompatible-schema');
 if(!c.packAvailable)return end('missing-pack');
 if(c.actualPackVersion!==o.packVersion)return end('incompatible-pack-version');
 if(!c.representationFound)return end('missing-representation');
 if(c.actualCoordinateSpace!==o.coordinateSpace)return end('incompatible-coordinate-space');
 if(!c.finiteCoordinates)return end('invalid-coordinate');
 if(c.requiresDistance&&!o.physicalCalibration)return end('uncalibrated');
 if(!c.ownerResolved)return end('unresolved-owner');
 if(o.visibility==='gm-only'&&c.audience==='player')return end('excluded-private');
 if(!c.policyReceipt)return end('blocked-policy');
 if(c.capabilityState!=='allowed')return end('blocked-rights');
 if(c.action==='export-original'&&c.redistribution!=='allowed')return end('blocked-redistribution');
 if(c.action==='export-original'&&c.byteState!=='byte-present')return end('missing-bytes');
 if(c.expectedOwnerVersion!==c.actualOwnerVersion)return end('stale-owner');
 if(c.ownerReceipt==='ambiguous')return end('query-operation-status');
 if(c.ownerReceipt==='accepted')return end('reuse-owner-receipt');
 return end('ready');
}
export function mapRights(state){if(state==='allowed')return 'granted';if(state==='denied'||state==='revoked')return 'denied';return 'unknown';}
export function mapCapability(cap){return cap==='redistribute'?'redistribution':cap;}
