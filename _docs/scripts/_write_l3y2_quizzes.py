#!/usr/bin/env python3
"""Generate quizzes A/B/C for all 11 L3 Y2 modules.

For each module: 8 base questions. Variant A keeps the order.
Variants B and C reorder the questions and shuffle the option order
where possible (using shuffled_index arrays).
"""
import json, random
from pathlib import Path

OUT = Path("data")
random.seed(42)

def write(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Reusable quiz-question types:
#   "scored"   {prompt, options, answerIndex, explanation}
#   "multi"    {prompt, options, correctIndices, explanation}
#   "insert"   {prompt, template, options, answerIndex, explanation}
#   "dragorder"{prompt, items, solution, explanation}

# Helper: shuffle option order, return new options + new answerIndex/correctIndices/solution
def shuffle_opts(q, rng):
    if q["type"] == "scored" or q["type"] == "insert":
        idxs = list(range(len(q["options"])))
        rng.shuffle(idxs)
        new_opts = [q["options"][i] for i in idxs]
        new_ans = idxs.index(q["answerIndex"])
        return {**q, "options": new_opts, "answerIndex": new_ans}
    if q["type"] == "multi":
        idxs = list(range(len(q["options"])))
        rng.shuffle(idxs)
        new_opts = [q["options"][i] for i in idxs]
        new_correct = [idxs.index(c) for c in q["correctIndices"]]
        return {**q, "options": new_opts, "correctIndices": new_correct}
    if q["type"] == "dragorder":
        # dragorder is a list reorder, not options; keep as-is
        return q
    return q

def gen(module_id, title, base_questions):
    """Produce three quiz files: A (base), B and C (reordered + option-shuffled)."""
    rng_a = random.Random(hash(module_id) & 0xffffffff)
    rng_b = random.Random((hash(module_id) ^ 0xB) & 0xffffffff)
    rng_c = random.Random((hash(module_id) ^ 0xC) & 0xffffffff)

    def build(variant, qs, rng):
        out_qs = []
        for i, q in enumerate(qs, start=1):
            qq = shuffle_opts(q, rng)
            qq["id"] = f"{module_id}-{variant}{i:02d}"
            out_qs.append(qq)
        return out_qs

    # Variant A: base order, light shuffle of options
    qs_a = build("A", base_questions, rng_a)
    # Variant B: reverse order, then shuffle
    qs_b = list(reversed(base_questions))
    qs_b = build("B", qs_b, rng_b)
    # Variant C: rotate by 3 and shuffle
    n = len(base_questions)
    qs_c = base_questions[3:] + base_questions[:3]
    qs_c = build("C", qs_c, rng_c)

    write(f"{module_id}-quiz-A.json",
          {"meta": {"section": module_id, "level": "l3", "year": "y2", "module": module_id.split("-")[-1].upper(), "variant": "A", "title": title},
           "questions": qs_a})
    write(f"{module_id}-quiz-B.json",
          {"meta": {"section": module_id, "level": "l3", "year": "y2", "module": module_id.split("-")[-1].upper(), "variant": "B", "title": title},
           "questions": qs_b})
    write(f"{module_id}-quiz-C.json",
          {"meta": {"section": module_id, "level": "l3", "year": "y2", "module": module_id.split("-")[-1].upper(), "variant": "C", "title": title},
           "questions": qs_c})
    print("generated", module_id, "x3")

# ============================================================
# Module A L3 Y2 questions
# ============================================================
qA = [
    {"type":"scored","prompt":"What is the framing of this Year 2 welcome session, according to the deck?",
     "options":["A repeat of last September's induction","A re-focus on where you're headed and what Year 2 demands","A pass-or-fail assessment of last year's work","A lecture on study skills"],
     "answerIndex":1,
     "explanation":"The deck frames this as a re-focus, not a re-run."},
    {"type":"dragorder","prompt":"Put the five beats of this welcome-back session in the order the deck presents them.",
     "items":["Where you're headed","What Year 2 demands","Staying on course","Support that still matters","Landing it"],
     "solution":[0,1,2,3,4],
     "explanation":"The five beats in order: Where you're headed, What Year 2 demands, Staying on course, Support that still matters, Landing it."},
    {"type":"scored","prompt":"Which is one of the three honest asks Year 2 makes?",
     "options":["Get a part-time job immediately","Grades carry weight - this year's results are the ones employers and universities actually see","Attend every social event","Pick a specialism in week one"],
     "answerIndex":1,
     "explanation":"Grades carry weight - this year's results are the ones employers, training providers and universities actually see."},
    {"type":"scored","prompt":"What is the usual cause of Year 2 students falling short, according to the deck?",
     "options":["Lack of intelligence","Drift - missed deadlines, skipped days, applications left too late","Bad teaching","Bad luck"],
     "answerIndex":1,
     "explanation":"They drifted. A missed deadline here, a few skipped days there, the application left too late."},
    {"type":"multi","prompt":"Which are the three routes out of Year 2? Select all that apply.",
     "options":["Into work","Apprenticeship","University / HE","Drop out and try again later"],
     "correctIndices":[0,1,2],
     "explanation":"Into work, apprenticeship, and university / HE are the three routes out."},
    {"type":"scored","prompt":"How often should you check Pro Portal?",
     "options":["Once a week","Every morning, no excuses","Only when something looks wrong","Once a term"],
     "answerIndex":1,
     "explanation":"Check Pro Portal every morning, no excuses."},
    {"type":"scored","prompt":"Which door covers UCAS and apprenticeship applications?",
     "options":["Wellbeing","Money & practical","Careers & progression","Academic support"],
     "answerIndex":2,
     "explanation":"Careers & progression covers real help with applications, interviews, UCAS and apprenticeships."},
    {"type":"scored","prompt":"What is the 'CV test' for enrichment and projects?",
     "options":["Only do things that look good on paper","Ask 'Will this give me something real to say in an interview or on an application?' - if yes, do it","Skip anything that doesn't pay","Do everything on offer"],
     "answerIndex":1,
     "explanation":"The CV test: 'Will this give me something real to say in an interview or on an application?' If yes - do it."},
]
gen("l3y2-a", "Welcome Back - This Is the Year That Counts", qA)

# ============================================================
# Module B
# ============================================================
qB = [
    {"type":"scored","prompt":"Which PROUD value does Module B anchor on?",
     "options":["Bring Positivity","Show Respect","Seek Opportunity","Encourage Unity"],
     "answerIndex":2,
     "explanation":"The PROUD value anchor is Seek Opportunity."},
    {"type":"dragorder","prompt":"Put the six beats of this Year 2 confidence session in order.",
     "items":["What shifts in Year 2","Time and the final fuse","Seek Opportunity","Confidence","Attendance","Your habit"],
     "solution":[0,1,2,3,4,5],
     "explanation":"Six beats: What shifts, Final fuse, Seek Opportunity, Confidence, Attendance, Your habit."},
    {"type":"scored","prompt":"What happens to gaps from Year 1 in Year 2?",
     "options":["They disappear over the summer","They compound - what you didn't consolidate in Year 1 is what you hand in for final assessment","They're forgiven by staff","They get covered in a refresher week"],
     "answerIndex":1,
     "explanation":"Gaps from Year 1 don't disappear - they compound."},
    {"type":"scored","prompt":"When does a missed brief actually hurt you, according to the deck?",
     "options":["The week you miss it","At the portfolio deadline, when you're catching up and trying to produce new work simultaneously","Only at the end of Year 2","Never, if you explain it"],
     "answerIndex":1,
     "explanation":"It hurts you at the portfolio deadline, when you're catching up and trying to produce new work simultaneously."},
    {"type":"multi","prompt":"Which are the three 'Seek Opportunity' Year 2 moves? Select all that apply.",
     "options":["Make progression concrete this year - it's active now, not pending","Build something to talk about - applications need things to have actually happened","Treat Year 2 setbacks as information - course-correct now, not in June","Wait for someone to offer you a placement"],
     "correctIndices":[0,1,2],
     "explanation":"Make progression concrete, build something to talk about, treat setbacks as information."},
    {"type":"scored","prompt":"What is 'the wall trap' in Year 2?",
     "options":["Hitting a literal wall in a shoot","Year 2 pressure is real and you don't want to admit you're struggling, so you don't ask","The college's server goes down during deadline week","You forget your login for Pro Portal"],
     "answerIndex":1,
     "explanation":"The wall trap: pressure is real and you don't want to admit you're struggling, so you don't ask."},
    {"type":"scored","prompt":"How do staff writing references remember attendance, according to the deck?",
     "options":["They use a database; it's all automatic","They remember who showed up in Year 2, not just Year 1","They use the same letter for everyone","They only ask for Year 1 attendance"],
     "answerIndex":1,
     "explanation":"References are written from memory - staff remember who showed up in Year 2, not just Year 1."},
    {"type":"scored","prompt":"Why does the deck ask for one habit, not five?",
     "options":["Five is too many words for a card","Habits change behaviour; five at once is a plan - which means none of them happen","The teacher can only mark one answer","Five cards cost more to print"],
     "answerIndex":1,
     "explanation":"Habits change behaviour. Plans don't. Five at once is a plan - which means none of them happen."},
]
gen("l3y2-b", "Confidence, Independence & the Last Lap", qB)

# ============================================================
# Module C
# ============================================================
qC = [
    {"type":"scored","prompt":"How does the Year 2 H&S session differ from Year 1's?",
     "options":["It covers completely new content","It's a brisk refresher with a couple of genuinely new bits - familiarity is the risk now","It removes the safeguarding element","It runs twice as long"],
     "answerIndex":1,
     "explanation":"It's a brisk refresher with a couple of genuinely new bits - familiarity is the risk now."},
    {"type":"scored","prompt":"Why do habits like skipping sandbags stop registering in year two?",
     "options":["Because you've become careless","Because you've become familiar - not careless. That's the trap","Because the equipment has changed","Because there's no time"],
     "answerIndex":1,
     "explanation":"These stop registering not because you've become careless, but because you've become familiar."},
    {"type":"multi","prompt":"Which are 'what slips' examples in year two? Select all that apply.",
     "options":["Lanyards worn 'most of the time'","Skipping the risk assessment for a familiar location because 'we've been there before'","Things you'd have flagged in week one but stopped noticing","Wearing the wrong colour lanyard"],
     "correctIndices":[0,1,2],
     "explanation":"Lanyards worn 'most of the time', skipping risk assessments for familiar locations, and things you'd have flagged in week one but stopped noticing are the year-two slips."},
    {"type":"scored","prompt":"If a session this year is in a different studio or building from last year, what should you do?",
     "options":["Assume the evacuation route is the same","Treat it as new information - do not assume it is unchanged","Wait until an alarm to find out","Skip the briefing"],
     "answerIndex":1,
     "explanation":"If your sessions this year use a different studio or building from last year, treat this as new information."},
    {"type":"scored","prompt":"How has the 'show respect' excuse changed in Year 2?",
     "options":["The standard has dropped","A year in, 'I didn't realise' carries less weight than it did in week one","There is now an excuse for everything","Show respect no longer applies"],
     "answerIndex":1,
     "explanation":"A year in, 'I didn't realise' carries less weight than it did in week one."},
    {"type":"scored","prompt":"What do Content Creation students now do that they didn't in Year 1?",
     "options":["Run live media (Eastbourne Youth Radio, Tag magazine) - with contributor consent and editorial duty of care","Skip H&S briefings","Stop using consent forms","Move to a different building"],
     "answerIndex":0,
     "explanation":"Content Creation students are now running live media - broadcasting and publishing carry different H&S obligations."},
    {"type":"scored","prompt":"If you are the last person using a piece of equipment, who is responsible for returning it?",
     "options":["Whoever signed it out first that day","You - regardless of who signed it out","The technician only","Nobody - it can wait"],
     "answerIndex":1,
     "explanation":"If you are the last person using something, you are responsible for returning it, regardless of who signed it out."},
    {"type":"scored","prompt":"Beyond physical hazards, what else counts as 'something's not right' to tell someone about?",
     "options":["Only a fire","Anything - a space, an activity, or the way someone's behaving towards you or someone else - that's made you feel uncomfortable or unsafe","Only damage to college property","Only safeguarding team instructions"],
     "answerIndex":1,
     "explanation":"If a space, an activity, or the way someone's behaving towards you or someone else has made you feel uncomfortable or unsafe, that counts too."},
]
gen("l3y2-c", "Health & Safety - A Year In, Not Starting Again", qC)

# ============================================================
# Module D
# ============================================================
qD = [
    {"type":"scored","prompt":"How many reps does this group elect today?",
     "options":["One - the subject rep","Two - a subject rep and a GCSE English/maths rep","Three - subject, English, and maths","None - they're elected next term"],
     "answerIndex":1,
     "explanation":"This group elects two reps - subject rep and GCSE English/maths rep."},
    {"type":"dragorder","prompt":"Put the eight beats of this session in order.",
     "items":["Check in","Students' Voice","Ways to get involved","The Rep role","The Governor role","Encourage Unity (PROUD)","Election","Close"],
     "solution":[0,1,2,3,4,5,6,7],
     "explanation":"Check in -> Students' Voice -> Ways to get involved -> Rep role -> Governor role -> Encourage Unity -> Election -> Close."},
    {"type":"scored","prompt":"Which is feedback that 'names the thing'?",
     "options":["'Feedback is bad'","'Coursework feedback arrives too late to act on'","'Things aren't great'","'It's all a bit rubbish'"],
     "answerIndex":1,
     "explanation":"'Coursework feedback arrives too late to act on' beats 'feedback is bad' - that's feedback that names the thing."},
    {"type":"multi","prompt":"Which of these are 'ways to get involved'? Select all that apply.",
     "options":["Student Rep","Student Governor","NUS Membership (TOTUM card)","Surveys & Forums"],
     "correctIndices":[0,1,2,3],
     "explanation":"All four are ways to get involved."},
    {"type":"scored","prompt":"How many Student Council meetings per year does a rep attend?",
     "options":["1","3","6","12"],
     "answerIndex":1,
     "explanation":"Reps attend 3 Student Council meetings per year."},
    {"type":"scored","prompt":"What is the eligibility requirement to apply for Student Governor?",
     "options":["Any current student, in any year","Planning to study at ESCG for at least one more year - L3 students progressing here qualify","Only Year 1 students","Only students with a UCAS offer"],
     "answerIndex":1,
     "explanation":"Planning to study at ESCG for at least one more year - L3 students progressing here qualify."},
    {"type":"insert","prompt":"Fill in the blank: Student Governor applications close at midday on Friday ____ October.",
     "template":"Student Governor applications close at midday on Friday ____ October.",
     "options":["9th","16th","23rd","30th"],
     "answerIndex":1,
     "explanation":"Applications close at midday, Friday 16 October."},
    {"type":"scored","prompt":"By when must Student Rep elections be completed?",
     "options":["End of Week 1","No later than the end of Week 2 of the academic year","End of term","Whenever the rep finds time"],
     "answerIndex":1,
     "explanation":"Student Rep elections must be completed and the rep confirmed no later than the end of Week 2."},
]
gen("l3y2-d", "Students' Voice & Student Rep Elections", qD)

# ============================================================
# Module E
# ============================================================
qE = [
    {"type":"scored","prompt":"What is the Year 2 framing for this respect and values session?",
     "options":["Re-teach all of Year 1's content","Year 2 means setting the standard for others - peer-level, direct, application not awareness","Skip the values work","Cover new laws only"],
     "answerIndex":1,
     "explanation":"Year 2 means setting the standard for others. The register is peer-level and direct."},
    {"type":"dragorder","prompt":"Put the six beats of this Year 2 values session in order.",
     "items":["PROUD Values","British Values","Equality Act 2010","Behaviour Standards","Zero Tolerance","How to Report"],
     "solution":[0,1,2,3,4,5],
     "explanation":"PROUD -> British Values -> Equality Act -> Behaviour Standards -> Zero Tolerance -> How to Report."},
    {"type":"scored","prompt":"What does 'Seek Opportunity' mean in Year 2?",
     "options":["Look after yourself only","Opportunity includes developing others - not just yourself","Wait for opportunities to come to you","Skip placements to focus on coursework"],
     "answerIndex":1,
     "explanation":"In Year 2, opportunity includes developing others - not just yourself."},
    {"type":"scored","prompt":"How does the deck describe the 'Rule of Law' beat in Year 2?",
     "options":["You learn the rules for the first time","You understand the rules - the question is whether you're upholding them and challenging it when others don't","The rules don't apply on placement","It only covers online behaviour"],
     "answerIndex":1,
     "explanation":"You understand the rules - the question is whether you're upholding them and challenging it when others don't."},
    {"type":"scored","prompt":"Which is the deck's definition of victimisation under the Equality Act?",
     "options":["Treating someone better because they raised a concern","Treating someone unfairly because they raised a concern - or because they didn't join in with behaviour that targeted someone else","Any disagreement in a group","Only a formal disciplinary outcome"],
     "answerIndex":1,
     "explanation":"Victimisation: treating someone unfairly because they raised a concern - or because they didn't join in with behaviour that targeted someone else."},
    {"type":"scored","prompt":"Why is returning to a familiar placement a higher-risk moment?",
     "options":["Because the placement is shorter","Because familiarity is where professional standards are most at risk - your Year 2 behaviour shapes the reference your placement provider gives","Because the placement is unpaid","Because there is no manager"],
     "answerIndex":1,
     "explanation":"Returning to a familiar placement is where professional standards are most at risk - your Year 2 behaviour shapes the reference."},
    {"type":"scored","prompt":"What is the distinctive Year 2 addition to zero tolerance?",
     "options":["It no longer applies","Allowing it to happen makes you part of it - disciplinary procedures can include bystanders","It only applies online","It is optional"],
     "answerIndex":1,
     "explanation":"In Year 2, allowing it to happen makes you part of it. Formal disciplinary procedures apply - including for students who witnessed behaviour and did nothing."},
    {"type":"scored","prompt":"How does the deck describe the anonymous reporting route?",
     "options":["It is not available to students","You can report without giving your name - and it will still be investigated","It only works for safeguarding concerns","It is slower than telling your teacher"],
     "answerIndex":1,
     "explanation":"You can report without giving your name - and it will still be investigated."},
]
gen("l3y2-e", "Respect, Relationships & College Values", qE)

# ============================================================
# Module F
# ============================================================
qF = [
    {"type":"scored","prompt":"Which PROUD value is the anchor for this Year 2 safeguarding session?",
     "options":["Bring Positivity","Show Respect","Encourage Unity","Celebrate Diversity"],
     "answerIndex":2,
     "explanation":"PROUD anchor: Encourage Unity - looking out for peers, reporting concern, not coasting."},
    {"type":"scored","prompt":"Which is one of the three 'what changes in Year 2' for safeguarding?",
     "options":["Safeguarding no longer applies","New pressures, complacency risk, peer responsibility","You have to report yourself monthly","Tutors are no longer point of contact"],
     "answerIndex":1,
     "explanation":"The three Year 2 changes are: new pressures, complacency risk, and peer responsibility."},
    {"type":"scored","prompt":"Which is a Year 2 vulnerability factor for Prevent?",
     "options":["Having too much free time","Financial stress and debt - hard drives, printing and portfolio costs alongside travel to placement","Too many friends","Working in a studio"],
     "answerIndex":1,
     "explanation":"Financial stress and debt is a Year 2 vulnerability factor."},
    {"type":"scored","prompt":"How does the deck say AI-generated content posted as your own affects you in Year 2?",
     "options":["It's reputation risk as well as academic risk - placement employers, commissioners and admissions tutors are the people searching","It's only an academic risk","It's not a risk at all","It's only an issue for final-year projects"],
     "answerIndex":0,
     "explanation":"AI-generated content posted as your own is reputation risk as well as academic risk."},
    {"type":"scored","prompt":"Which awarding body is NOT listed in the deck for this department?",
     "options":["UAL","Pearson","EDUQAS","Cambridge Assessment"],
     "answerIndex":3,
     "explanation":"The awarding bodies listed are UAL, Pearson, EDUQAS and the Institute for Apprenticeships and Technical Education."},
    {"type":"scored","prompt":"What is the second step in 'How ESCG keeps you safe'?",
     "options":["Concern is investigated by the student","Right person told same-day - staff do not investigate themselves; Safeguarding Manager informed; logged on ProMonitor","The concern is posted on Pro Portal","Students are sent home"],
     "answerIndex":1,
     "explanation":"Right person told same-day - staff do not investigate themselves. Safeguarding Manager informed. All logged on ProMonitor."},
    {"type":"scored","prompt":"Who is the Safeguarding Manager for Hastings?",
     "options":["Rebecca Conroy","Fenella Potterton","Lydia Leonard - 07848 442081","Belle Howard"],
     "answerIndex":2,
     "explanation":"Safeguarding Manager - Hastings: Lydia Leonard - 07848 442081."},
    {"type":"scored","prompt":"Why do Year 2 students tend to under-report concerns, according to the deck?",
     "options":["Because they have no concerns","Because they feel they should manage independently - the expectation that you should handle everything yourself is wrong","Because the safeguarding team is closed","Because reporting is now banned"],
     "answerIndex":1,
     "explanation":"Year 2 students are less likely to report concerns - because they feel they should manage independently. The expectation that you should handle everything yourself is wrong."},
]
gen("l3y2-f", "Staying Safe at College", qF)

# ============================================================
# Module G
# ============================================================
qG = [
    {"type":"scored","prompt":"What is the framing of this Year 2 wellbeing session?",
     "options":["It's a lecture about eating vegetables","It's ninety minutes on the things that actually decide whether this year goes well - sleep, stress, money, and knowing where the doors are","It's a new-starter welcome","It's a placement briefing"],
     "answerIndex":1,
     "explanation":"It's ninety minutes on the things that actually decide whether this year goes well - sleep, stress, money, and knowing where the doors are."},
    {"type":"scored","prompt":"What is one thing that is 'heavier' in Year 2?",
     "options":["Uniform requirements","Workload, expectations, placements - the fact that everything counts now. FMP or ESP building alongside ongoing unit deadlines","Travelling to college","Fewer deadlines"],
     "answerIndex":1,
     "explanation":"Workload, expectations, placements - the fact that everything counts now."},
    {"type":"scored","prompt":"How does the deck describe the line between mental health states?",
     "options":["Fixed for life","Everyone is somewhere on this line and everyone moves along it - in both directions","Only people with diagnosed conditions are on it","It is a private matter, never to be discussed"],
     "answerIndex":1,
     "explanation":"Everyone is somewhere on this line and everyone moves along it - in both directions."},
    {"type":"scored","prompt":"Which is one of the four 'what actually works' moves for stress?",
     "options":["Move - regular physical activity, a walk counts","Buy more equipment","Hide from the problem","Work through the night"],
     "answerIndex":0,
     "explanation":"Move - regular physical activity, a walk counts - is one of the four highest-return moves."},
    {"type":"scored","prompt":"What is the 'sleep hygiene' definition the deck gives?",
     "options":["Washing your face before bed","The routines and conditions that make good sleep likely","Going to bed early every night","Taking sleeping pills"],
     "answerIndex":1,
     "explanation":"Sleep hygiene - the routines and conditions that make good sleep likely."},
    {"type":"scored","prompt":"How does the deck frame financial stress?",
     "options":["It's a personal failing","It's circumstance, not character - and it makes everything else on the list harder (sleep, concentration, mood, showing up)","It's the easiest problem to fix alone","It's not a college matter"],
     "answerIndex":1,
     "explanation":"It's circumstance, not character. Worry about money makes everything else on today's list harder."},
    {"type":"scored","prompt":"What is the 'Year 2 paradox'?",
     "options":["The year people most need support is the year they stop going","Year 2 has no support","Tutors forget Year 2 students","Year 2 students are better off without support"],
     "answerIndex":0,
     "explanation":"The year people most need support is the year they stop going. The door works exactly like it did last year."},
    {"type":"scored","prompt":"Which three-step sequence does the deck recommend for looking out for each other?",
     "options":["Notice, Ask, Tell someone","Watch, Wait, Walk away","Post, Tag, Share","Listen, Judge, Decide"],
     "answerIndex":0,
     "explanation":"Notice, Ask, Tell someone - that is the Encourage Unity in practice sequence."},
]
gen("l3y2-g", "Looking After Myself", qG)

# ============================================================
# Module H
# ============================================================
qH = [
    {"type":"scored","prompt":"What question does the deck say university, an apprenticeship and the studio all ask?",
     "options":["What school did you go to?","What can you actually do, and how do you know? Your Digital CV is your answer","What's your favourite film?","What are your predicted grades?"],
     "answerIndex":1,
     "explanation":"University, an apprenticeship and the studio all ask: what can you actually do, and how do you know? Your Digital CV is your answer."},
    {"type":"scored","prompt":"Where are the real gains in a Skills Assessment?",
     "options":["Green - by claiming strength","Amber - inconsistent under pressure, where most people sit. Red is usually already obvious","Red - because it's hardest","It doesn't matter - just tick the boxes"],
     "answerIndex":1,
     "explanation":"Amber is where the real gains are - Red is usually already obvious to you."},
    {"type":"scored","prompt":"What is the deck's 'one honest point' about UCAS and Year 1?",
     "options":["UCAS runs in Year 2, alongside your external assessments. The material for a personal statement is built in Year 1","UCAS is optional","Year 1 doesn't matter for UCAS","UCAS only matters for university"],
     "answerIndex":0,
     "explanation":"UCAS runs in Year 2, alongside your external assessments. The material for a personal statement is built in Year 1."},
    {"type":"scored","prompt":"What is 'the most useful outcome' of the careers quiz?",
     "options":["A clear YES - finding the perfect role","A clear NO - ruling something out is progress, faster than drifting into it","Skipping the quiz","Picking the highest-paid job"],
     "answerIndex":1,
     "explanation":"The most useful outcome of this quiz is a clear NO."},
    {"type":"scored","prompt":"What is the 'ten minutes now' rule the deck recommends?",
     "options":["Spend ten minutes on your portfolio per term","One entry per activity, logged the same week, tagged to the skills it evidences - ten minutes now saves an afternoon in Year 2","Take ten minutes off your placement","Spend ten minutes on social media"],
     "answerIndex":1,
     "explanation":"One entry per activity, logged the same week, tagged to the skills it evidences."},
    {"type":"scored","prompt":"What is the difference between the 'descriptive' and 'analytical' reflection examples?",
     "options":["There is no difference","The analytical one names the decision, the reasoning, the evidence and the change in practice - the level a personal statement or a professional portfolio needs","Descriptive is always better","Analytical removes emotion"],
     "answerIndex":1,
     "explanation":"The analytical one names the decision, the reasoning, the evidence and the change in practice."},
    {"type":"multi","prompt":"Which of these are among the eight 'first two weeks' tasks? Select all that apply.",
     "options":["App or shortcut set up","Skills Assessment completed honestly","Results interpreted - Green, Amber and Red","One activity logged, with a strong reflection"],
     "correctIndices":[0,1,2,3],
     "explanation":"All four are among the eight tasks to complete by the end of week two."},
    {"type":"scored","prompt":"What is the deck's 'Amber' definition in the Skills Assessment?",
     "options":["Evidenced strength","Inconsistent under pressure - most people sit here","Your development priority this term","Not relevant"],
     "answerIndex":1,
     "explanation":"Amber: Inconsistent under pressure - most people sit here."},
]
gen("l3y2-h", "Why Navigate Matters Here", qH)

# ============================================================
# Module I
# ============================================================
qI = [
    {"type":"scored","prompt":"What is the framing of this Year 2 professional behaviour session?",
     "options":["A repeat of last year","Deployment, not repetition - last year you built the evidence bank; this year you use it","A new-starter welcome","A pass/fail test"],
     "answerIndex":1,
     "explanation":"You built the evidence last year. This year you use it. The framing is deployment, not repetition."},
    {"type":"dragorder","prompt":"Put the eight beats of this Year 2 professional behaviour session in order.",
     "items":["Settling in - Year 2, week three","The standard didn't reset","Your reference goes live this year","Human skills - interview currency","Skills Assessment - what moved?","Claims versus evidence - sharper","Three strengths, application-ready","One thing"],
     "solution":[0,1,2,3,4,5,6,7],
     "explanation":"Settling in -> Standard didn't reset -> Reference goes live -> Human skills -> Skills Assessment moved -> Claims vs evidence -> Three strengths -> One thing."},
    {"type":"scored","prompt":"Why does the deck say 'this year counts double'?",
     "options":["Because you get two grades","Because this is the year referees and interviewers are actually watching - applications open, references get read","Because you have double the work","Because there are two of you"],
     "answerIndex":1,
     "explanation":"This year counts double because this is the year referees and interviewers are actually watching."},
    {"type":"scored","prompt":"What matters most for the reference, according to the deck?",
     "options":["Year 1 attendance only","Recent pattern - referees write from the freshest evidence, and this term is the one sitting in front of them","How many courses you took","Your predicted grades"],
     "answerIndex":1,
     "explanation":"Recent pattern weighs heaviest - referees write from the freshest evidence."},
    {"type":"scored","prompt":"What is the deck's claim about interview questions?",
     "options":["They are all about technical skill","At interview, nearly every question is secretly about one of the human skills (communication, teamwork, reliability, problem-solving, adaptability, initiative)","They are random","They are about personality tests only"],
     "answerIndex":1,
     "explanation":"At interview, nearly every question is secretly about one of the six human skills."},
    {"type":"scored","prompt":"What is the Year 2 reframe of the Skills Assessment?",
     "options":["Same as Year 1 - what are my skills?","What moved, and what does that prove? - movement is the story","Pass or fail","A self-assessment only"],
     "answerIndex":1,
     "explanation":"Today's question isn't 'what are my skills?' - it's 'what moved, and what does that prove?'"},
    {"type":"scored","prompt":"Which of these is 'evidence' rather than a claim, according to the deck?",
     "options":["'I'm reliable and hard-working'","'On placement I fixed a file nobody else could open - then wrote a one-page guide so the next person could do it without me'","'I'm a team player'","'I work well under pressure'"],
     "answerIndex":1,
     "explanation":"That is specific, checkable, memorable evidence - the level a personal statement or a professional portfolio needs."},
    {"type":"scored","prompt":"What should students do with the three strengths at the end of the activity?",
     "options":["Keep them in a folder","Replace last year's versions in Navigate - they go into live applications this term","Memorise them word for word","Email them to the safeguarding team"],
     "answerIndex":1,
     "explanation":"Replace last year's versions. These go into live applications this term."},
]
gen("l3y2-i", "Professional Behaviour & Personal Strengths", qI)

# ============================================================
# Module J
# ============================================================
qJ = [
    {"type":"scored","prompt":"What is the Year 2 framing of this work experience session?",
     "options":["Starting from zero","Building on what you know - this is a fresh run at it, not a repeat test","Skip it - you did it last year","It's a placement-finding workshop"],
     "answerIndex":1,
     "explanation":"You've done this once already - so this time we're building on what you know, not starting from zero."},
    {"type":"scored","prompt":"Why does a second placement matter more?",
     "options":["It counts as a third course","Two placements beat one: two CV entries, two referees, a portfolio that shows range as well as skill","It's required by law","It is worth double marks"],
     "answerIndex":1,
     "explanation":"Two placements beat one: two entries on a CV, two referees, and a portfolio that shows range as well as skill."},
    {"type":"scored","prompt":"What happens if you don't get a placement by Skills Week?",
     "options":["You're marked absent","You come into college for an employer-set brief and employer talks instead. It still counts","You fail the year","You take a 30-hour penalty"],
     "answerIndex":1,
     "explanation":"No placement by Skills Week? You come into college for an employer-set brief and employer talks instead."},
    {"type":"scored","prompt":"What is the Skills Week date for Year 2?",
     "options":["Monday 8 March 2027","Monday 1 February 2027","Friday 5 February 2027","Monday 15 March 2027"],
     "answerIndex":0,
     "explanation":"Skills Week: Monday 8 March 2027."},
    {"type":"scored","prompt":"What are the college hours a placement must fit within?",
     "options":["9am-5pm","8.30am-5.30pm, max 8-hour day","8am-6pm","Anytime"],
     "answerIndex":1,
     "explanation":"Placements must fit within college hours (8.30am-5.30pm), max 8-hour day."},
    {"type":"scored","prompt":"Where is the Careers & Employability team based at Lewes?",
     "options":["ECAT House, room 101","Careers Hub, Ground Floor","Cliffe Building, room 134","Ask at reception"],
     "answerIndex":2,
     "explanation":"Lewes: Cliffe Building, room 134 - Lewes.Careers@escg.ac.uk."},
    {"type":"scored","prompt":"What should you do if you are running late or unwell for placement?",
     "options":["Text a friend","Contact the employer AND the college","Just turn up when you can","Stay home and email your tutor only"],
     "answerIndex":1,
     "explanation":"Running late or unwell? Contact the employer AND the college."},
    {"type":"scored","prompt":"What is the closing line of the Year 2 work-experience session?",
     "options":["Good luck, see you next term","This is round two - use what you already know, and go further than last time. In this industry the people who get taken on are the ones who came back sharper. Seek the opportunity - again.","Remember to log your hours","We'll send a reminder"],
     "answerIndex":1,
     "explanation":"This is round two - use what you already know, and go further than last time. Seek the opportunity - again."},
]
gen("l3y2-j", "Work Experience - Skills Week, Aimed at Your Specialism", qJ)

# ============================================================
# Module K
# ============================================================
qK = [
    {"type":"scored","prompt":"What is the framing of this final progression session?",
     "options":["A ceremonial farewell","The last induction session you'll ever sit through - ninety minutes to turn two years of evidence into a plan, with the first application deadline already live","An exam preparation session","A placement briefing"],
     "answerIndex":1,
     "explanation":"The last induction session you will ever sit through."},
    {"type":"dragorder","prompt":"Put the eight beats of this final progression session in order.",
     "items":["Final year - what is actually different","The map, with dates on it","Two years of evidence - now it gets used","Application goals - concrete by definition","Three horizons - backwards from the deadlines","Right route? - the honest check","Closing the loop","One goal, on paper"],
     "solution":[0,1,2,3,4,5,6,7],
     "explanation":"Final year -> Map with dates -> Two years of evidence -> Application goals -> Three horizons -> Right route? -> Closing the loop -> One goal on paper."},
    {"type":"scored","prompt":"What is the deck's claim about 'results day' in relation to the application cycle?",
     "options":["Results day is more important than the application","Every deadline above exists to protect the time you need to earn them - the application is the easy half","Results day is the only thing that matters","It is at the end of Year 2"],
     "answerIndex":1,
     "explanation":"Every deadline above exists to protect the time you need to earn them - the application is the easy half."},
    {"type":"scored","prompt":"What is the deck's verdict on Year 1 evidence that isn't logged?",
     "options":["It's still useful informally","If it happened and is not logged, it effectively did not happen. Fix that this week","It can be re-created later","It only matters for university"],
     "answerIndex":1,
     "explanation":"If it happened and is not logged, it effectively did not happen."},
    {"type":"scored","prompt":"What is the 'test' the deck applies to Year 2 goals?",
     "options":["Does it look ambitious?","Does it beat the deadline with room to spare? On-time is the new late","Does it sound good in a tutor's meeting?","Does it match what your friends are doing?"],
     "answerIndex":1,
     "explanation":"The test this year is harsher: does it beat the deadline with room to spare? On-time is the new late."},
    {"type":"scored","prompt":"Why does the deck say to start drafting goals 'backwards from results day'?",
     "options":["It's easier to remember","Because the grades decide everything and the application calendar exists to protect the time they need","Because tutors prefer it","Because UCAS requires it"],
     "answerIndex":1,
     "explanation":"Start at results day and work backwards - the grades decide everything."},
    {"type":"scored","prompt":"What is the deck's mustard-line summary of the route check?",
     "options":["Just stick with what you chose","You can still change where you are going. You cannot get this year back","Talk to your parents","Apply to anything, fast"],
     "answerIndex":1,
     "explanation":"You can still change where you are going. You cannot get this year back."},
    {"type":"scored","prompt":"What is the closing line of the entire induction programme, according to the deck?",
     "options":["Good luck, Year 2","End of induction. Don't fumble the last lap. In Digital, Media and Film, the last lap is applications, portfolio and assessed work running in parallel. Plan for all three. Do not fumble the final year.","See you in September","Remember to log your hours"],
     "answerIndex":1,
     "explanation":"End of induction. Don't fumble the last lap. In Digital, Media and Film, the last lap is applications, portfolio and assessed work running in parallel."},
]
gen("l3y2-k", "Progression & Goals - The Final Year", qK)

print("\nAll 11 L3 Y2 modules generated x 3 variants = 33 quiz files")
