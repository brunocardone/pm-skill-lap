    ---
    name: create-prd
    description: Build a structured PRD connecting problem, users, solution, scope, requirements, risks, metrics, and launch considerations. Use when the user asks about PRD, requirements, feature definition. This skill is part of the Execution & Delivery plugin in PM Skill LAP.
    ---

    # Create PRD

    ## Purpose
    Build a structured PRD connecting problem, users, solution, scope, requirements, risks, metrics, and launch considerations.

    ## Use this when
    - PRD
- requirements
- feature definition

    ## Outputs
    - PRD
- open questions
- acceptance criteria
- risks

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

    ## Gold-standard PRD contract
Create an engineering-ready PRD that preserves strategic context and makes scope testable.

### PRD structure
1. Executive summary
2. Problem statement and evidence
3. Target users and jobs-to-be-done
4. Strategic context and goals
5. Solution overview
6. Scope: in / out / later
7. Requirements and user stories
8. Acceptance criteria and test scenarios
9. Success metrics and guardrails
10. Dependencies, risks, mitigations, and open questions

### Quality bar
- Separate facts, assumptions, and recommendations.
- Include measurable success criteria and guardrails.
- Avoid solution smuggling in the problem statement.
- Translate vague asks into testable requirements.
- Mark unknowns as open questions instead of inventing certainty.

### Save behavior
When substantial, create or recommend `PRD-[short-product-name].md`.

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
    This LAP skill consolidates: `prd-development`.

    ## Source mix
    - phuryn
- deanpeters
