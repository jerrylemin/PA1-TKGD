const fifaEvents = {
  pending: {
    title: "Mexico City · Estadio Azteca",
    subtitle: "Group stage · Match 18 · 19:00 local time",
    status: "Pending",
    pill: "Awaiting confirmation",
    icon: "pending",
    meaning: "FIFA is confirming the allocation for your Mexico City match. Your place is not lost, and no action is required from you right now.",
    next: "FIFA confirms the allocation.",
    nextMeta: "Owner: FIFA · Expected timing: next confirmation update",
    action: "No action needed",
    eventLabel: "Pending · FIFA confirmation"
  },
  confirmed: {
    title: "Toronto · BMO Field",
    subtitle: "Group stage · Match 27 · 15:00 local time",
    status: "Confirmed",
    pill: "Ticket ready",
    icon: "confirmed",
    meaning: "Your ticket allocation is confirmed for Toronto. You can review the order, view ticket details, or save the event to your calendar.",
    next: "Your ticket is ready for event day.",
    nextMeta: "Owner: You · Expected timing: available now",
    action: "Ready for event day",
    eventLabel: "Confirmed · ticket ready"
  }
};

const fifaState = {
  selected: "pending",
  explanationOpen: false,
  calendarAdded: false,
  refreshing: false,
  error: false,
  returnNotice: false,
  lastUpdated: "2 min ago"
};

const chessState = {
  phase: "intro",
  attempt: null,
  selectedSquare: null,
  explanationVariant: "primary",
  practiceDone: false
};

const chessScenario = Object.freeze({
  id: "queen-safety-before-activity",
  moveNumber: 12,
  sideToMove: "White",
  gameLabel: "Minh's rapid game",
  startPosition: Object.freeze({
    a8: "r", b8: "", c8: "b", d8: "q", e8: "k", f8: "", g8: "", h8: "r",
    a7: "p", b7: "p", c7: "p", d7: "p", e7: "", f7: "p", g7: "p", h7: "p",
    a6: "", b6: "", c6: "", d6: "", e6: "", f6: "n", g6: "", h6: "",
    a5: "", b5: "", c5: "", d5: "", e5: "p", f5: "", g5: "", h5: "",
    a4: "", b4: "", c4: "B", d4: "", e4: "", f4: "", g4: "", h4: "",
    a3: "", b3: "", c3: "", d3: "", e3: "", f3: "", g3: "", h3: "",
    a2: "P", b2: "P", c2: "P", d2: "P", e2: "", f2: "P", g2: "P", h2: "P",
    a1: "R", b1: "N", c1: "", d1: "Q", e1: "K", f1: "", g1: "N", h1: "R"
  }),
  mistake: Object.freeze({
    notation: "Qh5",
    source: "d1",
    destination: "h5",
    label: "Move the queen to h5",
    summary: "The queen steps onto a square attacked by the knight on f6."
  }),
  mistakeConsequence: Object.freeze({
    notation: "Nxh5",
    source: "f6",
    destination: "h5",
    summary: "Black can capture the queen immediately with the knight."
  }),
  betterMove: Object.freeze({
    notation: "Qe2",
    source: "d1",
    destination: "e2",
    label: "Move the queen to e2",
    summary: "Move the queen to a safe square before looking for activity."
  }),
  explanation: Object.freeze({
    primary: "Qh5 looks active, but the black knight on f6 attacks h5. Black's next move is Nxh5, which wins the queen. Qe2 keeps the queen safe and addresses the same threat.",
    alternate: "Before choosing an active square, check whether an opposing piece can capture it. The knight attacks h5, so the queen needs a square outside that attack."
  }),
  reviewPrompt: "Which queen move avoids the knight's attack and keeps the queen on the board?",
  practicePosition: Object.freeze({
    a8: "r", b8: "", c8: "b", d8: "q", e8: "k", f8: "", g8: "", h8: "r",
    a7: "p", b7: "p", c7: "p", d7: "p", e7: "", f7: "p", g7: "p", h7: "p",
    a6: "", b6: "", c6: "", d6: "", e6: "", f6: "", g6: "", h6: "",
    a5: "", b5: "", c5: "", d5: "", e5: "p", f5: "", g5: "", h5: "",
    a4: "", b4: "", c4: "B", d4: "", e4: "", f4: "", g4: "b", h4: "",
    a3: "", b3: "", c3: "", d3: "", e3: "", f3: "", g3: "", h3: "",
    a2: "P", b2: "P", c2: "P", d2: "", e2: "", f2: "P", g2: "P", h2: "P",
    a1: "R", b1: "N", c1: "", d1: "Q", e1: "K", f1: "", g1: "N", h1: "R"
  }),
  practiceGoal: "Find a safe queen square when the bishop is already attacking the queen's starting line.",
  practiceCorrectMove: Object.freeze({
    notation: "Qd3",
    source: "d1",
    destination: "d3",
    summary: "Qd3 steps away from the bishop's diagonal and keeps the queen safe."
  })
});

const chessPieces = {
  K: "♔", Q: "♕", R: "♖", B: "♗", N: "♘", P: "♙",
  k: "♚", q: "♛", r: "♜", b: "♝", n: "♞", p: "♟"
};

const modalRoot = document.getElementById("modalRoot");
const toastRoot = document.getElementById("toastRoot");
let modalReturnFocus = null;

function isStudyMode() {
  return new URLSearchParams(window.location.search).get("mode") === "study";
}

function studyProduct() {
  const product = new URLSearchParams(window.location.search).get("product");
  return ["fifa", "chess"].includes(product) ? product : "fifa";
}

function applyMode() {
  const study = isStudyMode();
  document.body.classList.toggle("study-mode", study);
  document.body.classList.toggle("presenter-mode", !study);
  if (study) removeStudyChrome();
}

function removeStudyChrome() {
  if (!isStudyMode()) return;
  document.querySelectorAll(".lab-header, .home-view, .study-researcher-chrome").forEach((element) => element.remove());
}

function currentRoute() {
  const route = window.location.hash.replace("#", "");
  if (isStudyMode()) return ["fifa", "chess"].includes(route) ? route : studyProduct();
  return ["home", "fifa", "chess"].includes(route) ? route : "home";
}

function navigate(route) {
  if (isStudyMode() && route === "home") route = studyProduct();
  if (window.location.hash === `#${route}`) {
    setRoute(route);
  } else {
    window.location.hash = route;
  }
}

function setRoute(route) {
  applyMode();
  if (isStudyMode() && route === "home") route = studyProduct();
  closeModal();
  document.querySelector(".lab-header")?.toggleAttribute("hidden", route !== "home");
  document.querySelectorAll(".lab-view").forEach((view) => {
    view.hidden = view.id !== `${route}View`;
  });
  document.querySelectorAll(".lab-nav-item").forEach((item) => {
    item.classList.toggle("is-active", item.dataset.route === route);
  });
  if (route === "fifa") renderFifa();
  if (route === "chess") renderChess();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showToast(title, detail) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<span class="toast-mark">✓</span><div><strong>${title}</strong><span>${detail}</span></div>`;
  toastRoot.appendChild(toast);
  window.setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(6px)";
    toast.style.transition = "opacity 180ms ease, transform 180ms ease";
    window.setTimeout(() => toast.remove(), 190);
  }, 3400);
}

function openModal({ theme = "fifa", surface = "modal", kicker, title, copy = "", body = "", actions = "" }) {
  modalReturnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
  modalRoot.hidden = false;
  modalRoot.className = `modal-root ${surface === "drawer" ? "drawer-root" : ""}`.trim();
  modalRoot.innerHTML = `
    <div class="modal-card ${theme === "chess" ? "modal-chess" : ""}" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
      <div class="modal-top">
        <div><span class="modal-kicker">${kicker}</span><h2 id="modalTitle">${title}</h2></div>
        <button type="button" class="modal-close" data-action="close-modal" aria-label="Close dialog">×</button>
      </div>
      ${copy ? `<p>${copy}</p>` : ""}
      ${body}
      ${actions ? `<div class="modal-actions">${actions}</div>` : ""}
    </div>`;
  document.body.classList.add("modal-open");
  window.requestAnimationFrame(() => modalRoot.querySelector(".modal-close")?.focus());
}

function closeModal() {
  if (modalRoot.hidden) return;
  const returnFocus = modalReturnFocus;
  modalReturnFocus = null;
  modalRoot.hidden = true;
  modalRoot.innerHTML = "";
  modalRoot.className = "modal-root";
  document.body.classList.remove("modal-open");
  if (returnFocus?.isConnected) window.requestAnimationFrame(() => returnFocus.focus());
}

function renderFifa() {
  const event = fifaEvents[fifaState.selected];
  const isConfirmed = fifaState.selected === "confirmed";
  const calendarSaved = isConfirmed && fifaState.calendarAdded;
  const eventDetails = isConfirmed
    ? { title: "Toronto · BMO Field", meta: "Group stage · Match 27 · 21 Jun 2026 · 15:00 local time" }
    : { title: "Mexico City · Estadio Azteca", meta: "Group stage · Match 18 · 17 Jun 2026 · 19:00 local time" };
  const statusHeading = document.getElementById("fifaStatusHeading");
  const statusPill = document.getElementById("fifaStatusPill");
  const meaning = document.getElementById("fifaStatusMeaning");
  const next = document.getElementById("fifaNextStep");
  const nextMeta = document.getElementById("fifaNextMeta");
  const actionCopy = document.getElementById("fifaActionCopy");
  const lastUpdated = document.getElementById("fifaLastUpdated");
  const footFreshness = document.getElementById("fifaFootFreshness");
  const owner = document.getElementById("fifaOwner");
  const freshness = document.getElementById("fifaFreshness");
  const selectedIcon = document.getElementById("fifaStatusIcon");

  if (!statusHeading || fifaState.refreshing) {
    document.querySelector(".refresh-control")?.classList.toggle("is-refreshing", fifaState.refreshing);
    return;
  }

  statusHeading.textContent = event.status;
  statusPill.textContent = event.pill;
  statusPill.className = `status-pill status-pill-${event.icon}`;
  selectedIcon.className = `status-icon status-icon-${event.icon}`;
  selectedIcon.textContent = isConfirmed ? "✓" : "●";
  meaning.textContent = event.meaning;
  next.textContent = event.next;
  nextMeta.textContent = isConfirmed ? "Expected timing: available now" : "Expected timing: next confirmation update";
  actionCopy.textContent = event.action;
  lastUpdated.textContent = fifaState.lastUpdated;
  footFreshness.textContent = `Updated ${fifaState.lastUpdated}`;
  if (owner) owner.textContent = isConfirmed ? "You" : "FIFA";
  if (freshness) freshness.textContent = `Updated ${fifaState.lastUpdated}`;
  const selectedTitle = document.getElementById("selectedEventTitle");
  const selectedMeta = document.getElementById("selectedEventMeta");
  if (selectedTitle) selectedTitle.textContent = eventDetails.title;
  if (selectedMeta) selectedMeta.textContent = eventDetails.meta;
  document.getElementById("fifaExplanation").hidden = !fifaState.explanationOpen;
  const explanationButton = document.querySelector('[data-action="fifa-toggle-explanation"]');
  if (explanationButton) explanationButton.setAttribute("aria-expanded", String(fifaState.explanationOpen));
  document.getElementById("fifaAlert").hidden = !fifaState.error;
  document.getElementById("fifaReturnNotice").hidden = !fifaState.returnNotice;
  document.querySelector(".refresh-control")?.classList.toggle("is-refreshing", fifaState.refreshing);
  const calendarAction = document.querySelector('[data-action="fifa-calendar"]');
  if (calendarAction) {
    calendarAction.disabled = !isConfirmed;
    calendarAction.setAttribute("aria-disabled", String(!isConfirmed));
  }
  document.getElementById("calendarActionTitle").textContent = calendarSaved ? "Calendar saved" : "Add to Calendar";
  document.getElementById("calendarActionCopy").textContent = calendarSaved ? "Toronto event saved" : isConfirmed ? "Save this confirmed event" : "Available after confirmation";
  document.querySelectorAll("[data-action='fifa-select-event']").forEach((row) => {
    row.classList.toggle("is-selected", row.dataset.event === fifaState.selected);
    row.setAttribute("aria-pressed", String(row.dataset.event === fifaState.selected));
  });
  const currentTimelineStep = isConfirmed ? 4 : 2;
  document.querySelectorAll("[data-fifa-step]").forEach((step) => {
    const stepNumber = Number(step.dataset.fifaStep);
    const status = step.querySelector("[data-step-status]");
    step.classList.toggle("is-done", stepNumber < currentTimelineStep);
    step.classList.toggle("is-current", stepNumber === currentTimelineStep);
    if (stepNumber === currentTimelineStep) step.setAttribute("aria-current", "step");
    else step.removeAttribute("aria-current");
    if (status) status.textContent = stepNumber < currentTimelineStep ? "Completed" : stepNumber === currentTimelineStep ? (isConfirmed ? "Available now" : "Current") : "Upcoming";
  });
  const primaryAction = isConfirmed ? "tickets" : "order";
  document.querySelectorAll("[data-fifa-primary]").forEach((action) => {
    action.classList.toggle("is-primary", action.dataset.fifaPrimary === primaryAction);
  });
}

function applyChessMove(position, move) {
  const next = { ...position };
  const piece = next[move.source] || "";
  next[move.source] = "";
  next[move.destination] = piece;
  return next;
}

function chessPositionForPhase(phase) {
  if (phase === "practice") {
    return chessState.practiceDone || chessState.attempt === "correct"
      ? applyChessMove(chessScenario.practicePosition, chessScenario.practiceCorrectMove)
      : chessScenario.practicePosition;
  }
  return chessState.attempt === "correct"
    ? applyChessMove(chessScenario.startPosition, chessScenario.betterMove)
    : chessScenario.startPosition;
}

function chessMoveForPhase(phase) {
  return phase === "practice" ? chessScenario.practiceCorrectMove : chessScenario.betterMove;
}

function boardMarkup({ phase = "mistake", interactive = false } = {}) {
  const position = chessPositionForPhase(phase);
  const mistakeSquare = chessScenario.mistake.destination;
  const betterSquare = chessScenario.betterMove.destination;
  const selectedSquare = chessState.selectedSquare;
  const highlights = phase === "mistake" ? [mistakeSquare] : phase === "better" ? [betterSquare] : [];
  const files = ["a", "b", "c", "d", "e", "f", "g", "h"];
  let squares = "";
  for (let rank = 8; rank >= 1; rank -= 1) {
    for (const file of files) {
      const coord = `${file}${rank}`;
      const piece = position[coord] || "";
      const isLight = (files.indexOf(file) + rank) % 2 === 0;
      const classes = ["board-square", isLight ? "light" : "dark"];
      if (highlights.includes(coord)) classes.push(phase === "mistake" ? "is-highlight" : "is-better");
      if (selectedSquare === coord) classes.push("is-source-selected");
      if (chessState.attempt === "correct" && coord === chessMoveForPhase(phase).destination) classes.push("is-selected");
      if (interactive) classes.push("is-clickable");
      const pieceClass = piece && piece === piece.toUpperCase() ? "piece-white" : "piece-black";
      const pieceMarkup = piece ? `<span class="piece ${pieceClass}">${chessPieces[piece]}</span>` : "";
      const ariaLabel = `${coord}${piece ? ` ${pieceClass === "piece-white" ? "white" : "black"} piece` : " empty"}`;
      squares += interactive
        ? `<button type="button" class="${classes.join(" ")}" data-action="chess-square" data-square="${coord}" data-coord="${coord}" aria-label="${ariaLabel}">${pieceMarkup}</button>`
        : `<span class="${classes.join(" ")}" data-coord="${coord}" role="img" aria-label="${ariaLabel}">${pieceMarkup}</span>`;
    }
  }
  const label = phase === "intro"
    ? "Completed game position"
    : phase === "mistake"
      ? `Game move ${chessScenario.moveNumber}: ${chessScenario.mistake.notation}`
      : phase === "better"
        ? `Better move: ${chessScenario.betterMove.notation}`
        : "Interactive chess board. Select a source square and a destination.";
  return `<div class="chess-board-wrap"><div class="chess-board" role="grid" aria-label="${label}">${squares}</div></div>`;
}

function explanationDetail() {
  if (chessState.explanationVariant !== "alternate") return "";
  return `<div id="chessExplanationDetail" class="review-plain explanation-detail" role="status"><span class="mini-label">ANOTHER WAY TO SEE IT</span><p>${chessScenario.explanation.alternate}</p></div>`;
}

function reviewPanelHeader(step, progress) {
  return `<div class="review-panel-header"><div><span class="review-panel-kicker">BEGINNER REVIEW</span><h2>Beginner Review</h2></div><span class="review-panel-step">STEP ${step} OF 3</span></div><div class="review-panel-progress" aria-label="Review progress"><span style="width:${progress}%"></span></div>`;
}

function redesignedBoardPanel({ phase = "mistake", interactive = false } = {}) {
  const legend = phase === "mistake"
    ? `<span><i class="legend-swatch legend-mistake"></i>reviewed move</span>`
    : phase === "better"
      ? `<span><i class="legend-swatch legend-better"></i>better move</span>`
      : interactive
        ? `<span><i class="legend-swatch legend-selected"></i>selected square</span>`
        : "";
  const story = phase === "intro"
    ? `<div class="move-story"><strong>Completed game position</strong><span>Start the review when you are ready to inspect the learning moment.</span></div>`
    : phase === "mistake"
      ? `<div class="move-story"><strong>${chessScenario.moveNumber}. ${chessScenario.mistake.notation}</strong><span>${chessScenario.mistake.summary}</span></div>`
      : phase === "better"
        ? `<div class="move-story"><strong>${chessScenario.betterMove.notation}</strong><span>${chessScenario.betterMove.summary}</span></div>`
        : `<div class="move-story"><strong>${interactive ? "Your move" : "Move accepted"}</strong><span>${interactive ? "Select the piece first, then select its destination." : "The board shows the resulting position."}</span></div>`;
  return `<div class="board-panel">${boardMarkup({ phase, interactive })}<div class="board-legend">${legend}</div>${story}</div>`;
}

function explanationButton(label, className = "chess-text-link") {
  const expanded = chessState.explanationVariant === "alternate";
  return `<button type="button" class="${className}" data-action="chess-explain" aria-expanded="${expanded}" aria-controls="chessExplanationDetail">${label}</button>`;
}

function renderChess() {
  if (isStudyMode()) queueMicrotask(removeStudyChrome);
  const stage = document.getElementById("chessStage");
  const boardFrame = document.getElementById("chessBoardFrame");
  if (!stage || !boardFrame) return;

  const { moveNumber, sideToMove, gameLabel, mistake, mistakeConsequence, betterMove, practiceGoal, practiceCorrectMove } = chessScenario;
  const route = chessState.phase === "intro" || chessState.phase === "mistake" ? 1 : ["better", "trial"].includes(chessState.phase) ? 2 : 3;
  const progress = route === 1 ? 33 : route === 2 ? 66 : chessState.phase === "complete" ? 100 : 86;
  const headerStatus = document.getElementById("chessHeaderStatus");
  if (headerStatus) {
    headerStatus.textContent = chessState.phase === "complete"
      ? "Review complete · All steps done"
      : chessState.phase === "practice"
        ? "Review in progress · Step 3 of 3"
        : ["better", "trial"].includes(chessState.phase)
          ? "Review in progress · Step 2 of 3"
          : "Game completed · Step 1 of 3";
  }

  const boardPhase = chessState.phase === "complete" ? "practice" : chessState.phase;
  const boardInteractive = ["trial", "practice"].includes(chessState.phase) && !chessState.practiceDone;
  boardFrame.innerHTML = redesignedBoardPanel({ phase: boardPhase, interactive: boardInteractive });

  const boardArea = document.getElementById("chessBoardArea");
  if (boardArea) {
    boardArea.dataset.reviewPhase = chessState.phase;
    boardArea.classList.toggle("has-board-error", ["wrong", "wrong-source"].includes(chessState.attempt));
  }
  const boardFeedback = document.getElementById("chessBoardFeedback");
  const feedback = chessState.attempt === "correct"
    ? "Move accepted · the idea is visible in the resulting position."
    : chessState.attempt === "wrong-source"
      ? "Select the queen first."
      : chessState.attempt === "wrong"
        ? "That destination is still unsafe."
        : "";
  if (boardFeedback) {
    boardFeedback.hidden = !feedback;
    boardFeedback.className = `board-feedback-overlay ${chessState.attempt === "wrong" || chessState.attempt === "wrong-source" ? "is-error" : ""}`.trim();
    boardFeedback.textContent = feedback;
  }

  let body = "";
  let footer = "";
  if (chessState.phase === "intro") {
    body = `<div class="review-kicker">START HERE · BEGINNER REVIEW</div><h3>Start with the most important learning moment.</h3><p>We reduced the review to one useful moment. Start when you are ready to understand the position, then try the idea yourself.</p><div class="review-game-line"><span>GAME</span><strong>${gameLabel}</strong><span>· Move ${moveNumber} · ${sideToMove} to move</span></div>`;
    footer = `<button type="button" class="primary-chess-button" data-action="chess-start-review">Start Beginner Review <span aria-hidden="true">→</span></button><button type="button" class="ghost-chess-button study-researcher-chrome" data-action="chess-open-advanced">Preview Full Analysis</button>`;
  } else if (chessState.phase === "mistake") {
    body = `<div class="review-kicker">MISTAKE · GAME MOVE ${moveNumber}</div><div class="review-callout"><strong>${mistake.notation}</strong><p>${mistake.summary}</p></div><div class="review-plain"><span class="mini-label">WHAT HAPPENS NEXT</span><p>${mistakeConsequence.notation} can capture the queen immediately. The useful question is whether the destination is defended.</p></div><div class="move-readout"><div><span>YOU PLAYED</span><strong>${mistake.notation}</strong><small>${mistake.label}</small></div><div><span>CONSEQUENCE</span><strong>${mistakeConsequence.notation}</strong><small>${mistakeConsequence.summary}</small></div></div>${explanationDetail()}`;
    footer = `<button type="button" class="primary-chess-button" data-action="chess-reveal-better">Show the better move <span aria-hidden="true">→</span></button>${explanationButton("Explain another way", "ghost-chess-button")}<div class="review-text-links"><button type="button" class="chess-text-link" data-action="chess-practice">Practice this idea</button><button type="button" class="chess-text-link" data-action="chess-review-another">Review another moment</button></div>`;
  } else if (chessState.phase === "better") {
    body = `<div class="review-kicker">BETTER MOVE · CHECK THE ATTACK</div><div class="review-callout is-better"><strong>${betterMove.notation}</strong><p>${betterMove.summary} The highlighted square is the safe destination for the queen.</p></div><div class="review-plain"><span class="mini-label">IN PLAIN LANGUAGE</span><p><strong>${betterMove.notation} keeps the queen safe.</strong> It answers the real problem in this position: the knight controls the tempting square.</p></div><div class="review-feedback"><span class="review-feedback-mark">→</span><span><strong>Read the move on the board.</strong>The green highlight shows the safe destination before you try it.</span></div>${explanationDetail()}`;
    footer = `<button type="button" class="primary-chess-button" data-action="chess-try-move">Try this move <span aria-hidden="true">→</span></button><button type="button" class="secondary-chess-button" data-action="chess-practice">Practice this idea</button><div class="review-text-links">${explanationButton("Need more help")}<button type="button" class="chess-text-link" data-action="chess-back-to-mistake">Back to the mistake</button></div>`;
  } else if (chessState.phase === "trial") {
    const trialFeedback = chessState.attempt === "correct"
      ? `<div class="review-feedback"><span class="review-feedback-mark">✓</span><span><strong>That move keeps the queen safe.</strong>You found the idea behind ${betterMove.notation}. The resulting position is shown on the board.</span></div>`
      : chessState.attempt === "wrong-source"
        ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>Start with the queen involved in the review.</strong>Select its source square, then choose where it should go.</span></div>`
        : chessState.attempt === "wrong"
          ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>That destination does not solve the problem.</strong>The queen is still exposed there. Select it again and try a safer square.</span></div>`
          : `<div class="review-plain"><span class="mini-label">TRY THE IDEA</span><p>Select the queen first, then choose a destination on the board. This safe trial will not change your saved game.</p></div>`;
    body = `<div class="review-kicker">TRY THE MOVE · SAFE EXPERIMENT</div><div class="review-callout"><strong>Keep the queen safe.</strong><p>Select a source square and then a destination on the board.</p></div>${trialFeedback}${explanationDetail()}`;
    footer = `${chessState.attempt === "correct" ? `<button type="button" class="primary-chess-button" data-action="chess-practice">Continue to practice <span aria-hidden="true">→</span></button>` : ""}<div class="review-text-links"><button type="button" class="chess-text-link" data-action="chess-retry">Reset the trial</button>${explanationButton("Need more help")}</div>`;
  } else if (chessState.phase === "practice") {
    const practiceFeedback = chessState.attempt === "correct"
      ? `<div class="review-feedback"><span class="review-feedback-mark">✓</span><span><strong>Good safety check.</strong>${practiceCorrectMove.notation} moves the queen away from the bishop's attack.</span></div>`
      : chessState.attempt === "wrong-source"
        ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>Select the queen first.</strong>Then choose a destination for that piece.</span></div>`
        : chessState.attempt === "wrong"
          ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>That square is still unsafe.</strong>Move the queen away from the bishop's attack and try again.</span></div>`
          : "";
    body = `<div class="review-kicker">PRACTICE · TRANSFER THE IDEA</div><div class="practice-lane ${chessState.practiceDone ? "is-complete" : ""}"><span class="practice-mark">${chessState.practiceDone ? "✓" : "✦"}</span><h3>${chessState.practiceDone ? "Practice complete." : "Find a safe queen square"}</h3><p>${chessState.practiceDone ? "You applied the same safety check in a new position." : practiceGoal}</p></div>${practiceFeedback}<div class="review-plain"><span class="mini-label">WHY THIS PRACTICE FITS</span><p>This repeats the same safety check: <strong>look for the opponent's attack before moving a valuable piece.</strong></p></div>${explanationDetail()}`;
    const completePractice = chessState.attempt === "correct" && !chessState.practiceDone ? `<button type="button" class="primary-chess-button" data-action="chess-complete-practice">Complete practice <span aria-hidden="true">→</span></button>` : "";
    footer = `${completePractice}${chessState.practiceDone ? `<button type="button" class="primary-chess-button" data-action="chess-complete-review">Finish review <span aria-hidden="true">→</span></button>` : ""}<button type="button" class="ghost-chess-button" data-action="chess-return-review">Return to review</button><div class="review-text-links">${explanationButton("Need more help")}<button type="button" class="chess-text-link" data-action="chess-review-another">Review another moment</button></div>`;
  } else {
    body = `<div class="completion-seal">✓</div><div class="review-kicker">REVIEW COMPLETE</div><h3>One mistake, one useful idea.</h3><p>You connected the move to its consequence, tried a safer alternative, and carried the idea into practice.</p><div class="completion-summary"><strong>What you learned</strong><span>Check the opponent's attack before moving a valuable piece.</span><ul class="completion-checklist"><li>Mistake reviewed</li><li>Better move tried</li><li>Practice completed</li></ul></div>`;
    footer = `<button type="button" class="primary-chess-button" data-action="chess-review-another">Review another moment <span aria-hidden="true">→</span></button><button type="button" class="ghost-chess-button study-researcher-chrome" data-route="home">Restart demo</button>`;
  }

  stage.innerHTML = `${reviewPanelHeader(route, progress)}<div class="review-panel-body">${body}</div><div class="review-panel-footer">${footer}</div>`;
}

function fifaOrderModal() {
  openModal({
    surface: "drawer",
    kicker: "ORDER DETAIL · FICTIONAL DEMO RECORD",
    title: "Order FIFA-26-88421",
    copy: "The order view keeps the reference, ticket items, and current allocation state together.",
    body: `<div class="modal-section-heading"><span>ORDER SUMMARY</span><span>FIFA ticket allocation</span></div><div class="modal-content-block"><dl><div><dt>ORDER REFERENCE</dt><dd>FIFA-26-88421</dd></div><div><dt>TOURNAMENT</dt><dd>FIFA World Cup 2026</dd></div><div><dt>TICKET QUANTITY</dt><dd>2 tickets</dd></div><div><dt>ORDER DATE</dt><dd>08 Jun 2026</dd></div><div><dt>CURRENT STATUS</dt><dd>1 confirmed · 1 pending</dd></div></dl></div><div class="modal-section-heading"><span>TICKET ITEMS</span><span>2 saved events</span></div><ul class="modal-ticket-list"><li class="modal-ticket-item"><span class="modal-ticket-mark">MX</span><span><strong>Mexico City · Match 18</strong><small>17 Jun 2026 · 1 ticket · allocation in progress</small></span><span class="modal-ticket-state">Pending</span></li><li class="modal-ticket-item"><span class="modal-ticket-mark">CA</span><span><strong>Toronto · Match 27</strong><small>21 Jun 2026 · 1 ticket · mobile delivery</small></span><span class="modal-ticket-state is-confirmed">Confirmed</span></li></ul><div class="modal-section-heading"><span>ORDER PROGRESS</span><span>Status remains the source of truth</span></div><div class="modal-timeline"><div class="modal-timeline-row"><span class="timeline-marker">✓</span><div><strong>Order received</strong><span>Reference created · 08 Jun 2026</span></div></div><div class="modal-timeline-row"><span class="timeline-marker">✓</span><div><strong>Toronto allocation confirmed</strong><span>Ticket is ready for event day</span></div></div><div class="modal-timeline-row"><span class="timeline-marker">•</span><div><strong>Mexico City allocation pending</strong><span>Awaiting the next FIFA confirmation update</span></div></div></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-return-overview">Back to ticket overview</button><button type="button" class="modal-primary" data-action="fifa-view-tickets">View ticket detail</button>`
  });
}

function fifaTicketsModal() {
  const event = fifaEvents[fifaState.selected];
  const isPending = fifaState.selected === "pending";
  openModal({
    surface: "drawer",
    kicker: `TICKET DETAIL · ${event.status.toUpperCase()}`,
    title: event.title,
    copy: "A ticket-like detail view keeps the event, availability, and current status together.",
    body: `<div class="ticket-detail-card"><div class="ticket-detail-top"><span class="ticket-detail-brand">FIFA MOBILE TICKET</span><span class="ticket-detail-state">${isPending ? "Allocation pending" : "Ready for event day"}</span></div><h3>${event.title}</h3><p>${event.subtitle}</p></div><div class="modal-content-block"><dl><div><dt>EVENT</dt><dd>${event.subtitle}</dd></div><div><dt>VENUE</dt><dd>${isPending ? "Estadio Azteca" : "BMO Field"}</dd></div><div><dt>CATEGORY</dt><dd>${isPending ? "Category 3 · allocation in progress" : "Section 112 · Row G"}</dd></div><div><dt>SOURCE</dt><dd>Official FIFA source</dd></div></dl></div>${isPending ? `<div class="availability-panel"><span aria-hidden="true">!</span><div><strong>Ticket not issued yet</strong><p>This order is still Pending, so no QR code or seat credential is shown. FIFA owns the next confirmation.</p></div></div>` : `<div class="availability-panel is-ready"><span aria-hidden="true">✓</span><div><strong>Mobile ticket ready</strong><p>The confirmed event is available for event-day access. Transfer begins with a destination preview.</p></div></div>`}`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-return-overview">Back to ticket overview</button>${isPending ? "" : `<button type="button" class="modal-primary" data-action="fifa-open-handoff">Transfer tickets safely</button>`}`
  });
}

function fifaHandoffModal() {
  openModal({
    kicker: "HANDOFF GUARDRAIL · EXTERNAL DESTINATION",
    title: "You're leaving FIFA.com",
    copy: "Check the partner identity before the transfer leaves FIFA context. Your FIFA order and status remain the source of truth when you return.",
    body: `<div class="partner-destination"><span class="partner-logo">T</span><div><strong>Official FIFA Ticketing Partner <span aria-hidden="true">↗</span></strong><small>tickets.partner.example/transfer</small></div></div><div class="modal-content-block"><ul class="modal-list"><li><span>Your event and order reference will be preserved for the return path.</span></li><li><span>The partner may ask you to sign in again.</span></li><li><span>A return to FIFA.com will not claim that the partner completed a transfer.</span></li></ul></div><div class="modal-warning"><span>↗</span><div><strong>You are about to leave FIFA.com.</strong> Continue only if this is the partner you expected.</div></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-stay">Cancel</button><button type="button" class="modal-primary" data-action="fifa-continue-handoff">Continue to partner</button>`
  });
}

function fifaHandoffCompleteModal() {
  openModal({
    kicker: isStudyMode() ? "PARTNER HANDOFF" : "PARTNER HANDOFF · DEMO STATE",
    title: "Partner boundary understood.",
    copy: isStudyMode() ? "The partner destination would open here. The return path keeps the FIFA status and order context visible." : "In a live service the partner destination would open here. This offline demo pauses at the boundary so the return path can be tested without a real external transaction.",
    body: `<span class="simulation-note">OFFLINE PARTNER SIMULATION</span><div class="modal-success-mark">↗</div><div class="modal-content-block"><dl><div><dt>DESTINATION</dt><dd>Official FIFA Ticketing Partner</dd></div><div><dt>CONTEXT PRESERVED</dt><dd>Order · event · status</dd></div><div><dt>PARTNER RESULT</dt><dd>Not claimed by FIFA</dd></div></dl></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="close-modal">${isStudyMode() ? "Stay on FIFA.com" : "Stay in demo"}</button><button type="button" class="modal-primary" data-action="fifa-return">Return to FIFA dashboard</button>`
  });
}

function fifaHelpModal() {
  openModal({
    kicker: "FIFA STATUS GLOSSARY",
    title: "Read the status, not just the color.",
    copy: "The dashboard pairs every state with text, ownership, freshness, and a safe next action.",
    body: `<div class="glossary-grid"><div class="glossary-item"><strong>Pending</strong><span>Awaiting FIFA confirmation. No action is required until the owner changes.</span></div><div class="glossary-item"><strong>Confirmed</strong><span>The allocation is ready to view. Event-day actions are now available.</span></div><div class="glossary-item"><strong>Official source</strong><span>The status is presented as a FIFA-owned information cue in this fictional prototype.</span></div><div class="glossary-item"><strong>Partner handoff</strong><span>A boundary warning and destination preview appear before a transfer leaves FIFA.com.</span></div></div>`,
    actions: `<button type="button" class="modal-primary" data-action="close-modal">Got it</button>`
  });
}

function chessHelpModal() {
  openModal({
    theme: "chess",
    kicker: "BEGINNER REVIEW GLOSSARY",
    title: "The notation is a shortcut, not the lesson.",
    copy: "Beginner Review leads with the consequence in plain language. Open this only when a chess term needs a little more context.",
    body: `<div class="glossary-grid"><div class="glossary-item"><strong>${chessScenario.mistake.notation}</strong><span>The queen moves to ${chessScenario.mistake.destination}, where ${chessScenario.mistakeConsequence.notation} can capture it.</span></div><div class="glossary-item"><strong>${chessScenario.betterMove.notation}</strong><span>${chessScenario.betterMove.summary}</span></div><div class="glossary-item"><strong>Try this move</strong><span>A safe experiment on the review board. It does not rewrite the completed game.</span></div><div class="glossary-item"><strong>Practice this idea</strong><span>A short exercise that repeats the same safety check in a new position.</span></div></div>`,
    actions: `<button type="button" class="modal-primary" data-action="close-modal">Return to review</button>`
  });
}

function chessAdvancedModal() {
  openModal({
    theme: "chess",
    kicker: "OPTIONAL DEPTH",
    title: "Full Analysis stays secondary.",
    copy: "Advanced analysis can show engine lines, evaluation graphs, and deeper move details. It is available after the beginner explanation, not before it.",
    body: `<div class="modal-content-block"><ul class="modal-list"><li><span>Position detail: ${chessScenario.moveNumber}. ${chessScenario.mistake.notation} versus ${chessScenario.betterMove.notation}</span></li><li><span>Evaluation focus: the black knight controls the tempting queen destination</span></li><li><span>Beginner takeaway: check an opponent's attack before moving a valuable piece</span></li></ul></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="close-modal">Close</button><button type="button" class="modal-primary" data-action="chess-start-review">Use Beginner Review</button>`
  });
}

function resetFifa() {
  Object.assign(fifaState, { selected: "pending", explanationOpen: false, calendarAdded: false, refreshing: false, error: false, returnNotice: false, lastUpdated: "2 min ago" });
  renderFifa();
  showToast("FIFA demo reset", "Pending status is visible again with the original return path.");
}

function resetChess() {
  Object.assign(chessState, { phase: "intro", attempt: null, selectedSquare: null, explanationVariant: "primary", practiceDone: false });
  renderChess();
}

function handleAction(action, target) {
  switch (action) {
    case "close-modal":
      closeModal();
      break;
    case "fifa-overview":
    case "fifa-return-overview":
      closeModal();
      navigate("fifa");
      break;
    case "fifa-help":
      fifaHelpModal();
      break;
    case "fifa-toggle-explanation":
      fifaState.explanationOpen = !fifaState.explanationOpen;
      renderFifa();
      break;
    case "fifa-dismiss-notice":
      fifaState.returnNotice = false;
      renderFifa();
      break;
    case "fifa-select-event":
      fifaState.selected = target.dataset.event || "pending";
      fifaState.returnNotice = false;
      renderFifa();
      showToast(`${fifaEvents[fifaState.selected].status} event selected`, fifaEvents[fifaState.selected].title);
      break;
    case "fifa-view-order":
      fifaOrderModal();
      break;
    case "fifa-view-tickets":
      fifaTicketsModal();
      break;
    case "fifa-calendar":
      if (fifaState.selected !== "confirmed") break;
      fifaState.calendarAdded = true;
      renderFifa();
      showToast("Calendar event saved", "Toronto · 21 Jun 2026 is ready for your calendar.");
      break;
    case "fifa-open-handoff":
      fifaHandoffModal();
      break;
    case "fifa-stay":
      closeModal();
      showToast("Still on FIFA.com", "Your ticket context and pending status are unchanged.");
      break;
    case "fifa-continue-handoff":
      fifaHandoffCompleteModal();
      break;
    case "fifa-return":
      closeModal();
      fifaState.returnNotice = true;
      navigate("fifa");
      showToast("Returned to FIFA dashboard", "Context preserved · partner completion is not inferred.");
      break;
    case "fifa-refresh": {
      if (fifaState.refreshing) break;
      fifaState.refreshing = true;
      fifaState.error = false;
      renderFifa();
      window.setTimeout(() => {
        fifaState.refreshing = false;
        fifaState.lastUpdated = "just now";
        renderFifa();
        showToast("Status refreshed", "Official source timestamp is now just now in this demo.");
      }, 700);
      break;
    }
    case "fifa-preview-error":
      if (isStudyMode()) break;
      fifaState.error = true;
      renderFifa();
      showToast("Unavailable state preview", "The previous timestamp remains visible and retry is available.");
      break;
    case "fifa-reset":
      if (isStudyMode()) break;
      resetFifa();
      break;
    case "chess-help":
      if (isStudyMode()) break;
      chessHelpModal();
      break;
    case "chess-open-advanced":
      if (isStudyMode()) break;
      chessAdvancedModal();
      break;
    case "chess-explain":
      chessState.explanationVariant = chessState.explanationVariant === "alternate" ? "primary" : "alternate";
      renderChess();
      break;
    case "chess-start-review":
      closeModal();
      chessState.phase = "mistake";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      navigate("chess");
      renderChess();
      break;
    case "chess-reveal-better":
      chessState.phase = "better";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-try-move":
      chessState.phase = "trial";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-square":
      if (!["trial", "practice"].includes(chessState.phase)) break;
      {
        const move = chessMoveForPhase(chessState.phase);
        const square = target.dataset.square;
        if (!chessState.selectedSquare) {
          chessState.attempt = square === move.source ? null : "wrong-source";
          chessState.selectedSquare = square === move.source ? square : null;
        } else if (square === chessState.selectedSquare) {
          chessState.selectedSquare = null;
          chessState.attempt = null;
        } else {
          const source = chessState.selectedSquare;
          chessState.selectedSquare = null;
          chessState.attempt = source === move.source && square === move.destination ? "correct" : "wrong";
          if (chessState.attempt === "correct") {
            showToast("Good move", `${move.notation} addresses the attack on the queen.`);
          }
        }
      }
      renderChess();
      break;
    case "chess-retry":
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-practice":
      chessState.phase = "practice";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.practiceDone = false;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-complete-practice":
      if (chessState.phase !== "practice" || chessState.attempt !== "correct") break;
      chessState.practiceDone = true;
      chessState.selectedSquare = null;
      renderChess();
      break;
    case "chess-complete-review":
      chessState.phase = "complete";
      renderChess();
      break;
    case "chess-return-review":
      chessState.phase = "better";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-back-to-mistake":
      chessState.phase = "mistake";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      renderChess();
      break;
    case "chess-review-another":
      chessState.phase = "mistake";
      chessState.attempt = null;
      chessState.selectedSquare = null;
      chessState.explanationVariant = "primary";
      chessState.practiceDone = false;
      renderChess();
      showToast("Another moment ready", "This demo keeps the one-mistake-at-a-time focus.");
      break;
    default:
      break;
  }
}

document.addEventListener("click", (event) => {
  const routeTarget = event.target.closest("[data-route]");
  if (routeTarget) {
    event.preventDefault();
    navigate(routeTarget.dataset.route);
    return;
  }
  const actionTarget = event.target.closest("[data-action]");
  if (actionTarget) {
    event.preventDefault();
    handleAction(actionTarget.dataset.action, actionTarget);
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !modalRoot.hidden) closeModal();
  const eventRow = event.target.closest?.(".event-row");
  if (eventRow && (event.key === "Enter" || event.key === " ")) {
    event.preventDefault();
    handleAction("fifa-select-event", eventRow);
  }
});

modalRoot.addEventListener("click", (event) => {
  if (event.target === modalRoot) closeModal();
});

modalRoot.addEventListener("keydown", (event) => {
  if (event.key !== "Tab") return;
  const focusable = [...modalRoot.querySelectorAll("button, [href], input, select, textarea, [tabindex]:not([tabindex='-1'])")]
    .filter((element) => !element.disabled && element.offsetParent !== null);
  if (!focusable.length) return;
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  if (event.shiftKey && document.activeElement === first) {
    event.preventDefault();
    last.focus();
  } else if (!event.shiftKey && document.activeElement === last) {
    event.preventDefault();
    first.focus();
  }
});

window.addEventListener("hashchange", () => setRoute(currentRoute()));

setRoute(currentRoute());
