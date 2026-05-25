# Release Packaging

`plugins/` is the source of truth. Generated artifacts live under `dist/`.

## Validate

```bash
bash scripts/validate-pm-lap.sh
```

## Build everything

```bash
bash scripts/build-release.sh
```

## Generated artifacts

```text
dist/
  skill-zips/                 # one upload-ready ZIP per skill
  claude-desktop/             # curated packs of skill ZIPs
  plugins/                    # one ZIP per Claude Code plugin
  codex/                      # .agents/skills package for Codex-style agents
  release/                    # assembled release tree
  pm-skill-lap-<version>-release.zip
```

## Release process

```bash
bash scripts/validate-pm-lap.sh
bash scripts/build-release.sh
git add .
git commit -m "Release PM Skill LAP v2.1.0"
git tag v2.1.0
git push origin main --tags
```

## Rules

- Do not edit `dist/` manually.
- Bump versions in `.claude-plugin/marketplace.json` and plugin manifests before releases.
- Run `claude plugin validate .` and `claude plugin validate ./plugins/<plugin> --strict` before publishing.
- Preserve `pm-skills-select` as the primary entrypoint.
