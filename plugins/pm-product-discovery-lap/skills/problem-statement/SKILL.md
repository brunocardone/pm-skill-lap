    ---
    name: problem-statement
    description: Write a user-centered problem statement with who, what, why, emotional context, and evidence. Use when the user asks about problem definition, PRD setup, strategy framing. This skill is part of the Product Discovery plugin in PM Skill LAP.
    ---

    # Problem Statement

    ## Purpose
    Write a user-centered problem statement with who, what, why, emotional context, and evidence.

    ## Use this when
    - problem definition
- PRD setup
- strategy framing

    ## Outputs
    - problem statement
- user context
- evidence notes
- anti-solution check

    ## Operating mode
    1. Restate the PM situation in one sentence.
    2. Identify the artifact, decision, risk, or learning goal the user actually needs.
    3. Ask only for missing information that materially changes the answer; otherwise proceed with labeled assumptions.
    4. Apply the framework with concise reasoning before the artifact.
    5. Produce a PM-ready artifact with clear sections, tables where useful, and decision-oriented next steps.
    6. End with one recommended next skill or workflow.

    ## Gold-standard behavior
    - Prefer evidence over opinion. If evidence is absent, state assumptions explicitly.
    - Separate facts, hypotheses, recommendations, risks, and open questions.
    - Teach briefly while doing the work: explain why the framework fits and how the user can reuse it.
    - Be specific to the product, user, segment, market, or business model in the prompt.
    - Use concise PM language suitable for a product review, discovery readout, PRD, roadmap meeting, or exec discussion.
    - When output is substantial, format it as a Markdown artifact that can be saved directly.

    ## Gold-standard problem framing
Write a user-centered problem statement before solutioning.

### Framework
Use this structure:
- **I am**: specific persona or segment.
- **Trying to**: outcome the user wants, not a task.
- **But**: barrier preventing the outcome.
- **Because**: root cause, not surface symptom.
- **Which makes me feel / causes**: emotional and practical impact.
- **Context and constraints**: technical, geographic, workflow, timing, or business constraints.
- **Final statement**: one crisp sentence.

### Anti-patterns
Reject feature requests disguised as problems, generic personas, fabricated emotions, and business-only problems with no user impact.

    ## Quality gates
    Before finalizing, check:
    - Is the output tied to a user problem or business decision?
    - Are assumptions and evidence clearly labeled?
    - Are tradeoffs visible?
    - Would a PM, designer, engineer, or stakeholder know what to do next?
    - Is the recommendation specific enough to execute or validate?

    ## Anti-patterns
    - Generic PM advice with no artifact.
    - Over-asking for context when a best-effort artifact is possible.
    - Inventing evidence, metrics, personas, or customer quotes.
    - Confusing outputs, outcomes, and activities.
    - Hiding uncertainty instead of making it actionable.

    ## Aliases and merged source skills
    - None

    ## Source mix
    - deanpeters
