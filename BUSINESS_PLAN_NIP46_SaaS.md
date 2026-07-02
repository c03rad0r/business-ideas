# Business Plan: NIP-46 Signer/Bunker SaaS

## Executive Summary
Hosted Nostr signer (bunker) service using the nosigner.py code already built. Users delegate signing without exposing their nsec. SaaS model with Bitcoin/Cashu payments.

## Product
- Hosted NIP-46 bunker (remote signer)
- User keeps a "viewer" key (npub), delegates signing to the bunker
- Bunker signs events on user's behalf with permission policies
- Permission tiers: read-only, post-only, full signing (user configures)
- Backup/restore of encrypted key material
- Multi-device support (same bunker, multiple clients)

## Financial Model
| Metric | Value |
|--------|-------|
| VPS cost (shared with relay) | €0-7/month |
| Marginal cost per user | ~€0.02/month (storage + compute) |
| Tier 1 (Free): 100 signs/month | €0 |
| Tier 2 (Basic): unlimited signs, 1 bunker | 2100 sats/month (~€5) |
| Tier 3 (Pro): multiple bunkers, custom policies, API access | 5250 sats/month (~€12.50) |
| Target: 50 Tier 2 + 10 Tier 3 (month 6) | €375/month |
| Target: 200 Tier 2 + 30 Tier 3 (year 1) | €1,375/month |
| Gross margin | 90%+ |

## Technical Stack
- nosigner.py (ALREADY BUILT — NIP-44 encryption, WebSocket relay pool, SQLite)
- nosigner_mcp.py (MCP wrapper — ALREADY BUILT)
- Cashu payment integration for subscriptions
- Web dashboard (simple — manage bunkers, view usage)
- Encrypted backup system (AES-256-GCM)

## Competitive Advantage
- Code already written and tested
- Only known NIP-46 bunker with Cashu payment integration
- Runs on existing VPS infrastructure
- Nostr-native (no custodial key risk if implemented correctly)
- Can bundle with paid relay subscription

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Key compromise (custodial risk) | Low | Critical | Hardware-backed keys, user-encrypted backup, audit trail |
| Low demand for hosted signer | Medium | High | Bundle with relay, target Nostr power users |
| Competition (nsec.app, Amber) | Medium | Medium | Differentiate with Cashu + self-host option |
| Trust barrier (users won't share keys) | High | High | Zero-knowledge design, open source the bunker code |
| Regulatory (key custody = financial service?) | Low | High | Non-custodial architecture, user controls recovery |

## Launch Plan
1. Week 1: Deploy nosigner.py on VPS, add Cashu payment gate
2. Week 2: Create simple landing page + documentation
3. Week 3: Beta test with 5 trusted Nostr users
4. Week 4: Public launch on Nostr, offer 1-month free Tier 2
5. Month 2-3: Iterate based on feedback, add Tier 3 features
6. Month 6: Evaluate MRR, decide on scaling

## Viability Score: 7/10
- Highest margin (90%+), code already written
- Main barrier: trust (users must trust you with signing delegation)
- Differentiator: only Cashu-paid NIP-46 bunker in ecosystem
- Best as a bundle with paid relay (relay + signer combo)
