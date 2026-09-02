#!/usr/bin/env python3
"""Write Module D L3 Y1 learn file - safer than hand-written JSON."""
import json
from pathlib import Path

learn = {
    "section": "l3y1-d",
    "level": "l3",
    "year": "y1",
    "module": "D",
    "title": "Students' Voice & Student Rep Elections",
    "note": "Content sourced from the Year 2 / L3 variant of this deck (see SOURCE_OF_TRUTH note in the PowerPoint's teacher appendix). Swap when a true Year 1 deck is provided.",
    "slides": [
        {
            "title": "What this session is about",
            "content": "You're training for industry — placements, employer briefs, live products. This is how you get a say in how that training runs. The session is around 100 minutes. The PROUD value this module is grounded in is Encourage Unity.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which PROUD value is this module grounded in?",
                "options": ["Seek Opportunity", "Show Respect", "Encourage Unity", "Be Proud"],
                "answerIndex": 2,
                "explanation": "Module D is grounded in Encourage Unity."
            }
        },
        {
            "title": "The session in eight beats",
            "content": "Eight beats in around 100 minutes: Check-in (10) -> Students' Voice (10) -> Ways to get involved (10) -> The Rep role (10) -> The Governor role (15) -> Encourage Unity (5) -> Election (30-35) -> Close. Today ends with an election.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the eight beats of this session in the order the deck presents them.",
                "items": [
                    "Check-in",
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
            "title": "What makes student voice actually work",
            "content": "Students' Voice doesn't work automatically. It works when the rep is genuinely plugged in, and when the group uses them. Four conditions for effectiveness: reps who actually consult their group - not just improvise at meetings; feedback that names the thing - 'four edit stations can't run Premiere' beats 'the software is rubbish'; groups who tell their rep what matters - before the meeting, not after; students who follow up - checking the licence actually arrived, or the kit was actually booked. Collective voice is a shared responsibility, not just the rep's job.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is an example of feedback that 'names the thing', according to the deck?",
                "options": [
                    "'The software is rubbish'",
                    "'Four edit stations can't run Premiere'",
                    "'The course could be better'",
                    "'Things would be good if they were better'"
                ],
                "answerIndex": 1,
                "explanation": "'Four edit stations can't run Premiere' beats 'the software is rubbish' - that's feedback that names the thing."
            }
        },
        {
            "title": "Four ways to get involved",
            "content": "Pick the one that fits. Student Rep - elected today; you speak for this group at Student Council, and you elect a rep for your English and maths class too. Student Governor - 3 places on the Main Governing Board, where studio, kit and software investment gets decided; applications close midday, Friday 16 October. NUS Membership - you're already a member; TOTUM card (£14.99/year) gives discounts across hundreds of retailers. Surveys & Forums - the Induction Survey opens 3 November; three minutes, the place to report a software, kit or placement problem while there's still time to fix it.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are 'ways to get involved' from the deck? Select all that apply.",
                "options": ["Student Rep", "Student Governor", "NUS Membership (TOTUM card)", "Surveys & Forums"],
                "correctIndices": [0, 1, 2, 3],
                "explanation": "All four are the ways to get involved."
            }
        },
        {
            "title": "What the Student Rep does",
            "content": "Reps gather and convey student opinions to college leadership; attend 3 Student Council meetings per year; provide feedback on teaching, studios, edit suites, kit and software licences; work with staff to develop solutions - not just present problems; keep the group informed after every meeting. This group also elects an English/maths rep today who represents the group in that class. Employers notice this role: it is evidence of communication, negotiation and professional conduct, and it develops leadership, problem-solving and employability skills. Rep training: Wednesday 14 October (all campuses) - mandatory for newly elected reps.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How many Student Council meetings per year does a rep attend, according to the deck?",
                "options": ["1", "3", "6", "12"],
                "answerIndex": 1,
                "explanation": "Reps attend 3 Student Council meetings per year."
            }
        },
        {
            "title": "What a Student Governor does",
            "content": "There are 3 Student Governor places on the Main Governing Board - strategic decisions about the whole college. Governors represent authentic student experience - what an industry placement or an employer-set brief is actually like; contribute to decisions on curriculum and budget - software licences, studio kit, where investment goes; and it's described as exceptional leadership experience - genuinely CV-worthy at this level. The role is different from Student Rep: strategic scope and institutional weight rather than group representation. You must be planning to study at ESCG for at least one more year - Year 2 of this course counts.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the eligibility requirement to apply for Student Governor, according to the deck?",
                "options": [
                    "Any current student, in any year",
                    "Students planning to study at ESCG for at least one more year",
                    "Only Year 1 students",
                    "Only students with a UCAS offer"
                ],
                "answerIndex": 1,
                "explanation": "You must be planning to study at ESCG for at least one more year - Year 2 of this course counts."
            }
        },
        {
            "title": "Governor commitment and application",
            "content": "The commitment is roughly 3-5 hours a month, across the academic year: 4 Board meetings (2-3 hours each), around 3 committee meetings, 2 strategy days, plus reading papers in advance. Support: induction with the Director of Governance, ongoing training, Governor portal and iPad, expenses reimbursed, and an annual 1:1 with the Chair. To apply: (1) submit the online nomination form by midday, Friday 16 October; (2) informal conversation about your interest (2-5 November - not an interview); (3) student ballot if more candidates than places (9-23 November); (4) committee recommendation 24 November; formal Board appointment 14 December. Director of Governance: Belle Howard, Belle.Howard@escg.ac.uk.",
            "example": "",
            "exampleOutput": "",
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
            "title": "One person's complaint, a group's evidence",
            "content": "Encourage Unity is the point of this module. One person's complaint is an opinion. A group saying the same thing is evidence - and evidence is what changes decisions. One person waiting for a camera is bad luck. A whole cohort waiting is evidence. On placement and in the studio you already spot what isn't working - you flag a fault on a shoot without being asked. Do the same here. A rep you helped choose is a rep who'll listen when you tell them what matters. The group that engages this year sets the standard for the one that comes after.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck describe the difference between one person's complaint and a group's view?",
                "options": [
                    "Both are opinions",
                    "One is an opinion; a group saying the same thing is evidence - and evidence is what changes decisions",
                    "A single complaint carries more weight than a group",
                    "Only written complaints counts"
                ],
                "answerIndex": 1,
                "explanation": "One person's complaint is an opinion. A group saying the same thing is evidence - and evidence is what changes decisions."
            }
        },
        {
            "title": "Election time",
            "content": "The election has four stages: Nominations - any student may put themselves forward; two seats are elected today: course rep and English/maths rep. Candidate pitches - 1 minute each; say what you'd actually do, be specific. The vote - the group decides the fairest method; slips work well when the group is split across placement days. Confirm & register - announce both results and add both reps to the central Student Rep Register before the session ends. Student Rep elections must be completed and the rep confirmed no later than the end of Week 2.",
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these are stages of the election in the deck? Select all that apply.",
                "options": ["Nominations", "Candidate pitches", "The vote", "Confirm & register"],
                "correctIndices": [0, 1, 2, 3],
                "explanation": "All four are the stages: Nominations -> Pitches -> Vote -> Confirm & register."
            }
        }
    ]
}

out = Path("data/l3y1-d-learn.json")
out.write_text(json.dumps(learn, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {out}")