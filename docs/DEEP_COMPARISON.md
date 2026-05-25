# Deep Comparison: phuryn/pm-skills vs deanpeters/Product-Manager-Skills

PM Skill LAP v2 was rebuilt after the first version was too shallow. This version treats the two source repositories as complementary systems, not as aesthetic inspiration.

## What phuryn contributes

- Marketplace-first architecture: eight domain plugins instead of one flat folder.
- Clear command layer: slash commands chain skills into end-to-end PM workflows.
- Strong PM operating-system framing: discovery, strategy, execution, market research, analytics, GTM, marketing/growth, and toolkit.
- Broad coverage: 65 skills and 36 workflows.

## What Dean Peters contributes

- Pedagogic-first philosophy: skills should make the PM better, not just generate an artifact.
- Skill quality discipline: sharper triggers, validation thinking, release packaging, and install paths.
- Extra domains missing or underrepresented in phuryn: finance/SaaS economics, AI PM, career/leadership, skill authoring, workshops.
- Better coaching posture: explain why a framework applies and how to reuse it.

## What LAP changes

1. Keeps phuryn's plugin-and-command architecture.
2. Adds Dean's coaching and learning standard to every skill.
3. Expands the plugin set from 8 source plugins to 12 LAP plugins.
4. Represents all source skills either as canonical skills or aliases in `catalog/overlap-map.json`.
5. Makes `/pm-skills-select` the default entry point.
6. Adds delete-and-recreate scripts so the repo can be rebuilt cleanly.

## Overlap handling

Overlaps are not blindly duplicated. LAP keeps the better canonical shape and stores aliases. Examples:

- `create-prd` + `prd-development` -> `create-prd`
- `market-sizing` + `tam-sam-som-calculator` -> `market-sizing`
- `pestle-analysis` + `pestel-analysis` -> `pestel-analysis`
- `user-stories` + `user-story` -> `user-stories`
- `brainstorm-experiments-*` + `pol-probe*` -> `experiment-design`
- `positioning-ideas` + `positioning-statement` -> `positioning-statement`

## Coverage summary

- Plugins: 12
- Skills: 100
- Workflows: 54
- Explicit overlap aliases: 14
