#!/usr/bin/env python3
"""Module I L3 Y1 (Professional Behaviour & Personal Strengths)."""
import json
from pathlib import Path

META_LEARN = {
    "section": "l3y1-i",
    "level": "l3",
    "year": "y1",
    "module": "I",
    "title": "Professional Behaviour & Personal Strengths",
}

slides_data = [
    {
        "title": "What this module is about",
        "content": "Today is about two things that decide more interviews than grades do - how you operate, and whether you can talk about what you're good at with a straight face. By the end of the session you'll have written three things about yourself that you could say in an interview next week. The headline: one standard, in college, on placement, and in employment. The PROUD value this module is grounded in is Show Respect - respect for people's time, for the work, and for your own future. Requires Navigate (Module H).",
        "exercise": {"type": "scored",
                     "prompt": "Which PROUD value is this module grounded in?",
                     "options": ["Seek Opportunity", "Show Respect", "Encourage Unity", "Be Proud"],
                     "answerIndex": 1,
                     "explanation": "Show Respect - respect for people's time, the work, and your own future."}
    },
    {
        "title": "One standard, three contexts",
        "content": "Professionalism isn't a costume you put on for interviews. It's a set of habits - and the habits don't change with the setting. The list is the same in college, on placement, and in employment: turning up (on time, kit charged, files backed up); flagging problems early (before a deadline or a deliverable slips); how you speak to people (in the room, in the group chat, and online); owning mistakes and putting them right, rather than hiding them.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these are the four habits the deck lists? Select all that apply.",
                     "options": ["Turning up - on time, kit charged, files backed up",
                     "Flagging problems early - before a deadline or a deliverable slips",
                     "How you speak to people - in the room, in the group chat, and online",
                     "Owning mistakes and putting them right, rather than hiding them"],
                     "correctIndices": [0, 1, 2, 3],
                     "explanation": "All four are the professional habits - the same across college, placement, and employment."}
    },
    {
        "title": "The reference you're already writing",
        "content": "When you apply for a placement, an apprenticeship, a job or a degree, they ask us about you. You should know that from the start - not find out in Year 2. References from ESCG staff routinely include attendance, punctuality and reliability - because employers and admissions teams ask for exactly that. Nobody is compiling a charge sheet - a rough week happens to everyone. What a reference reflects is the pattern across the year. One rough week doesn't follow you. A pattern does. That's actually good news, because patterns are the one thing you fully control. The record is built from small, repeated behaviours. Starting today, you are the one writing it.",
        "exercise": {"type": "scored",
                     "prompt": "According to the deck, what matters for your reference?",
                     "options": ["A single bad day",
                     "The pattern across the year - which is the one thing you fully control",
                     "Your tutor's mood",
                     "Your predicted grade"],
                     "answerIndex": 1,
                     "explanation": "One rough week doesn't follow you. A pattern does - and that's the one thing you fully control."}
    },
    {
        "title": "Human skills - what actually gets you hired",
        "content": "Qualifications and technical skills get you shortlisted. At entry level, employers consistently report that the deciding factors are human. Six: Communication (explaining your work clearly - to a team, a client or an audience); Teamwork (being someone people want to work with again); Reliability (delivering what you promised, on the date you promised it); Problem-solving (working it out when there's no tutorial and no template); Adaptability (coping well when the brief, the kit or the client changes); Initiative (spotting what needs doing without being asked). There's nothing soft about being the person a team relies on. These are also the skills that don't automate - which makes them the safest investment you can make.",
        "exercise": {"type": "insert",
                     "prompt": "Fill in the blank: the deck lists six human skills; the most consistently reported entry-level deciding factor is that the deciding factors are ____.",
                     "template": "According to the deck, at entry level the deciding factors are ____.",
                     "options": ["technical", "human", "academic", "creative"],
                     "answerIndex": 1,
                     "explanation": "At entry level, employers consistently report that the deciding factors are human."}
    },
    {
        "title": "Your Skills Assessment - read it like data",
        "content": "You completed the Navigate Skills Assessment in the Navigate session. Today you put the results to work. Open your results, then interrogate them - do you agree? Where's the gap between what it says and how you see yourself? Pick two things: one strength it confirmed, and one development priority for this year. Cross-check with a partner - does their read of you match the assessment's? If your partner and the assessment disagree about you, that's not a problem - that's information. Which of them has seen you under pressure? The assessment is a starting point, not a verdict. Its job is to give you language and a place to begin - the judgement stays yours.",
        "exercise": {"type": "scored",
                     "prompt": "How does the deck frame disagreement between your partner's read and the Skills Assessment?",
                     "options": ["A problem",
                     "Information - which of them has seen you under pressure?",
                     "An argument",
                     "A reason to ignore the assessment"],
                     "answerIndex": 1,
                     "explanation": "If your partner and the assessment disagree about you, that's not a problem - that's information."}
    },
    {
        "title": "Claims versus evidence",
        "content": "'I'm a good team player' is a claim. Anyone can say it - it costs nothing and proves nothing. Interviewers hear it forty times a week. 'On our last project I chaired the planning and set the deadlines - everyone knew their job, and we submitted on time' is evidence. Specific, checkable, memorable - only you can say it. Formula: SITUATION -> WHAT YOU ACTUALLY DO -> WHAT IT SHOWS. Evidence doesn't have to be paid work. Projects, placement, part-time jobs, caring for someone, sport, anything you've made or run - it all counts.",
        "exercise": {"type": "scored",
                     "prompt": "Which version of the team-player claim lands as evidence?",
                     "options": ["'I'm a good team player'",
                     "'On our last project I chaired the planning and set the deadlines - everyone knew their job, and we submitted on time'",
                     "'I'm confident'",
                     "'I'm hard-working'"],
                     "answerIndex": 1,
                     "explanation": "Specific, checkable, memorable - only you can say it."}
    },
    {
        "title": "Three strengths, with proof",
        "content": "Choose three - use your quick audit, your Skills Assessment results and your partner's read. Pick the three with the strongest evidence behind them, not the three that sound best. Draft each as an evidenced statement: Situation -> what you actually do -> what it shows. No claims without proof. Test on a partner - their only job is to ask 'what's your evidence?' until they believe you. If they don't, the statement isn't ready. Refine, then put all three into Navigate - they'll feed your Digital CV, your placement applications and everything else you apply for. If you can't find three, you're not short of strengths - you're short of practice noticing them.",
        "exercise": {"type": "scored",
                     "prompt": "How should you choose which three strengths to draft?",
                     "options": ["The ones that sound best",
                     "The three with the strongest evidence behind them - not the three that sound best",
                     "The ones your friends like",
                     "The ones you've never mentioned before"],
                     "answerIndex": 1,
                     "explanation": "Pick the three with the strongest evidence behind them - not the three that sound best."}
    },
    {
        "title": "Your one thing for this week",
        "content": "Pick one. Write it down, make it specific, hand it in. Your tutor keeps the cards - and will ask you how it went. (1) Act on my Skills Assessment development priority - one concrete step, named. (2) Use one of my three strength statements somewhere real - Navigate, an application, a conversation. (3) Practise one professional habit deliberately for the week - name the habit and where. (4) Tell someone about something that's making it hard to show up. Small and done beats impressive and imaginary.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these are options on the 'one thing' card? Select all that apply.",
                     "options": ["Act on my Skills Assessment development priority - one concrete step, named",
                     "Use one of my three strength statements somewhere real",
                     "Practise one professional habit deliberately for the week",
                     "Tell someone about something that's making it hard to show up"],
                     "correctIndices": [0, 1, 2, 3],
                     "explanation": "All four are the options on the 'one thing' card."}
    },
    {
        "title": "The standard doesn't reset",
        "content": "One standard, three contexts. It's the same tomorrow as it was today. That's the whole point. The Navigate record you built today is live: Skills Assessment, strengths, Digital CV - a portfolio that builds all year, not the night before an application. Next: Work Experience (Module J) - finding and applying for placements, using exactly what you wrote today.",
        "exercise": {"type": "scored",
                     "prompt": "What's the module's closing line?",
                     "options": ["'Get good marks'",
                     "'One standard, three contexts - it's the same tomorrow as it was today. That's the whole point.'",
                     "'Wait until Year 2'",
                     "'Focus on the grade'"],
                     "answerIndex": 1,
                     "explanation": "The standard doesn't reset - one standard, three contexts."}
    }
]

learn = {**META_LEARN, "slides": slides_data}

p = Path("data/l3y1-i-learn.json")
p.write_text(json.dumps(learn, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {p} ({len(slides_data)} slides)")