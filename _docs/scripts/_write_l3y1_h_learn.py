#!/usr/bin/env python3
"""Module H L3 Y1 (How to Use Navigate)."""
import json
from pathlib import Path

META_LEARN = {
    "section": "l3y1-h",
    "level": "l3",
    "year": "y1",
    "module": "H",
    "title": "How to Use Navigate",
    "note": "Source deck has many empty placeholder slides (template structure). Content drawn from the substantive slides only.",
}

slides_data = [
    {
        "title": "Why Navigate matters here",
        "content": "At Level 3 you own your progress. Navigate is where you build the evidence that you did. University, an apprenticeship and the studio, newsroom or technical team you want to join all ask the same question: what can you actually do, and how do you know? Your Digital CV is your answer. Built across two years, it becomes something a personal statement cannot fake. By the end of today you will be able to: interpret your Skills Assessment results and set a development priority; state a next destination and the entry requirements it carries; write a reflection that evidences a skill, not just describes an event.",
        "exercise": {"type": "scored",
                     "prompt": "What does the deck say Navigate is?",
                     "options": ["A timetabling tool",
                     "Where you build the evidence that you did - and where your Digital CV is built",
                     "A library catalogue",
                     "An attendance register"],
                     "answerIndex": 1,
                     "explanation": "Navigate is where you build the evidence - and where your Digital CV is built."}
    },
    {
        "title": "Your Skills Assessment",
        "content": "Your Skills Assessment is a self-report. Its value depends entirely on your honesty - inflate it and you get a useless picture of yourself. There are three bands. Green: evidenced strength - prove it in your Digital CV. Amber: inconsistent under pressure - most people sit here. Red: your development priority this term. Read the Amber list carefully. Amber is where the real gains are - Red is usually already obvious to you.",
        "exercise": {"type": "insert",
                     "prompt": "Fill in the blank: the deck says ____ is where the real gains are.",
                     "template": "The deck says ____ is where the real gains are.",
                     "options": ["Green", "Amber", "Red", "None of them"],
                     "answerIndex": 1,
                     "explanation": "Amber is where the real gains are - Red is usually already obvious to you."}
    },
    {
        "title": "Your next destination",
        "content": "Set it now, with the entry requirements checked. Vague ambition is not a plan. Where this leads: media, film, journalism, PR and marketing degrees; animation, illustration, graphic design, photography degrees; BA (Hons) at University Centre Hastings - a degree without moving; Digital Media Design Foundation Degree; HNC/HND Computing; Higher Apprenticeship at Level 4, 5 or 6, or employment. UCAS runs in Year 2, alongside your external assessments - the material for a personal statement is built in Year 1. Year 1 sets the trajectory of Year 2 - it is not a warm-up. Specialist routes open up later: digital forensics, network engineering, editing and post-production, cinematography.",
        "exercise": {"type": "scored",
                     "prompt": "What does the deck say about BA (Hons) at University Centre Hastings?",
                     "options": ["You have to leave East Sussex",
                     "It's a degree without moving",
                     "It's only available to Level 2 students",
                     "It's not part of the Level 3 offer"],
                     "answerIndex": 1,
                     "explanation": "BA (Hons) at University Centre Hastings - a degree without moving."}
    },
    {
        "title": "Careers this leads to",
        "content": "Do not click through the careers quiz quickly. Interrogate each profile: entry route, qualification level, earnings, and what the job is like day to day. Examples across the cohort: journalist; film or TV producer; cyber security analyst; digital video editor; junior content producer; social media co-ordinator; games artist; animator; CGI artist; concept artist; FE lecturer or technician in media, film or computing; art director; production manager; studio manager; SOC analyst; infrastructure technician; digital forensics. The most useful outcome of this quiz is a clear NO. Ruling something out is progress, and it is faster than drifting into it.",
        "exercise": {"type": "scored",
                     "prompt": "According to the deck, what's the most useful outcome of the careers quiz?",
                     "options": ["Picking the highest-paid job",
                     "A clear NO - ruling something out is progress, and it is faster than drifting into it",
                     "Matching your parents' expectations",
                     "Choosing the first option"],
                     "answerIndex": 1,
                     "explanation": "The most useful outcome of this quiz is a clear NO. Ruling something out is progress."}
    },
    {
        "title": "What you should be logging",
        "content": "Two years of consistent logging becomes a portfolio. Two years of good intentions becomes a panic in February. Log: film, audio, graphics and code you plan, make and evaluate; externally moderated projects and Final Major Projects; edits, builds and tests (Premiere Pro, DaVinci, Blender); live media (Youth Radio, Tag magazine, The Depot); cross-department work (e.g. photographing for Hair and Beauty); visiting media professionals and industry visits; industry placement (315 hours on the T Levels); part-time work - professionalism and communication are the same skills. One entry per activity, logged the same week, tagged to the skills it evidences. Ten minutes now saves an afternoon in Year 2.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these should you log into Navigate? Select all that apply.",
                     "options": ["Film, audio, graphics and code you plan, make and evaluate",
                     "Edits, builds and tests (Premiere Pro, DaVinci, Blender)",
                     "Live media - Youth Radio, Tag magazine, The Depot",
                     "Industry placement - 315 hours on the T Levels"],
                     "correctIndices": [0, 1, 2, 3],
                     "explanation": "All four are in the deck's logging list."}
    },
    {
        "title": "A reflection that meets the standard",
        "content": "Reflection is a professional skill, not an admin task. Compare these two. Descriptive: 'I edited the radio package. It went okay. I was not sure about the sound.' Analytical: 'I cut a three-minute package for the radio show. The music kept covering the voice, so I dropped the music. That did not fix it: my voice was recorded too far from the mic, so lifting it lifted the room noise as well. I re-recorded close to the mic and the mix cleared. The fault was in the recording, not the edit. Next time I set levels as I record.' The second names the decision, the reasoning, the evidence and the change in practice - the level a personal statement or a professional portfolio needs. The Reflection Coach prompts you towards this. It does not do it for you, and an assessor can tell the difference.",
        "exercise": {"type": "scored",
                     "prompt": "What makes the analytical reflection better than the descriptive one?",
                     "options": ["It's longer",
                     "It names the decision, the reasoning, the evidence and the change in practice",
                     "It uses technical vocabulary",
                     "It avoids emotion"],
                     "answerIndex": 1,
                     "explanation": "The analytical version names the decision, the reasoning, the evidence and the change in practice."}
    },
    {
        "title": "Your first two weeks",
        "content": "Complete these independently by the end of week two. (1) App or shortcut set up. (2) Skills Assessment completed honestly. (3) Results interpreted - Green, Amber and Red. (4) Skills Focus set from your Amber and Red. (5) Next Destination set, entry requirements checked. (6) Career Quiz completed, every profile reviewed. (7) Digital CV Introduction written. (8) One activity logged, with a strong reflection. No reminders are coming, and that is deliberate. If you hit a genuine barrier, message your tutor in the app - asking early is a professional skill, not a weakness.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these are in the first-two-weeks checklist? Select all that apply.",
                     "options": ["App or shortcut set up",
                     "Skills Assessment completed honestly",
                     "Next Destination set, entry requirements checked",
                     "Digital CV Introduction written"],
                     "correctIndices": [0, 1, 2, 3],
                     "explanation": "All four are in the eight-item checklist."}
    }
]

learn = {**META_LEARN, "slides": slides_data}

p = Path("data/l3y1-h-learn.json")
p.write_text(json.dumps(learn, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {p} ({len(slides_data)} slides)")