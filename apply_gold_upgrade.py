#!/usr/bin/env python3
"""
PM Skill LAP Gold Upgrade

Run from the root of brunocardone/pm-skill-lap.
It upgrades the repository into a stricter Claude Code marketplace with:
- corrected plugin manifests
- richer skill bodies
- command frontmatter and workflow contracts
- release/build scripts
- install/release docs
- validation workflow

The script is idempotent and creates a timestamped backup of files it modifies.
"""
from __future__ import annotations

import json
import re
import shutil
import stat
import sys
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path.cwd()
BACKUP_DIR = ROOT / f".gold-upgrade-backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
VERSION = "2.1.0"

PLUGIN_META: Dict[str, Dict[str, object]] = {
    "pm-skills-select": {
        "displayName": "PM Skills Select",
        "description": "Gold-standard router that diagnoses a PM request and selects the best LAP plugin, command, skill, or multi-step chain, then executes the selected path when enough context exists.",
        "category": "meta",
        "keywords": ["product-management", "router", "skill-selection", "workflow-selection", "pm-chief-of-staff"],
    },
    "pm-product-discovery-lap": {
        "displayName": "PM Product Discovery LAP",
        "description": "Gold-standard product discovery workflows for problem framing, customer learning, JTBD, assumptions, experiments, opportunity trees, interviews, personas, journeys, and validation planning.",
        "category": "product-management",
        "keywords": ["product-management", "discovery", "experiments", "jtbd", "customer-research"],
    },
    "pm-product-strategy-lap": {
        "displayName": "PM Product Strategy LAP",
        "description": "Gold-standard product strategy workflows for vision, value propositions, business models, pricing, competitive strategy, working backwards, market choices, and executive-ready strategy artifacts.",
        "category": "product-management",
        "keywords": ["product-management", "strategy", "positioning", "pricing", "business-model"],
    },
    "pm-execution-lap": {
        "displayName": "PM Execution LAP",
        "description": "Gold-standard execution workflows for PRDs, OKRs, outcome roadmaps, sprints, retros, releases, stories, epics, test scenarios, pre-mortems, and stakeholder alignment.",
        "category": "product-management",
        "keywords": ["product-management", "execution", "prd", "roadmap", "delivery"],
    },
    "pm-market-research-lap": {
        "displayName": "PM Market Research LAP",
        "description": "Gold-standard market and customer research workflows for personas, segmentation, journey maps, market sizing, competitor analysis, company research, sentiment, and evidence synthesis.",
        "category": "product-management",
        "keywords": ["product-management", "market-research", "competitive-analysis", "persona", "segmentation"],
    },
    "pm-data-analytics-lap": {
        "displayName": "PM Data Analytics LAP",
        "description": "Gold-standard analytics workflows for metrics diagnostics, SQL, cohorts, A/B tests, retention curves, dashboards, evidence quality, and decision-oriented product analytics.",
        "category": "product-management",
        "keywords": ["product-management", "analytics", "metrics", "sql", "experimentation"],
    },
    "pm-go-to-market-lap": {
        "displayName": "PM Go To Market LAP",
        "description": "Gold-standard GTM workflows for launch planning, ICP, beachhead selection, acquisition channels, growth loops, GTM motions, battlecards, sales enablement, and adoption strategy.",
        "category": "product-management",
        "keywords": ["product-management", "go-to-market", "launch", "icp", "growth"],
    },
    "pm-marketing-growth-lap": {
        "displayName": "PM Marketing Growth LAP",
        "description": "Gold-standard product marketing and growth workflows for positioning, messaging, naming, North Star metrics, organic growth diagnostics, activation, retention, and growth experimentation.",
        "category": "product-management",
        "keywords": ["product-management", "growth", "marketing", "positioning", "north-star"],
    },
    "pm-finance-saas-lap": {
        "displayName": "PM Finance SaaS LAP",
        "description": "Gold-standard SaaS finance workflows for unit economics, ARR/MRR, retention, pricing economics, feature ROI, acquisition efficiency, business health, and PM-friendly financial decisions.",
        "category": "product-management",
        "keywords": ["product-management", "saas", "finance", "unit-economics", "pricing"],
    },
    "pm-ai-product-lap": {
        "displayName": "PM AI Product LAP",
        "description": "Gold-standard AI product workflows for AI readiness, context engineering, recommendation systems, proof-of-life probes, eval thinking, AI UX risk, and product validation for AI-shaped products.",
        "category": "product-management",
        "keywords": ["product-management", "ai", "context-engineering", "evals", "ai-readiness"],
    },
    "pm-career-leadership-lap": {
        "displayName": "PM Career Leadership LAP",
        "description": "Gold-standard PM leadership coaching for product sense, director readiness, VP/CPO altitude, executive onboarding, org leverage, communication, and career progression.",
        "category": "career",
        "keywords": ["product-management", "career", "leadership", "coaching", "executive"],
    },
    "pm-toolkit-lap": {
        "displayName": "PM Toolkit LAP",
        "description": "Gold-standard PM utility workflows for proofreading, resume review, NDA drafting, privacy policy drafting, dummy data, meeting summaries, and skill authoring support.",
        "category": "utility",
        "keywords": ["product-management", "toolkit", "writing", "templates", "utility"],
    },
}

COMMANDS: Dict[str, Dict[str, object]] = {
    "pm-skills-select": {
        "description": "Route any PM request to the best LAP plugin, skill, command, or chain and execute the chosen path when context is sufficient.",
        "argument": "<PM situation, artifact request, decision, or messy context>",
        "uses": ["pm-skills-select"],
        "outputs": ["route card", "recommended plugin", "recommended command", "skill chain", "executed first-pass artifact", "next command"],
        "goal": "Act as a PM chief of staff: understand the request, choose the best LAP route, and produce useful work instead of only naming a skill.",
        "workflow": [
            "Classify the user's intent: discovery, strategy, execution, research, analytics, GTM, growth, finance, AI, leadership, or utility.",
            "Identify the artifact, decision, risk, or conversation outcome the user actually needs.",
            "Score candidate routes by fit, evidence requirement, user effort, and downstream usefulness.",
            "Select one primary route and up to two alternates; explain tradeoffs briefly.",
            "If context is sufficient, execute the first useful step immediately. Ask questions only when the answer would materially change the route or artifact.",
        ],
    },
    "discover": {
        "description": "Run a structured discovery loop from problem framing through ideas, assumptions, prioritization, and validation experiments.",
        "argument": "<problem, opportunity, feature area, or product idea>",
        "uses": ["problem-statement", "brainstorm-ideas-new", "identify-assumptions-new", "prioritize-assumptions", "experiment-design"],
        "outputs": ["discovery plan", "prioritized assumptions", "experiment backlog", "decision framework"],
        "goal": "Move from vague product idea to evidence-backed validation plan.",
        "workflow": [
            "Frame the discovery question and identify the target user, business outcome, and decision to be informed.",
            "Draft or refine the problem statement before solutioning.",
            "Generate solution options from product, design, engineering, data, and GTM lenses.",
            "Surface assumptions across desirability, usability, feasibility, viability, data, and GTM.",
            "Prioritize leap-of-faith assumptions and design fast validation probes with success criteria.",
        ],
    },
    "brainstorm": {
        "description": "Generate strong product ideas or experiment ideas using multiple PM, design, engineering, data, and GTM perspectives.",
        "argument": "<existing product, new product, opportunity, or assumption>",
        "uses": ["brainstorm-ideas-existing", "brainstorm-ideas-new", "experiment-design"],
        "outputs": ["idea portfolio", "prioritized shortlist", "assumptions", "next tests"],
        "goal": "Create a diverse but decision-ready set of ideas, not a generic list.",
        "workflow": ["Clarify existing vs new product context.", "Generate divergent ideas by lens.", "Cluster and deduplicate ideas.", "Prioritize by customer value, speed to learn, differentiation, and risk.", "Recommend the next validation step."],
    },
    "write-prd": {
        "description": "Create a PRD from discovery context, problem framing, and solution scope with requirements, metrics, risks, and open questions.",
        "argument": "<feature, product idea, problem statement, or discovery notes>",
        "uses": ["problem-statement", "create-prd", "test-scenarios"],
        "outputs": ["PRD", "acceptance criteria", "test scenarios", "risks", "open questions"],
        "goal": "Produce an engineering-ready PRD that preserves the why and makes scope testable.",
        "workflow": ["Frame the problem and target users.", "Define solution overview and scope boundaries.", "Write requirements as user stories or acceptance criteria.", "Define success metrics and launch/readiness constraints.", "Add risks, dependencies, test scenarios, and open questions."],
    },
    "strategy": {
        "description": "Create product strategy across vision, customer, problem, value proposition, choices, moat, metrics, risks, and narrative.",
        "argument": "<product, company, market, or strategic question>",
        "uses": ["product-strategy", "product-vision", "value-proposition", "north-star-metric"],
        "outputs": ["strategy canvas", "strategic choices", "metrics", "risks", "executive narrative"],
        "goal": "Turn ambiguous strategy inputs into explicit choices and an executive-ready product strategy.",
        "workflow": ["Clarify the strategic decision and altitude.", "Define target customer, problem, and desired outcome.", "State value proposition and differentiation.", "Make explicit tradeoffs and non-goals.", "Attach metrics, risks, and next proof points."],
    },
    "business-model": {
        "description": "Analyze business model options using lean canvas, business model canvas, startup canvas, and value proposition logic.",
        "argument": "<business idea, product, startup, or monetization question>",
        "uses": ["lean-canvas", "business-model", "startup-canvas", "value-proposition"],
        "outputs": ["business model canvas", "lean canvas", "assumption map", "validation plan"],
        "goal": "Make business model assumptions explicit and testable.",
        "workflow": ["Define customer and job.", "Map value creation and capture.", "Identify channels, cost drivers, revenue logic, and unfair advantage.", "Prioritize assumptions by risk.", "Recommend validation tests."],
    },
    "pricing": {
        "description": "Design pricing and packaging using value, willingness-to-pay, unit economics, competitive context, and experiments.",
        "argument": "<product, plan, pricing problem, or packaging choice>",
        "uses": ["pricing-strategy", "feature-investment-advisor", "saas-economics-efficiency-metrics"],
        "outputs": ["pricing options", "packaging logic", "tradeoff analysis", "experiment plan"],
        "goal": "Turn pricing into a testable product/business decision.",
        "workflow": ["Clarify buyer, user, value metric, and constraints.", "Generate pricing/packaging options.", "Assess value capture, complexity, fairness, and unit economics.", "Recommend a preferred path and validation experiment."],
    },
    "plan-okrs": {
        "description": "Draft outcome-based product OKRs aligned with strategy, customer outcomes, and measurable leading indicators.",
        "argument": "<team, product area, quarter, strategy, or planning context>",
        "uses": ["brainstorm-okrs", "north-star-metric"],
        "outputs": ["OKRs", "metric tree", "anti-metrics", "review cadence"],
        "goal": "Create OKRs that guide decisions instead of listing activities.",
        "workflow": ["Identify strategic theme and target outcome.", "Draft objectives in plain language.", "Create measurable KRs with baselines and targets.", "Add guardrail metrics and review cadence."],
    },
    "transform-roadmap": {
        "description": "Transform a feature-heavy roadmap into outcome themes, bets, learning milestones, and sequencing logic.",
        "argument": "<feature roadmap, backlog, or planning notes>",
        "uses": ["outcome-roadmap", "prioritization-frameworks"],
        "outputs": ["outcome roadmap", "sequencing rationale", "tradeoffs", "learning milestones"],
        "goal": "Move roadmap conversation from feature delivery to measurable outcomes.",
        "workflow": ["Cluster features into outcomes.", "Define customer/business impact per theme.", "Prioritize using a fit-for-context framework.", "Sequence bets by risk, dependency, confidence, and learning value."],
    },
    "plan-launch": {
        "description": "Create a launch plan with audience, positioning, channels, readiness, risks, metrics, and cross-functional owners.",
        "argument": "<feature, product, release, or launch context>",
        "uses": ["gtm-strategy", "launch-plan", "positioning-statement"],
        "outputs": ["launch plan", "readiness checklist", "messaging", "metrics", "risks"],
        "goal": "Make launch execution coordinated, measurable, and audience-specific.",
        "workflow": ["Define target audience and adoption goal.", "Write positioning and core message.", "Plan channels, enablement, comms, and owners.", "Set launch metrics, risks, rollback, and follow-up cadence."],
    },
    "ai-readiness": {
        "description": "Assess whether a product/business problem is AI-shaped and what proof is needed before building.",
        "argument": "<AI idea, product workflow, automation opportunity, or company context>",
        "uses": ["ai-readiness", "context-engineering", "recommendation-canvas"],
        "outputs": ["AI readiness assessment", "risk map", "proof-of-life plan", "build/no-build recommendation"],
        "goal": "Separate real AI leverage from AI theater and define the fastest proof path.",
        "workflow": ["Clarify user job and decision loop.", "Assess data, context, eval, UX, risk, and operations readiness.", "Identify proof-of-life probes and eval criteria.", "Recommend build, defer, or redesign."],
    },
}

SPECIAL_SKILLS: Dict[str, str] = {
    "pm-skills-select": """
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
""",
    "create-prd": """
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
""",
    "problem-statement": """
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
""",
    "brainstorm-ideas-new": """
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
""",
    "experiment-design": """
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
""",
    "prioritize-assumptions": """
## Gold-standard assumption prioritization
Rank assumptions by expected damage if wrong and uncertainty today.

### Categories
Assess desirability, usability, feasibility, viability, data quality, GTM, legal/compliance, operational readiness, and stakeholder alignment.

### Output contract
Create an Impact x Uncertainty table with priority, evidence currently available, best next test, and owner. Highlight leap-of-faith assumptions first.
""",
    "opportunity-solution-tree": """
## Gold-standard Opportunity Solution Tree
Build an OST from outcome to opportunities, solutions, and experiments.

### Structure
- Desired outcome and metric
- Opportunity branches based on customer needs/pains
- Solution candidates under each opportunity
- Experiment candidates under each solution
- Evidence strength and confidence notes

### Quality bar
Do not mix solutions into opportunities. Keep opportunity wording in user language. Show where evidence is thin.
""",
    "jobs-to-be-done": """
## Gold-standard JTBD analysis
Uncover the job, trigger, desired progress, alternatives, pains, gains, anxieties, and switching forces.

### Output contract
Produce a JTBD table with functional, emotional, and social jobs; struggling moments; current workaround; desired outcome; success metric; and product implications.
""",
    "interview-script": """
## Gold-standard interview script
Create a non-leading customer interview guide.

### Output contract
Include learning goals, screener, opening script, warm-up questions, timeline reconstruction, JTBD probes, evidence probes, anti-leading checks, closing questions, and synthesis tags.
""",
    "summarize-interview": """
## Gold-standard interview synthesis
Turn notes or transcripts into decision-ready insights.

### Output contract
Extract jobs, pains, gains, quotes, behaviors, current workarounds, objections, evidence strength, contradictions, opportunity areas, and follow-up questions. Label facts vs. interpretations.
""",
    "product-strategy": """
## Gold-standard product strategy
Create explicit choices, not a generic strategy document.

### Output contract
Cover target customer, problem, insight, value proposition, differentiated wedge, strategic choices, non-goals, business model, metrics, risks, moat, roadmap implications, and next proof points.
""",
    "product-vision": """
## Gold-standard product vision
Write an inspiring but choice-making vision.

### Output contract
Provide vision statement, customer transformation, why now, strategic principles, excluded futures, and evidence needed to believe it.
""",
    "value-proposition": """
## Gold-standard value proposition
Use JTBD logic: who, struggling moment, desired progress, current alternative, differentiated capability, proof, and before/after transformation.
""",
    "pricing-strategy": """
## Gold-standard pricing strategy
Evaluate value metric, buyer/user split, WTP, competitive anchors, packaging, unit economics, fairness, complexity, and testability. Recommend one preferred path plus experiments.
""",
    "outcome-roadmap": """
## Gold-standard outcome roadmap
Convert features into outcome themes, bets, metrics, learning milestones, and sequencing logic. Show what changes in user behavior and how the team will know.
""",
    "brainstorm-okrs": """
## Gold-standard OKRs
Create objectives that express strategic outcomes, not activity. KRs must include metric, baseline when known, target, owner, cadence, and guardrail/anti-metric.
""",
    "prioritization-frameworks": """
## Gold-standard prioritization advisor
Select the framework based on the decision: RICE for reach/impact tradeoffs, ICE for early uncertainty, MoSCoW for release scope, Kano for satisfaction, WSJF for cost of delay, opportunity scoring for discovery, and custom weighted scoring for portfolio choices.

Always explain why the chosen framework fits and where it can mislead.
""",
    "user-stories": """
## Gold-standard user stories
Write stories with the 3 Cs and INVEST. Include persona, job, acceptance criteria, edge cases, analytics events, dependencies, and split suggestions when stories are too large.
""",
    "test-scenarios": """
## Gold-standard test scenarios
Generate happy paths, edge cases, error states, permission states, data states, accessibility, abuse/misuse, analytics validation, and regression risks. Link scenarios to acceptance criteria.
""",
    "release-notes": """
## Gold-standard release notes
Write customer-facing notes in plain language. Include what changed, why it matters, who gets it, how to use it, limitations, migration impact, and support path.
""",
    "pre-mortem": """
## Gold-standard pre-mortem
Assume the initiative failed. Identify tigers, paper tigers, elephants, leading indicators, mitigations, owners, and kill/scope-change thresholds.
""",
    "stakeholder-map": """
## Gold-standard stakeholder map
Map stakeholders by power, interest, influence, incentives, concerns, decision rights, preferred communication, and risk of misalignment. Output a communication plan.
""",
    "north-star-metric": """
## Gold-standard North Star metric
Define the value-exchange metric that predicts durable customer and business value. Include input metrics, guardrails, segments, instrumentation needs, and anti-patterns.
""",
    "metrics-dashboard": """
## Gold-standard metrics dashboard
Design a decision-oriented dashboard: North Star, input metrics, guardrails, cohorts/segments, thresholds, ownership, refresh cadence, and action playbook for metric movement.
""",
    "ai-readiness": """
## Gold-standard AI readiness
Assess user value, data/context quality, eval feasibility, reliability tolerance, UX trust, cost/latency, risk/compliance, operations, and proof-of-life path. Recommend build, defer, or redesign.
""",
    "context-engineering": """
## Gold-standard context engineering
Map the AI task, user goal, required context, retrieval sources, freshness, tool calls, memory, evaluation cases, failure modes, and context budget. Output a context architecture and eval plan.
""",
    "recommendation-canvas": """
## Gold-standard recommendation canvas
Define user goal, candidate universe, ranking signals, constraints, feedback loops, cold start, explanation UX, diversity/fairness, metrics, and evaluation plan.
""",
}

MARKETPLACE_JSON = {
    "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
    "name": "pm-skill-lap",
    "version": VERSION,
    "description": "PM Skills Like A Pro: gold-standard Claude Code marketplace synthesizing phuryn/pm-skills and deanpeters/Product-Manager-Skills into PM plugins, skills, and workflows with /pm-skills-select as the router.",
    "owner": {"name": "Bruno Cardone", "email": "bruno.cardone@sensapartners.com"},
    "plugins": [
        {
            "name": plugin,
            "displayName": str(meta["displayName"]),
            "description": str(meta["description"]),
            "version": VERSION,
            "source": f"./plugins/{plugin}",
            "category": str(meta["category"]),
            "tags": list(meta["keywords"]),
        }
        for plugin, meta in PLUGIN_META.items()
    ],
}


def backup(path: Path) -> None:
    if not path.exists():
        return
    rel = path.relative_to(ROOT)
    target = BACKUP_DIR / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    if path.is_dir():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(path, target)
    else:
        shutil.copy2(path, target)


def write_text(path: Path, content: str, executable: bool = False) -> None:
    if path.exists():
        current = path.read_text(encoding="utf-8")
        if current == content:
            if executable:
                path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            return
        backup(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            raw = text[4:end].strip().splitlines()
            body = text[end + len("\n---") :].lstrip("\n")
            data: Dict[str, str] = {}
            for line in raw:
                if ":" in line:
                    k, v = line.split(":", 1)
                    data[k.strip()] = v.strip().strip('"').strip("'")
            return data, body
    return {}, text


def slug_to_title(slug: str) -> str:
    special = {"prd": "PRD", "okrs": "OKRs", "gtm": "GTM", "jtbd": "JTBD", "ai": "AI", "saas": "SaaS", "sql": "SQL"}
    return " ".join(special.get(w.lower(), w.capitalize()) for w in slug.replace("_", "-").split("-"))


def extract_list_section(body: str, header: str) -> List[str]:
    pattern = rf"##\s+{re.escape(header)}\s*\n(.*?)(?=\n##\s+|\Z)"
    m = re.search(pattern, body, flags=re.S | re.I)
    if not m:
        return []
    return [line.strip()[2:].strip() for line in m.group(1).splitlines() if line.strip().startswith("- ")]


def extract_purpose(body: str, fallback: str) -> str:
    m = re.search(r"##\s+Purpose\s*\n(.*?)(?=\n##\s+|\Z)", body, flags=re.S | re.I)
    if m:
        text = " ".join([ln.strip() for ln in m.group(1).splitlines() if ln.strip() and not ln.strip().startswith("#")])
        if text:
            return text[:700]
    return fallback


def clean_description(desc: str, name: str) -> str:
    desc = re.sub(r"\s+", " ", (desc or "").strip()) or f"Use {name} for product-management work."
    if "use when" not in desc.lower():
        desc += " Use when the user asks for this PM framework, artifact, analysis, or workflow."
    return desc


def make_skill_body(path: Path, plugin_name: str) -> str:
    original = read_text(path)
    fm, body = parse_frontmatter(original)
    name = fm.get("name") or path.parent.name
    desc = clean_description(fm.get("description", ""), name)
    purpose = extract_purpose(body, desc)
    outputs = extract_list_section(body, "Outputs") or ["decision-ready PM artifact", "assumptions", "risks", "recommended next step"]
    use_when = extract_list_section(body, "Use this when") or ["the user needs this PM artifact or framework", "the request maps to the skill description"]
    source_mix = extract_list_section(body, "Source mix")
    aliases = []
    m_alias = re.search(r"##\s+Aliases and merged source skills\s*\n(.*?)(?=\n##\s+|\Z)", body, flags=re.S | re.I)
    if m_alias:
        aliases = [ln.strip() for ln in m_alias.group(1).splitlines() if ln.strip()]
    special = SPECIAL_SKILLS.get(name, "")
    title = slug_to_title(name)
    outputs_md = "\n".join(f"- {x}" for x in outputs)
    use_when_md = "\n".join(f"- {x}" for x in use_when)
    source_md = "\n".join(f"- {x}" for x in source_mix) if source_mix else "- LAP gold-standard synthesis"
    alias_md = "\n".join(aliases) if aliases else "- None"
    default_contract = "## Default artifact contract\nProduce a structured artifact with: context, assumptions, framework application, table or canvas where useful, recommendation, risks, open questions, and next action."
    return textwrap.dedent(f"""\
    ---
    name: {name}
    description: {desc}
    ---

    # {title}

    ## Purpose
    {purpose}

    ## Use this when
    {use_when_md}

    ## Outputs
    {outputs_md}

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

    {special.strip() if special else default_contract}

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
    {alias_md}

    ## Source mix
    {source_md}
    """)


def parse_command_name(path: Path, text: str) -> str:
    fm, body = parse_frontmatter(text)
    if fm.get("name"):
        return fm["name"].strip().lstrip("/")
    m = re.search(r"#\s*/?([a-z0-9][a-z0-9-]*)", body or text)
    if m:
        return m.group(1)
    return path.stem


def parse_skill_chain(text: str) -> List[str]:
    chain = []
    for match in re.finditer(r"`([a-z0-9][a-z0-9-]+)`", text):
        token = match.group(1)
        if token not in chain and not token.startswith("pm-"):
            chain.append(token)
    return chain[:8]


def make_command_body(path: Path) -> str:
    original = read_text(path)
    name = parse_command_name(path, original)
    data = COMMANDS.get(name, {})
    desc = str(data.get("description") or f"Run the {name} PM workflow and produce a decision-ready artifact.")
    arg = str(data.get("argument") or "<PM context>")
    uses = list(data.get("uses") or parse_skill_chain(original) or [name])
    outputs = list(data.get("outputs") or ["PM artifact", "assumptions", "risks", "next step"])
    goal = str(data.get("goal") or f"Execute /{name} as a structured PM workflow.")
    workflow = list(data.get("workflow") or [
        "Clarify the PM situation and expected artifact.",
        "Load or apply the listed skills in order.",
        "Produce the artifact directly when context is sufficient.",
        "Label assumptions, risks, and open questions.",
        "Recommend the next command.",
    ])
    uses_md = "\n".join(f"  - {x}" for x in uses)
    outputs_md = "\n".join(f"  - {x}" for x in outputs)
    workflow_md = "\n".join(f"{i+1}. {x}" for i, x in enumerate(workflow))
    return textwrap.dedent(f"""\
    ---
    name: {name}
    description: {desc}
    argument-hint: "{arg}"
    uses:
{uses_md}
    outputs:
{outputs_md}
    ---

    # /{name}

    ## Goal
    {goal}

    ## Inputs
    Accept a direct prompt, pasted notes, files, links, data excerpts, or rough context. If inputs are incomplete, proceed with labeled assumptions unless the missing information would materially change the artifact.

    ## Workflow
    {workflow_md}

    ## Execution rules
    - Prefer doing the work over only explaining the workflow.
    - Ask at most 3 targeted questions, and only when needed to avoid a materially wrong output.
    - Use tables or canvases when they make decisions easier.
    - Separate facts, assumptions, recommendations, risks, and open questions.
    - If the output is substantial, create a Markdown-ready artifact with a clear title and sections.

    ## Final output
    Produce:
{outputs_md}

    ## Next step
    End with one recommended follow-on command or skill.
    """)


def update_marketplace() -> None:
    write_text(ROOT / ".claude-plugin" / "marketplace.json", json.dumps(MARKETPLACE_JSON, indent=2, ensure_ascii=False) + "\n")


def update_plugin_manifests() -> None:
    plugins_dir = ROOT / "plugins"
    if not plugins_dir.exists():
        print("ERROR: plugins/ directory not found. Run this from the pm-skill-lap repo root.", file=sys.stderr)
        sys.exit(1)
    for plugin_dir in sorted(p for p in plugins_dir.iterdir() if p.is_dir()):
        name = plugin_dir.name
        meta = PLUGIN_META.get(name, {
            "displayName": slug_to_title(name),
            "description": f"PM Skill LAP plugin for {slug_to_title(name)} workflows.",
            "keywords": ["product-management", name],
        })
        manifest = {
            "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
            "name": name,
            "displayName": meta["displayName"],
            "version": VERSION,
            "description": meta["description"],
            "author": {"name": "Bruno Cardone", "email": "bruno.cardone@sensapartners.com"},
            "repository": "https://github.com/brunocardone/pm-skill-lap",
            "license": "CC-BY-NC-SA-4.0",
            "keywords": meta["keywords"],
        }
        write_text(plugin_dir / ".claude-plugin" / "plugin.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def update_skills() -> int:
    count = 0
    for skill_file in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md")):
        plugin_name = skill_file.parts[-4]
        write_text(skill_file, make_skill_body(skill_file, plugin_name))
        count += 1
    return count


def update_commands() -> int:
    count = 0
    for command_file in sorted((ROOT / "plugins").glob("*/commands/*.md")):
        write_text(command_file, make_command_body(command_file))
        count += 1
    local = ROOT / ".claude" / "commands" / "pm-skills-select.md"
    write_text(local, make_command_body(local))
    count += 1
    return count


def write_scripts() -> None:
    write_text(ROOT / "scripts" / "validate-pm-lap.sh", VALIDATE_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "build-skill-zips.sh", BUILD_SKILL_ZIPS_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "build-plugin-zips.sh", BUILD_PLUGIN_ZIPS_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "build-claude-desktop-packs.sh", BUILD_CLAUDE_PACKS_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "build-codex-package.sh", BUILD_CODEX_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "build-release.sh", BUILD_RELEASE_SCRIPT, executable=True)
    write_text(ROOT / "scripts" / "print-catalog.py", PRINT_CATALOG_SCRIPT, executable=True)


def write_docs() -> None:
    write_text(ROOT / "docs" / "GOLD-STANDARD-OPERATING-MODE.md", GOLD_STANDARD_DOC)
    write_text(ROOT / "docs" / "INSTALL-CLAUDE-CODE.md", INSTALL_CLAUDE_CODE_DOC)
    write_text(ROOT / "docs" / "RELEASE-PACKAGING.md", RELEASE_PACKAGING_DOC)
    write_text(ROOT / "docs" / "INSTALL-CLAUDE-DESKTOP.md", INSTALL_CLAUDE_DESKTOP_DOC)
    write_text(ROOT / "docs" / "INSTALL-CODEX.md", INSTALL_CODEX_DOC)
    write_text(ROOT / ".github" / "workflows" / "validate-and-release.yml", CI_WORKFLOW)


def main() -> None:
    if not (ROOT / ".claude-plugin" / "marketplace.json").exists() or not (ROOT / "plugins").exists():
        print("ERROR: Run this script from the root of brunocardone/pm-skill-lap.", file=sys.stderr)
        sys.exit(1)
    print("PM Skill LAP Gold Upgrade")
    print(f"Repo: {ROOT}")
    update_marketplace()
    update_plugin_manifests()
    skill_count = update_skills()
    command_count = update_commands()
    write_scripts()
    write_docs()
    print(f"Updated {skill_count} skill files")
    print(f"Updated {command_count} command files")
    print("Wrote scripts, docs, marketplace, plugin manifests, and CI workflow")
    if BACKUP_DIR.exists():
        print(f"Backup: {BACKUP_DIR.relative_to(ROOT)}")
    print("\nNext commands:")
    print("  bash scripts/validate-pm-lap.sh")
    print("  bash scripts/build-release.sh")
    print("  git diff --stat")
    print("  git add . && git commit -m 'Upgrade PM Skill LAP gold standard marketplace' && git push")


VALIDATE_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[1/4] JSON syntax"
python3 - <<'PYVALIDATE'
import json
from pathlib import Path
for p in [Path('.claude-plugin/marketplace.json')] + sorted(Path('plugins').glob('*/.claude-plugin/plugin.json')):
    with p.open(encoding='utf-8') as f:
        json.load(f)
    print(f"ok {p}")
PYVALIDATE

echo "[2/4] Required marketplace/plugin paths"
test -f .claude-plugin/marketplace.json
for plugin in plugins/*; do
  [ -d "$plugin" ] || continue
  test -f "$plugin/.claude-plugin/plugin.json"
  test -d "$plugin/skills" || echo "warning: $plugin has no skills/"
  if [ -d "$plugin/commands" ]; then
    find "$plugin/commands" -maxdepth 1 -name '*.md' -print | grep -q . || echo "warning: $plugin/commands has no .md files"
  fi
done

echo "[3/4] Markdown frontmatter sanity"
python3 - <<'PYFRONTMATTER'
from pathlib import Path
bad=[]
for p in list(Path('plugins').glob('*/skills/*/SKILL.md')) + list(Path('plugins').glob('*/commands/*.md')):
    s=p.read_text(encoding='utf-8')
    if not s.startswith('---\n') or '\n---\n' not in s[4:]:
        bad.append(str(p))
if bad:
    print('\n'.join(bad))
    raise SystemExit('frontmatter missing or malformed')
print('ok frontmatter')
PYFRONTMATTER

echo "[4/4] Claude Code validation when available"
if command -v claude >/dev/null 2>&1; then
  claude plugin validate .
  for plugin in plugins/*; do
    [ -d "$plugin" ] || continue
    claude plugin validate "$plugin" --strict
  done
else
  echo "claude CLI not found; skipped Claude-native validation"
fi

echo "Validation complete."
'''

BUILD_SKILL_ZIPS_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/skill-zips"
rm -rf "$OUT"
mkdir -p "$OUT"
if ! command -v zip >/dev/null 2>&1; then
  echo "Error: zip not found. Install zip and retry." >&2
  exit 1
fi
count=0
for skill_file in "$ROOT"/plugins/*/skills/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  tmp="$(mktemp -d)"
  cp -R "$skill_dir" "$tmp/$skill_name"
  (cd "$tmp" && zip -qr "$OUT/$skill_name.zip" "$skill_name")
  rm -rf "$tmp"
  count=$((count+1))
done
echo "Created $count skill ZIPs in dist/skill-zips"
'''

BUILD_PLUGIN_ZIPS_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/plugins"
rm -rf "$OUT"
mkdir -p "$OUT"
if ! command -v zip >/dev/null 2>&1; then
  echo "Error: zip not found. Install zip and retry." >&2
  exit 1
fi
count=0
for plugin_dir in "$ROOT"/plugins/*; do
  [ -d "$plugin_dir" ] || continue
  plugin_name="$(basename "$plugin_dir")"
  (cd "$ROOT/plugins" && zip -qr "$OUT/$plugin_name.zip" "$plugin_name")
  count=$((count+1))
done
echo "Created $count plugin ZIPs in dist/plugins"
'''

BUILD_CLAUDE_PACKS_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_ZIPS="$ROOT/dist/skill-zips"
OUT="$ROOT/dist/claude-desktop"
mkdir -p "$OUT"
bash "$ROOT/scripts/build-skill-zips.sh" >/dev/null
pack() {
  local zip_name="$1"; shift
  local tmp="$(mktemp -d)"
  local count=0
  for skill in "$@"; do
    if [ -f "$SKILL_ZIPS/$skill.zip" ]; then
      cp "$SKILL_ZIPS/$skill.zip" "$tmp/"
      count=$((count+1))
    else
      echo "warning: missing skill zip $skill.zip" >&2
    fi
  done
  if [ "$count" -eq 0 ]; then
    echo "error: pack $zip_name would be empty" >&2
    exit 1
  fi
  (cd "$tmp" && zip -qr "$OUT/$zip_name" .)
  rm -rf "$tmp"
  echo "Created $zip_name ($count skills)"
}
pack 01-core-pm-starter-pack.zip pm-skills-select problem-statement jobs-to-be-done prioritization-frameworks create-prd outcome-roadmap product-strategy
cp "$OUT/01-core-pm-starter-pack.zip" "$OUT/pm-skills-starter-pack.zip"
pack 02-discovery-pack.zip discovery-process problem-statement jobs-to-be-done opportunity-solution-tree interview-script summarize-interview experiment-design prioritize-assumptions
pack 03-strategy-pack.zip product-strategy product-vision value-proposition positioning-statement pricing-strategy lean-canvas business-model
pack 04-delivery-pack.zip create-prd user-stories test-scenarios outcome-roadmap brainstorm-okrs sprint-plan release-notes
pack 05-ai-pm-pack.zip ai-readiness context-engineering recommendation-canvas experiment-design metrics-dashboard
(cd "$SKILL_ZIPS" && zip -qr "$OUT/99-all-skills-pack.zip" .)
echo "Claude Desktop/Web packs ready in dist/claude-desktop"
'''

BUILD_CODEX_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/codex"
SKILLS_OUT="$OUT/.agents/skills"
rm -rf "$OUT"
mkdir -p "$SKILLS_OUT"
count=0
for skill_file in "$ROOT"/plugins/*/skills/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  rm -rf "$SKILLS_OUT/$skill_name"
  cp -R "$skill_dir" "$SKILLS_OUT/$skill_name"
  count=$((count+1))
done
cat > "$OUT/AGENTS.md" <<'EOFAGENTS'
# PM Skill LAP for Codex

Use the skills in `.agents/skills` as reusable PM workflows. Start with `pm-skills-select` when the user is unsure which PM framework or artifact is needed.
EOFAGENTS
(cd "$OUT" && zip -qr "$ROOT/dist/codex/pm-skill-lap-codex.zip" .agents AGENTS.md)
echo "Created Codex package with $count skills in dist/codex"
'''

BUILD_RELEASE_SCRIPT = r'''#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
VERSION="$(python3 - <<'PYVERSION'
import json
print(json.load(open('.claude-plugin/marketplace.json')).get('version','dev'))
PYVERSION
)"
DIST="$ROOT/dist"
RELEASE="$DIST/release"

echo "[1/5] Validate"
bash scripts/validate-pm-lap.sh

echo "[2/5] Build skill ZIPs"
bash scripts/build-skill-zips.sh

echo "[3/5] Build Claude Desktop/Web packs"
bash scripts/build-claude-desktop-packs.sh

echo "[4/5] Build plugin ZIPs and Codex package"
bash scripts/build-plugin-zips.sh
bash scripts/build-codex-package.sh

echo "[5/5] Build master release artifact"
rm -rf "$RELEASE"
mkdir -p "$RELEASE/docs"
cp -R .claude-plugin "$RELEASE/.claude-plugin"
cp -R plugins "$RELEASE/plugins"
cp -R dist/skill-zips "$RELEASE/skill-zips"
cp -R dist/claude-desktop "$RELEASE/claude-desktop"
cp -R dist/plugins "$RELEASE/plugin-zips"
cp -R dist/codex "$RELEASE/codex"
cp README.md "$RELEASE/README.md"
cp docs/INSTALL-CLAUDE-CODE.md docs/INSTALL-CLAUDE-DESKTOP.md docs/INSTALL-CODEX.md docs/RELEASE-PACKAGING.md docs/GOLD-STANDARD-OPERATING-MODE.md "$RELEASE/docs/"
artifact="$DIST/pm-skill-lap-$VERSION-release.zip"
rm -f "$artifact"
(cd "$RELEASE" && zip -qr "$artifact" .)
echo "Release artifact: $artifact"
'''

PRINT_CATALOG_SCRIPT = r'''#!/usr/bin/env python3
import json
from pathlib import Path
market=json.load(open('.claude-plugin/marketplace.json', encoding='utf-8'))
print(f"# {market['name']} v{market.get('version','')}")
for p in market['plugins']:
    root=Path(p['source'].replace('./',''))
    skills=sorted(x.parent.name for x in root.glob('skills/*/SKILL.md'))
    commands=sorted(x.stem for x in root.glob('commands/*.md'))
    print(f"\n## {p['name']}")
    print(p.get('description',''))
    print(f"Skills ({len(skills)}): " + ', '.join(skills))
    print(f"Commands ({len(commands)}): " + ', '.join('/'+c for c in commands))
'''

GOLD_STANDARD_DOC = '''# PM Skill LAP Gold-Standard Operating Mode

This repository is a Claude Code marketplace for product-management work. It synthesizes two useful patterns:

1. **phuryn/pm-skills**: plugin marketplace architecture, command chaining, PM execution artifacts, and Markdown-first workflow outputs.
2. **deanpeters/Product-Manager-Skills**: pedagogic-first skill design, rich framework explanations, release packaging, Claude Desktop/Web skill ZIPs, and Codex portability.

## Design principles

- Keep `pm-skills-select` as the front door.
- Prefer executable PM artifacts over explanations.
- Ask fewer questions; proceed with labeled assumptions when possible.
- Teach the framework briefly while producing the artifact.
- Separate facts, assumptions, recommendations, risks, and open questions.
- Save substantial outputs as Markdown-ready artifacts.
- Keep plugin manifests strict and minimal; use default `skills/` and `commands/` discovery.

## Skill quality bar

Every skill should produce a concrete PM deliverable, include tradeoffs, and recommend one next workflow. Generic advice is a defect.

## Workflow quality bar

Every command should include frontmatter, a skill chain, final outputs, execution rules, and a next step. A command should do work directly when context is sufficient.
'''

INSTALL_CLAUDE_CODE_DOC = '''# Install PM Skill LAP in Claude Code

## From GitHub

```bash
claude plugin marketplace add brunocardone/pm-skill-lap
claude plugin marketplace update pm-skill-lap
claude plugin install pm-skills-select@pm-skill-lap
```

Install the full marketplace when desired:

```bash
for plugin in \
  pm-product-discovery-lap \
  pm-product-strategy-lap \
  pm-execution-lap \
  pm-market-research-lap \
  pm-data-analytics-lap \
  pm-go-to-market-lap \
  pm-marketing-growth-lap \
  pm-finance-saas-lap \
  pm-ai-product-lap \
  pm-career-leadership-lap \
  pm-toolkit-lap; do
  claude plugin install "$plugin@pm-skill-lap"
done
```

## Local development install

From the parent directory of this repo:

```bash
claude plugin marketplace add ./pm-skill-lap --scope local
claude plugin install pm-skills-select@pm-skill-lap --scope local
claude plugin validate ./pm-skill-lap
```

## Usage

Start with:

```text
/pm-skills-select:pm-skills-select <your PM situation>
```

Plugin skills are namespaced with the plugin name. Examples:

```text
/pm-product-discovery-lap:problem-statement Frame the onboarding problem for SMB users
/pm-execution-lap:create-prd Create a PRD for guided onboarding
/pm-product-strategy-lap:product-strategy Build a strategy for our AI onboarding assistant
```

Commands can also be invoked from installed plugins. If in doubt, use `/pm-skills-select` first.
'''

RELEASE_PACKAGING_DOC = '''# Release Packaging

`plugins/` is the source of truth. Generated artifacts live under `dist/`.

## Validate

```bash
bash scripts/validate-pm-lap.sh
```

## Build everything

```bash
bash scripts/build-release.sh
```

## Generated artifacts

```text
dist/
  skill-zips/                 # one upload-ready ZIP per skill
  claude-desktop/             # curated packs of skill ZIPs
  plugins/                    # one ZIP per Claude Code plugin
  codex/                      # .agents/skills package for Codex-style agents
  release/                    # assembled release tree
  pm-skill-lap-<version>-release.zip
```

## Release process

```bash
bash scripts/validate-pm-lap.sh
bash scripts/build-release.sh
git add .
git commit -m "Release PM Skill LAP v2.1.0"
git tag v2.1.0
git push origin main --tags
```

## Rules

- Do not edit `dist/` manually.
- Bump versions in `.claude-plugin/marketplace.json` and plugin manifests before releases.
- Run `claude plugin validate .` and `claude plugin validate ./plugins/<plugin> --strict` before publishing.
- Preserve `pm-skills-select` as the primary entrypoint.
'''

INSTALL_CLAUDE_DESKTOP_DOC = '''# Install PM Skill LAP in Claude Desktop/Web as custom skills

Run:

```bash
bash scripts/build-claude-desktop-packs.sh
```

Then open `dist/claude-desktop/`.

Recommended start:

1. Download or open `pm-skills-starter-pack.zip`.
2. Unzip it.
3. Upload the individual skill ZIPs inside to Claude custom skills.
4. Ask Claude to use `pm-skills-select` first when unsure.

The all-skills pack is `99-all-skills-pack.zip`.
'''

INSTALL_CODEX_DOC = '''# Install PM Skill LAP for Codex-style agents

Run:

```bash
bash scripts/build-codex-package.sh
```

Use the generated package:

```text
dist/codex/pm-skill-lap-codex.zip
```

It contains:

```text
.agents/skills/<skill-name>/SKILL.md
AGENTS.md
```
'''

CI_WORKFLOW = '''name: Validate PM Skill LAP

on:
  pull_request:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  validate-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install zip
        run: sudo apt-get update && sudo apt-get install -y zip
      - name: Validate repository
        run: bash scripts/validate-pm-lap.sh
      - name: Build release artifacts
        run: bash scripts/build-release.sh
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: pm-skill-lap-dist
          path: dist/
'''

if __name__ == "__main__":
    main()
