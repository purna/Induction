# East Sussex College Group — Student Induction Quiz

This is the single reference for how the induction quiz app is structured, how
content is authored, and how the app behaves. If code and this document ever
disagree, this document wins — fix the code.

---

## 1. Purpose

A client-side, offline-first PWA that delivers the **ESCG Student Induction**
programme (2026–27) for **Level 3, Level 2 and Level 1 Digital, Media and
Computing students** as a self-paced online experience that mirrors the
in-class induction sessions.

Students are grouped **first by Level (1, 2 or 3)** and **then by Year
(Year 1 or Year 2)**. Each level/year combination has **11 modules, A
through K**, all using the same learn-then-test flow: students read short,
scannable slides (Learn), then take a short quiz (Quiz) to confirm the key
takeaways. Each module ships **three quiz variants — A, B and C** — and the
app picks one at random per attempt.

The quiz is also a **light-touch evidence trail** — the app records a
student's email, level and year, and which modules they have completed, so
induction leads can see who has engaged with induction and which modules they
have finished.

> **Current content status:** **Level 3 only.** The Level 3 PowerPoints
> live in `_induction/l3/y1/` and `_induction/l3/y2/` (one file per module
> A–K). **Level 2 and Level 1 intake flows, module lists and content will
> be added once those PowerPoints are available** — drop them into
> `_induction/l2/{y1,y2}/` and `_induction/l1/{y1,y2}/` when ready. The
> intake screen, module ids, configuration model and Firestore schema
> already anticipate all three levels.

---

## 2. User flow

1. **Sign-in / intake screen** (`#startScreen`)
   - Student picks a **Level** (Level 1, Level 2 or Level 3).
   - Once a level is picked, a **Year** picker appears (Year 1 / Year 2)
     for that level. Some levels may have only one year — in which case
     the year picker is skipped.
   - Student enters their **college email address**.
   - Student confirms a consent statement ("I confirm this is my email and
     I understand my progress will be recorded").
   - These details are stored in `app.state.user = { email, level, year }`
     and also persisted to `localStorage` under `inductionUser`. They are
     pre-filled on subsequent visits.
   - If a student is already signed in via Google (optional Firebase path),
     the Google account's email overrides the typed email.

2. **Module grid** (`#sectionSelection`)
   - Shows the 11 modules (A–K) for the student's chosen level/year, as
     cards.
   - Each card shows the module title, a one-line summary, a Learn button,
     a Quiz button, and a completion badge.

3. **Learn mode** (`#learnScreen`)
   - 4–8 short slides per module (drawn from the in‑class presentation).
   - Optional interactive `multiplechoice`, `fillblank` and `dragdrop`
     exercises.

4. **Quiz mode** (`#quizContainer`)
   - 6–10 questions drawn from
     `data/{level}-{year}-{module}-quiz-{A|B|C}.json` (see §5 for naming).
   - The app picks one of A / B / C at random per attempt and remembers
     the student's last variant in `app.state.quizVariant`.
   - Mix of `scored` (single-select), `multi` (select all), `insert`
     (fill blank) and `dragorder` question types.
   - Configurable timer (default 5 min, can be disabled in Settings).
   - 80 % pass mark.

5. **Results / review** (`#resultsContainer`)
    - Shows score, pass/retry, and a per-question review.
   - Saves the attempt to `localStorage` and (if Firebase is configured)
     pushes it to Firestore under the user's email/level/year.

6. **Teacher mode** (optional, future)
   - A read-only "view progress" view is out of scope for v1.

---

## 3. Levels, years and modules

Each **Level** (`l1`, `l2`, `l3`) has one or more **Years** (`y1`, `y2`),
and each level/year combination has 11 modules **A–K** mapped 1:1 to the
PowerPoints in `_induction/{level}/{year}/`.

| Level | Year | Modules today     | Source folder                  |
| ----- | ---- | ----------------- | ------------------------------ |
| l3    | y1   | A–K (11 modules)  | `_induction/l3/y1/` (built)    |
| l3    | y2   | A–K (11 modules)  | `_induction/l3/y2/` (built)    |
| l2    | y1   | (being added)     | `_induction/l2/y1/`            |
| l2    | y2   | (being added)     | `_induction/l2/y2/`            |
| l1    | y1   | (being added)     | `_induction/l1/y1/`            |

> Today's presentations sit in `_induction/y1/` and `_induction/y2/` and
> are **Level 3** material. When the Level 2 and Level 1 decks land they
> will move into `_induction/l2/`, `_induction/l3/` (reorganised) and
> `_induction/l1/`. The data-id scheme below already uses `lN` prefixes
> so no further renames are needed.

### 3.1 Module list (Level 3 reference)

The module list and titles are taken from the 22 Level-3 induction decks
in `_induction/y1/` and `_induction/y2/`. Module A–K are mapped 1:1 to
those PowerPoints.

| ID  | Module title                                | Year 1 focus                                                        | Year 2 focus                                                |
| --- | ------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| A   | Welcome, Belonging & Support                | Settling in, meet the group, study programme, support services       | Welcome back — final year, where you're headed              |
| B   | Confidence & Attendance                     | School → college, the long fuse, attendance case                    | Year 1 → Year 2, the final fuse, Year-2 attendance case     |
| C   | Health & Safety                             | Introduction, basics, subject-specific, noticing & reporting         | Year-2 refresher, familiarity is the risk                  |
| D   | Students' Voice & Student Rep Elections     | How student voice works, Rep / Governor roles, election               | Year-2 view of student voice, leadership roles             |
| E   | Respect, Relationships & College Values     | PROUD values, British Values, Equality Act 2010, behaviour standards | Same content, framed as accountability & consistency        |
| F   | Staying Safe at College                     | Safeguarding, Prevent, online safety, AI & data, reporting           | Year-2 risk profile (FMP, placement, UCAS)                 |
| G   | Looking After Myself (Wellbeing)            | Mental health, stress, sleep, money, support, looking out for others | Same — Year 2 asks more of you                             |
| H   | How to Use Navigate                         | Skills assessment, next destination, careers, logging, reflection    | Same — refresh and audit your evidence                     |
| I   | Professional Behaviour & Personal Strengths | Standard, attendance, employability, strengths with evidence         | Standard didn't reset, references, application-ready       |
| J   | Work Experience                             | Why it matters, block vs flexible, dates, finding a placement        | Second, sharper placement — same process, higher bar        |
| K   | Progression Opportunities & Setting Goals   | Where Level 3 leads, evidence, three horizons, write one goal         | Final year — calendar, deadlines, one dated application goal|

When Level 2 and Level 1 content is added, each level/year combination will
follow the same A–K shape, with topics adapted (e.g. Level 2's Progression
module will talk about apprenticeships and Level 1 placements rather than
UCAS / FMP). The module titles for L2 / L1 will be filled in as the
presentations are authored.

---

## 4. File structure

```
induction/
├── SOURCE_OF_TRUTH.md                ← this file
├── README.md                         ← user-facing overview
├── index.html                        ← single page shell (all screens live here)
├── styles.css                        ← all styling, incl. light/dark theme tokens
├── sw.js                             ← service worker (caches app shell for offline)
├── manifest.webmanifest      ← PWA manifest
│
├── js/
│   ├── firebaseConfig.js             ← Firebase init + Google sign-in
│   ├── databaseManager.js            ← Firestore sync layer (results, prefs)
│   ├── classroom.js                  ← (legacy) Google Classroom submission
│   ├── app.js                        ← root: app.state, app.el, app.config,
│   │                                    app.init, intake flow, helpers
│   ├── storage.js                    ← localStorage persistence
│   ├── helpers.js                    ← CSS var reader, canvas helpers
│   ├── settings.js                   ← theme, timer, tutorial gate
│   ├── learn.js                      ← Learn slide rendering + exercises
│   ├── quiz.js                       ← Quiz rendering + scoring (A/B/C)
│   ├── results.js                    ← Results / review
│   └── progress.js                   ← Completion badges, overall progress
│
├── data/
│   ├── l3y1-a-learn.json  … l3y1-k-learn.json     ← Learn content (L3, Y1)
│   ├── l3y1-a-quiz-A.json … l3y1-k-quiz-A.json    ← Quiz variant A
│   ├── l3y1-a-quiz-B.json … l3y1-k-quiz-B.json    ← Quiz variant B
│   ├── l3y1-a-quiz-C.json … l3y1-k-quiz-C.json    ← Quiz variant C
│   ├── l3y2-a-learn.json  … l3y2-k-learn.json     ← … and the same for L3 Y2
│   ├── l3y2-a-quiz-A.json … l3y2-k-quiz-C.json
│   ├── l2-*, l1-*                                   ← added as content lands
│   └── csharp-*                                    ← legacy C# practice mode
│
├── _induction/
│   ├── l3/y1/  ← 11 source PowerPoints (Level 3, Year 1)
│   ├── l3/y2/  ← 11 source PowerPoints (Level 3, Year 2)
│   ├── l2/y1/  ← Level 2 Year 1 (planned — drops here when decks arrive)
│   ├── l2/y2/  ← Level 2 Year 2 (planned)
│   ├── l1/y1/  ← Level 1 Year 1 (planned)
│   └── l1/y2/  ← Level 1 Year 2 (planned — confirm if Level 1 is single-year)
│
├── functions/                        ← Firebase Cloud Functions (legacy Classroom)
├── plans/                            ← development notes
└── Quiz3.zip                         ← historical archive (can be removed)
```

> The folder currently called `_induction/y1/` holds **Level 3 Year 1**
> decks. When the L2 / L1 folders are populated, the Y1 / Y2 folders will be
> renamed to `l3/y1/` and `l3/y2/` for clarity. The data-id scheme uses
> `lN` prefixes already, so renaming the folders will not require any
> further id renames.

---

## 5. Naming conventions

- **Level id:** `l1`, `l2`, `l3`.
- **Year id (within a level):** `y1`, `y2`. A level with only one year uses
  `y1` and the year picker is hidden in the UI.
- **Section / module id:** `{level}{year}-{module}` where module is `a`
  through `k`. Example: `l3y1-a`, `l3y2-k`, `l2y1-c`.
- **Learn file:** `data/{level}{year}-{module}-learn.json`
  Example: `data/l3y1-c-learn.json` (Level 3, Year 1, Module C — Health &
  Safety).
- **Quiz file:** `data/{level}{year}-{module}-quiz-{A|B|C}.json`
  Example: `data/l3y2-f-quiz-A.json`. Every module ships **all three**
  variants A, B and C — the app picks one at random per attempt.
- **Legacy / unused ids** that remain on disk for now:
  `csharp-*` files. These power the original C# quiz screens (still
  reachable from the help flow if you want to keep them as a "practice"
  mode). See §11 (Backwards compatibility) below.

---

## 6. Data formats

### Learn file — `data/{level}-{year}-{module}-learn.json`

```json
{
  "section": "l3y1-a",
  "level": "l3",
  "year": "y1",
  "module": "A",
  "title": "Welcome, Belonging & Support",
  "slides": [
    {
      "title": "What we'll do in this session",
      "content": "There's nothing to revise and nothing to get wrong today. Here's the plan.",
      "example": "",
      "exampleOutput": "",
      "exercise": {
        "type": "multiplechoice",
        "prompt": "Which of these is part of your study programme?",
        "options": ["Just your lessons", "English & maths (if applicable)", "Industry placement (where relevant)", "Tutorial & personal development", "All of the above"],
        "answer": "All of the above"
      }
    }
  ]
}
```

Supported slide-exercise `type`s: `multiplechoice`, `fillblank`,
`dragdrop`. The legacy `code` exercise type is still rendered by
`learn.js` for the C# practice mode but is **not used** by induction
content.

### Quiz file — `data/{level}-{year}-{module}-quiz-{A|B|C}.json`

```json
{
  "meta": {
    "section": "l3y1-a",
    "level": "l3",
    "year": "y1",
    "module": "A",
    "title": "Welcome, Belonging & Support"
  },
  "questions": [
    {
      "id": "l3y1-a-01",
      "type": "scored",
      "prompt": "What is the single biggest factor in whether students stay, attend and succeed?",
      "options": ["Tight deadlines", "Belonging", "High-stakes testing", "Strict uniforms"],
      "answerIndex": 1,
      "explanation": "Belonging is the single biggest factor in whether students stay, attend and succeed."
    },
    {
      "id": "l3y1-a-02",
      "type": "insert",
      "prompt": "Fill in the blank: check your Pro Portal every ____ before you set off.",
      "template": "Check your Pro Portal every ____ before you set off.",
      "options": ["morning", "week", "term", "year"],
      "answerIndex": 0
    },
    {
      "id": "l3y1-a-03",
      "type": "multi",
      "prompt": "Which of these are part of your study programme? Select all that apply.",
      "options": ["Your Digital or Media qualification", "English & maths (where applicable)", "Work-related learning", "Tutorial & personal development"],
      "correctIndices": [0, 1, 2, 3]
    },
    {
      "id": "l3y1-a-04",
      "type": "dragorder",
      "prompt": "Put these 'what we expect' items in the order the deck presents them.",
      "items": ["Meet your group", "Meet your teachers", "Get to know your study programme", "Find out about support"],
      "solution": [0, 1, 2, 3]
    }
  ]
}
```

Supported question `type`s: `scored`, `multi`, `insert`, `dragorder`. The
legacy types `typing`, `coderunner`, `pyramid`, `visual`, `matrix-3x3`,
`cluster-missing`, `profiled` remain supported by `quiz.js` for the
legacy C# practice mode.

**Quiz variants:** Every module ships three quiz files — `quiz-A.json`,
`quiz-B.json`, `quiz-C.json`. They may use different questions, different
ordering, or different wording, but they must all cover the same module
takeaways. The app picks one of A / B / C at random per attempt and stores
the chosen variant in `app.state.quizVariant` so the results screen can
show which variant was used.

---

## 7. UI screens (index.html)

Each screen is a `<main>` element with an `id` and a `hidden` toggle. JS flips
the `hidden` class to navigate.

| Screen                | id                       | Purpose                                              |
| --------------------- | ------------------------ | ---------------------------------------------------- |
| Start / intake        | `startScreen`            | Level picker → Year picker → email → consent         |
| Section (module) list | `sectionSelection`       | 11 cards for the chosen level/year                   |
| Learn                 | `learnScreen`            | Slide-based lesson with optional exercises          |
| Quiz                  | `quizContainer`          | One question at a time + progress bar + nav          |
| Results               | `resultsContainer`       | Score, review, retry/back                            |
| Tutorial              | `tutorialScreen`         | First-run "how this works" overview (legacy / help)  |
| Settings modal        | `settingsModal`          | Timer, per-question timer, reset progress            |

The start screen replaces the old tutorial-as-gate in the new flow:
- **First ever visit** → show `startScreen` (level → year → email →
  consent).
- **Return visit** → if `localStorage.inductionUser` exists, jump
  straight to `sectionSelection`.

The "How it works" button (`#helpBtn`) still opens the original
`tutorialScreen` for anyone who needs a refresher. The tutorial screen
also acts as a gateway to the legacy C# practice mode (see §11).

### 7.1 Start screen intake (Level → Year)

1. Student sees three large cards: **Level 1**, **Level 2**, **Level 3**.
2. Picking a level reveals the **Year** picker (Year 1 / Year 2) for
   that level, unless the level only has one year (in which case the
   year picker is hidden and `y1` is used).
3. Once a level and (if applicable) a year are picked, the email +
   consent fields appear.
4. **Continue** is enabled only when level is selected, year is selected
   (if applicable), email is valid, and consent is ticked.

---

## 8. State and persistence

### `app.state` additions over the C# quiz
```js
app.state.user = null;            // { email, level, year } once intake is complete
app.state.level = 'l3';           // active level ('l1', 'l2' or 'l3')
app.state.year = 'y1';            // active year ('y1' or 'y2')
app.state.section = null;         // active module id, e.g. 'l3y1-a'
app.state.quizVariant = null;     // 'A' | 'B' | 'C' for the current attempt
```

### localStorage keys
- `inductionUser` — `{ email, level, year, startedAt }` set on intake.
- `inductionResults` — `{ [sectionId]: { bestPct, passed, attempts,
  lastVariant, history: [...] } }`.
- `inductionLearnProgress` — `{ [sectionId]: { lastSlide, total,
  completed } }`.
- The legacy keys (`quizResults`, `learnProgress`, `quizTheme`,
  `quizTimerMinutes`, `quizTutorialSeen`, `quizPqTimerSeconds`) are kept
  for the optional legacy C# practice flow.

### Firestore (optional, when Firebase is configured)

Per-user document structure under `users/{uid}/`:

```
users/{uid}/
  induction/
      profile:    { email, level, year, startedAt }
      results:    { [sectionId]: { bestPct, passed, attempts, lastVariant, history, updatedAt } }
      attempts:   { [attemptId]: { sectionId, level, year, email, score, total, date, ... } }
  results:       ← legacy C# quiz (kept)
  preferences:   ← legacy C# quiz settings (kept)
```

---

## 9. App behaviour rules

### Sign-in / intake
1. On first visit, the start screen is shown.
2. The student selects a **Level** (L1 / L2 / L3) by clicking one of
   three large cards.
3. If the level has two years, a **Year** picker appears and the
   student picks Year 1 or Year 2.
4. The student types their email. Client-side validation: must contain
   `@` and end in `.ac.uk` (or any other configured college domain —
   see `ALLOWED_EMAIL_DOMAINS` below).
5. The student ticks the consent checkbox.
6. **Continue** is enabled only when level is selected, year is
   selected (if applicable), email is valid, and consent is ticked.
7. On continue:
   - Save `inductionUser` to localStorage.
   - Set `app.state.user = { email, level, year }`, `app.state.level`,
     `app.state.year`.
   - Hide `startScreen`, show `sectionSelection`.
   - Render the 11 module cards for the chosen level/year.

### Module grid
- Each card shows: module letter (A–K), title, one-line summary, Learn
  button, Quiz button, completion badge.
- Completion badge states (driven by `progress.js`):
  - empty — never attempted
  - "Learned" badge — learn slides completed
  - gold star + 100 % — quiz passed (≥ 80 %)
   - percentage circle — quiz attempted but not yet passed

### Quiz rules
- 80 % pass mark.
- **Three quiz variants (A / B / C) per module.** The app picks one at
  random per attempt and remembers it as `app.state.quizVariant`. The
  results screen shows which variant was used.
- Timer can be disabled in Settings (default 5 min).
- Question types: `scored`, `multi`, `insert`, `dragorder`.
- On finish → render results, save to localStorage, push to Firestore
  if configured.

### Accessibility

**General**
- All buttons keyboard reachable.
- Focus rings preserved.
- Colour contrast meets WCAG AA against both light and dark themes.
- Quiz timer is decorative — students are not penalised for time over
  budget; they are simply auto-submitted.

**Accessibility Modal** (`#a11yModal`, opened via `#a11yBtn` in the header)

Managed by `js/accessibility.js`. Closes via close button, footer "Done"
button, backdrop click, or `Escape` key.

| Section              | Feature          | `data-feature`   | Effect                                                   |
|----------------------|------------------|------------------|----------------------------------------------------------|
| Vision               | High Contrast    | `high_contrast`  | Adds `body.high-contrast` — stronger borders & brighter text |
| Vision               | Large Text       | `large_text`     | Sets `html` `font-size` to `120%`                        |
| Hearing / Speech     | Read Aloud (TTS) | `tts`            | Enables Web Speech API TTS via `app.speak(text)`         |
| Hearing / Speech     | Slow Speech      | `slow_speech`    | Reduces TTS rate from `0.9` to `0.65`                    |
| Hearing / Speech     | Sound            | `sound`          | Toggles background ambience and sound effects            |
| Reading / Cognition  | Simple Language   | `simple_mode`    | Adds `body.simple-mode` — signals simpler vocabulary     |
| Reading / Cognition  | Reduce Motion    | `reduce_motion`  | Adds `body.reduce-motion` — disables all CSS animations  |

Each toggle is an iOS-style pill (`role="switch"`, `aria-checked`) styled by
`.toggle-btn`. All preferences persist to `localStorage` (`a11y-*` keys) and
restore on page load. The module exposes `app.a11y` (state object),
`app.speak()`, `app.openA11y()`, and `app.closeA11y()` for use by other
modules.

---

## 10. Configuration constants

In `js/app.js`:

```js
app.config = {
  ALLOWED_EMAIL_DOMAINS: ['escg.ac.uk', 'sussexcoast.ac.uk', 'hastings.ac.uk'],
  LEVELS: [
    { id: 'l3', label: 'Level 3', years: ['y1', 'y2'] },
    { id: 'l2', label: 'Level 2', years: ['y1', 'y2'] },
    { id: 'l1', label: 'Level 1', years: ['y1'] },
  ],
  MODULES: [
    // Level 3, Year 1
    { id: 'l3y1-a', level: 'l3', year: 'y1', module: 'A', title: 'Welcome, Belonging & Support', summary: '...' },
    { id: 'l3y1-b', level: 'l3', year: 'y1', module: 'B', title: 'Confidence & Attendance',    summary: '...' },
    // … l3y1-c … l3y1-k
    // Level 3, Year 2
    { id: 'l3y2-a', level: 'l3', year: 'y2', module: 'A', title: 'Welcome back — final year',   summary: '...' },
    // … l3y2-b … l3y2-k
    // Level 2 / Level 1 entries added as content lands
  ],
  PASS_THRESHOLD: 80
};
```

`LEVELS` drives the Level → Year picker on the start screen. `MODULES`
drives the section-selection grid. Both are the source of truth for the
UI — `index.html` does not contain hard-coded module cards for
induction content.

---

## 11. Backwards compatibility (legacy C# practice mode)

The 40+ `csharp-*` data files and the `csharp-*` cards in
`#sectionSelection` are **kept** but **no longer the default flow**. They
are reachable from the Help button — that opens the original tutorial
screen with a "Try the C# practice quiz" link. This preserves the
original learning content while making the induction flow the primary
experience.

If at any point you want to remove the legacy flow:

1. Delete `data/csharp-*.json`.
2. Delete the `csharp-*` section cards from `index.html`.
3. Update `sw.js` so it doesn't pre-cache the deleted files.

---

## 12. Authoring checklist for a new induction module

For each module `{l1|l2|l3}-{y1|y2}-{a..k}`:

1. Drop the PowerPoint into `_induction/{level}/{year}/`.
2. Read through the deck and pick the 5–8 key slides to adapt into
   Learn slides.
3. Write `data/{level}-{year}-{letter}-learn.json` (see §6 for schema).
   Keep slides short — one paragraph + one exercise per slide.
4. Write `data/{level}-{year}-{letter}-quiz-A.json` with 6–10 questions
   covering the module's takeaways. Mix `scored`, `multi`, `insert`,
   `dragorder`.
5. Write `data/{level}-{year}-{letter}-quiz-B.json` and `…-quiz-C.json`.
   Variants may reorder the same questions or reword them; the goal is
   that repeating the quiz still feels fresh.
6. Add an entry to `app.config.MODULES` in `js/app.js` (only if the
   level / year combination is new — otherwise the module letter just
   needs the entry added).
7. Open the app, pick the right level → year, run through Learn →
   Quiz end to end.
8. Confirm the module card shows up in the grid with the correct
   title.

---

## 13. Removed: Flow Builder

The Flow Builder (`js/flow-builder.js`, the `flowbuilder` exercise type,
and the `renderFlowBuilderExercise` helper) has been **removed**. It was
a visual flowchart editor used by the original C# quiz's flow-control
exercises. None of the Level 3 / Level 2 / Level 1 induction decks use
it, and the exercise type is no longer rendered by `learn.js`.

If a future deck genuinely needs a flowchart-style exercise, prefer
using the existing `dragdrop` / `dragorder` question types with a
plain text expected answer.