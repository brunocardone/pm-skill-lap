    ---
    name: brainstorm
    description: Generate strong product ideas or experiment ideas using multiple PM, design, engineering, data, and GTM perspectives.
    argument-hint: "<existing product, new product, opportunity, or assumption>"
    uses:
  - brainstorm-ideas-existing
  - brainstorm-ideas-new
  - experiment-design
    outputs:
  - idea portfolio
  - prioritized shortlist
  - assumptions
  - next tests
    ---

    # /brainstorm

    ## Goal
    Create a diverse but decision-ready set of ideas, not a generic list.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Clarify existing vs new product context.
2. Generate divergent ideas by lens.
3. Cluster and deduplicate ideas.
4. Prioritize by customer value, speed to learn, differentiation, and risk.
5. Recommend the next validation step.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - idea portfolio
  - prioritized shortlist
  - assumptions
  - next tests

    ## Next step
    End with one recommended follow-on command or skill.
