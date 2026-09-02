#!/usr/bin/env python3
"""Write all 11 L3 Y2 learn JSON files in one pass."""
import json
from pathlib import Path

OUT = Path("data")

def write(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", p)

# ============================================================
# Module A L3 Y2: Welcome back - this is the year that counts
# ============================================================
mod_a = {
    "section": "l3y2-a", "level": "l3", "year": "y2", "module": "A",
    "title": "Welcome Back - This Is the Year That Counts",
    "slides": [
        {
            "title": "Welcome back - and yes, this year counts",
            "content": "Welcome back. Year 2 is about 45 minutes, and it's not a re-run of last September. It's a re-focus: where you're headed, what Year 2 demands, staying on course, support that still matters, and landing it. You've done the hard part - you got here, and you passed Year 1. The last lap is the one that decides what it was all for.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the framing of this Year 2 welcome session, according to the deck?",
                "options": [
                    "A repeat of last September's induction",
                    "A re-focus on where you're headed and what Year 2 demands",
                    "A pass-or-fail assessment of last year's work",
                    "A lecture on study skills"
                ],
                "answerIndex": 1,
                "explanation": "The deck frames this as a re-focus, not a re-run: where you're headed, what Year 2 demands, staying on course, support that still matters, and landing it."
            }
        },
        {
            "title": "The session in five beats",
            "content": "Five beats in about 45 minutes: 1) Where you're headed (3 routes out); 2) What Year 2 demands (three honest asks); 3) Staying on course (tools and a habit); 4) Support that still matters (4 doors); 5) Landing it (the final-year focus card).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the five beats of this welcome-back session in the order the deck presents them.",
                "items": [
                    "Where you're headed",
                    "What Year 2 demands",
                    "Staying on course",
                    "Support that still matters",
                    "Landing it"
                ],
                "solution": [0, 1, 2, 3, 4]
            }
        },
        {
            "title": "Three honest asks for Year 2",
            "content": "Year 2 makes three honest asks. (1) Grades carry weight - this year's results are the ones employers, training providers and universities actually see. (2) Deadlines stack up - coursework, Final Major Project or Extended Diploma, placement hours and applications all run at once; drift is the real enemy. (3) More on you - less chasing from us, more independence from you; deliberate. This is what next year looks like.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is one of the three honest asks Year 2 makes, according to the deck?",
                "options": [
                    "Get a part-time job immediately",
                    "Grades carry weight - this year's results are the ones employers and universities actually see",
                    "Attend every social event",
                    "Pick a specialism in week one"
                ],
                "answerIndex": 1,
                "explanation": "Grades carry weight - this year's results are the ones employers, training providers and universities actually see."
            }
        },
        {
            "title": "Don't fumble the last lap",
            "content": "Most students who don't get the result they're capable of in Year 2 weren't not clever enough. They drifted. A missed deadline here, a few skipped days there, the application left too late. You've already done the hard part - you got here, and you passed Year 1. The last lap is the one that decides what it was all for. Run it properly.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what is the usual cause of Year 2 students falling short of what they're capable of?",
                "options": ["Lack of intelligence", "Drift - missed deadlines, skipped days, applications left too late", "Bad teaching", "Bad luck"],
                "answerIndex": 1,
                "explanation": "They drifted. A missed deadline here, a few skipped days there, the application left too late."
            }
        },
        {
            "title": "Three routes out - no second-best",
            "content": "There are three routes out of Year 2. Into work: content creator, production assistant, junior designer, social media coordinator - real careers, begun. Apprenticeship: earn while you train; real qualifications, real experience, no student debt. University / HE: BA Media, Film, Games Art, Photography, Digital Design; UCH Hastings offers BA degrees locally for Games Art students. There is no 'second-best' route - the best route is the one that gets YOU where you want to be, and this year is how you earn it.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are the three routes out of Year 2, according to the deck? Select all that apply.",
                "options": ["Into work", "Apprenticeship", "University / HE", "Drop out and try again later"],
                "correctIndices": [0, 1, 2],
                "explanation": "Into work, apprenticeship, and university / HE are the three routes out."
            }
        },
        {
            "title": "Stay on course - three tools, one rule",
            "content": "Three tools to stay on course. Pro Portal - timetable, rooms, messages; check every morning, no excuses. Your deadlines - every assessment and application date in one place. Track your progress - attendance and grades; catch a slip early, not in March. The rule: a slip caught in October is fixable. A slip caught in March is the year.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How often does the deck say you should check Pro Portal?",
                "options": ["Once a week", "Every morning, no excuses", "Only when something looks wrong", "Once a term"],
                "answerIndex": 1,
                "explanation": "Check Pro Portal every morning, no excuses."
            }
        },
        {
            "title": "Support that still matters",
            "content": "Final year is the year people quietly struggle and don't say anything. Four doors are still open. Careers & progression - real help with applications, interviews, UCAS and apprenticeships. Wellbeing - final-year pressure is real; talking to someone is a strength, not a slip. Money & practical - bursary still there for Year 2. Academic support - stuck on coursework? Get help early.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which door covers help with UCAS and apprenticeship applications, according to the deck?",
                "options": ["Wellbeing", "Money & practical", "Careers & progression", "Academic support"],
                "answerIndex": 2,
                "explanation": "Careers & progression covers real help with applications, interviews, UCAS and apprenticeships."
            }
        },
        {
            "title": "Make it count - and the CV test",
            "content": "Enrichment, competitions, projects, placement - treat it as a long interview. Many students get their first paid work through placements. The CV test: 'Will this give me something real to say in an interview or on an application?' If yes - do it.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the 'CV test' the deck recommends for enrichment, projects and placement?",
                "options": [
                    "Only do things that look good on paper",
                    "Ask 'Will this give me something real to say in an interview or on an application?' - if yes, do it",
                    "Skip anything that doesn't pay",
                    "Do everything on offer, regardless of fit"
                ],
                "answerIndex": 1,
                "explanation": "The CV test: 'Will this give me something real to say in an interview or on an application?' If yes - do it."
            }
        },
        {
            "title": "My final-year focus card",
            "content": "Write three answers now, on the card you take away: (1) Where I want to be when this year ends. (2) The one habit that will get me there. (3) The one thing I need to sort early - and won't leave. Your tutor keeps the card and checks in with you.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are the three questions on the final-year focus card? Select all that apply.",
                "options": [
                    "Where I want to be when this year ends",
                    "The one habit that will get me there",
                    "The one thing I need to sort early - and won't leave",
                    "My favourite placement employer so far"
                ],
                "correctIndices": [0, 1, 2],
                "explanation": "The three questions are about destination, the habit, and the one thing to sort early."
            }
        }
    ]
}
write("l3y2-a-learn.json", mod_a)

# ============================================================
# Module B L3 Y2: Confidence, Independence & Attendance
# ============================================================
mod_b = {
    "section": "l3y2-b", "level": "l3", "year": "y2", "module": "B",
    "title": "Confidence, Independence & the Last Lap",
    "slides": [
        {
            "title": "Why this session is different from Year 1",
            "content": "Not new-starter content. The Year 2 version - what's different, what's still true, what you're committing to today. About 55 minutes. You've produced the work now - Year 2 is where the Final Major Project, the portfolio, and the industry placement all have to come together. PROUD value anchor: Seek Opportunity.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which PROUD value does this module anchor on?",
                "options": ["Bring Positivity", "Show Respect", "Seek Opportunity", "Encourage Unity"],
                "answerIndex": 2,
                "explanation": "The PROUD value anchor for this module is Seek Opportunity."
            }
        },
        {
            "title": "The session in six beats",
            "content": "Six beats in about 55 minutes: 1) What shifts in Year 2; 2) Time and the final fuse; 3) Seek Opportunity; 4) Confidence; 5) Attendance; 6) Your habit.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the six beats of this Year 2 confidence session in the order the deck presents them.",
                "items": [
                    "What shifts in Year 2",
                    "Time and the final fuse",
                    "Seek Opportunity",
                    "Confidence",
                    "Attendance",
                    "Your habit"
                ],
                "solution": [0, 1, 2, 3, 4, 5]
            }
        },
        {
            "title": "Year 1 to Year 2: three concrete shifts",
            "content": "Year 1 was foundation-building. Year 2 is where you build on it. Three shifts: foundation -> building on it (gaps from Year 1 don't disappear, they compound); freedom to find your feet -> the margin's gone (final assessments and graded portfolios - what you hand in is what you're judged on); staff were patient with orientation -> staff expect the self-managed version of you. They're right to.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what happens to gaps from Year 1 in Year 2?",
                "options": [
                    "They disappear over the summer",
                    "They compound - what you didn't consolidate in Year 1 is what you hand in for final assessment",
                    "They're forgiven by staff",
                    "They get covered in a refresher week"
                ],
                "answerIndex": 1,
                "explanation": "Gaps from Year 1 don't disappear - they compound."
            }
        },
        {
            "title": "Time and the final fuse",
            "content": "The long fuse: missed work doesn't punish you the week you miss it. It punishes you at the portfolio deadline, when you're catching up and trying to produce new work simultaneously. It's avoidable - if you decide in advance. The one move that still helps: treat free periods as actual sessions. The students who finish Year 2 well aren't the ones who worked hardest in June - they're the ones who didn't leave everything until June.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "When does the deck say a missed brief actually hurts you?",
                "options": [
                    "The week you miss it",
                    "At the portfolio deadline, when you're catching up and trying to produce new work simultaneously",
                    "Only at the end of Year 2",
                    "Never, if you explain it"
                ],
                "answerIndex": 1,
                "explanation": "It hurts you at the portfolio deadline, when you're catching up and trying to produce new work simultaneously."
            }
        },
        {
            "title": "Seek Opportunity - the Year 2 version",
            "content": "The honest version of 'be ambitious' in Year 2. Make progression concrete this year: apprenticeship, higher education, employment - whatever your route, it has to be active now, not pending. Build something to talk about: a completed placement logbook entry, a short film or editorial piece for your portfolio, a live Behance or Vimeo page - applications need things to have actually happened. Treat Year 2 setbacks as information - there's still time to course-correct, not in June, but now.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are the three Year 2 'Seek Opportunity' moves, according to the deck? Select all that apply.",
                "options": [
                    "Make progression concrete this year - it's active now, not pending",
                    "Build something to talk about - applications need things to have actually happened",
                    "Treat Year 2 setbacks as information - course-correct now, not in June",
                    "Wait for someone to offer you a placement"
                ],
                "correctIndices": [0, 1, 2],
                "explanation": "The three moves are: make progression concrete, build something to talk about, treat setbacks as information."
            }
        },
        {
            "title": "The Year 2 confidence trap",
            "content": "Year 2 students split two ways. The coasting trap: Year 1 went fine. Year 2 can feel like more of the same - until the stakes stop being practice. The wall trap: Year 2 pressure is real and you don't want to admit you're struggling. So you don't ask. Both lead to the same place. Asking early is the move. The trap is 'Year 1 was fine. I know how to do this - I don't need to change anything.' The honest version is 'Year 2 is a different job. The habits that got me through Year 1 need upgrading - and if I'm struggling, I'll say so early.'",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is 'the wall trap' in Year 2, according to the deck?",
                "options": [
                    "Hitting a literal wall in a shoot",
                    "Year 2 pressure is real and you don't want to admit you're struggling, so you don't ask",
                    "The college's server goes down during deadline week",
                    "You forget your login for Pro Portal"
                ],
                "answerIndex": 1,
                "explanation": "The wall trap: Year 2 pressure is real and you don't want to admit you're struggling, so you don't ask."
            }
        },
        {
            "title": "Attendance - the Year 2 case",
            "content": "No thresholds. No lecture. The Year 2 case for showing up. The bit that isn't on the slides - off-script teaching, grade-band detail, answers to questions; not catchable up from notes. Final assessments compound - missing teaching while completing final work doesn't work. References are written from memory - staff remember who showed up in Year 2, not just Year 1. Being seen at the finish - Year 2 is when 'put the effort in' or 'coasted' gets written; attendance is how it's seen.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck say staff writing references remember attendance?",
                "options": [
                    "They use a database; it's all automatic",
                    "They remember who showed up in Year 2, not just Year 1",
                    "They use the same letter for everyone",
                    "They only ask for Year 1 attendance"
                ],
                "answerIndex": 1,
                "explanation": "References are written from memory - staff remember who showed up in Year 2, not just Year 1."
            }
        },
        {
            "title": "Real barriers - not excuses",
            "content": "Attendance isn't always about willpower. Sometimes it's about something real, and the response is help, not a warning. Real barriers: burnout from Year 1 (production hours, portfolio deadlines, live project responsibilities all stacking up); pressure (high stakes feeling paralysing, not motivating); money and travel; things at home (caring, family pressure, unsafe situations); neurodivergence not yet supported, or chronic health. Tell someone. Early. A barrier we know about is one we can help with. A barrier we don't know about is one that quietly takes you out.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what is the right response when a real barrier (not an excuse) is making attendance hard?",
                "options": [
                    "Issue a formal warning immediately",
                    "Help - tell someone early, so the barrier is one we can work with",
                    "Wait until attendance drops further",
                    "Refer directly to exam board"
                ],
                "answerIndex": 1,
                "explanation": "Tell someone. Early. A barrier we know about is one we can help with."
            }
        },
        {
            "title": "My one habit - one specific thing this week",
            "content": "Pick one. One thing. This week. Not a resolution - a specific action. Your tutor keeps the card. Options: (1) Decide in advance what one free period this week is actually for. (2) Address one thing brought forward from Year 1 - an unresolved portfolio unit, a placement reflection you haven't written, or a Final Major Project specialism you haven't decided. (3) Take one Seek-Opportunity step - progression planning, work experience. (4) Tell someone about a barrier that's making it hard to come in. Why one habit, not five - habits change behaviour. Plans don't. Five at once is a plan - which means none of them happen.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Why does the deck ask for one habit, not five?",
                "options": [
                    "Five is too many words for a card",
                    "Habits change behaviour; five at once is a plan - which means none of them happen",
                    "The teacher can only mark one answer",
                    "Five cards cost more to print"
                ],
                "answerIndex": 1,
                "explanation": "Habits change behaviour. Plans don't. Five at once is a plan - which means none of them happen."
            }
        },
        {
            "title": "Wrapping up - what you take from this",
            "content": "Today you have: named what's different about Year 2 and why it's the decisive lap; seen where the final fuse leads; revisited Seek Opportunity in Year 2 terms; heard the Year 2 case for attendance; picked one habit for this week. The rest of induction covers wellbeing, progression planning, and the careers and pathways work that turns Year 2 effort into what happens next. Don't fumble the last lap. Decide in advance. Ask early. Tell us when it's hard. That's the year.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which of these is the deck's closing line for this session?",
                "options": [
                    "Good luck in Year 2 - you'll be fine",
                    "Don't fumble the last lap. Decide in advance. Ask early. Tell us when it's hard. That's the year.",
                    "Remember to log your hours",
                    "See you next September"
                ],
                "answerIndex": 1,
                "explanation": "Don't fumble the last lap. Decide in advance. Ask early. Tell us when it's hard. That's the year."
            }
        }
    ]
}
write("l3y2-b-learn.json", mod_b)

print("Wrote A and B so far - test before continuing")
