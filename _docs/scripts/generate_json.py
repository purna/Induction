#!/usr/bin/env python3
"""Generate learn and quiz JSON files from MD files in _induction."""

import json
import os
import re
import random

INDUCTION_DIR = "/Users/nigelmorris/Documents/GitHub/induction/_induction"
DATA_Y1_DIR = "/Users/nigelmorris/Documents/GitHub/induction/data/y1"
DATA_Y2_DIR = "/Users/nigelmorris/Documents/GitHub/induction/data/y2"

MODULES = {
    'A': 'Module A.md',
    'B': 'Module B.md',
    'C': 'Module C.md',
    'D': 'Module D.md',
    'E': 'Module E.md',
    'F': 'Module F.md',
    'G': 'Module G.md',
    'H': 'Module H.md',
    'I': 'Module I.md',
    'J': 'Module J.md',
    'K': 'Module K.md',
}


def strip_links(text):
    """Remove all markdown link patterns from text."""
    # Remove [[text | PowerPoint]](url) patterns
    text = re.sub(r'\[\[[^\]]*\]\]\([^)]*\)', '', text)
    # Remove [text](url) patterns
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove [[text]] patterns
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    # Remove standalone links in parentheses that are left over
    text = re.sub(r'\s+\(https?://[^\s)]+\)', '', text)
    return text


def clean_content(text):
    """Clean markdown content for slide content field."""
    text = strip_links(text)
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('####'):
            label = line.replace('####', '').strip()
            if label:
                lines.append(label + ':')
        elif line.startswith('#'):
            continue
        elif line.startswith('- '):
            lines.append(line[2:].strip())
        else:
            lines.append(line)
    result = ' '.join(lines).strip()
    return re.sub(r'\s+', ' ', result)


def extract_bullet_items(text):
    """Extract and clean bullet point items from text."""
    items = []
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            item = strip_links(line[2:].strip())
            item = re.sub(r'\s+', ' ', item).strip()
            if item.endswith('.'):
                item = item[:-1].strip()
            if item:
                items.append(item)
    return items


def extract_subsections(text):
    """Extract ### N. Title subsections and their content."""
    pattern = r'###\s+(\d+)\.\s+([^\n]+)'
    matches = list(re.finditer(pattern, text))
    
    subsections = []
    for i, m in enumerate(matches):
        title = strip_links(m.group(2).strip())
        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        
        raw_content = text[content_start:content_end].strip()
        content = clean_content(raw_content)
        items = extract_bullet_items(raw_content)
        
        subsections.append({
            'title': title,
            'content': content,
            'items': items,
        })
    
    return subsections


def extract_mc_questions(text):
    """Extract multiple choice questions from quiz text."""
    pattern = r'###\s+(\d+)\.\s+([^\n]+)'
    matches = list(re.finditer(pattern, text))
    
    questions = []
    for m in matches:
        q_text = strip_links(m.group(2).strip())
        after = text[m.end():].strip()
        
        lines = after.split('\n')
        options_line = ''
        for line in lines:
            stripped = line.strip()
            if re.match(r'^A\.\s+', stripped):
                options_line = stripped
                break
        
        if not options_line:
            continue
        
        marked = ' ' + options_line.replace('✅', ' __CORRECT__')
        parts = re.split(r'\s+([A-D])\.\s+', marked)
        
        options = []
        correct_idx = -1
        for idx in range(1, len(parts), 2):
            text_part = parts[idx + 1] if idx + 1 < len(parts) else ''
            text_part = strip_links(text_part)
            if '__CORRECT__' in text_part:
                correct_idx = len(options)
                text_part = text_part.replace('__CORRECT__', '').strip()
            text_part = re.sub(r'\s+', ' ', text_part).strip()
            if text_part.endswith('.'):
                text_part = text_part[:-1].strip()
            options.append(text_part)
        
        if len(options) == 4 and correct_idx >= 0:
            questions.append({
                'question': q_text,
                'options': options,
                'correct_idx': correct_idx,
            })
    
    return questions


def extract_revision_items(text, year_label):
    """Extract bullet items from Quick Revision Summary for a given year."""
    rev_start = text.find('# Quick Revision Summary')
    if rev_start < 0:
        return []
    
    rev_text = text[rev_start:]
    pattern = rf'### {year_label}\s*\n(.*?)(?=\n###|\Z)'
    m = re.search(pattern, rev_text, re.DOTALL)
    if not m:
        return []
    
    items = []
    for line in m.group(1).split('\n'):
        line = line.strip()
        if line.startswith('- '):
            item = strip_links(line[2:].strip())
            if item.endswith('.'):
                item = item[:-1].strip()
            if re.sub(r'\s+', ' ', item).strip():
                items.append(re.sub(r'\s+', ' ', item).strip())
    
    return items


def extract_key_fact(content, max_len=120):
    """Extract the first meaningful sentence from content, truncated if needed."""
    sentences = re.split(r'(?<=[.!?])\s+', content)
    for s in sentences:
        s = s.strip().rstrip('.!?')
        if 15 < len(s) <= max_len:
            return s
    for s in sentences:
        s = s.strip().rstrip('.!?')
        if len(s) > 15:
            return s[:max_len]
    return content[:max_len].rstrip('.!?') if len(content) > max_len else content.rstrip('.!?')


def gen_distractors(title, count=3):
    """Generate generic distractor options."""
    distractors = [
        "It is optional and not required",
        "It is only assessed in exams",
        "It applies only to certain students",
        "It can be safely ignored if busy",
        "It is handled entirely by staff",
        "It only matters in the first term",
    ]
    return distractors[:count]


def generate_exercises(subsections):
    """Generate exercises for learn JSON slides."""
    exercises = []
    all_items = []
    for sub in subsections:
        all_items.extend(sub['items'])
    # Remove duplicates while preserving order
    seen = set()
    unique_items = []
    for item in all_items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    
    for i, sub in enumerate(subsections):
        title = sub['title']
        items = sub['items']
        content = sub['content']
        
        if len(items) >= 3 and len(items) <= 6:
            opts = items[:4]
            exercise = {
                "type": "multi",
                "prompt": f"Which of the following are mentioned in '{title}'? Select all that apply.",
                "options": opts,
                "correctIndices": list(range(len(opts))),
                "explanation": f"All of these are covered in the section on {title}."
            }
        elif items:
            correct = items[0]
            other_items = [it for it in unique_items if it != correct and it not in items]
            distractors = (other_items[:3] if len(other_items) >= 3
                          else other_items + gen_distractors(title))
            distractors = distractors[:3]
            
            opts = [correct] + distractors
            rng = random.Random(hash(title + str(i)) & 0xFFFFFFFF)
            rng.shuffle(opts)
            correct_idx = opts.index(correct)
            
            exercise = {
                "type": "scored",
                "prompt": f"Which of the following is a key point about '{title}'?",
                "options": opts,
                "answerIndex": correct_idx,
                "explanation": f"This is a key point from the section on {title}."
            }
        else:
            fact = extract_key_fact(content)
            distractors = gen_distractors(title, 3)
            opts = [fact] + distractors
            rng = random.Random(hash(title + str(i) + 'text') & 0xFFFFFFFF)
            rng.shuffle(opts)
            correct_idx = opts.index(fact)
            
            exercise = {
                "type": "scored",
                "prompt": f"What is a key message of '{title}'?",
                "options": opts,
                "answerIndex": correct_idx,
                "explanation": fact
            }
        
        exercises.append(exercise)
    
    return exercises


def make_learn_json(module_letter, year, title, subsections, revision_items=None):
    """Generate a learn JSON file structure."""
    exercises = generate_exercises(subsections)
    
    slides = []
    for i, sub in enumerate(subsections):
        slide = {
            "title": sub['title'],
            "content": sub['content'],
            "example": "",
            "exampleOutput": "",
            "exercise": exercises[i] if i < len(exercises) else None
        }
        slides.append(slide)
    
    if revision_items and len(revision_items) >= 3:
        rev_opts = revision_items[:4]
        slides.append({
            "title": "Quick Revision Summary",
            "content": "Key points to remember: " + " ".join(revision_items),
            "example": "",
            "exampleOutput": "",
            "exercise": {
                "type": "multi",
                "prompt": "Which of these points are in the quick revision summary? Select all that apply.",
                "options": rev_opts,
                "correctIndices": list(range(len(rev_opts))),
                "explanation": "These points are summarised in the Quick Revision Summary."
            }
        })
    
    section = f"l3{year}-{module_letter.lower()}"
    
    return {
        "section": section,
        "level": "l3",
        "year": year,
        "module": module_letter,
        "title": title,
        "slides": slides
    }


def make_quiz_variant(module_letter, year, title, variant, mc_questions, subsections):
    """Generate a quiz JSON file with a specific variant."""
    section = f"l3{year}-{module_letter.lower()}"
    questions = []
    
    if variant == 'A':
        # Original MC questions + 2 additional from content
        for i, mq in enumerate(mc_questions[:6]):
            q_id = f"{section}-A{i+1:02d}"
            opts = list(mq['options'])
            correct = opts[mq['correct_idx']]
            wrong = [o for j, o in enumerate(opts) if j != mq['correct_idx']]
            
            rng = random.Random(hash(q_id) & 0xFFFFFFFF)
            combined = [(correct, True)] + [(w, False) for w in wrong]
            rng.shuffle(combined)
            options = [c[0] for c in combined]
            answer_idx = options.index(correct)
            
            questions.append({
                "id": q_id,
                "type": "scored",
                "prompt": mq['question'],
                "options": options,
                "answerIndex": answer_idx,
                "explanation": correct
            })
        
        # Add 2 additional from content using key facts with generic distractors
        added = 0
        for idx in range(len(subsections)):
            if added >= 2:
                break
            sub = subsections[idx]
            q_id = f"{section}-A{len(questions)+1:02d}"
            fact = extract_key_fact(sub['content'])
            distractors = gen_distractors(title, 3)
            opts = [fact] + distractors
            rng = random.Random(hash(q_id) & 0xFFFFFFFF)
            rng.shuffle(opts)
            answer_idx = opts.index(fact)
            
            questions.append({
                "id": q_id,
                "type": "scored",
                "prompt": f"What does the module say about '{sub['title']}'?",
                "options": opts,
                "answerIndex": answer_idx,
                "explanation": fact
            })
            added += 1
    
    elif variant == 'B':
        rephrasings = {
            'What is Pro Portal mainly used for?': 'Which of the following can you do using Pro Portal?',
            'Which is part of your study programme?': 'What is included as part of your study programme?',
            'What should you do if something is not working?': 'What should you do when something at college is not working?',
            'College support can include:': 'Which services does college support include?',
            'Why is belonging important?': 'What is the importance of belonging?',
            'How often should you check Pro Portal?': 'How frequently should you check Pro Portal?',
        }
        
        for i, mq in enumerate(mc_questions[:6]):
            q_id = f"{section}-B{i+1:02d}"
            opts = list(mq['options'])
            correct = opts[mq['correct_idx']]
            wrong = [o for j, o in enumerate(opts) if j != mq['correct_idx']]
            
            rng = random.Random(hash(q_id) & 0xFFFFFFFF)
            combined = [(correct, True)] + [(w, False) for w in wrong]
            rng.shuffle(combined)
            options = [c[0] for c in combined]
            answer_idx = options.index(correct)
            
            prompt = rephrasings.get(mq['question'], mq['question'])
            
            questions.append({
                "id": q_id,
                "type": "scored",
                "prompt": prompt,
                "options": options,
                "answerIndex": answer_idx,
                "explanation": correct
            })
        
        # Add 2 additional from content (multi type), fallback to scored
        added = 0
        start_idx = len(subsections) // 2
        for idx in range(start_idx, len(subsections)):
            if added >= 2:
                break
            sub = subsections[idx]
            q_id = f"{section}-B{len(questions)+1:02d}"
            if len(sub['items']) >= 3 and len(sub['items']) <= 6:
                items_opt = sub['items'][:min(len(sub['items']), 4)]
                questions.append({
                    "id": q_id,
                    "type": "multi",
                    "prompt": f"Which of the following are part of '{sub['title']}'? Select all that apply.",
                    "options": items_opt,
                    "correctIndices": list(range(len(items_opt))),
                    "explanation": f"All of these are part of {sub['title']}."
                })
                added += 1
        
        # Fallback: use scored questions with generic distractors if needed
        if added < 2:
            for idx in range(len(subsections)):
                if added >= 2:
                    break
                sub = subsections[idx]
                fact = extract_key_fact(sub['content'])
                if not fact:
                    continue
                q_id = f"{section}-B{len(questions)+1:02d}"
                distractors = gen_distractors(title, 3)
                opts = [fact] + distractors
                rng = random.Random(hash(q_id + 'fallback') & 0xFFFFFFFF)
                rng.shuffle(opts)
                answer_idx = opts.index(fact)
                questions.append({
                    "id": q_id,
                    "type": "scored",
                    "prompt": f"Which statement about '{sub['title']}' is correct?",
                    "options": opts,
                    "answerIndex": answer_idx,
                    "explanation": fact
                })
                added += 1
    
    elif variant == 'C':
        # 8 new questions from content
        q_idx = 0
        for idx in range(len(subsections)):
            if q_idx >= 8:
                break
            sub = subsections[idx]
            q_id = f"{section}-C{q_idx+1:02d}"
            
            if len(sub['items']) >= 3 and len(sub['items']) <= 6 and q_idx < 6:
                items_opt = sub['items'][:min(len(sub['items']), 4)]
                questions.append({
                    "id": q_id,
                    "type": "multi",
                    "prompt": f"Which of the following are mentioned in '{sub['title']}'? Select all that apply.",
                    "options": items_opt,
                    "correctIndices": list(range(len(items_opt))),
                    "explanation": f"All of these are mentioned in the section on {sub['title']}."
                })
                q_idx += 1
            elif sub['items'] and q_idx < 8:
                correct = sub['items'][0]
                distractors = gen_distractors(title, 3)
                opts = [correct] + distractors
                rng = random.Random(hash(q_id) & 0xFFFFFFFF)
                rng.shuffle(opts)
                answer_idx = opts.index(correct)
                
                questions.append({
                    "id": q_id,
                    "type": "scored",
                    "prompt": f"What is a key point about '{sub['title']}'?",
                    "options": opts,
                    "answerIndex": answer_idx,
                    "explanation": correct
                })
                q_idx += 1
        
        # Fill remaining
        while len(questions) < 8:
            sub = subsections[len(questions) % len(subsections)] if subsections else {'title': 'the module', 'content': 'This is mentioned in the module.'}
            q_id = f"{section}-C{len(questions)+1:02d}"
            fact = extract_key_fact(sub['content'])
            distractors = gen_distractors(title, 3)
            opts = [fact] + distractors
            rng = random.Random(hash(q_id) & 0xFFFFFFFF)
            rng.shuffle(opts)
            answer_idx = opts.index(fact)
            
            questions.append({
                "id": q_id,
                "type": "scored",
                "prompt": f"What does the module state about '{sub['title']}'?",
                "options": opts,
                "answerIndex": answer_idx,
                "explanation": fact
            })
        
        questions = questions[:8]
    
    return {
        "meta": {
            "section": section,
            "level": "l3",
            "year": year,
            "module": module_letter,
            "variant": variant,
            "title": title,
        },
        "questions": questions
    }


def parse_year_section(text, year_label):
    """Parse a year section to extract learn content and quiz."""
    learn_start = text.find('## What You Need to Know')
    quiz_marker = '# YEAR'
    quiz_start = text.find(quiz_marker, learn_start + 10 if learn_start >= 0 else 0)
    
    if learn_start >= 0 and quiz_start > learn_start:
        learn_text = text[learn_start:quiz_start]
        quiz_text = text[quiz_start:]
    else:
        learn_text = text[learn_start:] if learn_start >= 0 else text
        quiz_text = ''
    
    subsections = extract_subsections(learn_text)
    mc_questions = extract_mc_questions(quiz_text)
    
    return {
        'subsections': subsections,
        'mc_questions': mc_questions,
    }


def clean_all_options(data):
    """Strip trailing periods and normalize whitespace in all options/items."""
    if isinstance(data, dict):
        if 'options' in data and isinstance(data['options'], list):
            data['options'] = [re.sub(r'\s+', ' ', opt.strip().rstrip('.!?,;')) for opt in data['options']]
        if 'items' in data and isinstance(data['items'], list):
            data['items'] = [re.sub(r'\s+', ' ', item.strip().rstrip('.!?,;')) for item in data['items']]
        if 'explanation' in data:
            data['explanation'] = re.sub(r'\s+', ' ', str(data['explanation']).strip())
        for key in data:
            data[key] = clean_all_options(data[key])
    elif isinstance(data, list):
        return [clean_all_options(item) for item in data]
    return data


def process_module(module_letter, md_file):
    """Process a single module MD file and generate JSON files."""
    filepath = os.path.join(INDUCTION_DIR, md_file)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    title_match = re.match(r'# Module [A-K]: (.+)', content)
    title = title_match.group(1).strip()
    
    y1_start = content.find('# YEAR 1')
    y2_start = content.find('# YEAR 2')
    revision_start = content.find('# Quick Revision Summary')
    
    if revision_start < 0:
        revision_start = len(content)
    
    y1_text = content[y1_start:y2_start]
    y2_text = content[y2_start:revision_start]
    
    y1_data = parse_year_section(y1_text, '1')
    y2_data = parse_year_section(y2_text, '2')
    
    # Extract revision items from full content
    y1_rev = extract_revision_items(content, 'Year 1')
    y2_rev = extract_revision_items(content, 'Year 2')
    
    # Generate Y1 learn
    learn_y1 = make_learn_json(module_letter, 'y1', title, y1_data['subsections'], y1_rev)
    learn_y1 = clean_all_options(learn_y1)
    with open(os.path.join(DATA_Y1_DIR, f"l3y1-{module_letter.lower()}-learn.json"), 'w') as f:
        json.dump(learn_y1, f, indent=2, ensure_ascii=False)
    
    # Generate Y1 quizzes
    for variant in ['A', 'B', 'C']:
        quiz = make_quiz_variant(module_letter, 'y1', title, variant, y1_data['mc_questions'], y1_data['subsections'])
        quiz = clean_all_options(quiz)
        with open(os.path.join(DATA_Y1_DIR, f"l3y1-{module_letter.lower()}-quiz-{variant}.json"), 'w') as f:
            json.dump(quiz, f, indent=2, ensure_ascii=False)
    
    # Generate Y2 learn
    learn_y2 = make_learn_json(module_letter, 'y2', title, y2_data['subsections'], y2_rev)
    learn_y2 = clean_all_options(learn_y2)
    with open(os.path.join(DATA_Y2_DIR, f"l3y2-{module_letter.lower()}-learn.json"), 'w') as f:
        json.dump(learn_y2, f, indent=2, ensure_ascii=False)
    
    # Generate Y2 quizzes
    for variant in ['A', 'B', 'C']:
        quiz = make_quiz_variant(module_letter, 'y2', title, variant, y2_data['mc_questions'], y2_data['subsections'])
        quiz = clean_all_options(quiz)
        with open(os.path.join(DATA_Y2_DIR, f"l3y2-{module_letter.lower()}-quiz-{variant}.json"), 'w') as f:
            json.dump(quiz, f, indent=2, ensure_ascii=False)
    
    n_slides = len(y1_data['subsections'])
    n_mc = len(y1_data['mc_questions'])
    n_rev = len(y1_rev)
    print(f"Module {module_letter}: {title}")
    print(f"  Y1: {n_slides} slides, {n_mc} MC questions, {n_rev} revision items")
    n_slides2 = len(y2_data['subsections'])
    n_mc2 = len(y2_data['mc_questions'])


def main():
    os.makedirs(DATA_Y1_DIR, exist_ok=True)
    os.makedirs(DATA_Y2_DIR, exist_ok=True)
    
    for module_letter, md_file in MODULES.items():
        process_module(module_letter, md_file)
    
    print("\nDone! All JSON files generated.")


if __name__ == '__main__':
    main()
