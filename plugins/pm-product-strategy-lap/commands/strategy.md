    ---
    name: strategy
    description: Create product strategy across vision, customer, problem, value proposition, choices, moat, metrics, risks, and narrative.
    argument-hint: "<product, company, market, or strategic question>"
    uses:
  - product-strategy
  - product-vision
  - value-proposition
  - north-star-metric
    outputs:
  - strategy canvas
  - strategic choices
  - metrics
  - risks
  - executive narrative
    ---

    # /strategy

    ## Goal
    Turn ambiguous strategy inputs into explicit choices and an executive-ready product strategy.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Clarify the strategic decision and altitude.
2. Define target customer, problem, and desired outcome.
3. State value proposition and differentiation.
4. Make explicit tradeoffs and non-goals.
5. Attach metrics, risks, and next proof points.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - strategy canvas
  - strategic choices
  - metrics
  - risks
  - executive narrative

    ## Next step
    End with one recommended follow-on command or skill.
