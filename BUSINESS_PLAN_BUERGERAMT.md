# Business Plan: Berlin Bürgeramt Appointment Notification Service

## Executive Summary
Playwright-based monitoring service that watches service.berlin.de for appointment slot openings and notifies subscribers via Signal/Nostr. Users book the appointment themselves (we never touch their data). Pay-per-find model.

## Product
- Monitoring service for Berlin Bürgeramt appointment slots
- User specifies: desired office(s), service type, date range
- System polls service.berlin.de every 60+ seconds from VPS
- When a slot opens, user gets instant Signal + Nostr notification with direct booking link
- User clicks link and books the appointment in their own browser
- We NEVER enter user data, NEVER book on their behalf

## Financial Model
| Metric | Value |
|--------|-------|
| VPS cost (Hetzner CX22) | €4.50/month |
| Captcha solving (if needed) | €0-15/month |
| Proxy (if needed) | €0-50/month |
| Marginal cost per customer | €0.50-2/month |
| Pay-per-find price | €19 per successful notification |
| Target: 20 customers/month (month 2) | €380/month |
| Target: 50 customers/month (month 4) | €950/month |
| Target: 100 customers/month (month 6) | €1,900/month |
| Gross margin | 90%+ |

## Legal Framework
- **Model:** Sell the NOTIFICATION, never the appointment
- Appointments are free and non-transferable — selling them directly is illegal
- A monitoring/alert service is a SaaS product (like a stock price alert)
- service.berlin.de ToS prohibits automated access — this is the main risk
- Risk is administrative (IP ban) not criminal, based on available precedent
- Hard constraints:
  - NEVER enter user personal data into berlin.de
  - NEVER book on behalf of users
  - NEVER poll faster than 60s per target
  - NEVER run from home IP
  - Frame as "monitoring service" not "booking service"
  - Keep customer count low initially

## Technical Architecture
```
VPS (Hetzner, German IP)
├── Playwright + stealth plugin (headless Chromium)
├── Poller: 60-180s interval, random jitter ±15s
├── Slot parser: extract available dates/times from calendar
├── Dedup: don't notify about same slot twice
├── Notification router:
│   ├── Signal (via signal-cli)
│   ├── Nostr (NIP-04 encrypted DM)
│   └── Email (SMTP fallback)
├── State store: SQLite (seen_slots, customers, billing)
├── Captcha handler: manual-solve alert → 2Captcha API fallback
└── systemd timer + service
```

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| IP ban from berlin.de | Medium | High | 60s+ polling, proxy rotation, residential IP |
| Captcha escalation | Medium | Critical | Manual-solve fallback, shutdown protocol |
| Cease-and-desist | Low | Critical | Notification-only model, open source tool, low profile |
| Reputation risk | Low | Medium | Frame as community service, not commercial exploitation |
| Competition | High | Medium | Nostr/Signal distribution unique, Bitcoin payment unique |

## Shutdown Protocol
Immediate shutdown if ANY of:
1. Cease-and-desist letter from Berlin Senate
2. Captcha made permanent (can't monitor anymore)
3. Criminal complaint filed
4. IP permanently banned across all proxy options

## Launch Plan
1. Week 1: Build Playwright poller on VPS, test with own appointment needs
2. Week 2-3: Add Signal/Nostr notification, SQLite tracking
3. Week 4: List on Plebeian Market (€10 floor auction, €19 pay-per-find)
4. Month 2: First 5-10 paying customers
5. Month 3: Evaluate ban rate, revenue, legal signals
6. Month 4+: Scale if metrics are positive

## Viability Score: 6/10
- Conditional GO (notification-only model)
- Real demand exists (structural Berlin appointment shortage)
- Legal gray area — main risk is administrative, not criminal
- Treat as side-income experiment, not scalable startup
- Have shutdown protocol ready before launching
