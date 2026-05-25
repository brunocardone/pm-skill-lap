    ---
    name: write-prd
    description: Create a PRD from discovery context, problem framing, and solution scope with requirements, metrics, risks, and open questions.
    argument-hint: "<feature, product idea, problem statement, or discovery notes>"
    uses:
  - problem-statement
  - create-prd
  - test-scenarios
    outputs:
  - PRD
  - acceptance criteria
  - test scenarios
  - risks
  - open questions
    ---

    # /write-prd

    ## Goal
    Produce an engineering-ready PRD that preserves the why and makes scope testable.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Frame the problem and target users.
2. Define solution overview and scope boundaries.
3. Write requirements as user stories or acceptance criteria.
4. Define success metrics and launch/readiness constraints.
5. Add risks, dependencies, test scenarios, and open questions.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - PRD
  - acceptance criteria
  - test scenarios
  - risks
  - open questions

    ## Next step
    End with one recommended follow-on command or skill.
