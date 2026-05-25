    ---
    name: transform-roadmap
    description: Transform a feature-heavy roadmap into outcome themes, bets, learning milestones, and sequencing logic.
    argument-hint: "<feature roadmap, backlog, or planning notes>"
    uses:
  - outcome-roadmap
  - prioritization-frameworks
    outputs:
  - outcome roadmap
  - sequencing rationale
  - tradeoffs
  - learning milestones
    ---

    # /transform-roadmap

    ## Goal
    Move roadmap conversation from feature delivery to measurable outcomes.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Cluster features into outcomes.
2. Define customer/business impact per theme.
3. Prioritize using a fit-for-context framework.
4. Sequence bets by risk, dependency, confidence, and learning value.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - outcome roadmap
  - sequencing rationale
  - tradeoffs
  - learning milestones

    ## Next step
    End with one recommended follow-on command or skill.
