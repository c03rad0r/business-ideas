# Business Plan: Paid Nostr Relay Service

## Executive Summary
Operate a premium Nostr relay with paid subscription tiers, leveraging existing VPS infrastructure and Nostr expertise. Revenue from monthly subscriptions + zap-based micropayments.

## Product
- Tier 1 (Free): Read-only access, rate-limited, 7-day event retention
- Tier 2 (Subscriber): Full read/write, 1-year retention, 210 sats/month (~€0.50)
- Tier 3 (Premium): Full read/write, permanent retention, NIP-46 bunker, priority propagation, 2100 sats/month (~€5)
- Tier 4 (Enterprise): Dedicated relay, custom policies, white-label, 21000 sats/month (~€50)

## Financial Model
| Metric | Value |
|--------|-------|
| VPS cost (Hetzner CX32) | €7-13/month |
| Bandwidth (included) | 20TB/month |
| Storage (200GB NVMe) | Included |
| Marginal cost per free user | ~€0.01/month |
| Marginal cost per paid user | ~€0.05/month |
| Revenue per subscriber (Tier 2) | ~€0.50/month |
| Revenue per subscriber (Tier 3) | ~€5/month |
| Target: 100 Tier 2 + 20 Tier 3 | €60/month |
| Target: 500 Tier 2 + 50 Tier 3 | €275/month |
| Target: 2000 Tier 2 + 200 Tier 3 | €1,100/month |
| Gross margin | 85-95% |

## Technical Stack
- strfry relay (already running on VPS) or nostr-rs-relay
- NIP-42 authentication for paid write access
- NIP-46 bunker integration (nosigner.py already built!)
- Payment: Cashu/LNBits for subscription management
- Monitoring: uptime checks, event throughput metrics
- Auto-scaling: add VPS nodes as load increases

## Competitive Advantage
- Already running relay infrastructure (strfry-agg)
- NIP-46 signer code written (nosigner.py)
- Nostr ecosystem knowledge + community presence
- Can bundle with NIP-46 bunker service (differentiator)
- Bitcoin-native payment (no Stripe/PayPal dependency)

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| No one pays for relays | Medium | High | Free tier as funnel, zap micropayments |
| Free tier abuse | High | Medium | Rate limiting, storage quotas |
| VPS costs scale faster than revenue | Medium | Medium | Auto-scale, hard quotas |
| Competition from free relays | High | Medium | Premium features (retention, NIP-46, propagation) |
| Technical complexity | Low | Low | Already running relay infrastructure |

## Launch Plan
1. Week 1: Configure paid relay with NIP-42 auth on existing VPS
2. Week 2: Set up Cashu/LNBits subscription management
3. Week 3: Announce on Nostr, offer free Tier 2 to first 50 users
4. Week 4: Start charging, monitor conversion rate
5. Month 2: Add NIP-46 bunker as Tier 3 differentiator
6. Month 3: Evaluate metrics, adjust pricing

## Viability Score: 7/10
- Very low cost to launch (use existing infra)
- Uncertain willingness-to-pay in Nostr ecosystem
- Best as a bundle with NIP-46 bunker (unique combo)
- Revenue scales slowly but margins are excellent
