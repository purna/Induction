#!/usr/bin/env python3
"""Write L3 Y2 learn JSON for modules H, I, J, K."""
import json
from pathlib import Path

OUT = Path("data")

def write(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", p)

# ============================================================
# Module H L3 Y2: Why Navigate Matters Here
# ============================================================
mod_h = {
    "section": "l3y2-h", "level": "l3", "year": "y2", "module": "H",
    "title": "Why Navigate Matters Here",
    "slides": [
        {
            "title": "Why Navigate matters at Level 3",
            "content": "At Level 3 you own your progress. Navigate is where you build the evidence that you did. University, an apprenticeship and the studio, newsroom or technical team you want to join all ask the same question: what can you actually do, and how do you know? Your Digital CV is your answer. Built across two years, it becomes something a personal statement cannot fake. By the end of today you will be able to: interpret your Skills Assessment results and set a development priority; state a next destination and the entry requirements it carries; write a reflection that evidences a skill, not just describes an event.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What question does the deck say university, an apprenticeship and the studio all ask?",
                "options": [
                    "What school did you go to?",
                    "What can you actually do, and how do you know? Your Digital CV is your answer",
                    "What's your favourite film?",
                    "What are your predicted grades?"
                ],
                "answerIndex": 1,
                "explanation": "University, an apprenticeship and the studio all ask the same question: what can you actually do, and how do you know? Your Digital CV is your answer."
            }
        },
        {
            "title": "Your Skills Assessment - and Amber is where the gains are",
            "content": "This is a self-report. Its value depends entirely on your honesty - inflate it and you get a useless picture of yourself. The scenario tests professional judgement, communication, and the duty of care you carry the moment you work with someone you film, photograph or interview, a client, or a system other people rely on. Green: evidenced strength - prove it in your Digital CV. Amber: inconsistent under pressure - most people sit here. Red: your development priority this term. Read the Amber list carefully. Amber is where the real gains are - Red is usually already obvious to you.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, where are the real gains in a Skills Assessment?",
                "options": [
                    "Green - by claiming strength",
                    "Amber - inconsistent under pressure, where most people sit. Red is usually already obvious",
                    "Red - because it's hardest",
                    "It doesn't matter - just tick the boxes"
                ],
                "answerIndex": 1,
                "explanation": "Read the Amber list carefully. Amber is where the real gains are - Red is usually already obvious to you."
            }
        },
        {
            "title": "Your next destination - set it now",
            "content": "Set it now, with the entry requirements checked. Vague ambition is not a plan. Where this leads: media, film, journalism, PR and marketing degrees; animation, illustration, graphic design, photography degrees; BA (Hons) at University Centre Hastings - a degree without moving; Digital Media Design Foundation Degree; HNC/HND Computing; higher apprenticeship at Level 4, 5 or 6, or employment. Two honest points: UCAS runs in Year 2, alongside your external assessments. The material for a personal statement is built in Year 1. Year 1 sets the trajectory of Year 2. It is not a warm-up. Specialist routes open up later: digital forensics, network engineering, editing and post-production, cinematography.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's 'one honest point' about UCAS and Year 1?",
                "options": [
                    "UCAS runs in Year 2, alongside your external assessments. The material for a personal statement is built in Year 1",
                    "UCAS is optional",
                    "Year 1 doesn't matter for UCAS",
                    "UCAS only matters for university"
                ],
                "answerIndex": 0,
                "explanation": "UCAS runs in Year 2, alongside your external assessments. The material for a personal statement is built in Year 1."
            }
        },
        {
            "title": "Careers this leads to - and the most useful outcome is a clear NO",
            "content": "Roles: journalist; film or TV producer; cyber security analyst; digital video editor; junior content producer; social media co-ordinator; games artist; animator; CGI artist; concept artist; FE lecturer or technician in media, film or computing; art director; production manager; studio manager; SOC analyst; infrastructure technician; digital forensics. Interrogate each profile: entry route, qualification level, earnings, what the job is like day to day. The most useful outcome of this quiz is a clear NO. Ruling something out is progress, and it is faster than drifting into it.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what is 'the most useful outcome' of the careers quiz?",
                "options": [
                    "A clear YES - finding the perfect role",
                    "A clear NO - ruling something out is progress, faster than drifting into it",
                    "Skipping the quiz",
                    "Picking the highest-paid job"
                ],
                "answerIndex": 1,
                "explanation": "The most useful outcome of this quiz is a clear NO. Ruling something out is progress, and it is faster than drifting into it."
            }
        },
        {
            "title": "What you should be logging",
            "content": "Two years of consistent logging becomes a portfolio. Two years of good intentions becomes a panic in February. Log: film, audio, graphics and code you plan, make and evaluate; externally moderated projects and Final Major Projects; edits, builds and tests (Premiere Pro, DaVinci, Blender); live media (Youth Radio, Tag magazine, The Depot); cross-department work (photographing for Hair and Beauty); visiting media professionals and industry visits; industry placement - 315 hours on the T Levels; part-time work - professionalism and communication are the same skills. One entry per activity, logged the same week, tagged to the skills it evidences. Ten minutes now saves an afternoon in Year 2.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the 'ten minutes now' rule the deck recommends?",
                "options": [
                    "Spend ten minutes on your portfolio per term",
                    "One entry per activity, logged the same week, tagged to the skills it evidences - ten minutes now saves an afternoon in Year 2",
                    "Take ten minutes off your placement",
                    "Spend ten minutes on social media"
                ],
                "answerIndex": 1,
                "explanation": "One entry per activity, logged the same week, tagged to the skills it evidences. Ten minutes now saves an afternoon in Year 2."
            }
        },
        {
            "title": "A reflection that meets the standard",
            "content": "Reflection is a professional skill, not an admin task. Compare: Descriptive: 'I edited the radio package. It went okay. I was not sure about the sound.' Analytical: 'I cut a three-minute package for the radio show. The music kept covering the voice, so I dropped the music. That did not fix it: my voice was recorded too far from the mic, so lifting it lifted the room noise as well. I re-recorded close to the mic and the mix cleared. The fault was in the recording, not the edit. Next time I set levels as I record.' The second names the decision, the reasoning, the evidence and the change in practice - the level a personal statement or a professional portfolio needs. The Reflection Coach prompts you towards this. It does not do it for you, and an assessor can tell the difference.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the difference between the 'descriptive' and 'analytical' reflection examples?",
                "options": [
                    "There is no difference",
                    "The analytical one names the decision, the reasoning, the evidence and the change in practice - the level a personal statement or a professional portfolio needs",
                    "Descriptive is always better",
                    "Analytical removes emotion"
                ],
                "answerIndex": 1,
                "explanation": "The second names the decision, the reasoning, the evidence and the change in practice - the level a personal statement or a professional portfolio needs."
            }
        },
        {
            "title": "Your first two weeks - eight tasks",
            "content": "Complete these independently by the end of week two. (1) App or shortcut set up. (2) Skills Assessment completed honestly. (3) Results interpreted - Green, Amber and Red. (4) Skills Focus set from your Amber and Red. (5) Next Destination set, entry requirements checked. (6) Career Quiz completed, every profile reviewed. (7) Digital CV Introduction written. (8) One activity logged, with a strong reflection. No reminders are coming, and that is deliberate. If you hit a genuine barrier, message your tutor in the app - asking early is a professional skill, not a weakness.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are among the eight 'first two weeks' tasks the deck lists? Select all that apply.",
                "options": [
                    "App or shortcut set up",
                    "Skills Assessment completed honestly",
                    "Results interpreted - Green, Amber and Red",
                    "One activity logged, with a strong reflection"
                ],
                "correctIndices": [0, 1, 2, 3],
                "explanation": "All four are among the eight tasks to complete by the end of week two."
            }
        }
    ]
}
write("l3y2-h-learn.json", mod_h)

# ============================================================
# Module I L3 Y2: Professional Behaviour & Personal Strengths
# ============================================================
mod_i = {
    "section": "l3y2-i", "level": "l3", "year": "y2", "module": "I",
    "title": "Professional Behaviour & Personal Strengths",
    "slides": [
        {
            "title": "Why this is a deployment, not a repeat",
            "content": "You built the evidence last year. This year you use it. About 90 minutes. Requires Navigate. PROUD anchor: Show Respect. Last year you were building an evidence bank - this year applications open, and today we get that bank application-ready. Everything you produce this morning goes into something live.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the framing of this Year 2 professional behaviour session, according to the deck?",
                "options": [
                    "A repeat of last year",
                    "Deployment, not repetition - last year you built the evidence bank; this year you use it",
                    "A new-starter welcome",
                    "A pass/fail test"
                ],
                "answerIndex": 1,
                "explanation": "You built the evidence last year. This year you use it. The framing is deployment, not repetition."
            }
        },
        {
            "title": "The session in eight beats",
            "content": "Eight beats in about 90 minutes: (1) Settling in - Year 2, week three (10) (2) The standard didn't reset (15) (3) Your reference goes live this year (10) (4) Human skills - interview currency (15) (5) Skills Assessment - what moved? (15) (6) Claims versus evidence - sharper (10) (7) Three strengths, application-ready (10) (8) One thing (5). The outputs go straight into this year's applications.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the eight beats of this Year 2 professional behaviour session in the order the deck presents them.",
                "items": [
                    "Settling in - Year 2, week three",
                    "The standard didn't reset",
                    "Your reference goes live this year",
                    "Human skills - interview currency",
                    "Skills Assessment - what moved?",
                    "Claims versus evidence - sharper",
                    "Three strengths, application-ready",
                    "One thing"
                ],
                "solution": [0, 1, 2, 3, 4, 5, 6, 7]
            }
        },
        {
            "title": "The standard didn't reset - and this year counts double",
            "content": "You know the standard - you kept it for a year, including on placement. Year 2 isn't about learning it. It's about not fumbling it in the year that counts double. The list you already know: turning up - on time, kit charged, files backed up; flagging problems early - before a deadline or a deliverable slips; how you speak to people - in the room, in the group chat, and online; owning mistakes and putting them right, rather than hiding them. This is Show Respect in practice - respect for people's time, for the work, and for your own future. You practised it all last year. This year, referees are watching.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Why does the deck say 'this year counts double'?",
                "options": [
                    "Because you get two grades",
                    "Because this is the year referees and interviewers are actually watching - applications open, references get read",
                    "Because you have double the work",
                    "Because there are two of you"
                ],
                "answerIndex": 1,
                "explanation": "This year counts double because this is the year referees and interviewers are actually watching."
            }
        },
        {
            "title": "Your reference goes live this year",
            "content": "Last year we told you your reference was being written. This year it gets read - applications for apprenticeships, jobs and degrees, including at University Centre Hastings, go out in the months ahead. What gets drawn on: references reflect attendance, punctuality and reliability across the whole record - employers, providers and admissions teams ask for exactly that. Recent pattern weighs heaviest: referees write from the freshest evidence. Whatever last year looked like, this term is the one sitting in front of them. A strong finish is in your control. The record is built from small, repeated behaviours - which makes the last lap the easiest one to get right on purpose.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what matters most for the reference?",
                "options": [
                    "Year 1 attendance only",
                    "Recent pattern - referees write from the freshest evidence, and this term is the one sitting in front of them",
                    "How many courses you took",
                    "Your predicted grades"
                ],
                "answerIndex": 1,
                "explanation": "Recent pattern weighs heaviest - referees write from the freshest evidence."
            }
        },
        {
            "title": "Human skills - interview currency",
            "content": "You've now seen these in the wild - on placement, on projects, in part-time work. At interview, nearly every question is secretly about one of them. Six skills: Communication (explaining your work clearly - to a team, a client or an audience); Teamwork (being someone people want to work with again); Reliability (delivering what you promised, on the date you promised it); Problem-solving (working it out when there's no tutorial and no template); Adaptability (coping well when the brief, the kit or the client changes); Initiative (spotting what needs doing without being asked). Quick audit: which two did placement prove you're strongest at? Which one would your placement supervisor say needs work?",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's claim about interview questions?",
                "options": [
                    "They are all about technical skill",
                    "At interview, nearly every question is secretly about one of the human skills (communication, teamwork, reliability, problem-solving, adaptability, initiative)",
                    "They are random",
                    "They are about personality tests only"
                ],
                "answerIndex": 1,
                "explanation": "At interview, nearly every question is secretly about one of the six human skills."
            }
        },
        {
            "title": "Skills Assessment - what moved?",
            "content": "You have a Year 1 baseline. Today's question isn't 'what are my skills?' - it's 'what moved, and what does that prove?' Steps: (1) Open your results (log in to Navigate). (2) Compare against last year - what moved? What didn't? Placement should show up here - does it? (3) Pick two things: one strength with a year of evidence behind it, and the one development priority that matters for your applications. (4) Cross-check with a partner who knows your work. Movement is the story. A skill that shifted over a year, with placement evidence behind it, is exactly what interviewers ask about.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the Year 2 reframe of the Skills Assessment, according to the deck?",
                "options": [
                    "Same as Year 1 - what are my skills?",
                    "What moved, and what does that prove? - movement is the story",
                    "Pass or fail",
                    "A self-assessment only"
                ],
                "answerIndex": 1,
                "explanation": "Today's question isn't 'what are my skills?' - it's 'what moved, and what does that prove?'"
            }
        },
        {
            "title": "Claims versus evidence - sharper",
            "content": "'I'm reliable and hard-working.' A claim. Every application form says it - it costs nothing, proves nothing, and shortlisters skim straight past it. 'On placement I fixed a file nobody else could open - then wrote a one-page guide so the next person could do it without me.' Evidence. Specific, checkable, memorable - and only you can say it. SITUATION -> WHAT YOU ACTUALLY DO -> WHAT IT SHOWS. You have a year the Year 1s don't: placement, briefs you delivered, part-time work, everything you made or fixed. Mine all of it. You are the best-evidenced applicants this college produces. Most of you just haven't written it down yet.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, which of these is 'evidence' rather than a claim?",
                "options": [
                    "'I'm reliable and hard-working'",
                    "'On placement I fixed a file nobody else could open - then wrote a one-page guide so the next person could do it without me'",
                    "'I'm a team player'",
                    "'I work well under pressure'"
                ],
                "answerIndex": 1,
                "explanation": "'On placement I fixed a file nobody else could open - then wrote a one-page guide' is specific, checkable, memorable evidence."
            }
        },
        {
            "title": "Three strengths, application-ready",
            "content": "Not a worksheet. These are your interview answers and application paragraphs, in draft. Steps: (1) Choose three - draw on placement and the whole of last year; pick the three with the strongest evidence, the ones a referee would recognise. (2) Draft each as an evidenced statement - Situation -> what you actually do -> what it shows. Placement evidence first where you have it. (3) Test on a partner - their only job is to ask 'what's your evidence?' until they believe you - then ask the interview follow-up: 'what happened next?' (4) Refine - then update Navigate. Replace last year's versions. These go into live applications this term. Write them like they'll be read by the person deciding whether to interview you - because this year, they will be.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What should students do with the three strengths at the end of this activity?",
                "options": [
                    "Keep them in a folder",
                    "Replace last year's versions in Navigate - they go into live applications this term",
                    "Memorise them word for word",
                    "Email them to the safeguarding team"
                ],
                "answerIndex": 1,
                "explanation": "Replace last year's versions. These go into live applications this term."
            }
        },
        {
            "title": "One thing - this week",
            "content": "Pick one. Write it down, make it specific, hand it in. Your tutor keeps the cards - and will ask you how it went. (1) Act on my applications-critical development priority - one concrete step, named. (2) Use one of my three statements in something live - an application, my Navigate CV, an interview prep answer. (3) Reset the professional habit that slipped over summer - name it, and name where. (4) Tell someone about something that's making it hard to show up. Small and done beats impressive and imaginary.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's tagline for the commitment card?",
                "options": [
                    "Think big, dream big",
                    "Small and done beats impressive and imaginary",
                    "Big and bold is best",
                    "You have to do all four"
                ],
                "answerIndex": 1,
                "explanation": "Small and done beats impressive and imaginary."
            }
        }
    ]
}
write("l3y2-i-learn.json", mod_i)

# ============================================================
# Module J L3 Y2: Work Experience
# ============================================================
mod_j = {
    "section": "l3y2-j", "level": "l3", "year": "y2", "module": "J",
    "title": "Work Experience - Skills Week, Aimed at Your Specialism",
    "slides": [
        {
            "title": "What this session covers - and the framing",
            "content": "Work Experience - Skills Week, your second placement, aimed at your specialism. About 1 hour. PROUD anchor: Seek Opportunity. The returner framing: 'You've done this once already - so this time we're building on what you know, not starting from zero.' However last year went, this is a fresh run at it - not a repeat test. The real risk with this group is complacency, not unfamiliarity - name it directly.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the Year 2 framing of this work experience session, according to the deck?",
                "options": [
                    "Starting from zero",
                    "Building on what you know - this is a fresh run at it, not a repeat test",
                    "Skip it - you did it last year",
                    "It's a placement-finding workshop"
                ],
                "answerIndex": 1,
                "explanation": "You've done this once already - so this time we're building on what you know, not starting from zero."
            }
        },
        {
            "title": "Why it matters even more this year",
            "content": "Two placements beat one: two entries on a CV, two referees, and a portfolio that shows range as well as skill. UCAS and apprenticeship applications open soon. A recent, relevant placement is stronger evidence than last year's alone. Aim it at your Final Major Project or specialism - the work you want to be known for after college. Seek Opportunity: doing this once was practising the value. Doing it again, deliberately, is what turns it into a habit.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, why does a second placement matter more?",
                "options": [
                    "It counts as a third course",
                    "Two placements beat one: two CV entries, two referees, a portfolio that shows range as well as skill",
                    "It's required by law",
                    "It is worth double marks"
                ],
                "answerIndex": 1,
                "explanation": "Two placements beat one: two entries on a CV, two referees, and a portfolio that shows range as well as skill."
            }
        },
        {
            "title": "What's on offer - and the 30-hour reset",
            "content": "Block placement, employer visits, volunteering, live project briefs, industry partnerships - same options as last year. This time, choose the one closest to the specialism you are heading into. Yes, it's another 30 hours. The requirement resets each academic year - last year's hours don't carry over. On a T Level, this sits inside your larger industry placement. No placement by Skills Week? You come into college for an employer-set brief and employer talks instead. It still counts.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What happens if you don't get a placement by Skills Week?",
                "options": [
                    "You're marked absent",
                    "You come into college for an employer-set brief and employer talks instead. It still counts",
                    "You fail the year",
                    "You take a 30-hour penalty"
                ],
                "answerIndex": 1,
                "explanation": "No placement by Skills Week? You come into college for an employer-set brief and employer talks instead. It still counts."
            }
        },
        {
            "title": "This year's dates - Skills Week and the deadline",
            "content": "Skills Week: Monday 8 March 2027 - this is your Work Experience week, the placement itself happens here. Request deadline: Friday 5 February 2027 - your placement must be requested on Navigate by this date, at least 4 weeks before Skills Week. Why 4 weeks? It gives the Careers & Employability team time to check your employer - health & safety, insurance and safeguarding checks - before you're allowed to start. Miss the deadline and there may not be time to approve your placement before Skills Week. Some placements also need a DBS check, or the employer's own IT and confidentiality rules.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the Skills Week date for Year 2, according to the deck?",
                "options": ["Monday 8 March 2027", "Monday 1 February 2027", "Friday 5 February 2027", "Monday 15 March 2027"],
                "answerIndex": 0,
                "explanation": "Skills Week: Monday 8 March 2027."
            }
        },
        {
            "title": "Requesting your placement - the Navigate refresher",
            "content": "Same process as last year - you'll source and request your placement through Navigate. Need a refresher? See Module H - How to Use Navigate. You'll need: company name & full address; employer contact name, phone & email; start and end dates; the days and times you've agreed; your tutor's name; what tasks/role you'll be doing. Placements must fit within college hours (8.30am-5.30pm), max 8-hour day. Agency, studio and IT support hours fit easily; shoots, events and live broadcasts may not - agree your times in writing before you request. Access via My Student Life; direct login: login.navigate.uk.com.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What are the college hours a placement must fit within, according to the deck?",
                "options": ["9am-5pm", "8.30am-5.30pm, max 8-hour day", "8am-6pm", "Anytime"],
                "answerIndex": 1,
                "explanation": "Placements must fit within college hours (8.30am-5.30pm), max 8-hour day."
            }
        },
        {
            "title": "Careers & Employability team - by campus",
            "content": "Same team, same campuses. Eastbourne: ECAT House, room 101 - Eastbourne.Careers@escg.ac.uk. Hastings: Careers Hub, Ground Floor - Hastings.Careers@escg.ac.uk. Ore: ask at reception - Hastings.Careers@escg.ac.uk. Lewes: Cliffe Building, room 134 - Lewes.Careers@escg.ac.uk. Newhaven: ask at reception - Lewes.Careers@escg.ac.uk. The email addresses are shared team inboxes, not one individual. If a placement isn't progressing, or something doesn't feel right, don't wait - go to your campus Careers & Employability team, or tell your tutor.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Where is the Careers & Employability team based at Lewes, according to the deck?",
                "options": ["ECAT House, room 101", "Careers Hub, Ground Floor", "Cliffe Building, room 134", "Ask at reception"],
                "answerIndex": 2,
                "explanation": "Lewes: Cliffe Building, room 134 - Lewes.Careers@escg.ac.uk."
            }
        },
        {
            "title": "On placement - raising the bar",
            "content": "Timekeeping: be on time, every day. Running late or unwell? Contact the employer AND the college. Dress & conduct: check the dress code before you start. Most studios, agencies and IT teams are smart casual; on a shoot or an install, wear something you can actually work in. Communication: keep in touch with your placement provider - don't go quiet if plans change. Logging hours: complete your Navigate journal and timesheet every day you attend. Record what you actually did - your reference will be written from it. Raising concerns: speak to your employer contact first if it's minor - or your tutor / Careers & Employability team if it isn't. Professionalism compounds - employers and referees remember you.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What should you do if you are running late or unwell for placement?",
                "options": [
                    "Text a friend",
                    "Contact the employer AND the college",
                    "Just turn up when you can",
                    "Stay home and email your tutor only"
                ],
                "answerIndex": 1,
                "explanation": "Running late or unwell? Contact the employer AND the college."
            }
        },
        {
            "title": "One thing I'll do this week",
            "content": "Pick one option. Write or draw it on your card. Your tutor keeps it and will check in with you. (1) Build on last time - I'll decide whether to go somewhere new or go deeper with the same employer, and which is closer to my specialism. (2) Note the dates - I'll write 5 Feb and 8 March somewhere I'll actually see them. (3) Refresh on Navigate - I'll check I remember what information I'll need before I request a placement. (4) Tell someone - I'll tell my tutor or the Careers & Employability team if I'm unsure about something, or a placement concern comes up.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the closing line of the Year 2 work-experience session?",
                "options": [
                    "Good luck, see you next term",
                    "This is round two - use what you already know, and go further than last time. In this industry the people who get taken on are the ones who came back sharper. Seek the opportunity - again.",
                    "Remember to log your hours",
                    "We'll send a reminder"
                ],
                "answerIndex": 1,
                "explanation": "This is round two - use what you already know, and go further than last time. In this industry the people who get taken on are the ones who came back sharper. Seek the opportunity - again."
            }
        }
    ]
}
write("l3y2-j-learn.json", mod_j)

# ============================================================
# Module K L3 Y2: Progression & Goals - The Final Year
# ============================================================
mod_k = {
    "section": "l3y2-k", "level": "l3", "year": "y2", "module": "K",
    "title": "Progression & Goals - The Final Year",
    "slides": [
        {
            "title": "The last induction session you'll ever sit through",
            "content": "Progression & Goals: The Final Year. Group 3: Employability, Careers & Progression. About 90 minutes. PROUD anchor: Seek Opportunity. Ninety minutes to turn two years of digital and media evidence into a plan - with the first application deadline already live. The deck earns its place by being useful, not ceremonial. Urgency without panic - the antidote to both is margin ('early beats on-time' said calmly, often).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the framing of this final progression session, according to the deck?",
                "options": [
                    "A ceremonial farewell",
                    "The last induction session you'll ever sit through - ninety minutes to turn two years of evidence into a plan, with the first application deadline already live",
                    "An exam preparation session",
                    "A placement briefing"
                ],
                "answerIndex": 1,
                "explanation": "The last induction session you will ever sit through. Ninety minutes to turn two years of digital and media evidence into a plan - with the first application deadline already live."
            }
        },
        {
            "title": "The session in eight beats",
            "content": "Eight beats in about 90 minutes: (1) Final year - what is actually different (10) (2) The map, with dates on it (15) (3) Two years of evidence - now it gets used (10) (4) Application goals - concrete by definition (10) (5) Three horizons - backwards from the deadlines (15) (6) Right route? - the honest check (10) (7) Closing the loop (10) (8) One goal, on paper (10).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the eight beats of this final progression session in the order the deck presents them.",
                "items": [
                    "Final year - what is actually different",
                    "The map, with dates on it",
                    "Two years of evidence - now it gets used",
                    "Application goals - concrete by definition",
                    "Three horizons - backwards from the deadlines",
                    "Right route? - the honest check",
                    "Closing the loop",
                    "One goal, on paper"
                ],
                "solution": [0, 1, 2, 3, 4, 5, 6, 7]
            }
        },
        {
            "title": "The map, with dates on it",
            "content": "Autumn - now: research routes, audit your Navigate record, register with UCAS if university is in the plan. Everything on this slide is easier done in October than in January. By January: university applications in - the UCAS equal-consideration deadline lands mid-January. Done before Christmas beats done in a panic, every single year. Autumn to spring: higher and degree apprenticeship vacancies run on rolling deadlines all year - the strongest close early. Digital degree apprenticeship employers typically open between October and January. The strongest vacancies close first. Check individual closing dates this week. Results day: the grades that convert offers into places. Every deadline above exists to protect the time you need to earn them - the application is the easy half.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's claim about 'results day' in relation to the application cycle?",
                "options": [
                    "Results day is more important than the application",
                    "Every deadline above exists to protect the time you need to earn them - the application is the easy half",
                    "Results day is the only thing that matters",
                    "It is at the end of Year 2"
                ],
                "answerIndex": 1,
                "explanation": "Every deadline above exists to protect the time you need to earn them - the application is the easy half."
            }
        },
        {
            "title": "Two years of evidence - now it gets used",
            "content": "Everything you logged in Year 1 becomes application material this term. Audit it now, while gaps are still fixable. My Digital CV - this is the raw material for every application you make this year. Audit it this week - what is missing is fixable in October and unfixable in January. Skills Assessment - your results point at what to sharpen before interviews and assessments, and the growth since Year 1 is exactly what statements and interviews want to hear about. Opportunities record - every placement and project from Year 1 is application evidence. If it happened and is not logged, it effectively did not happen. Fix that this week. Where it goes, starting now: UCAS, apprenticeship applications, references. Your references and applications get written from this record this term - not from anyone's memory.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's verdict on Year 1 evidence that isn't logged?",
                "options": [
                    "It's still useful informally",
                    "If it happened and is not logged, it effectively did not happen. Fix that this week",
                    "It can be re-created later",
                    "It only matters for university"
                ],
                "answerIndex": 1,
                "explanation": "If it happened and is not logged, it effectively did not happen. Fix that this week."
            }
        },
        {
            "title": "Application goals - concrete by definition",
            "content": "Aspiration: 'I want to study Games Design at university.' Goal: 'By half-term my UCAS choices are confirmed and my personal statement has had one round of teacher feedback. First step: arrange a feedback session this week.' The test this year is harsher: does it beat the deadline with room to spare? On-time is the new late. On-time is dangerous because references, predictions and redrafts all consume calendar the student does not control.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the 'test' the deck applies to Year 2 goals?",
                "options": [
                    "Does it look ambitious?",
                    "Does it beat the deadline with room to spare? On-time is the new late",
                    "Does it sound good in a tutor's meeting?",
                    "Does it match what your friends are doing?"
                ],
                "answerIndex": 1,
                "explanation": "The test this year is harsher: does it beat the deadline with room to spare? On-time is the new late."
            }
        },
        {
            "title": "Three horizons - backwards from the deadlines",
            "content": "Three horizons, drafted backwards from results day because the grades decide everything and the calendar exists to protect the time they need. (1) This half-term - route chosen, record audited, first application started; the groundwork. (2) By January - every application submitted, before the deadline, not on it. (3) Results day - the grades that turn offers into places, what the whole year answers to. Draft one goal for each horizon. Start at results day and work backwards. The strongest becomes your card, and all three feed your ILP.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Why does the deck say to start drafting goals 'backwards from results day'?",
                "options": [
                    "It's easier to remember",
                    "Because the grades decide everything and the application calendar exists to protect the time they need",
                    "Because tutors prefer it",
                    "Because UCAS requires it"
                ],
                "answerIndex": 1,
                "explanation": "Start at results day and work backwards - the grades decide everything, and the application calendar exists to protect the time they need."
            }
        },
        {
            "title": "Right route? - the honest check",
            "content": "Nobody in this room gets a course change - that ship sailed last year. But the destination is still yours to choose, and Year 2 pressure is real. 'The route feels shaky' - normal, Year 2 pressure does that to solid plans. This is a support conversation, not a crisis: tutor, subject staff, and the plan you have just written. Shaky is not the same as wrong. 'The route is wrong' - university, apprenticeship, employment: changing the destination is still entirely possible this term, and cheaper now than after applications go in. Changing the effort level is not. Book Careers this week. You can still change where you are going. You cannot get this year back.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the deck's mustard-line summary of the route check?",
                "options": [
                    "Just stick with what you chose",
                    "You can still change where you are going. You cannot get this year back",
                    "Talk to your parents",
                    "Apply to anything, fast"
                ],
                "answerIndex": 1,
                "explanation": "You can still change where you are going. You cannot get this year back."
            }
        },
        {
            "title": "One goal, on paper",
            "content": "Take the strongest goal from your three horizons - or choose one of these. Write it. Specific, first step, date with margin. (1) My application goal is ... and my first step this week is .... (2) I will audit my Navigate record this week and fix one gap. (3) I will research and shortlist my application route - university, degree apprenticeship or industry role - and book a Careers conversation about what a strong application from this course actually looks like. (4) I am worried about this year - I will talk to my tutor this week. Your tutor keeps these. This one follows you into your ILP - and this year, it gets checked against real dates. End of induction. Don't fumble the last lap. In Digital, Media and Film, the last lap is applications, portfolio and assessed work running in parallel. Plan for all three. Do not fumble the final year.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the closing line of the entire induction programme, according to the deck?",
                "options": [
                    "Good luck, Year 2",
                    "End of induction. Don't fumble the last lap. In Digital, Media and Film, the last lap is applications, portfolio and assessed work running in parallel. Plan for all three. Do not fumble the final year.",
                    "See you in September",
                    "Remember to log your hours"
                ],
                "answerIndex": 1,
                "explanation": "End of induction. Don't fumble the last lap. In Digital, Media and Film, the last lap is applications, portfolio and assessed work running in parallel."
            }
        }
    ]
}
write("l3y2-k-learn.json", mod_k)

print("Wrote H, I, J, K")
