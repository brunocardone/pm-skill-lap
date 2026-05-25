    ---
    name: experiment-design
    description: Design lean experiments, pretotypes, concierge tests, landing pages, fake doors, interviews, and data probes matched to the riskiest assumption. Use when the user asks about experiment planning, validation roadmap, proof before build. This skill is part of the Product Discovery plugin in PM Skill LAP.
    ---

    # Experiment Design

    ## Purpose
    Design lean experiments, pretotypes, concierge tests, landing pages, fake doors, interviews, and data probes matched to the riskiest assumption.

    ## Use this when
    - experiment planning
- validation roadmap
- proof before build

    ## Outputs
    - experiment cards
- success thresholds
- sample plan
- decision rule

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

    ## Gold-standard experiment design
Design lean validation probes matched to the riskiest assumption.

### Experiment menu
Use interviews, fake doors, landing pages, concierge MVPs, prototypes, Wizard-of-Oz tests, data probes, A/B tests, smoke tests, price tests, or sales tests.

### Output contract
For each experiment include:
- Assumption tested
- Hypothesis
- Method and setup
- Target sample
- Success criteria
- Failure criteria
- Timeline and effort
- Decision rule: persevere, pivot, kill, or learn more

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
    This LAP skill consolidates: `brainstorm-experiments-existing`, `brainstorm-experiments-new`, `pol-probe`, `pol-probe-advisor`.

    ## Source mix
    - phuryn
- deanpeters
