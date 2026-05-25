    ---
    name: discover
    description: Run a structured discovery loop from problem framing through ideas, assumptions, prioritization, and validation experiments.
    argument-hint: "<problem, opportunity, feature area, or product idea>"
    uses:
  - problem-statement
  - brainstorm-ideas-new
  - identify-assumptions-new
  - prioritize-assumptions
  - experiment-design
    outputs:
  - discovery plan
  - prioritized assumptions
  - experiment backlog
  - decision framework
    ---

    # /discover

    ## Goal
    Move from vague product idea to evidence-backed validation plan.

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    1. Frame the discovery question and identify the target user, business outcome, and decision to be informed.
2. Draft or refine the problem statement before solutioning.
3. Generate solution options from product, design, engineering, data, and GTM lenses.
4. Surface assumptions across desirability, usability, feasibility, viability, data, and GTM.
5. Prioritize leap-of-faith assumptions and design fast validation probes with success criteria.

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
  - discovery plan
  - prioritized assumptions
  - experiment backlog
  - decision framework

    ## Next step
    End with one recommended follow-on command or skill.
