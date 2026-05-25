# Install PM Skill LAP in Claude Code

## From GitHub

```bash
claude plugin marketplace add brunocardone/pm-skill-lap
claude plugin marketplace update pm-skill-lap
claude plugin install pm-skills-select@pm-skill-lap
```

Install the full marketplace when desired:

```bash
for plugin in   pm-product-discovery-lap   pm-product-strategy-lap   pm-execution-lap   pm-market-research-lap   pm-data-analytics-lap   pm-go-to-market-lap   pm-marketing-growth-lap   pm-finance-saas-lap   pm-ai-product-lap   pm-career-leadership-lap   pm-toolkit-lap; do
  claude plugin install "$plugin@pm-skill-lap"
done
```

## Local development install

From the parent directory of this repo:

```bash
claude plugin marketplace add ./pm-skill-lap --scope local
claude plugin install pm-skills-select@pm-skill-lap --scope local
claude plugin validate ./pm-skill-lap
```

## Usage

Start with:

```text
/pm-skills-select:pm-skills-select <your PM situation>
```

Plugin skills are namespaced with the plugin name. Examples:

```text
/pm-product-discovery-lap:problem-statement Frame the onboarding problem for SMB users
/pm-execution-lap:create-prd Create a PRD for guided onboarding
/pm-product-strategy-lap:product-strategy Build a strategy for our AI onboarding assistant
```

Commands can also be invoked from installed plugins. If in doubt, use `/pm-skills-select` first.
