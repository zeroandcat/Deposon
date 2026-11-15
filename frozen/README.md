# Frozen faces

- `p2p_blind_kh_frozen.json` - P2' blind K_h mapping: 32-key subset of the
  128-key space (low half k<64: 13 keys; high half k>=64: 19 keys),
  seed 20261115, frozen at launch.
- `g6f_blind_kh_frozen.json` - G6f supplement frozen face (same blind set,
  same seed; byte-identity is verified in the G6f MANIFEST).

Both files are original frozen artifacts; the blind face is referenced by the
gate arithmetic in `gates/` (composition 13/19 is a load-bearing constant of
the G7' coupling criterion).
