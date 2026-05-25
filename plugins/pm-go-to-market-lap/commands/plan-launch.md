    ---
    name: plan-launch
    description: Create a launch plan with audience, positioning, channels, readiness, risks, metrics, and cross-functional owners.
    argument-hint: "<feature, product, release, or launch context>"
    uses:
  - gtm-strategy
  - launch-plan
  - positioning-statement
    outputs:
  - launch plan
  - readiness checklist
  - messaging
  - metrics
  - risks
    ---

    # /plan-launch

    ## Goal
    Make launch execution coordinated, measurable, and audience-specific.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Define target audience and adoption goal.
2. Write positioning and core message.
3. Plan channels, enablement, comms, and owners.
4. Set launch metrics, risks, rollback, and follow-up cadence.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - launch plan
  - readiness checklist
  - messaging
  - metrics
  - risks

    ## Next step
    End with one recommended follow-on command or skill.
