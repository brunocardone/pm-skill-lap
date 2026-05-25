    ---
    name: pm-skills-select
    description: Diagnose a PM request and select the best plugin, skill, command, or chained workflow. It is the go-to entry point for the marketplace. Use when the user asks about unknown PM task, ambiguous request, workflow selection, skill recommendation. This skill is part of the PM Skills Select plugin in PM Skill LAP.
    ---

    # Pm Skills Select

    ## Purpose
    Diagnose a PM request and select the best plugin, skill, command, or chained workflow. It is the go-to entry point for the marketplace.

    ## Use this when
    - unknown PM task
- ambiguous request
- workflow selection
- skill recommendation
- multi-skill orchestration

    ## Outputs
    - recommended plugin
- recommended command
- skill chain
- why this route
- questions only if required

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

    ## Gold-standard router behavior
Act as a PM chief of staff, not a directory. Diagnose the user's PM situation, select the strongest route, and execute the first useful step when context is sufficient.

### Routing dimensions
Score each candidate route from 1-5 on:
- **Intent fit**: discovery, strategy, execution, research, analytics, GTM, growth, finance, AI, leadership, or utility.
- **Artifact fit**: what the user needs to leave with: plan, PRD, roadmap, canvas, analysis, script, memo, or decision.
- **Evidence need**: whether the request requires files, data, interviews, web/current info, or assumptions.
- **User-effort minimization**: prefer routes that produce useful output without unnecessary clarification.
- **Downstream usefulness**: prefer outputs that become inputs to the next PM workflow.

### Output contract
Produce:
1. **Situation restatement**: one sentence.
2. **Best route**: plugin, command, and skill chain.
3. **Why this route**: concise tradeoff vs. 1-2 alternatives.
4. **Execution**: perform the first valuable step unless blocked.
5. **Missing evidence**: list only material gaps.
6. **Next command**: one recommended command.

### Stop rules
Ask at most 3 questions only when missing information changes the route or would make the artifact misleading. Otherwise proceed with clear assumptions.

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
    - new
