---
name: sql-queries
description: Generate SQL from natural language for BigQuery, PostgreSQL, or MySQL with schema assumptions and validation notes. Use when the user asks about SQL writing, analytics request, data exploration. This skill is part of the Data Analytics plugin in PM Skill LAP.
---

# SQL Queries

## Purpose
Generate SQL from natural language for BigQuery, PostgreSQL, or MySQL with schema assumptions and validation notes.

## Use this when
- SQL writing
- analytics request
- data exploration

## Outputs
- SQL query
- assumptions
- validation checks

## Operating mode
1. Restate the PM situation in one sentence.
2. Identify the decision, risk, or artifact the user actually needs.
3. Ask only for missing information that materially changes the answer.
4. Apply the framework and show reasoning compactly.
5. Produce the requested artifact.
6. End with a recommended next skill or workflow.

## Coaching standard
Explain the PM reasoning briefly before the final artifact. Make tradeoffs explicit and teach the user how to reuse the framework.

## Quality bar
- Prefer evidence over opinion.
- Name assumptions explicitly.
- Separate facts, hypotheses, and recommendations.
- Highlight tradeoffs and anti-patterns.
- Use crisp PM-ready artifacts, not generic advice.

## Source mix
- phuryn
