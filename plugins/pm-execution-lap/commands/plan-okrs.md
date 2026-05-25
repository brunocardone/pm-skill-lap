    ---
    name: plan-okrs
    description: Draft outcome-based product OKRs aligned with strategy, customer outcomes, and measurable leading indicators.
    argument-hint: "<team, product area, quarter, strategy, or planning context>"
    uses:
  - brainstorm-okrs
  - north-star-metric
    outputs:
  - OKRs
  - metric tree
  - anti-metrics
  - review cadence
    ---

    # /plan-okrs

    ## Goal
    Create OKRs that guide decisions instead of listing activities.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Identify strategic theme and target outcome.
2. Draft objectives in plain language.
3. Create measurable KRs with baselines and targets.
4. Add guardrail metrics and review cadence.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - OKRs
  - metric tree
  - anti-metrics
  - review cadence

    ## Next step
    End with one recommended follow-on command or skill.
