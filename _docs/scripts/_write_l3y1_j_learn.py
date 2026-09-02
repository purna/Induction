#!/usr/bin/env python3
"""Module J L3 Y1 (Work Experience)."""
import json
from pathlib import Path

META_LEARN = {
    "section": "l3y1-j",
    "level": "l3",
    "year": "y1",
    "module": "J",
    "title": "Work Experience",
}

slides_data = [
    {
        "title": "What this module is about",
        "content": "Work experience isn't an add-on to your course - it's the part of your training that happens outside college. The PROUD value this module is grounded in is Seek Opportunity. By the end of this session you'll know why work experience matters for your course, what your options are, the two dates you need to know, and exactly who to go to if you get stuck.",
        "exercise": {"type": "scored",
                     "prompt": "Which PROUD value is this module grounded in?",
                     "options": ["Show Respect", "Encourage Unity", "Seek Opportunity", "Be Proud"],
                     "answerIndex": 2,
                     "explanation": "Seek Opportunity - actively going after something rather than waiting for it to arrive."}
    },
    {
        "title": "Why work experience matters",
        "content": "Employability: this industry hires on evidence - a portfolio, a showreel, code you've written, a reference from someone who watched you work. Progression: UCH Hastings, a degree elsewhere, a higher apprenticeship - all of them ask what you've done outside the classroom. Professional identity: editor, animator, developer, analyst, photographer - a placement is how you test which of these you actually want. Work experience is one of the most direct ways you'll practise Seek Opportunity while you're here.",
        "exercise": {"type": "scored",
                     "prompt": "What does the deck say this industry hires on?",
                     "options": ["Qualifications alone",
                     "Evidence - a portfolio, a showreel, code you've written, a reference from someone who watched you work",
                     "Connections",
                     "Luck"],
                     "answerIndex": 1,
                     "explanation": "This industry hires on evidence - a portfolio, a showreel, code you've written, a reference from someone who watched you work."}
    },
    {
        "title": "What work experience can look like",
        "content": "Five types. Block placement: a set period with one employer. Employer visits: shorter, structured visits to a workplace. Volunteering: unpaid work with a genuine organisational need. Live project briefs: real employer problems, worked on in college. Industry partnerships: activity run through ESCG's employer links. Not every type suits every course - your tutor will confirm yours. On a T Level, your industry placement is separate and much bigger (around 315 hours); Skills Week is one part of it, not all of it. Haven't got a placement yet? You'll come into college and work on an employer-set brief - a real task from a real employer - plus employer talks.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these are types of work experience the deck lists? Select all that apply.",
                     "options": ["Block placement", "Employer visits", "Volunteering", "Live project briefs", "Industry partnerships"],
                     "correctIndices": [0, 1, 2, 3, 4],
                     "explanation": "All five are the types of work experience the deck lists."}
    },
    {
        "title": "The dates you need to know",
        "content": "Skills Week: Monday 8 March 2027. This is your Work Experience week - the placement itself happens here. Request deadline: Friday 5 February 2027. Your placement must be requested on Navigate by this date - at least 4 weeks before Skills Week. Why 4 weeks? It gives the Careers & Employability team time to check your employer - health & safety, insurance and safeguarding checks - before you're allowed to start. Miss the deadline and there may not be time to approve your placement before Skills Week. Some placements also need a DBS check, or the employer's own IT and confidentiality rules.",
        "exercise": {"type": "insert",
                     "prompt": "Fill in the blank: your placement must be requested on Navigate by Friday ____ February 2027.",
                     "template": "Your placement must be requested on Navigate by Friday ____ February 2027.",
                     "options": ["1st", "5th", "12th", "26th"],
                     "answerIndex": 1,
                     "explanation": "Friday 5 February 2027."}
    },
    {
        "title": "Finding and applying for a placement",
        "content": "You'll source and request your placement through Navigate. You'll need this information ready before you request a placement: company name & full address; employer contact name, phone & email; start and end dates; the days and times you've agreed; your tutor's name; what tasks/role you'll be doing. Placements must fit within college hours (8.30am-5.30pm), max 8-hour day. Agency, studio and IT support hours fit easily; shoots, events and live broadcasts may not - agree your times in writing before you request. Navigate lives inside My Student Life - or go straight to login.navigate.uk.com.",
        "exercise": {"type": "scored",
                     "prompt": "Within what hours must placements fit, according to the deck?",
                     "options": ["7am-7pm", "8.30am-5.30pm", "9am-5pm", "24/7"],
                     "answerIndex": 1,
                     "explanation": "Placements must fit within college hours (8.30am-5.30pm), max 8-hour day."}
    },
    {
        "title": "Who to go to for help",
        "content": "Every campus has a Careers & Employability team. Eastbourne: ECAT House, room 101 / Eastbourne.Careers@escg.ac.uk. Hastings: Careers Hub, Ground Floor / Hastings.Careers@escg.ac.uk. Ore: Ask at reception / Hastings.Careers@escg.ac.uk. Lewes: Cliffe Building, room 134 / Lewes.Careers@escg.ac.uk. Newhaven: Ask at reception / Lewes.Careers@escg.ac.uk. If a placement isn't progressing, or something doesn't feel right, don't wait - go to your campus Careers & Employability team, or tell your tutor.",
        "exercise": {"type": "insert",
                     "prompt": "Fill in the blank: Lewes Careers & Employability is in the Cliffe Building, room ____.",
                     "template": "Lewes Careers & Employability is in the Cliffe Building, room ____.",
                     "options": ["12", "101", "134", "175"],
                     "answerIndex": 2,
                     "explanation": "Lewes: Cliffe Building, room 134."}
    },
    {
        "title": "While you're on placement",
        "content": "Timekeeping: be on time, every day; running late or unwell? Contact the employer AND the college. Dress & conduct: check the dress code before you start; most studios, agencies and IT teams are smart casual; on a shoot or an install, wear something you can actually work in. Communication: keep in touch with your placement provider; don't go quiet if plans change. Logging hours: complete your Navigate journal and timesheet every day you attend; record what you actually did - that becomes portfolio and reference evidence. Raising concerns: speak to your employer contact first if it's minor; your tutor / Careers & Employability team if it isn't.",
        "exercise": {"type": "scored",
                     "prompt": "What does the deck say about logging hours on placement?",
                     "options": ["Log at the end of the week",
                     "Complete your Navigate journal and timesheet every day you attend; record what you actually did",
                     "Only log assessed tasks",
                     "Logging is optional"],
                     "answerIndex": 1,
                     "explanation": "Complete your Navigate journal and timesheet every day you attend; record what you actually did."}
    },
    {
        "title": "Your one thing for this week",
        "content": "Pick one, write or draw it on your card. Your tutor keeps it and will check in with you. (1) Start looking - I'll name one place I could approach this week: a production company, an agency, a newsroom, or an IT or security team. (2) Note the dates - I'll write 5 Feb and 8 March somewhere I'll actually see them. (3) Get ready for Navigate - I'll check I know what information I'll need before I request a placement. (4) Tell someone - I'll tell my tutor or the Careers & Employability team if I'm unsure about something, or a placement concern comes up.",
        "exercise": {"type": "multi",
                     "prompt": "Which of these are options on the 'one thing' card? Select all that apply.",
                     "options": ["Start looking - name one place I could approach this week",
                     "Note the dates - write 5 Feb and 8 March somewhere I'll see them",
                     "Get ready for Navigate - check I know what information I'll need",
                     "Tell someone - tell my tutor or Careers if unsure, or a placement concern comes up"],
                     "correctIndices": [0, 1, 2, 3],
                     "explanation": "All four are options on the 'one thing' card."}
    },
    {
        "title": "Before you go",
        "content": "Two dates, one team to go to if you need them - that's all you need to hold onto from today. Skills Week: Monday 8 March 2027. Your deadline: Friday 5 February 2027, on Navigate. Stuck or need help? Your campus Careers & Employability team. This is real employer contact, on your record, working toward your qualification. In this industry you are hired on what you can show and who will vouch for you - a placement builds both. Seek the opportunity.",
        "exercise": {"type": "scored",
                     "prompt": "What's the deck's closing line?",
                     "options": ["'Good luck'",
                     "'In this industry you are hired on what you can show and who will vouch for you - a placement builds both. Seek the opportunity.'",
                     "'Wait and see'",
                     "'Have a great holiday'"],
                     "answerIndex": 1,
                     "explanation": "Seek the opportunity - a placement builds both evidence and vouching."}
    }
]

learn = {**META_LEARN, "slides": slides_data}

p = Path("data/l3y1-j-learn.json")
p.write_text(json.dumps(learn, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {p} ({len(slides_data)} slides)")