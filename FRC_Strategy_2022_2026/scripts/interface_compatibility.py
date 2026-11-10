"""Conservative interface screening, never a certification of mechanical fit."""
FIELDS = ['orientation','direction','entry_exit_height','effective_feed_width','velocity',
          'compression','ownership_readiness','occupied_swept_space','structural_loads',
          'electrical_simultaneity','jam_recovery_service']

def compare(producer, consumer, enforce_1833=True):
    conflicts, unresolved = [], []
    if producer['role'] != 'output' or consumer['role'] != 'input':
        conflicts.append('Compare a producer output to a consumer input, in that order.')
    a,b=producer['piece'],consumer['piece']
    if a['state']=='supported' and b['state']=='supported':
        if a['value'] != b['value']:conflicts.append('Different game-piece definitions; cross-game geometry/material transfer is unvalidated.')
    else:unresolved.append('Piece identity is not established at both ports.')
    if enforce_1833:
        for p in [producer,consumer]:
            if p.get('requires_turret'):conflicts.append(p['id']+': historical yaw turret violates 1833 policy; fixed outlet redesign required.')
            if p.get('requires_pneumatics'):conflicts.append(p['id']+': pneumatic actuation violates 1833 policy; electric/passive redesign required.')
    details=[]
    for k in FIELDS:
        x,y=producer[k],consumer[k]
        # Identical words do not establish common datums, clearances, load cases,
        # electrical duty, or signal semantics. Never turn string equality into fit.
        unresolved.append(k+': '+x['state']+' output / '+y['state']+' input; review both source conditions and transform into a common datum.')
        details.append(dict(field=k,producer=x,consumer=y))
    return dict(status='incompatible_as_documented' if conflicts else 'unresolved',
                compatible=False,producer=producer['id'],consumer=consumer['id'],
                conflicts=conflicts,unresolved=unresolved,fields=details,
                boundary='Screening only. Shared piece type, matching words and nominal dimensions never establish compatible contacts, loading, controls or service access.')
