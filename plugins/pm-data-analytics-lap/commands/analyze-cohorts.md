    ---
    name: analyze-cohorts
    description: Run the analyze-cohorts PM workflow and produce a decision-ready artifact.
    argument-hint: "<PM context>"
    uses:
  - cohort-analysis
    outputs:
  - PM artifact
  - assumptions
  - risks
  - next step
    ---

    # /analyze-cohorts

    ## Goal
    Execute /analyze-cohorts as a structured PM workflow.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Clarify the PM situation and expected artifact.
2. Load or apply the listed skills in order.
3. Produce the artifact directly when context is sufficient.
4. Label assumptions, risks, and open questions.
5. Recommend the next command.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - PM artifact
  - assumptions
  - risks
  - next step

    ## Next step
    End with one recommended follow-on command or skill.
