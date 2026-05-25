# Execution & Delivery Plugin

> Turn strategy into buildable, testable, shippable work.

PRDs, OKRs, roadmaps, sprints, retros, release notes, stories, epics, test scenarios, pre-mortems, and stakeholder management.

## Skills

| Skill | Purpose | Source mix |
| --- | --- | --- |
| create-prd | Build a structured PRD connecting problem, users, solution, scope, requirements, risks, metrics, and launch considerations. | phuryn, deanpeters |
| brainstorm-okrs | Create team-level objectives and measurable key results aligned with product and company strategy. | phuryn |
| outcome-roadmap | Transform feature lists into outcome-focused roadmap themes, bets, metrics, and sequencing. | phuryn, deanpeters |
| sprint-plan | Plan a sprint with capacity, story selection, risks, dependencies, and definition of done. | phuryn |
| retro | Facilitate a retrospective that turns learning into concrete improvement experiments. | phuryn |
| release-notes | Write user-facing release notes from tickets, PRDs, changelogs, or shipped features. | phuryn |
| pre-mortem | Run a pre-mortem and classify risks as tigers, paper tigers, and elephants with mitigations. | phuryn |
| stakeholder-map | Map stakeholders by power, interest, influence, incentives, concerns, and communication plan. | phuryn |
| summarize-meeting | Turn meeting notes or transcript into decisions, action items, risks, open questions, and follow-ups. | phuryn |
| user-stories | Write user stories with 3 Cs, INVEST, acceptance criteria, and testable boundaries. | phuryn, deanpeters |
| job-stories | Write job stories using situation, motivation, and outcome framing. | phuryn |
| wwas | Write backlog items in Why-What-Acceptance format to connect purpose, scope, and testability. | phuryn |
| test-scenarios | Generate happy paths, edge cases, error states, abuse cases, accessibility considerations, and data scenarios. | phuryn |
| dummy-dataset | Generate realistic dummy datasets as CSV, JSON, SQL, or Python for demos, tests, and analytics examples. | phuryn |
| prioritization-frameworks | Select and explain frameworks such as RICE, ICE, MoSCoW, Kano, Opportunity Score, Cost of Delay, and Weighted Shortest Job First. | phuryn, deanpeters |
| epic-breakdown-advisor | Break epics into smaller deliverable stories using proven split patterns. | deanpeters |
| epic-hypothesis | Frame an epic as a testable hypothesis with user, outcome, expected impact, and validation. | deanpeters |
| storyboard | Create a six-frame storyboard showing a user journey from problem to solution and outcome. | deanpeters |
| user-story-mapping | Create a story map with activities, steps, tasks, backbone, release slices, and MVP boundaries. | deanpeters |
| user-story-mapping-workshop | Run an interactive story-mapping workshop with adaptive prompts and facilitation guidance. | deanpeters |
| user-story-splitting | Split large user stories into smaller valuable, testable increments. | deanpeters |

## Workflows

| Command | Skill chain | When to use |
| --- | --- | --- |
| /write-prd | problem-statement -> create-prd -> test-scenarios | Use when moving from discovery to delivery. |
| /plan-okrs | brainstorm-okrs -> north-star-metric | Use during quarterly or annual planning. |
| /transform-roadmap | outcome-roadmap -> prioritization-frameworks | Use when the roadmap is too feature-heavy. |
| /sprint | sprint-plan -> retro -> release-notes | Use for delivery ceremonies. |
| /pre-mortem | pre-mortem -> stakeholder-map | Use before a risky commitment. |
| /meeting-notes | summarize-meeting | Use after stakeholder or team meetings. |
| /stakeholder-map | stakeholder-map | Use for complex alignment. |
| /write-stories | user-stories -> job-stories -> wwas -> user-story-splitting | Use for backlog creation. |
| /test-scenarios | test-scenarios | Use before QA or acceptance. |
| /generate-data | dummy-dataset | Use for demos and tests. |
| /story-map | user-story-mapping -> user-story-mapping-workshop | Use for MVP planning. |
