# PM Skill LAP Gold-Standard Operating Mode

This repository is a Claude Code marketplace for product-management work. It synthesizes two useful patterns:

1. **phuryn/pm-skills**: plugin marketplace architecture, command chaining, PM execution artifacts, and Markdown-first workflow outputs.
2. **deanpeters/Product-Manager-Skills**: pedagogic-first skill design, rich framework explanations, release packaging, Claude Desktop/Web skill ZIPs, and Codex portability.

## Design principles

- Keep `pm-skills-select` as the front door.
- Prefer executable PM artifacts over explanations.
- Ask fewer questions; proceed with labeled assumptions when possible.
- Teach the framework briefly while producing the artifact.
- Separate facts, assumptions, recommendations, risks, and open questions.
- Save substantial outputs as Markdown-ready artifacts.
- Keep plugin manifests strict and minimal; use default `skills/` and `commands/` discovery.

## Skill quality bar

Every skill should produce a concrete PM deliverable, include tradeoffs, and recommend one next workflow. Generic advice is a defect.

## Workflow quality bar

Every command should include frontmatter, a skill chain, final outputs, execution rules, and a next step. A command should do work directly when context is sufficient.
