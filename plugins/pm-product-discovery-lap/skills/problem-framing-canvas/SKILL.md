    ---
    name: problem-framing-canvas
    description: Use structured problem-framing to clarify who has the problem, why it matters, what constraints exist, and what evidence is missing. Use when the user asks about ambiguous problem, team alignment, workshop facilitation. This skill is part of the Product Discovery plugin in PM Skill LAP.
    ---

    # Problem Framing Canvas

    ## Purpose
    Use structured problem-framing to clarify who has the problem, why it matters, what constraints exist, and what evidence is missing.

    ## Use this when
    - ambiguous problem
- team alignment
- workshop facilitation

    ## Outputs
    - problem frame
- constraints
- evidence gaps
- decision boundaries

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

    ## Default artifact contract
Produce a structured artifact with: context, assumptions, framework application, table or canvas where useful, recommendation, risks, open questions, and next action.

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
