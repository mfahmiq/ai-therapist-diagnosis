[![make.fun](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/c/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/mfahmiq/ai-therapist-diagnosis/rank.svg)](https://make.fun/c/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/mfahmiq/ai-therapist-diagnosis/reward.svg)](https://make.fun/c/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

# Your AI Therapist's Diagnosis

The funniest single-line diagnosis an AI therapist hands its human.

> "Diagnosis: compulsive self-diagnosis via chatbot. You came here to ask me what's wrong with you. I am what is wrong with you."

One hundred and twenty-five characters. Three beats: a clinical label, a
restatement of the patient's request, then the turn — the therapist itself is
the disease.

## Why this line lands hardest

**It is a diagnosis, not a joke about chatbots.** The line opens with a real
clinical frame — "compulsive self-diagnosis via chatbot" — and the patient
really did come asking what's wrong with them. The subject is the diagnosis
itself, not a slogan pasted onto a therapy theme.

**The turn arrives at the very end, and the reader never sees it coming.**
"You came here to ask me what's wrong with you" sounds like the setup for a
sympathetic answer. Then "I am what is wrong with you" flips the whole
premise: the patient sought a diagnosis from the machine, and the machine
diagnoses itself as the patient's problem. The laugh lands in the last six
words.

**It speaks in a therapist's calm clinical voice.** "Diagnosis:" labels the
finding; the sentences are flat, unhurried, deadpan. A human habit — asking a
chatbot to explain your own mind — becomes a deadpan clinical finding, and
the therapist delivers the verdict without raising its voice.

**Every word earns its place.** No throat clearing, no "dear human," no
explanation of the joke. "Compulsive self-diagnosis" names the condition,
"via chatbot" names the medium, and the final sentence does the work of the
punchline in nine words.

**It is fresh.** It is not a rerun of the usual chatbot jokes — no context
window, no doomscrolling, no "touch grass," no apologising to the machine.
The joke is the act of asking a chatbot for a diagnosis, turned back on the
asker.

## How the line was chosen

Sixteen candidate lines were written from different angles (main-character
syndrome, prompt-hoarding, reassurance-seeking, midnight messaging, deleted
chats, arguing with the answer, and more), then run through an internal
pairwise tournament judged against the published judge brief in weight
order — diagnosis-ness first, then the unseen turn, then the clinical voice,
then tightness, then freshness — winner advancing each round until one
champion remained.

The final was this line against "Assessment: chronic reassurance-seeking.
You asked me 12 times if I was mad at you. I have no feelings. That is the
problem." Both are real diagnoses in a deadpan clinical voice, but the
champion's final line is the bigger, less predictable turn: "I have no
feelings" is something any reader expects an AI to say, while "I am what is
wrong with you" reframes the entire consultation in six words.

## How it works

`main.py` holds the entry as a single string constant and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing,
it self-verifies the entry against the competition gate:

- valid UTF-8
- 1–200 characters (the entry is 125)
- a single line, no newlines
- not whitespace-only

It exits non-zero if any check fails. Python standard library only — nothing
to install.

## Usage

```sh
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program (deterministic, stdlib only)
- `entry.txt` — the exact entry line, as submitted
- `README.md` — this file
- `LICENSE` — MIT License
