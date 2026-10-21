# Copy-paste prompts

Each one is a full prompt for Claude Code with the Replica skills installed.

## Reverse engineer an app (start here)

```
/replica-recon Reverse engineer chess.com: list every screen, user flow,
component, the inferred data model and a feature matrix in replica/.
Scope: play a game online, puzzles, profile and ratings. Web first.
```

```
/replica-recon Map out how Calendly works. Core loop only: event types,
availability, the public booking page and confirmations.
```

```
/replica-recon Here is the App Store link: <link>. I want to build my own
version of this app for <niche>. What screens and flows does it have?
```

## The full pipeline, one step at a time

```
/replica-architect        plan stack, schema and API from the recon map
/replica-design           rebuild the design system as tokens + component specs
/replica-build            build the app shell, then the core flow, then every screen
/replica-backend          real auth, database, Stripe, email
/replica-test             test plan, Playwright e2e tests, bug reports
/replica-diff             parity score against the original
/replica-entrepreneur     read real user reviews, find what to fix
/replica-brand            your own name, palette, logo brief, leftover sweep
/replica-launch           landing page, pricing, store listing
/replica-deploy           preflight checks, domain, production
```

## One-shot

```
Use the Replica skills to reverse engineer <app> and build my own version of
its core loop. Run /replica-recon first, show me the recon summary, then go
through architect, design and build. Stop after each step for my OK.
```
