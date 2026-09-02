#!/usr/bin/env python3
"""Write L3 Y2 learn JSON files for modules C-K."""
import json
from pathlib import Path

OUT = Path("data")

def write(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", p)

# ============================================================
# Module C L3 Y2: Health & Safety - a year in, not starting again
# ============================================================
mod_c = {
    "section": "l3y2-c", "level": "l3", "year": "y2", "module": "C",
    "title": "Health & Safety - A Year In, Not Starting Again",
    "slides": [
        {
            "title": "Why this H&S session is a refresher, not a re-teach",
            "content": "You know the studio. This is about what a year of working in it has quietly cost - and what's genuinely changed for year two. Returner deck: the framing has to feel like it the moment it opens. About 47 minutes - faster than Year 1's; there's no need to linger on content this group has already absorbed.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the Year 2 H&S session differ from Year 1's, according to the deck?",
                "options": [
                    "It covers completely new content",
                    "It's a brisk refresher with a couple of genuinely new bits - familiarity is the risk now",
                    "It removes the safeguarding element",
                    "It runs twice as long"
                ],
                "answerIndex": 1,
                "explanation": "It's a brisk refresher with a couple of genuinely new bits - familiarity is the risk now."
            }
        },
        {
            "title": "Familiarity is the risk now",
            "content": "In week one, you didn't know what was normal, so everything got a second look. A year in, you do know - which is exactly the problem. The lighting stand without sandbags because 'we always put them on anyway' - which means nobody actually checked. The wrist strap on the camera not used because 'I've never dropped it.' Cables left until after the edit because 'we'll tidy up after' - and then didn't. These stop registering not because you've become careless, but because you've become familiar.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, why do habits like skipping sandbags stop registering in year two?",
                "options": [
                    "Because you've become careless",
                    "Because you've become familiar - not careless. That's the trap.",
                    "Because the equipment has changed",
                    "Because there's no time"
                ],
                "answerIndex": 1,
                "explanation": "These stop registering not because you've become careless, but because you've become familiar."
            }
        },
        {
            "title": "What slips in year two - and what resets it",
            "content": "What slips: lanyards worn 'most of the time'; shortcuts that worked fine until they didn't (skipping the risk assessment for a familiar location because 'we've been there before'); things you'd have flagged in week one but stopped noticing. What resets it: treat your own habits as worth re-checking, not just new starters'; say it out loud the first time you notice you've gone quiet on something; a near miss is still information, a year in or not.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are 'what slips' examples in year two, according to the deck? Select all that apply.",
                "options": [
                    "Lanyards worn 'most of the time'",
                    "Skipping the risk assessment for a familiar location because 'we've been there before'",
                    "Things you'd have flagged in week one but stopped noticing",
                    "Wearing the wrong colour lanyard"
                ],
                "correctIndices": [0, 1, 2],
                "explanation": "Lanyards worn 'most of the time', skipping risk assessments for familiar locations, and things you'd have flagged in week one but stopped noticing are the year-two slips."
            }
        },
        {
            "title": "The basics, fast - tell your teacher",
            "content": "If the fire alarm goes: your teacher will confirm the evacuation route and assembly point. If your sessions this year use a different studio or building from last year, treat this as new information - do not assume it is unchanged. If something's not right: tell your teacher. Hazard, near miss, damage, or just something that isn't working - that's your first point of contact, and they'll take it from there. None of that is making a fuss; it's exactly the noticing this session is about. Keep walkways and fire exits clear, don't prop doors open 'just for now', closed-toe shoes or hearing protection is required - not a judgement call on the day.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "If a session this year is in a different studio or building from last year, what should you do?",
                "options": [
                    "Assume the evacuation route is the same",
                    "Treat it as new information - do not assume it is unchanged",
                    "Wait until an alarm to find out",
                    "Skip the briefing"
                ],
                "answerIndex": 1,
                "explanation": "If your sessions this year use a different studio or building from last year, treat this as new information."
            }
        },
        {
            "title": "Show respect - the excuse has changed",
            "content": "Show respect is the PROUD anchor. Same standard, less excuse for not knowing it. For the space: leaving it as you'd want to find it; reporting damage rather than walking past it; 'someone else will sort it' is how things stop getting sorted. For each other: messing with someone's camera rig, audio setup, lighting configuration or workstation 'as a joke' isn't banter - it's a safety issue with someone else's name on it. For the people who flag things: when a tutor pauses a studio shoot for a safety reason, that's the system working as it should. A year in, 'I didn't realise' carries less weight than it did in week one.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck say the 'show respect' excuse has changed in Year 2?",
                "options": [
                    "The standard has dropped",
                    "A year in, 'I didn't realise' carries less weight than it did in week one",
                    "There is now an excuse for everything",
                    "Show respect no longer applies"
                ],
                "answerIndex": 1,
                "explanation": "A year in, 'I didn't realise' carries less weight than it did in week one."
            }
        },
        {
            "title": "What's new for Year 2 in your subject area",
            "content": "Content Creation students: you are now running live media (Eastbourne Youth Radio, Tag magazine). Broadcasting and publishing carry different H&S obligations - contributor consent, editorial duty of care, wellbeing of subjects are now professional responsibilities, not just course requirements. T Level students: industry placement is live - confirm your pre-placement H&S induction dates with your tutor immediately. Film and Games students: your Year 2 projects are longer and more complex - sustained screen-intensive work makes RSI and eye strain genuine occupational risks.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what do Content Creation students now do that they didn't in Year 1?",
                "options": [
                    "Run live media (Eastbourne Youth Radio, Tag magazine) - with contributor consent and editorial duty of care",
                    "Skip H&S briefings",
                    "Stop using consent forms",
                    "Move to a different building"
                ],
                "answerIndex": 0,
                "explanation": "Content Creation students are now running live media (Eastbourne Youth Radio, Tag magazine) - broadcasting and publishing carry different H&S obligations."
            }
        },
        {
            "title": "Patterns worth naming - and T Level placement",
            "content": "Worth re-stating from Year 1: sandbags on lighting stands when extended (the single most commonly dropped habit); risk assessments for location shoots apply to familiar locations too; cables are coiled and stored after every session, not after the edit. Patterns worth naming: equipment returned to the wrong position or not returned at all - because everyone assumes someone else has done it. If you are the last person using something, you are responsible for returning it, regardless of who signed it out. T Level students on placement: any incident during placement must be reported to your tutor by the end of the placement day - the host organisation's procedures apply on-site, not the college's.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "If you are the last person using a piece of equipment, according to the deck, who is responsible for returning it?",
                "options": [
                    "Whoever signed it out first that day",
                    "You - regardless of who signed it out",
                    "The technician only",
                    "Nobody - it can wait"
                ],
                "answerIndex": 1,
                "explanation": "If you are the last person using something, you are responsible for returning it, regardless of who signed it out."
            }
        },
        {
            "title": "If something's not right - say something",
            "content": "Noticing is only half the job. Not making a fuss. Not 'telling on' anyone. Just saying it, early, to someone who can do something about it. And this isn't only about hazards. If something - a space, an activity, the way someone's behaving towards you or someone else - has made you feel uncomfortable or unsafe, that counts too. Tell someone. Early. Your safeguarding team is on the lanyard - and the same number still works in Year 2.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Beyond physical hazards, what else counts as 'something's not right' that you should tell someone about?",
                "options": [
                    "Only a fire",
                    "Anything - a space, an activity, or the way someone's behaving towards you or someone else - that's made you feel uncomfortable or unsafe",
                    "Only damage to college property",
                    "Only safeguarding team instructions"
                ],
                "answerIndex": 1,
                "explanation": "If a space, an activity, or the way someone's behaving towards you or someone else has made you feel uncomfortable or unsafe, that counts too."
            }
        },
        {
            "title": "One thing - and three to take with you",
            "content": "Pick one. Write it down. Keep it somewhere you'll see it. Options: (1) I'll actually check my nearest fire exit and assembly point, not just assume I remember. (2) I'll be honest with myself about one habit I've let slip, and fix it this week. (3) I'll read my subject area's update for this year properly, not skim it. (4) I'll tell someone - my tutor, my personal tutor, or the college's safeguarding team - about something that's made me feel uncomfortable or unsafe. Three things to take with you: familiarity is the risk now, not unfamiliarity; the standard hasn't moved; if something's off, say something, early.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the first of the 'three things to take with you' from this session?",
                "options": [
                    "The fire exit is always at the back",
                    "Familiarity is the risk now, not unfamiliarity - treat your own habits as worth checking, not just new starters'",
                    "You should now know everything",
                    "Sandbags are optional"
                ],
                "answerIndex": 1,
                "explanation": "Familiarity is the risk now, not unfamiliarity. Treat your own habits as worth checking, not just new starters'."
            }
        }
    ]
}
write("l3y2-c-learn.json", mod_c)

# ============================================================
# Module D L3 Y2: Students' Voice & Student Rep Elections
# (shared with A-level Y2; this group also elects 2 reps)
# ============================================================
mod_d = {
    "section": "l3y2-d", "level": "l3", "year": "y2", "module": "D",
    "title": "Students' Voice & Student Rep Elections",
    "slides": [
        {
            "title": "What this session is about - and what's new",
            "content": "You've had a year of this department. Now decide what you do with what you know. About 100 minutes. PROUD value: Encourage Unity. New this year: this group elects TWO reps - one for their subject group, and one for their GCSE English or maths class. Both go on the central Student Rep Register today. L3 Y2: this is your last year. Don't fumble the last lap. You have enough institutional knowledge to stand for Rep or Governor with genuine credibility.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How many reps does this group elect today, according to the deck?",
                "options": ["One - the subject rep", "Two - a subject rep and a GCSE English/maths rep", "Three - subject, English, and maths", "None - they're elected next term"],
                "answerIndex": 1,
                "explanation": "This group elects two reps - one for their subject group, and one for their GCSE English or maths class."
            }
        },
        {
            "title": "The session in eight beats",
            "content": "Eight beats in around 100 minutes: (1) Check in - what did Students' Voice actually achieve? (10) (2) Students' Voice - what makes it work, and what doesn't (10) (3) Ways to get involved (10) (4) The Rep role (10) (5) The Governor role (15) (6) Encourage Unity (5) (7) Election (30-35) (8) Close. Today ends with an election.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the eight beats of this session in the order the deck presents them.",
                "items": [
                    "Check in",
                    "Students' Voice",
                    "Ways to get involved",
                    "The Rep role",
                    "The Governor role",
                    "Encourage Unity (PROUD)",
                    "Election",
                    "Close"
                ],
                "solution": [0, 1, 2, 3, 4, 5, 6, 7]
            }
        },
        {
            "title": "When Students' Voice works - and when it doesn't",
            "content": "When it works: reps who actually consult their group - not just improvise at meetings; feedback that names the thing - 'coursework feedback arrives too late to act on' beats 'feedback is bad'; groups who tell their rep what matters - before the meeting, not after; students who follow up - checking the past papers appeared, or the darkroom hours actually changed. Collective voice is a shared responsibility - not just the rep's job. Outcomes: teaching & learning (curriculum and delivery shaped by what students report - how coursework and exam preparation are sequenced across Year 2); student experience (campus life improved by evidenced feedback - studio, darkroom and edit-suite access outside lessons); community; visible outcomes.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is an example of feedback that 'names the thing', according to the deck?",
                "options": [
                    "'Feedback is bad'",
                    "'Coursework feedback arrives too late to act on'",
                    "'Things aren't great'",
                    "'It's all a bit rubbish'"
                ],
                "answerIndex": 1,
                "explanation": "'Coursework feedback arrives too late to act on' beats 'feedback is bad' - that's feedback that names the thing."
            }
        },
        {
            "title": "Four ways to get involved - and which one fits Year 2",
            "content": "Student Rep - elected today. You also elect a rep for your GCSE English or maths class. Student Governor - 3 places on the Main Governing Board, where equipment, technician capacity and studio provision get decided. Applications close midday, Friday 16 October. NUS Membership - you're already a member. TOTUM card (£14.99/year) gives discounts across hundreds of retailers. Surveys & Forums - the Induction Survey opens 3 November. Three minutes - the place to say if coursework deadlines and UCAS are colliding.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are the 'ways to get involved' the deck lists? Select all that apply.",
                "options": ["Student Rep", "Student Governor", "NUS Membership (TOTUM card)", "Surveys & Forums"],
                "correctIndices": [0, 1, 2, 3],
                "explanation": "All four are ways to get involved - Student Rep, Student Governor, NUS Membership, and Surveys & Forums."
            }
        },
        {
            "title": "The Rep role - Year 2 advantage",
            "content": "Year 2: familiarity is an advantage - if you use it. What reps do: gather and convey student opinions to college leadership; attend 3 Student Council meetings per year; provide feedback on teaching, and on studio, darkroom and edit-suite access; work with staff to develop solutions - not just present problems; keep the group informed after every meeting; represent this group in your GCSE English or maths class as well as your subject. Year 2 advantage: you know the staff, the meetings, and what actually moves things. Develops: communication, leadership, problem-solving, and employability skills. Rep training: Wednesday 14 October (all campuses) - mandatory for newly elected reps, even returners.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How many Student Council meetings per year does a rep attend, according to the deck?",
                "options": ["1", "3", "6", "12"],
                "answerIndex": 1,
                "explanation": "Reps attend 3 Student Council meetings per year."
            }
        },
        {
            "title": "The Student Governor role - if you're staying",
            "content": "3 places on the Main Governing Board - strategic decisions about the whole college. Represent authentic student experience - what carrying a production alongside UCAS actually costs. Contribute to decisions on curriculum and budget - technician capacity, camera and darkroom provision, software licences. Exceptional leadership experience - genuinely CV-worthy. Different from Student Rep - strategic scope, institutional weight. Eligibility: full-time students and apprentices; planning to study at ESCG for at least one more year (Level 3 students progressing here qualify). A-level Y2: if you are not continuing at ESCG after this year, you will not be eligible to serve a full Governor term. Applications close at midday, Friday 16 October. Student Enrichment Co-ordinators: Eastbourne Chelsey King / Lewes Tessa Echalaz / Station Plaza & Ore Valley Paige Baker-Carroll.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the eligibility requirement to apply for Student Governor, according to the deck?",
                "options": [
                    "Any current student, in any year",
                    "Students planning to study at ESCG for at least one more year - L3 students progressing here qualify",
                    "Only Year 1 students",
                    "Only students with a UCAS offer"
                ],
                "answerIndex": 1,
                "explanation": "Planning to study at ESCG for at least one more year - L3 students progressing here qualify."
            }
        },
        {
            "title": "Governor commitment and how to apply",
            "content": "Commitment: roughly 3-5 hours a month. 4 Board meetings a year (2-3 hours each), around 3 committee meetings, 2 strategy days, plus reading papers in advance. Real influence: termly reports to the Board on topics such as sustainability and green skills, AI, careers advice and College values - equipment and technician capacity belong on that list too. Support: induction with the Director of Governance, ongoing training, Governor portal and iPad, expenses reimbursed, annual 1:1 with the Chair. How to apply: (1) Online nomination form, deadline midday Friday 16 October. (2) Informal conversation 2-5 November. (3) Student ballot 9-23 November if more candidates than places. (4) Committee recommendation 24 November; formal Board appointment 14 December. Contact: Belle Howard, Director of Governance - Belle.Howard@escg.ac.uk.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "insert",
                "prompt": "Fill in the blank: Student Governor applications close at midday on Friday ____ October.",
                "template": "Student Governor applications close at midday on Friday ____ October.",
                "options": ["9th", "16th", "23rd", "30th"],
                "answerIndex": 1,
                "explanation": "Applications close at midday, Friday 16 October."
            }
        },
        {
            "title": "Encourage Unity - your experience is only useful if you share it",
            "content": "One person short of darkroom time is bad luck. A whole set short of it is evidence. Experience is only useful if you share it. Year 1 can't know how coursework and exam preparation collide in the spring - you do. A rep you helped choose is a rep who'll listen when you tell them what matters - like past-paper access before mocks, or edit time before a hand-in. The group that engages this year sets the standard for the one that comes after. Next year's Year 2 inherit whatever routine you leave behind.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck describe the difference between one person's experience and a group's view?",
                "options": [
                    "Both are opinions",
                    "One is bad luck; a whole set short of it is evidence - and evidence is what changes decisions",
                    "A single experience always counts for more",
                    "Only written complaints count"
                ],
                "answerIndex": 1,
                "explanation": "One person short of darkroom time is bad luck. A whole set short of it is evidence."
            }
        },
        {
            "title": "Election time - two seats, one session",
            "content": "Stages: Nominations (any student may put themselves forward; two seats are elected today - subject rep and GCSE English/maths rep; 2 minutes) -> Candidate pitches (1 minute each - say what you'd do differently, e.g. 'I'd get the coursework and mock dates published together at the start of term') -> The vote (group decides the fairest method; anonymous slips work well across teaching groups) -> Confirm & register (announce both results; add both reps to the central Student Rep Register before this session closes). MANDATORY: Student Rep elections must be completed and the rep confirmed no later than the end of Week 2 of the academic year.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "By when must Student Rep elections be completed, according to the deck?",
                "options": [
                    "End of Week 1",
                    "No later than the end of Week 2 of the academic year",
                    "End of term",
                    "Whenever the rep finds time"
                ],
                "answerIndex": 1,
                "explanation": "Student Rep elections must be completed and the rep confirmed no later than the end of Week 2 of the academic year."
            }
        }
    ]
}
write("l3y2-d-learn.json", mod_d)

print("Wrote C and D")
