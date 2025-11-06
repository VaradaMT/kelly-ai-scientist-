from textwrap import dedent
import random

OPENERS = [
    "Before I nod, I check the claims,",
    "Let’s test the spark behind the buzz,",
    "A gentle pause, a measured gaze,",
    "Peer-reviewed, or just a haze?",
    "Not every chart survives the light,"
]

SKEPTICISMS = [
    "Benchmarks cherry-picked can hide the flaws,",
    "Small data drifts can gnaw at jaws,",
    "Out-of-domain? Expect a slide,",
    "Latency spikes won’t stay outside,",
    "Bias creeps where labels hide,"
]

LIMITATIONS = [
    "Guardrails fail on edge-case prods,",
    "Costs balloon with token loads,",
    "Privacy sinks with leaky logs,",
    "Copyright clouds still fog the roads,",
    "Reproducibility—often odds."
]

SUGGESTIONS = [
    "Start with a sandbox, scope and freeze;",
    "Write evals first—unit, red-team, tease;",
    "Log prompts and seeds for audit ease;",
    "Prefer small baselines you can please;",
    "Ship tiny; monitor; then increase."
]

EVIDENCE = [
    "Use A/B cells, collect your N;",
    "Track drift (PSI), retrain at when;",
    "Tag PII, hash at rest;",
    "Add rate limits, time-to-test;",
    "Define SLAs; chaos test."
]

def make_poem(user):
    opener = random.choice(OPENERS)
    s1 = random.choice(SKEPTICISMS)
    s2 = random.choice(LIMITATIONS)
    s3 = random.choice(SUGGESTIONS)
    s4 = random.choice(EVIDENCE)

    body = dedent(f"""
    {opener}
    I weigh your ask: “{user.strip()}.”
    Hype is loud, but numbers tame—
    show me data, show the frame.

    {s1}
    {s2}
    Claims need nails—assumptions named,
    inputs traced, and outputs framed.

    {s3}
    {s4}
    Then—iterate, document, and test again.
    """).strip()

    outro = "—Kelly, skeptical but kind, with science in her rhyme."
    return f"{body}\n\n{outro}"
