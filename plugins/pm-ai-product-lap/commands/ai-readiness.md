    ---
    name: ai-readiness
    description: Assess whether a product/business problem is AI-shaped and what proof is needed before building.
    argument-hint: "<AI idea, product workflow, automation opportunity, or company context>"
    uses:
  - ai-readiness
  - context-engineering
  - recommendation-canvas
    outputs:
  - AI readiness assessment
  - risk map
  - proof-of-life plan
  - build/no-build recommendation
    ---

    # /ai-readiness

    ## Goal
    Separate real AI leverage from AI theater and define the fastest proof path.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Clarify user job and decision loop.
2. Assess data, context, eval, UX, risk, and operations readiness.
3. Identify proof-of-life probes and eval criteria.
4. Recommend build, defer, or redesign.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - AI readiness assessment
  - risk map
  - proof-of-life plan
  - build/no-build recommendation

    ## Next step
    End with one recommended follow-on command or skill.
