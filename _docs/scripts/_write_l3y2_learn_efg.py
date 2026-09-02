#!/usr/bin/env python3
"""Write L3 Y2 learn JSON for modules E, F, G."""
import json
from pathlib import Path

OUT = Path("data")

def write(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", p)

# ============================================================
# Module E L3 Y2: Respect, Relationships & College Values
# ============================================================
mod_e = {
    "section": "l3y2-e", "level": "l3", "year": "y2", "module": "E",
    "title": "Respect, Relationships & College Values",
    "slides": [
        {
            "title": "Why this is a Year 2 session, not Year 1 again",
            "content": "You've seen this content before. This session is about how you apply it in Year 2. Familiarity is the risk. Group 2: Safeguarding, Wellbeing & Respect. The register is peer-level and direct, not introductory. Year 2 means setting the standard for others.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the Year 2 framing for this respect and values session, according to the deck?",
                "options": [
                    "Re-teach all of Year 1's content",
                    "Year 2 means setting the standard for others - peer-level, direct, application not awareness",
                    "Skip the values work",
                    "Cover new laws only"
                ],
                "answerIndex": 1,
                "explanation": "Year 2 means setting the standard for others. The register is peer-level and direct."
            }
        },
        {
            "title": "The session in six beats",
            "content": "Six things today: PROUD Values - consistency, not just awareness; British Values - application, not just knowledge; Equality Act 2010 - your obligations, not just rights; Behaviour Standards - familiarity is not an excuse; Zero Tolerance - inaction is also a choice; How to Report - your responsibility, not just an option.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "dragorder",
                "prompt": "Put the six beats of this Year 2 values session in the order the deck presents them.",
                "items": [
                    "PROUD Values",
                    "British Values",
                    "Equality Act 2010",
                    "Behaviour Standards",
                    "Zero Tolerance",
                    "How to Report"
                ],
                "solution": [0, 1, 2, 3, 4, 5]
            }
        },
        {
            "title": "PROUD in Year 2 - setting the standard",
            "content": "P - Bring Positivity: familiarity can breed indifference. Are you still actively creating a welcoming environment? R - Show Respect: comfort with colleagues isn't a reason to lower your standards of conduct. O - Seek Opportunity: in Year 2, opportunity includes developing others - not just yourself. U - Encourage Unity: established groups can become exclusive. Are you still including people? D - Celebrate Diversity: differences don't disappear because you know people better. Keep noticing them.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What does 'Seek Opportunity' mean in Year 2, according to the deck?",
                "options": [
                    "Look after yourself only",
                    "Opportunity includes developing others - not just yourself",
                    "Wait for opportunities to come to you",
                    "Skip placements to focus on coursework"
                ],
                "answerIndex": 1,
                "explanation": "In Year 2, opportunity includes developing others - not just yourself."
            }
        },
        {
            "title": "British Values - application, not just knowledge",
            "content": "Democracy: you've had a year to see how student voice works at ESCG. How effectively do you think it operates - and what would you do differently? Rule of Law: in Year 2, you understand the rules. The question is whether you're upholding them - and whether you're challenging it when others don't. Individual Liberty: your own choices are more visible now - to peers, staff, and placement providers. How consciously are you exercising that freedom? Mutual Respect & Tolerance: established friendships can make it harder to challenge poor behaviour. Year 2 is when you find out whether your values hold under social pressure.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck describe the 'Rule of Law' beat in Year 2?",
                "options": [
                    "You learn the rules for the first time",
                    "You understand the rules - the question is whether you're upholding them and challenging it when others don't",
                    "The rules don't apply on placement",
                    "It only covers online behaviour"
                ],
                "answerIndex": 1,
                "explanation": "In Year 2, you understand the rules. The question is whether you're upholding them - and whether you're challenging it when others don't."
            }
        },
        {
            "title": "Equality Act 2010 - your obligations",
            "content": "9 protected characteristics: age, disability, gender reassignment, marriage & civil partnership, pregnancy & maternity, race, religion or belief, sex, sexual orientation. Discrimination: treating someone unfairly because of a protected characteristic - including through inaction or allowing it to happen. Harassment: unwanted behaviour that violates dignity or creates a hostile environment - including between people who know each other well. Victimisation: treating someone unfairly because they raised a concern - or because they didn't join in with behaviour that targeted someone else. Knowing the law and applying it are two different things. Scenario: a student makes the same offensive joke repeatedly in your group. Everyone laughs along. Is anyone else liable - and why?",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which of the following is the deck's definition of victimisation?",
                "options": [
                    "Treating someone better because they raised a concern",
                    "Treating someone unfairly because they raised a concern - or because they didn't join in with behaviour that targeted someone else",
                    "Any disagreement in a group",
                    "Only a formal disciplinary outcome"
                ],
                "answerIndex": 1,
                "explanation": "Victimisation: treating someone unfairly because they raised a concern - or because they didn't join in with behaviour that targeted someone else."
            }
        },
        {
            "title": "Behaviour standards - in college, on placement, online",
            "content": "In college: knowing someone well doesn't lower the standard - it raises your responsibility to them. Group dynamics that formed in Year 1 may need to be challenged in Year 2. On industry placement: returning to a familiar placement is where professional standards are most at risk - particularly in a media production company, digital agency, or creative studio. Your Year 2 behaviour shapes the reference your placement provider gives. Online: your digital footprint is now more developed - and more visible to future employers. Content from Year 1 may still be findable - now is the time to audit it. Online group dynamics within the year group should meet the same standards as in person.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Why is returning to a familiar placement a higher-risk moment, according to the deck?",
                "options": [
                    "Because the placement is shorter",
                    "Because familiarity is where professional standards are most at risk - your Year 2 behaviour shapes the reference your placement provider gives",
                    "Because the placement is unpaid",
                    "Because there is no manager"
                ],
                "answerIndex": 1,
                "explanation": "Returning to a familiar placement is where professional standards are most at risk - your Year 2 behaviour shapes the reference your placement provider gives."
            }
        },
        {
            "title": "Zero tolerance - inaction is also a choice",
            "content": "This hasn't changed. And in Year 2, allowing it to happen makes you part of it. Harassment: unwanted behaviour targeting identity, dignity, or wellbeing - including behaviour that has 'always been like this'. Discrimination: treating someone worse because of who they are - including through group dynamics that single people out. Bullying: repeated targeting - including normalised 'jokes' that only one person doesn't find funny. Abuse: physical, verbal, or emotional - including online behaviour within closed groups. Formal disciplinary procedures apply - including for students who witnessed behaviour and did nothing.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the distinctive Year 2 addition to zero tolerance, according to the deck?",
                "options": [
                    "It no longer applies",
                    "Allowing it to happen makes you part of it - disciplinary procedures can include bystanders",
                    "It only applies online",
                    "It is optional"
                ],
                "answerIndex": 1,
                "explanation": "In Year 2, allowing it to happen makes you part of it. Formal disciplinary procedures apply - including for students who witnessed behaviour and did nothing."
            }
        },
        {
            "title": "How to report a concern",
            "content": "In Year 2, reporting isn't just an option - it's part of your responsibility. Tell Your Teacher: still the fastest route. Your teacher can act immediately, make a referral, or escalate. Don't assume someone else has already reported it. Formal Reporting System: ESCG has a formal process for reporting concerns about discrimination, harassment, bullying or abuse. The formal route creates a documented record that protects everyone. Anonymous Reporting: you can report without giving your name - and it will still be investigated. In Year 2, social pressure to stay quiet is real. Anonymous reporting exists precisely for that.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck describe the anonymous reporting route?",
                "options": [
                    "It is not available to students",
                    "You can report without giving your name - and it will still be investigated",
                    "It only works for safeguarding concerns",
                    "It is slower than telling your teacher"
                ],
                "answerIndex": 1,
                "explanation": "You can report without giving your name - and it will still be investigated."
            }
        },
        {
            "title": "Your commitment - one you'll do, one you'll challenge",
            "content": "Pick one from each column. Your tutor keeps the card and may check in with you. I will... (1) Actively challenge a group dynamic I've been letting slide since Year 1. (2) Review my online presence and make sure it reflects the professional I'm becoming. (3) Find out where to report a concern and use that route if I need to. (4) If I'm worried about myself or someone else, I'll speak to my tutor or the safeguarding team. I will challenge... A) A joke or comment that's become normalised in my group but that I know isn't acceptable. B) A situation where someone is being excluded or treated badly - even if everyone else ignores it. C) Behaviour in a group chat or online space that wouldn't be acceptable face-to-face. D) The assumption that because we've been together a year, anything goes.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the structure of the commitment card for this session?",
                "options": [
                    "One single commitment",
                    "Pick one from each of two columns: 'I will...' and 'I will challenge...'",
                    "Five habits to adopt",
                    "A list of laws to memorise"
                ],
                "answerIndex": 1,
                "explanation": "Pick one from each column - 'I will...' and 'I will challenge...'. Your tutor keeps the card and may check in with you."
            }
        }
    ]
}
write("l3y2-e-learn.json", mod_e)

# ============================================================
# Module F L3 Y2: Staying Safe at College
# ============================================================
mod_f = {
    "section": "l3y2-f", "level": "l3", "year": "y2", "module": "F",
    "title": "Staying Safe at College",
    "slides": [
        {
            "title": "Why this is different in Year 2",
            "content": "Staying safe in your production year: studio, placement and online. About 1.5 hours. PROUD anchor: Encourage Unity - looking out for peers, reporting concern, not coasting. Mandatory content: Safeguarding at college / Prevent / Online safety / How ESCG keeps you safe / Safeguarding Team contacts / Reporting a concern. Different in Year 2: AI policy has tightened (Final Major Project, the Occupational Specialism Project, A Level Component 3); online risk doesn't stay the same (UCAS and UCH Hastings applications, 315-hour industry placement, first paid freelance work); complacency is the main hazard (getting casual about consent - filming or photographing people without asking, because you always have); your support routes are still there - returners use them less, they shouldn't.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which PROUD value is the anchor for this Year 2 safeguarding session?",
                "options": ["Bring Positivity", "Show Respect", "Encourage Unity", "Celebrate Diversity"],
                "answerIndex": 2,
                "explanation": "PROUD anchor: Encourage Unity - looking out for peers, reporting concern, not coasting."
            }
        },
        {
            "title": "Safeguarding in Year 2 - same duty, different pressures",
            "content": "What hasn't changed: ESCG's duty to keep you safe is the same in Year 2 as it was in Year 1. You can self-refer to the Safeguarding Team or Wellbeing Team at any time - or start with your course tutor, the studio technician, or whoever coordinates your placement. All concerns - about yourself or a peer - are taken seriously. Confidentiality limits are the same: staff will not gossip, but they cannot promise secrecy where there is a risk of harm. What changes in Year 2: new pressures (paid freelance shoots and edits alongside study, and unpaid 'exposure' work that eats your time); complacency risk (familiarity breeds inattention - the consent conversation you now skip because the subject is a mate); peer responsibility (you now know this community - you know whose work has changed tone, and who has stopped turning up to their own production slots).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is one of the three 'what changes in Year 2' for safeguarding, according to the deck?",
                "options": [
                    "Safeguarding no longer applies",
                    "New pressures - paid freelance work and unpaid 'exposure' work that eats your time; complacency around consent; peer responsibility for the community you know",
                    "You have to report yourself monthly",
                    "Tutors are no longer point of contact"
                ],
                "answerIndex": 1,
                "explanation": "The three Year 2 changes are: new pressures, complacency risk, and peer responsibility."
            }
        },
        {
            "title": "Prevent in Year 2 - what's changed since Year 1",
            "content": "Still the same: radicalisation is the process by which someone comes to support terrorism or extremism; extremism is vocal or active opposition to fundamental British values, or calls for violence. What's changed: AI-generated extremist content has increased significantly; deepfake disinformation is more sophisticated; misogynistic online communities have grown; the speed of radicalisation online has accelerated - what took months can now take weeks. Year 2 vulnerability factors: financial stress and debt (hard drives, printing and portfolio costs alongside travel to placement); relationship breakdown (isolation and identity crisis); academic pressure (FMP, 35.5-hour specialism project, 15-hour practical exam); employment instability (unvetted freelance work found through DMs, 'ambassador' schemes that ask you for money first); reduced peer support as friendship groups shift. The distinction still holds: arguing about how a film or a news story represents a group of people is legitimate analysis. Being pushed toward hating a group of people is not the same thing.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is a Year 2 vulnerability factor for Prevent, according to the deck?",
                "options": [
                    "Having too much free time",
                    "Financial stress and debt - hard drives, printing and portfolio costs alongside travel to placement",
                    "Too many friends",
                    "Working in a studio"
                ],
                "answerIndex": 1,
                "explanation": "Financial stress and debt (hard drives, printing and portfolio costs alongside travel to placement) is a Year 2 vulnerability factor."
            }
        },
        {
            "title": "Online safety in Year 2 - your work goes out to real audiences",
            "content": "Risks that don't go away: personal information (what a placement employer or a UCH Hastings admissions tutor finds when they search you, including your public portfolio); grooming and exploitation (unpaid commissions from strangers that escalate, 'agency' approaches after you post work); non-consensual images (still a criminal offence, AI-generated images explicitly covered in law, portrait and practical footage shared beyond the studio, rushes left on shared drives). What has shifted in Year 2: financial scams have evolved (fake job offers target people with short work histories - exactly where Year 2 students are: fake remote editing gigs, 'content moderator' roles, kit-for-review deals); AI and your professional identity (AI-generated content posted as your own is reputation risk as well as academic risk - placement employers, commissioners and UCH Hastings admissions tutors are the people searching). The college uses Smoothwall for filtering and monitoring. Students' use of college systems is monitored.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck say AI-generated content posted as your own affects you in Year 2?",
                "options": [
                    "It's reputation risk as well as academic risk - placement employers, commissioners and admissions tutors are the people searching",
                    "It's only an academic risk",
                    "It's not a risk at all",
                    "It's only an issue for final-year projects"
                ],
                "answerIndex": 0,
                "explanation": "AI-generated content posted as your own is reputation risk as well as academic risk - placement employers, commissioners and UCH Hastings admissions tutors are the people searching."
            }
        },
        {
            "title": "AI and your data - the Year 2 update",
            "content": "JCQ regulations + ESCG data safety policy - tighter scrutiny this year. AI detection is more sophisticated in Year 2. Awarding bodies are actively developing detection methods, and disqualifications are increasing. Your awarding bodies here are UAL, Pearson, EDUQAS and the Institute for Apprenticeships and Technical Education - the rules differ between them. Do not: submit work for assessment that is not demonstrably your own (even partial AI use counts); copy, paraphrase, or reproduce AI content without acknowledgement (malpractice under JCQ); enter personal data, college information, or third-party details into public AI tools. Do: declare AI use precisely (name the tool, give the date, keep a screenshot, include it with the submission - incomplete acknowledgement is itself malpractice); build your own argument (AI gathering references is fine; the FMP rationale, the evaluation and the analysis have to be yours); ask before you use (rules differ by assessment - FMP and Occupational Specialism Project are externally moderated; A Level Component 3 has its own declaration).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which awarding body is NOT listed in the deck for this department?",
                "options": ["UAL", "Pearson", "EDUQAS", "Cambridge Assessment"],
                "answerIndex": 3,
                "explanation": "The awarding bodies listed are UAL, Pearson, EDUQAS and the Institute for Apprenticeships and Technical Education. Cambridge Assessment is not listed."
            }
        },
        {
            "title": "How ESCG keeps you safe - the process",
            "content": "Four steps. (1) Something is raised - student discloses, teacher notices, anonymous report; here it is often the studio technician who has seen this group for two years. (2) Right person told same-day - staff do not investigate themselves; Safeguarding Manager informed; logged on ProMonitor. (3) Concern assessed - Safeguarding Team decides the right response (wellbeing support through to external referral). (4) Confidentiality - same limits: staff will not share unnecessarily, but if there is a risk of harm they have a duty to act - and they will tell you what they are doing and why. The same limit applies in media work: a source's confidence does not cover a risk of harm.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the second step in 'How ESCG keeps you safe'?",
                "options": [
                    "Concern is investigated by the student",
                    "Right person told same-day - staff do not investigate themselves; Safeguarding Manager informed; logged on ProMonitor",
                    "The concern is posted on Pro Portal",
                    "Students are sent home"
                ],
                "answerIndex": 1,
                "explanation": "Right person told same-day - staff do not investigate themselves. Safeguarding Manager informed. All logged on ProMonitor."
            }
        },
        {
            "title": "The Safeguarding Team - and the Year 2 paradox",
            "content": "DSL: Rebecca Conroy (Principal & CEO). Deputy DSL: Fenella Potterton (Assistant Principal Student Experience). Safeguarding Manager - Hastings: Lydia Leonard - 07848 442081 - lydia.leonard@escg.ac.uk (same number as Year 1 - still on your lanyard). Eastbourne: Helen Ding 07980 049312. Lewes/Newhaven: Julia Proven 07823 668772. Prevent single point of contact (college): Julia Proven at Lewes/Newhaven. 24-hour support: escg.ac.uk/support/safeguarding. The Year 2 paradox: the year people most need support is the year they stop going. The door works exactly like it did last year. Year 2 students use the Wellbeing Team less - they shouldn't.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Who is the Safeguarding Manager for Hastings, according to the deck?",
                "options": ["Rebecca Conroy", "Fenella Potterton", "Lydia Leonard - 07848 442081", "Belle Howard"],
                "answerIndex": 2,
                "explanation": "Safeguarding Manager - Hastings: Lydia Leonard - 07848 442081."
            }
        },
        {
            "title": "Reporting a concern - about yourself or someone else",
            "content": "If you are worried about yourself: any member of staff you trust - same as Year 1; Lydia Leonard directly (Hastings) - 07848 442081; the Wellbeing Team - self-refer, no appointment needed; anonymously via escg.ac.uk/support/safeguarding. If you are worried about someone else: you know your peers better in Year 2. That knowledge is an asset - work that changes tone sharply, or someone who has stopped turning up to their own production slots. A concern is enough. You do not need proof. Anonymous reporting is available. The concern will still be acted on. Telling someone about a peer in trouble is not disloyalty - it is the right call - the same as stopping an unsafe shoot. Year 2 students are less likely to report concerns. Not because they have fewer problems - because they feel they should manage independently. The expectation that you should handle everything yourself is wrong.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, why do Year 2 students tend to under-report concerns?",
                "options": [
                    "Because they have no concerns",
                    "Because they feel they should manage independently - the expectation that you should handle everything yourself is wrong",
                    "Because the safeguarding team is closed",
                    "Because reporting is now banned"
                ],
                "answerIndex": 1,
                "explanation": "Year 2 students are less likely to report concerns - because they feel they should manage independently. The expectation that you should handle everything yourself is wrong."
            }
        },
        {
            "title": "One thing - before you leave",
            "content": "Choose one. Write it. Your teacher keeps the card. Options: (1) Check that I have the Safeguarding Team contact saved - and actually use it if something comes up this year. (2) Go back to asking for consent properly before I film or photograph anyone - including mates. (3) Check exactly what the AI rules are for my FMP, my specialism project or Component 3 - before I use AI in any of them. (4) Tell someone about something I have been managing on my own - that I probably should have raised earlier.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which option on the Year 2 commitment card is the safeguarding disclosure route?",
                "options": [
                    "Option 1 - check the contact is saved",
                    "Option 4 - tell someone about something I have been managing on my own that I probably should have raised earlier",
                    "Option 2 - go back to asking for consent",
                    "Option 3 - check the AI rules"
                ],
                "answerIndex": 1,
                "explanation": "Option 4 is the Year 2 equivalent of the disclosure route - it directly addresses the under-reporting pattern named in the session."
            }
        }
    ]
}
write("l3y2-f-learn.json", mod_f)

# ============================================================
# Module G L3 Y2: Looking After Myself
# ============================================================
mod_g = {
    "section": "l3y2-g", "level": "l3", "year": "y2", "module": "G",
    "title": "Looking After Myself",
    "slides": [
        {
            "title": "Why this session now",
            "content": "Year 2 Digital Media, Film and Computing asks more of you. Same tools, same doors - higher stakes. About 90 minutes. Group 2: Safeguarding, Wellbeing & Respect. Today isn't a lecture about eating vegetables. It's ninety minutes on the things that actually decide whether this year goes well - sleep, stress, money, and knowing where the doors are when something's getting in the way. Some of it you'll already know. Some of it you'll be glad you heard now rather than in January.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the framing of this Year 2 wellbeing session, according to the deck?",
                "options": [
                    "It's a lecture about eating vegetables",
                    "It's ninety minutes on the things that actually decide whether this year goes well - sleep, stress, money, and knowing where the doors are",
                    "It's a new-starter welcome",
                    "It's a placement briefing"
                ],
                "answerIndex": 1,
                "explanation": "It's ninety minutes on the things that actually decide whether this year goes well - sleep, stress, money, and knowing where the doors are."
            }
        },
        {
            "title": "Three weeks in - the settled check-in",
            "content": "In pairs or threes. The real answer, not the polite one. What's easier this year? You know the building, the people, the drill. What's heavier this year? Workload, expectations, placements - the fact that everything counts now. The Final Major Project or Employer Set Project building alongside ongoing unit deadlines. Industry placements requiring professional-standard work at the same time as coursework submissions. What did last year teach you about you? How you handle pressure, what your warning signs are, what helped. Nothing said here gets graded - this is a check-in, not an assessment.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "According to the deck, what is one thing that is 'heavier' in Year 2?",
                "options": [
                    "Uniform requirements",
                    "Workload, expectations, placements - the fact that everything counts now. FMP or ESP building alongside ongoing unit deadlines, and industry placements requiring professional-standard work at the same time as coursework submissions",
                    "Travelling to college",
                    "Fewer deadlines"
                ],
                "answerIndex": 1,
                "explanation": "Workload, expectations, placements - the fact that everything counts now. FMP or ESP building alongside ongoing unit deadlines."
            }
        },
        {
            "title": "Mental health is health",
            "content": "Everyone is somewhere on this line - and everyone moves along it. Thriving / Coping / Struggling / In crisis. You watched this line move last year - both ways. Year 2 is when workload peaks: the Final Major Project or Employer Set Project, the portfolio deadline, and the industry placement log - often arriving in the same window. Plan for it now. What moves it - in both directions: sleep, money, people, workload, home life, movement. At ESCG, mental health is a normal topic of conversation. Saying 'I'm struggling' is information, not weakness - and we can only work with what we know.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck describe the line between mental health states?",
                "options": [
                    "Fixed for life",
                    "Everyone is somewhere on this line and everyone moves along it - in both directions",
                    "Only people with diagnosed conditions are on it",
                    "It is a private matter, never to be discussed"
                ],
                "answerIndex": 1,
                "explanation": "Everyone is somewhere on this line and everyone moves along it - in both directions."
            }
        },
        {
            "title": "Stress - what it looks like, what works",
            "content": "What it looks like: can't switch off - or can't get started; sleep shifts - too little, or hiding in it; short fuse with people you actually like; avoiding the exact thing causing it - not opening the Final Major Project document because the scale of it is paralysing, or skipping a production session because Year 2 feels like exactly the wrong time to admit a technical gap. Common Year 2 triggers: final-year workload, placements, everything counting towards the grade, paid work, money, home. What the evidence says actually works: Move (regular physical activity - a walk counts); Connect (time with people, in person); Sleep (it's the next slide); Talk (naming it to someone halves its size - every time). None of this is a personality upgrade. It's maintenance - the same as eating and washing. Stress in small doses is normal and useful. It's when it stops switching off that it costs you.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which is one of the four 'what actually works' moves the deck recommends for stress?",
                "options": [
                    "Move - regular physical activity, a walk counts",
                    "Buy more equipment",
                    "Hide from the problem",
                    "Work through the night"
                ],
                "answerIndex": 0,
                "explanation": "Move - regular physical activity, a walk counts - is one of the four highest-return moves."
            }
        },
        {
            "title": "Sleep - the study tool most students ignore",
            "content": "Memory is built while you sleep. Revision without sleep is pouring water into a cracked jug - the consolidation never happens. The Final Major Project direction decided at midnight looks completely different in the morning. Concentration and focus are the first things to go. A tired brain reads the FMP brief and can't connect the work it requires. Everything feels worse tired. What's in your control: anchor your wake time (same time every day - including one weekend day); screens down, or out of reach (charge the phone across the room); nothing caffeinated after mid-afternoon (energy drinks included - caffeine hangs around for hours). Sleep hygiene - the routines and conditions that make good sleep likely. Real lives are messy - shared rooms, evening shifts, caring for someone. Control what you can. And if life makes sleep genuinely impossible, tell your tutor - it changes how we support you.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the 'sleep hygiene' definition the deck gives?",
                "options": [
                    "Washing your face before bed",
                    "The routines and conditions that make good sleep likely",
                    "Going to bed early every night",
                    "Taking sleeping pills"
                ],
                "answerIndex": 1,
                "explanation": "Sleep hygiene - the routines and conditions that make good sleep likely. That's all the term means."
            }
        },
        {
            "title": "Money pressure is a wellbeing issue",
            "content": "Financial stress and mental health are directly linked. Worry about money makes everything else on today's list harder - sleep, concentration, mood, showing up. It's also one of the most common pressures students carry silently, because it feels embarrassing. It shouldn't. It's circumstance, not character. The Hardship Fund: emergency financial support for students - travel, food, equipment, sudden changes at home. Asking is confidential, and far more common than you'd think. Money worries are a reason to talk to us - not a reason to disappear.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "How does the deck frame financial stress?",
                "options": [
                    "It's a personal failing",
                    "It's circumstance, not character - and it makes everything else on the list harder (sleep, concentration, mood, showing up)",
                    "It's the easiest problem to fix alone",
                    "It's not a college matter"
                ],
                "answerIndex": 1,
                "explanation": "It's circumstance, not character. Worry about money makes everything else on today's list harder."
            }
        },
        {
            "title": "Support - the Year 2 paradox",
            "content": "The Year 2 paradox: the year people most need support is the year they stop going. The door works exactly like it did last year. Needing support on the Final Major Project or the Employer Set Project is not a sign you shouldn't be here - every professional creative has mentors, directors, peer reviewers and editors. Using support in Year 2 is exactly what the industry does. Three steps, no drama: (1) Say something - to your tutor, a teacher you trust, or straight to the Wellbeing Team. Any door works. (2) Referral - quick and straightforward, and you stay in the loop the whole way. (3) Support arranged - matched to what you actually need. Tell us what we need to know: a disability, a mental health condition, a learning need - or anything that changed over the summer. Year 2 support builds on what we already know. Telling us now, not in March, means exam access and adjustments are in place when the pressure actually arrives.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the 'Year 2 paradox' the deck names?",
                "options": [
                    "The year people most need support is the year they stop going",
                    "Year 2 has no support",
                    "Tutors forget Year 2 students",
                    "Year 2 students are better off without support"
                ],
                "answerIndex": 0,
                "explanation": "The year people most need support is the year they stop going. The door works exactly like it did last year."
            }
        },
        {
            "title": "Look out for each other - Encourage Unity in practice",
            "content": "Notice: you've known each other a year - you'll notice first. Going quiet, dropping things, missed sessions. The person whose Final Major Project has stalled but who keeps saying it's fine. The one who stops turning up to production sessions and submits work that shows the gap. The one who has gone quiet about where they're heading after this year. Ask: 'You alright? Actually alright?' Then listen to the answer. Tell someone: a tutor or the Wellbeing Team. That's not breaking trust - it's getting help you can't give alone. If a friend tells you something serious and asks you to keep it secret: you can be loyal and still tell someone. Those aren't opposites. KEEP THESE: Samaritans 116 123 (free, 24/7, any problem, any size); MIND 0300 123 3393 / mind.org.uk; iRock (drop-in support for young people in East Sussex); TogetherAll (free, anonymous online support community); local crisis line (campus-specific).",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "Which three-step sequence does the deck recommend for looking out for each other?",
                "options": [
                    "Notice, Ask, Tell someone",
                    "Watch, Wait, Walk away",
                    "Post, Tag, Share",
                    "Listen, Judge, Decide"
                ],
                "answerIndex": 0,
                "explanation": "Notice, Ask, Tell someone - that is the Encourage Unity in practice sequence."
            }
        },
        {
            "title": "One thing - your commitment for the week",
            "content": "Write one specific thing you'll try this week. Not three. One. (1) Sleep - I'll anchor my wake time, same time every day, including one weekend day. (2) Pressure valve - I'll put one deliberate thing in my week that isn't work - movement, mates, or proper downtime. (3) Contacts - I'll re-save the support numbers and remind myself where the Wellbeing Team's door is. (4) Talk - I'll tell my tutor or the Wellbeing Team about something that's getting in the way. Your tutor keeps these and will check in on them. Choosing option 4 means someone follows up with you this week - quietly, and properly.",
            "example": "", "exampleOutput": "",
            "exercise": {
                "type": "scored",
                "prompt": "What is the special follow-up attached to option 4 of the commitment card?",
                "options": [
                    "Nothing - it's a private choice",
                    "Someone follows up with you this week - quietly, and properly",
                    "You're removed from class",
                    "Your parents are contacted"
                ],
                "answerIndex": 1,
                "explanation": "Choosing option 4 means someone follows up with you this week - quietly, and properly."
            }
        }
    ]
}
write("l3y2-g-learn.json", mod_g)

print("Wrote E, F, G")
