# Data Analytics Plugin

> Use data to decide, diagnose, and learn.

SQL generation, cohort analysis, A/B test analysis, metrics diagnostics, retention curves, and dashboards.

## Skills

| Skill | Purpose | Source mix |
| --- | --- | --- |
| sql-queries | Generate SQL from natural language for BigQuery, PostgreSQL, or MySQL with schema assumptions and validation notes. | phuryn |
| cohort-analysis | Analyze retention, feature adoption, engagement, and behavior by cohort. | phuryn |
| ab-test-analysis | Analyze experiment design, significance, sample size, guardrails, and ship/extend/stop recommendation. | phuryn |
| metrics-dashboard | Design a product metrics dashboard with North Star, input metrics, guardrails, thresholds, and review cadence. | phuryn |
| metrics-diagnostic | Diagnose metric symptoms, funnel leaks, retention decay, quality issues, and measurement gaps. | new, phuryn, deanpeters |

## Workflows

| Command | Skill chain | When to use |
| --- | --- | --- |
| /write-query | sql-queries | Use for analytics requests. |
| /analyze-cohorts | cohort-analysis | Use for lifecycle diagnostics. |
| /analyze-test | ab-test-analysis | Use after or before experiments. |
| /metrics-diagnostic | metrics-diagnostic -> metrics-dashboard -> north-star-metric | Use when metrics look wrong or incomplete. |
