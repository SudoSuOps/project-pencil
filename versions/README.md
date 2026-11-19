# Versions

Snapshots of the skill as it was tested. The current skill is in
`../skill/pencil/`.

| Folder | Role it implemented | Tested in |
|---|---|---|
| `v0.1/` | Transaction examiner for a broker; long decision briefs | CS-001, CS-002 |
| `v0.2/` | Same role; finding first, short answers, no invented inputs | CS-002 |
| `v0.3-reconstructed/` | Neutral validator and ledger, in instructions only | CS-005 |
| `v0.4/` | Neutral validator with the ledger in code, validator, review gate | CS-004, CS-005 |

`v0.3-reconstructed` was rebuilt by reversing the v0.4 edits, because no
snapshot was taken at the time. `v0.1` is the folder as it stood after the
two discovery documents were folded in, which is the state CS-001 tested.
