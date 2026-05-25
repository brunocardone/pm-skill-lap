    ---
    name: business-model
    description: Analyze business model options using lean canvas, business model canvas, startup canvas, and value proposition logic.
    argument-hint: "<business idea, product, startup, or monetization question>"
    uses:
  - lean-canvas
  - business-model
  - startup-canvas
  - value-proposition
    outputs:
  - business model canvas
  - lean canvas
  - assumption map
  - validation plan
    ---

    # /business-model

    ## Goal
    Make business model assumptions explicit and testable.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Define customer and job.
2. Map value creation and capture.
3. Identify channels, cost drivers, revenue logic, and unfair advantage.
4. Prioritize assumptions by risk.
5. Recommend validation tests.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - business model canvas
  - lean canvas
  - assumption map
  - validation plan

    ## Next step
    End with one recommended follow-on command or skill.
