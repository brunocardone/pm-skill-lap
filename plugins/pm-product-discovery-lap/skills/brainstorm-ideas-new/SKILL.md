    ---
    name: brainstorm-ideas-new
    description: Generate new-product concepts from a market, user problem, trend, or capability. Use when the user asks about new product ideation, zero-to-one concepting, problem exploration. This skill is part of the Product Discovery plugin in PM Skill LAP.
    ---

    # Brainstorm Ideas New

    ## Purpose
    Generate new-product concepts from a market, user problem, trend, or capability.

    ## Use this when
    - new product ideation
- zero-to-one concepting
- problem exploration

    ## Outputs
    - concept list
- target users
- value hypotheses
- risk notes

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

    ## Gold-standard zero-to-one ideation
Generate product ideas for a new product, market, capability, trend, or underserved job.

### Lenses
Generate options across:
- Product manager: market fit, value creation, strategic wedge.
- Designer: onboarding, workflow, habit, trust, accessibility.
- Engineer: technical feasibility, integrations, data loops, platform leverage.
- Data/analytics: measurable behavior, feedback loops, instrumentation.
- GTM: reachable segment, channel, willingness to try, adoption trigger.

### Output contract
Provide 10-15 ideas, cluster them, pick top 5, and for each top idea include target user, value hypothesis, differentiation, validation speed, and riskiest assumption.

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
    - phuryn
