(function () {
  'use strict';

  app.showResults = function () {
    app.stopPqTimer();
    app.el.pqTimerDisplay.classList.add('hidden');
    app.state.pqLocked = false;
    app.el.quizContainer.classList.add('hidden');
    app.el.resultsContainer.classList.add('hidden');
    app.el.timerDisplay.classList.add('hidden');

    const questions = app.state.data.questions;
    const isProfiled = questions[0] && questions[0].type === 'profiled';

    const wrap = document.createElement('div');

    if (isProfiled) {
      app.renderProfiledResults(wrap, questions);
    } else {
      app.renderScoredResults(wrap, questions);
    }

    app.updateCompletionBadges();
    app.updateOverallProgress();
    app.updateDownloadButtons();

    const actions = document.createElement('div');
    actions.className = 'results-actions';

    const backBtn = document.createElement('button');
    backBtn.className = 'btn btn-secondary';
    backBtn.textContent = 'Back to sections';
    backBtn.addEventListener('click', function () {
      app.el.resultsContainer.classList.add('hidden');
      app.el.sectionSelection.classList.remove('hidden');
      app.updateCompletionBadges();
      app.updateOverallProgress();
    });

    const retryBtn = document.createElement('button');
    retryBtn.className = 'btn';
    retryBtn.textContent = 'Retry this section';
    retryBtn.addEventListener('click', function () {
      app.startQuiz(app.state.section, app.state.level);
    });

    const pdfBtn = document.createElement('button');
    pdfBtn.className = 'btn btn-secondary';
    pdfBtn.innerHTML = '<i class="fa-solid fa-file-pdf"></i> Download PDF';
    pdfBtn.title = 'Download this result as a PDF';
    pdfBtn.addEventListener('click', app.generateResultsPDF);

    actions.appendChild(retryBtn);
    if (app.state.passed) {
      actions.appendChild(pdfBtn);
    }
    actions.appendChild(backBtn);
    wrap.appendChild(actions);

    app.el.resultsContainer.innerHTML = '';
    app.el.resultsContainer.appendChild(wrap);
    app.el.resultsContainer.classList.remove('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  app.renderScoredResults = function (wrap, questions) {
    let correct = 0;
    questions.forEach(function (q) {
      if (q.type === 'pyramid') {
        if (app.checkPyramidAnswer(q, app.state.answers[q.id])) correct++;
      } else if (q.type === 'typing') {
        const user = app.state.answers[q.id] || [];
        const expected = q.blanks || [];
        if (user.length === expected.length && expected.every(function (v, i) { return String(user[i]).trim().toLowerCase() === String(v).trim().toLowerCase(); })) {
          correct++;
        }
      } else if (q.type === 'dragorder') {
        const user = app.state.answers[q.id] || [];
        const expected = q.solution || [];
        if (JSON.stringify(user) === JSON.stringify(expected)) correct++;
      } else if (q.type === 'coderunner') {
        const code = app.state.answers[q.id] || '';
        const result = app.simulateCSharp(code, q);
        if (result.ok) correct++;
      } else if (q.type === 'insert') {
        const user = (app.state.answers[q.id] || [])[0];
        if (user === q.answerIndex) correct++;
      } else if (Array.isArray(q.correctIndices)) {
        const user = (app.state.answers[q.id] || []).sort(function (a, b) { return a - b; });
        const expected = q.correctIndices.slice().sort(function (a, b) { return a - b; });
        if (JSON.stringify(user) === JSON.stringify(expected)) correct++;
      } else if (app.state.answers[q.id] === q.answerIndex) {
        correct++;
      }
    });
    const pct = Math.round((correct / questions.length) * 100);
    app.state.score = pct;
    app.state.passed = pct >= 80;
    app.state.correct = correct;
    app.state.total = questions.length;

    if (app.speak) {
      app.speak('You scored ' + correct + ' out of ' + questions.length + '. ' + (pct >= 80 ? 'You passed.' : 'You did not pass.'));
    }

    app.saveQuizResult(app.state.section, app.state.level, app.state.quizVariant, pct, correct, questions.length);
    app.saveQuizSession(app.state.section, app.state.level, app.state.data, app.state.answers, pct, correct, questions.length, app.state.quizVariant);

    const hero = document.createElement('div');
    hero.className = 'results-hero';
    const passBadge = app.state.passed
      ? '<span class="pass-badge">PASS</span>'
      : '<span class="review-badge">Needs Review</span>';
    hero.innerHTML =
      '<p class="settings-hint" style="margin:0;padding:1rem 0;">' + app.sectionTitle() + '</p>' +
      passBadge +
      '<p class="results-score">' + pct + '%</p>' +
      '<p class="results-sub">' + correct + ' of ' + questions.length + ' correct</p>';
    wrap.appendChild(hero);

    const reviewHeading = document.createElement('h2');
    reviewHeading.textContent = 'Review';
    wrap.appendChild(reviewHeading);

    questions.forEach(function (q, i) {
      const userAnswers = app.state.answers[q.id];
      const isPyramid = q.type === 'pyramid';
      const isVisualType = q.type === 'visual' || q.type === 'matrix-3x3';

      let gotIt = false;
      if (isPyramid) {
        gotIt = app.checkPyramidAnswer(q, userAnswers);
      } else if (q.type === 'typing') {
        const user = userAnswers || [];
        const expected = q.blanks || [];
        gotIt = user.length === expected.length && expected.every(function (v, idx) { return String(user[idx]).trim().toLowerCase() === String(v).trim().toLowerCase(); });
      } else if (q.type === 'dragorder') {
        gotIt = JSON.stringify(userAnswers || []) === JSON.stringify(q.solution || []);
      } else if (q.type === 'coderunner') {
        gotIt = app.simulateCSharp(userAnswers || '', q).ok;
      } else if (q.type === 'insert') {
        gotIt = (userAnswers || [])[0] === q.answerIndex;
      } else if (Array.isArray(q.correctIndices)) {
        const user = (userAnswers || []).sort(function (a, b) { return a - b; });
        const expected = q.correctIndices.slice().sort(function (a, b) { return a - b; });
        gotIt = JSON.stringify(user) === JSON.stringify(expected);
      } else {
        gotIt = userAnswers === q.answerIndex;
      }

      const item = document.createElement('div');
      item.className = 'review-item';

      const p = document.createElement('p');
      p.className = 'review-prompt';
      p.textContent = (i + 1) + '. ' + q.prompt;
      item.appendChild(p);

      const tag = document.createElement('span');
      tag.className = 'tag ' + (gotIt ? 'good' : 'bad');
      tag.textContent = gotIt ? 'Correct' : 'Incorrect';
      item.appendChild(tag);

      if (isPyramid) {
        app.renderPyramidReview(item, q);
      } else if (q.type === 'matrix-3x3') {
        app.renderMatrixReview(item, q);
      } else if (q.type === 'typing') {
        const user = Array.isArray(userAnswers) ? userAnswers : [];
        const expected = q.blanks || [];
        const yourAnswer = document.createElement('p');
        yourAnswer.textContent = 'Your answer: ' + (user.length ? user.join(', ') : '(skipped)');
        yourAnswer.style.fontFamily = 'var(--font-mono)';
        yourAnswer.style.fontSize = '0.85rem';
        item.appendChild(yourAnswer);
        if (!gotIt) {
          const correctAnswer = document.createElement('p');
          correctAnswer.textContent = 'Correct answer: ' + (expected.length ? expected.join(', ') : '(none)');
          correctAnswer.style.fontFamily = 'var(--font-mono)';
          correctAnswer.style.fontSize = '0.85rem';
          correctAnswer.style.color = 'var(--good)';
          item.appendChild(correctAnswer);

          if (expected.length > 1) {
            const detail = document.createElement('p');
            detail.style.fontSize = '0.8rem';
            detail.style.color = 'var(--ink-soft)';
            detail.style.marginTop = '0.25rem';

            let wrongBlanks = [];
            expected.forEach(function (exp, idx) {
              const userVal = (user[idx] || '').trim().toLowerCase();
              const expVal = String(exp).trim().toLowerCase();
              if (userVal !== expVal) {
                wrongBlanks.push('Blank ' + (idx + 1) + ' (expected: ' + exp + ')');
              }
            });

            if (wrongBlanks.length > 0) {
              detail.textContent = 'Incorrect blanks: ' + wrongBlanks.join('; ');
              item.appendChild(detail);
            }
          }
        }
      } else if (q.type === 'insert') {
        const user = (userAnswers || [])[0];
        const yourAnswer = document.createElement('p');
        yourAnswer.textContent = 'Your answer: ' + (user !== undefined ? q.options[user] : '(skipped)');
        item.appendChild(yourAnswer);
        if (!gotIt) {
          const correctAnswer = document.createElement('p');
          correctAnswer.textContent = 'Correct answer: ' + q.options[q.answerIndex];
          item.appendChild(correctAnswer);
        }
      } else if (q.type === 'dragorder') {
        const yourAnswer = document.createElement('p');
        const order = Array.isArray(userAnswers) ? userAnswers : [];
        yourAnswer.textContent = 'Your order: ' + (order.length ? order.join(', ') : '(skipped)');
        item.appendChild(yourAnswer);
        if (!gotIt) {
          const correctAnswer = document.createElement('p');
          correctAnswer.textContent = 'Correct order: ' + (q.solution || []).join(', ');
          item.appendChild(correctAnswer);
        }
      } else if (q.type === 'coderunner') {
        const yourAnswer = document.createElement('p');
        const code = userAnswers || '';
        yourAnswer.textContent = 'Your code: ' + (code ? code.substring(0, 200) + (code.length > 200 ? '...' : '') : '(skipped)');
        item.appendChild(yourAnswer);
        if (!gotIt) {
          const exp = document.createElement('p');
          exp.style.color = 'var(--ink-soft)';
          exp.textContent = 'Expected output: ' + (q.expectedOutput || '(none)');
          item.appendChild(exp);
        }
      } else {
        const yourAnswer = document.createElement('p');
        if (q.type === 'visual') {
          yourAnswer.textContent = 'Your answer: ' + (userAnswers !== undefined ? 'Option ' + (['A','B','C','D','E','F'][userAnswers] || (userAnswers + 1)) : '(skipped)');
        } else if (Array.isArray(q.correctIndices) && Array.isArray(userAnswers)) {
          const labels = userAnswers.map(function (idx) { return q.options[idx]; }).filter(Boolean);
          yourAnswer.textContent = 'Your answer: ' + (labels.length ? labels.join(', ') : '(skipped)');
        } else {
          yourAnswer.textContent = 'Your answer: ' + (userAnswers !== undefined ? q.options[userAnswers] : '(skipped)');
        }
        item.appendChild(yourAnswer);

        if (!gotIt) {
          const correctAnswer = document.createElement('p');
          if (Array.isArray(q.correctIndices)) {
            const labels = q.correctIndices.map(function (idx) { return q.options[idx]; }).filter(Boolean);
            correctAnswer.textContent = 'Correct answer: ' + labels.join(', ');
          } else if (q.type === 'visual') {
            correctAnswer.textContent = 'Correct answer: Option ' + (['A','B','C','D','E','F'][q.answerIndex] || (q.answerIndex + 1));
          } else {
            correctAnswer.textContent = 'Correct answer: ' + q.options[q.answerIndex];
          }
          item.appendChild(correctAnswer);
        }

        if (q.type === 'visual') {
          const thumbs = document.createElement('div');
          thumbs.className = 'review-thumbs';
          if (userAnswers !== undefined) {
            const yourBox = document.createElement('div');
            yourBox.className = 'review-thumb';
            yourBox.appendChild(app.makeShapeCanvas(q.options[userAnswers], 56));
            const yourLabel = document.createElement('span');
            yourLabel.textContent = 'Yours';
            yourBox.appendChild(yourLabel);
            thumbs.appendChild(yourBox);
          }
          if (!gotIt) {
            const correctBox = document.createElement('div');
            correctBox.className = 'review-thumb';
            correctBox.appendChild(app.makeShapeCanvas(q.options[q.answerIndex], 56));
            const correctLabel = document.createElement('span');
            correctLabel.textContent = 'Correct';
            correctBox.appendChild(correctLabel);
            thumbs.appendChild(correctBox);
          }
          item.appendChild(thumbs);
        }
      }

      if (q.explanation) {
        const exp = document.createElement('p');
        exp.style.color = 'var(--ink-soft)';
        exp.textContent = q.explanation;
        item.appendChild(exp);
      }

      wrap.appendChild(item);
    });
  };

  app.renderProfiledResults = function (wrap, questions) {
    const traits = app.state.data.meta.traits || {};
    const tally = {};
    Object.keys(traits).forEach(function (k) { tally[k] = 0; });

    questions.forEach(function (q) {
      const idx = app.state.answers[q.id];
      if (idx === undefined) return;
      const opt = q.options[idx];
      if (opt && opt.trait && tally.hasOwnProperty(opt.trait)) tally[opt.trait]++;
    });

    const answered = Object.values(tally).reduce(function (a, b) { return a + b; }, 0) || 1;
    const sortedKeys = Object.keys(tally).sort(function (a, b) { return tally[b] - tally[a]; });
    const topKey = sortedKeys[0];

    const hero = document.createElement('div');
    hero.className = 'results-hero';
    hero.innerHTML =
      '<p class="settings-hint" style="margin:0;padding:1rem 0;">' + app.sectionTitle() + '</p>' +
      '<p class="results-score" style="font-size:2.2rem;">' + (traits[topKey] || topKey) + '</p>' +
      '<p class="results-sub">Your strongest tendency in this attempt</p>';
    wrap.appendChild(hero);

    const heading = document.createElement('h2');
    heading.textContent = 'Trait breakdown';
    wrap.appendChild(heading);

    sortedKeys.forEach(function (key) {
      const pct = Math.round((tally[key] / answered) * 100);
      const row = document.createElement('div');
      row.className = 'trait-row';
      row.innerHTML =
        '<div class="trait-row-head"><span>' + (traits[key] || key) + '</span><span>' + pct + '%</span></div>' +
        '<div class="trait-track"><div class="trait-fill" style="width:' + pct + '%"></div></div>';
      wrap.appendChild(row);
    });
  };

  app.checkQuestionCorrect = function (q) {
    const userAnswers = app.state.answers[q.id];
    if (q.type === 'pyramid') {
      return app.checkPyramidAnswer(q, userAnswers);
    } else if (q.type === 'typing') {
      const user = userAnswers || [];
      const expected = q.blanks || [];
      return user.length === expected.length && expected.every(function (v, i) {
        return String(user[i]).trim().toLowerCase() === String(v).trim().toLowerCase();
      });
    } else if (q.type === 'dragorder') {
      return JSON.stringify(userAnswers || []) === JSON.stringify(q.solution || []);
    } else if (q.type === 'coderunner') {
      return app.simulateCSharp(userAnswers || '', q).ok;
    } else if (q.type === 'insert') {
      return (userAnswers || [])[0] === q.answerIndex;
    } else if (Array.isArray(q.correctIndices)) {
      const user = (userAnswers || []).sort(function (a, b) { return a - b; });
      const expected = q.correctIndices.slice().sort(function (a, b) { return a - b; });
      return JSON.stringify(user) === JSON.stringify(expected);
    }
    return userAnswers === q.answerIndex;
  };

  app.downloadModuleCertificate = function (section, level) {
    var session = app.getQuizSession(section, level);
    if (!session) {
      if (app.speak) app.speak('Certificate data not available yet. Please complete the quiz first.');
      return;
    }
    var saved = {
      data: app.state.data,
      section: app.state.section,
      level: app.state.level,
      score: app.state.score,
      correct: app.state.correct,
      total: app.state.total,
      passed: app.state.passed,
      answers: app.state.answers,
      quizVariant: app.state.quizVariant,
      year: app.state.year,
    };
    app.state.data = session.data;
    app.state.section = section;
    app.state.level = level;
    app.state.score = session.score;
    app.state.correct = session.correct;
    app.state.total = session.total;
    app.state.passed = session.score >= (app.config.PASS_THRESHOLD || 80);
    app.state.answers = session.answers;
    app.state.quizVariant = session.variant || 'A';

    app.generateResultsPDF();

    app.state.data = saved.data;
    app.state.section = saved.section;
    app.state.level = saved.level;
    app.state.score = saved.score;
    app.state.correct = saved.correct;
    app.state.total = saved.total;
    app.state.passed = saved.passed;
    app.state.answers = saved.answers;
    app.state.quizVariant = saved.quizVariant;
    app.state.year = saved.year;
  };

  app.generateResultsPDF = function () {
    var _jspdf = window.jspdf;
    if (!_jspdf || !_jspdf.jsPDF) {
      if (app.speak) app.speak('PDF download is not available at the moment.');
      return;
    }
    var jsPDF = _jspdf.jsPDF;
    var doc = new jsPDF({ unit: 'pt', format: 'a4' });
    var lineHeight = 14;
    var margin = 56;
    var y = 0;
    var questions = app.state.data.questions || [];
    var moduleId = app.state.section || '';
    var moduleMeta = app.config.MODULES ? app.config.MODULES.find(function (m) {
      return m.id === moduleId;
    }) : null;
    var moduleTitle = (app.state.data.meta && app.state.data.meta.title) || app.sectionTitle() || moduleId;
    var moduleMark = (moduleMeta && moduleMeta.module) || '';
    var userEmail = (app.state.user && app.state.user.email) || '';
    var userName = userEmail ? userEmail.split('@')[0] : '';
    var levelLabel = '';
    var levelObj = (app.config.LEVELS || []).find(function (l) { return l.id === app.state.level; });
    if (levelObj) levelLabel = levelObj.label;
    var yearLabel = app.state.year === 'y1' ? 'Year 1' : app.state.year === 'y2' ? 'Year 2' : '';
    var isPassed = app.state.passed || false;
    var scorePct = app.state.score || 0;
    var correct = app.state.correct || 0;
    var total = app.state.total || questions.length;
    var attemptDate = new Date();
    var dateStr = attemptDate.toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric' });
    var statusColor = isPassed ? [46, 130, 91] : [198, 75, 75];

    var drawHeader = function (label) {
      doc.setFillColor(30, 35, 64);
      doc.rect(0, 0, 595, 40);
      doc.setTextColor(255, 255, 255);
      doc.setFontSize(14);
      doc.setFont('helvetica', 'bold');
      doc.text('ESC&G — Induction Quiz', 24, 26);
      doc.setFontSize(10);
      doc.setFont('helvetica', 'normal');
      doc.text(label || 'Module Result', 570, 26, { align: 'right' });
    };

    var drawFooter = function (pageNum) {
      doc.setDrawColor(225, 225, 238);
      doc.setLineWidth(0.5);
      doc.line(40, 800, 555, 800);
      doc.setTextColor(91, 95, 122);
      doc.setFontSize(8);
      doc.setFont('helvetica', 'normal');
      doc.text('Page ' + pageNum, 297, 820, { align: 'center' });
      doc.text('This is a practice result, not an official test.', 297, 835, { align: 'center' });
    };

    var drawCertBorder = function () {
      doc.setDrawColor(30, 35, 64);
      doc.setLineWidth(2);
      doc.rect(20, 20, 555, 752);
      doc.setDrawColor(181, 121, 42);
      doc.setLineWidth(4);
      doc.rect(12, 12, 571, 768);
    };

    var renderQuestionReview = function (startY, startPage) {
      if (startY === undefined || startY === null) startY = margin;
      var y = startY;
      var pageNum = startPage || 1;

      doc.setTextColor(30, 35, 64);
      doc.setFontSize(16);
      doc.setFont('helvetica', 'bold');
      doc.text('Question Review', margin, y);
      y += 24;

      questions.forEach(function (q, i) {
        if (y > 760) {
          drawFooter(pageNum);
          doc.addPage();
          pageNum++;
          drawHeader('Module Result');
          y = 60;
          doc.setTextColor(30, 35, 64);
          doc.setFontSize(16);
          doc.setFont('helvetica', 'bold');
          doc.text('Question Review (continued)', margin, y);
          y += 24;
        }

        var gotIt = app.checkQuestionCorrect(q);
        doc.setFontSize(11);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(30, 35, 64);
        var qText = (i + 1) + '. ' + q.prompt;
        var qLines = doc.splitTextToSize(qText, 480);
        doc.text(qLines, margin, y);
        y += qLines.length * (lineHeight) + 4;

        doc.setFont('helvetica', 'normal');
        doc.setTextColor(91, 95, 122);
        doc.setFontSize(10);

        var yourAnswer = '(no answer)';
        if (q.type === 'typing') {
          var u = (app.state.answers[q.id] || []);
          var exp = q.blanks || [];
          yourAnswer = u.length ? u.join(', ') : '(skipped)';
          if (!gotIt && exp.length) {
            yourAnswer += ' — expected: ' + exp.join(', ');
          }
        } else if (q.type === 'insert' || (q.type === 'visual')) {
          var idx = app.state.answers[q.id];
          yourAnswer = idx !== undefined ? (q.options ? q.options[idx] : ('Option ' + (idx + 1))) : '(skipped)';
          if (q.type !== 'visual' && !gotIt && q.options && q.options[q.answerIndex]) {
            yourAnswer += ' — expected: ' + q.options[q.answerIndex];
          }
        } else if (q.type === 'dragorder') {
          var order = app.state.answers[q.id] || [];
          yourAnswer = order.length ? order.join(', ') : '(skipped)';
          if (!gotIt && q.solution) {
            yourAnswer += ' — expected: ' + q.solution.join(', ');
          }
        } else if (q.type === 'coderunner') {
          yourAnswer = (app.state.answers[q.id] || '(skipped)');
          if (!gotIt && q.expectedOutput) {
            yourAnswer += ' — expected output: ' + q.expectedOutput;
          }
        } else if (q.type === 'pyramid') {
          yourAnswer = gotIt ? 'Correct' : 'Incorrect — see explanation';
        } else {
          var uIdx = app.state.answers[q.id];
          yourAnswer = uIdx !== undefined ? (q.options ? q.options[uIdx] : uIdx) : '(skipped)';
          if (!gotIt && q.options && q.options[q.answerIndex]) {
            yourAnswer += ' — expected: ' + q.options[q.answerIndex];
          }
        }

        if (gotIt) {
          doc.setTextColor(46, 130, 91);
        } else {
          doc.setTextColor(198, 75, 75);
        }
        var tag = gotIt ? '\u2713 Correct' : '\u2717 Incorrect';
        doc.text(tag + ' — ' + yourAnswer, margin, y);
        y += lineHeight + 2;

        if (q.explanation) {
          doc.setTextColor(91, 95, 122);
          doc.setFontSize(9);
          var expLines = doc.splitTextToSize('Note: ' + q.explanation, 480);
          doc.text(expLines, margin, y);
          y += expLines.length * (lineHeight - 2) + 6;
        }
        y += 4;
      });

      drawFooter(pageNum);
    };

    if (isPassed) {
      drawCertBorder();
      drawHeader('Certificate');

      if (app.config && app.config.CERT_LOGO_DATAURL) {
        doc.addImage(app.config.CERT_LOGO_DATAURL, 'PNG', 205, 60, 90, 45);
      }

      y = 130;

      doc.setTextColor(30, 35, 64);
      doc.setFontSize(24);
      doc.setFont('helvetica', 'bold');
      doc.text('Certificate of Completion', 297, y, { align: 'center' });
      y += 40;

      doc.setFontSize(12);
      doc.setFont('helvetica', 'normal');
      doc.text('This is to certify that', 297, y, { align: 'center' });
      y += 30;

      doc.setFontSize(22);
      doc.setFont('helvetica', 'bold');
      doc.setTextColor(30, 35, 64);
      if (userName) {
        var nameLines = doc.splitTextToSize(userName, 480);
        doc.text(nameLines, 297, y, { align: 'center' });
        y += nameLines.length * 28 + 10;
      } else {
        doc.setDrawColor(30, 35, 64);
        doc.setLineWidth(1);
        doc.line(170, y + 10, 424, y + 10);
        doc.setTextColor(150, 155, 172);
        doc.setFontSize(9);
        doc.setFont('helvetica', 'italic');
        doc.text('(print name here)', 297, y + 24, { align: 'center' });
        y += 40;
      }

      doc.setFontSize(12);
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(91, 95, 122);
      var certSub = 'has successfully completed the';
      doc.text(certSub, 297, y, { align: 'center' });
      y += 26;

      doc.setFontSize(18);
      doc.setFont('helvetica', 'bold');
      doc.setTextColor(30, 35, 64);
      var titleLines = doc.splitTextToSize(moduleTitle, 480);
      doc.text(titleLines, 297, y, { align: 'center' });
      y += titleLines.length * 22 + 14;

      doc.setFontSize(12);
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(91, 95, 122);
      var certDetail = 'Module ' + (moduleMark || '—') + ' \u2022 ' + levelLabel + ' ' + yearLabel;
      doc.text(certDetail, 297, y, { align: 'center' });
      y += 26;

      doc.setTextColor(91, 95, 122);
      doc.text('Score: ' + scorePct + '%  (' + correct + '/' + total + ' correct)', 297, y, { align: 'center' });
      y += 26;

      doc.setTextColor(30, 35, 64);
      doc.text('Date: ' + dateStr, 297, y, { align: 'center' });
      y += 40;

      doc.setDrawColor(181, 121, 42);
      doc.setLineWidth(1);
      doc.line(180, y, 414, y);
      y += 24;

      doc.setFontSize(11);
      doc.setTextColor(91, 95, 122);
      doc.text('College Programme Leader', 297, y, { align: 'center' });
      y += 24;

      doc.setFontSize(10);
      doc.setTextColor(91, 95, 122);
      doc.text('Student: ' + userEmail, 297, y, { align: 'center' });

      drawFooter(1);

      if (questions.length > 0) {
        doc.addPage();
        drawHeader('Module Result');
        renderQuestionReview(margin, 2);
      }

      doc.save('induction-certificate-' + (moduleMark || moduleId || 'module') + '-' + attemptDate.getFullYear() + '.pdf');
    } else {
      drawHeader('Module Result');
      y = 60;

      var titleLines2 = doc.splitTextToSize(moduleTitle, 480);
      doc.setFontSize(20);
      doc.setFont('helvetica', 'bold');
      doc.setTextColor(30, 35, 64);
      doc.text(titleLines2, margin, y);
      y += titleLines2.length * (lineHeight + 2) + 8;

      doc.setFontSize(13);
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(91, 95, 122);
      var detailLines = [
        ['Module', moduleMark || '\u2014'],
        ['Level', levelLabel || '\u2014'],
        ['Year', yearLabel || '\u2014'],
        ['Email', userEmail || '(not signed in)']
      ];
      doc.setTextColor(30, 35, 64);
      detailLines.forEach(function (row) {
        doc.setFont('helvetica', 'bold');
        doc.text(row[0], margin, y);
        doc.setFont('helvetica', 'normal');
        doc.text(row[1], margin + 70, y);
        y += lineHeight;
      });
      y += 6;

      doc.setDrawColor(225, 225, 238);
      doc.setLineWidth(0.5);
      doc.line(margin, y, 555, y);
      y += 14;

      doc.setFontSize(26);
      doc.setFont('helvetica', 'bold');
      doc.setTextColor(statusColor[0], statusColor[1], statusColor[2]);
      doc.text('Needs Review', margin, y);
      y += 6;

      doc.setFontSize(32);
      doc.setTextColor(30, 35, 64);
      doc.text(scorePct + '%', margin, y);
      y += 22;

      doc.setFontSize(12);
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(91, 95, 122);
      doc.text(correct + ' of ' + total + ' correct \u2014 ' + dateStr, margin, y);
      y += 22;

      if (questions.length > 0) {
        renderQuestionReview(y, 1);
      } else {
        drawFooter(1);
      }

      doc.save('induction-result-' + (moduleMark || moduleId || 'result') + '-' + attemptDate.getFullYear() + '.pdf');
    }
  };
})();
