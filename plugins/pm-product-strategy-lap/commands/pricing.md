    ---
    name: pricing
    description: Design pricing and packaging using value, willingness-to-pay, unit economics, competitive context, and experiments.
    argument-hint: "<product, plan, pricing problem, or packaging choice>"
    uses:
  - pricing-strategy
  - feature-investment-advisor
  - saas-economics-efficiency-metrics
    outputs:
  - pricing options
  - packaging logic
  - tradeoff analysis
  - experiment plan
    ---

    # /pricing

    ## Goal
    Turn pricing into a testable product/business decision.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Clarify buyer, user, value metric, and constraints.
2. Generate pricing/packaging options.
3. Assess value capture, complexity, fairness, and unit economics.
4. Recommend a preferred path and validation experiment.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - pricing options
  - packaging logic
  - tradeoff analysis
  - experiment plan

    ## Next step
    End with one recommended follow-on command or skill.
