const fifaEvents = {
  pending: {
    key: "pending",
    title: "Mexico City \u00b7 Estadio Azteca",
    subtitle: "Group stage \u00b7 Match 18 \u00b7 17 Jun 2026 \u00b7 19:00 local time",
    status: "Pending",
    owner: "FIFA",
    meaning: "FIFA is confirming the allocation. No immediate user action is required.",
    next: "FIFA confirms the allocation.",
  },
  confirmed: {
    key: "confirmed",
    title: "Toronto \u00b7 BMO Field",
    subtitle: "Group stage \u00b7 Match 27 \u00b7 21 Jun 2026 \u00b7 15:00 local time",
    status: "Confirmed",
    owner: "You",
    meaning: "The ticket is available. You can review it or save the event to your calendar.",
    next: "View the mobile ticket.",
  },
};

const fifaState = {
  selected: "pending",
  filter: "all",
  calendarAdded: false,
  notificationsEnabled: false,
  refreshing: false,
  error: false,
  returnNotice: false,
  lastUpdated: "2 min ago",
};

const chessState = {
  view: "dashboard",
  selectedMoment: null,
  filter: "all",
  solutionRevealed: false,
  expandedDetail: false,
  attempt: null,
  selectedSquare: null,
  practiceDone: false,
  reviewedMoments: new Set(),
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
    a1: "R", b1: "N", c1: "", d1: "Q", e1: "K", f1: "", g1: "N", h1: "R",
  }),
  mistake: Object.freeze({
    notation: "Qh5",
    source: "d1",
    destination: "h5",
    label: "Move the queen to h5",
    summary: "The queen steps onto a square attacked by the knight on f6.",
  }),
  mistakeConsequence: Object.freeze({
    notation: "Nxh5",
    source: "f6",
    destination: "h5",
    summary: "Black can capture the queen immediately with the knight.",
  }),
  betterMove: Object.freeze({
    notation: "Qe2",
    source: "d1",
    destination: "e2",
    label: "Move the queen to e2",
    summary: "Move the queen to a safe square before looking for activity.",
  }),
  explanation: Object.freeze({
    primary: "The queen moved onto a square controlled by the black knight. Black can take it immediately, so queen safety matters before activity.",
    alternate: "Before moving a valuable piece, scan the opponent's attacks on its destination. The tempting square fails that check.",
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
    a1: "R", b1: "N", c1: "", d1: "Q", e1: "K", f1: "", g1: "N", h1: "R",
  }),
  practiceGoal: "Find a safe queen square when the bishop is already attacking the queen's starting line.",
  practiceCorrectMove: Object.freeze({
    notation: "Qd3",
    source: "d1",
    destination: "d3",
    summary: "Qd3 steps away from the bishop's diagonal and keeps the queen safe.",
  }),
});

const chessMoments = Object.freeze([
  Object.freeze({
    id: "queen-safety",
    moveNumber: 12,
    title: "Queen safety",
    category: "Mistake",
    tone: "mistake",
    summary: "A queen move allowed an immediate capture.",
    detail: "The destination looked active, but an opposing knight already controlled it.",
    why: "Checking attacks before moving a valuable piece prevents a one-move loss.",
    actionLabel: "Review \u00b7 Try \u00b7 Practice",
    supportsTry: true,
    supportsPractice: true,
    focusSquare: "h5",
    previewMoves: Object.freeze([chessScenario.mistake]),
  }),
  Object.freeze({
    id: "development",
    moveNumber: 8,
    title: "Development with tempo",
    category: "Good move",
    tone: "good",
    summary: "A knight joined the game while challenging the centre.",
    detail: "Developing the knight improved coordination and made the next plan easier to see.",
    why: "Useful development connects a piece to the position instead of spending a move without a purpose.",
    actionLabel: "Review explanation",
    supportsTry: false,
    supportsPractice: false,
    focusSquare: "f3",
    previewMoves: Object.freeze([Object.freeze({ source: "g1", destination: "f3" })]),
  }),
  Object.freeze({
    id: "king-safety",
    moveNumber: 16,
    title: "King safety",
    category: "Mistake",
    tone: "mistake",
    summary: "The king stayed in the centre while lines were opening.",
    detail: "A quieter king-safety move was worth considering before starting another attack.",
    why: "Open central lines make an uncastled king harder to protect and reduce freedom elsewhere.",
    actionLabel: "Review explanation",
    supportsTry: false,
    supportsPractice: false,
    focusSquare: "e1",
    previewMoves: Object.freeze([]),
  }),
  Object.freeze({
    id: "opening-idea",
    moveNumber: 5,
    title: "Opening idea",
    category: "Idea",
    tone: "idea",
    summary: "A central pawn move opened useful lines for both bishops.",
    detail: "The pawn move claimed space and created routes for pieces that began behind it.",
    why: "An opening move is useful when it supports development and a clear next plan.",
    actionLabel: "Review explanation",
    supportsTry: false,
    supportsPractice: false,
    focusSquare: "d4",
    previewMoves: Object.freeze([Object.freeze({ source: "d2", destination: "d4" })]),
  }),
]);

const chessPieces = {
  K: "\u2654", Q: "\u2655", R: "\u2656", B: "\u2657", N: "\u2658", P: "\u2659",
  k: "\u265a", q: "\u265b", r: "\u265c", b: "\u265d", n: "\u265e", p: "\u265f",
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
  if (window.location.hash === `#${route}`) setRoute(route);
  else window.location.hash = route;
}

function setRoute(route) {
  applyMode();
  if (isStudyMode() && route === "home") route = studyProduct();
  closeModal();
  document.querySelector(".lab-header")?.toggleAttribute("hidden", route !== "home");
  document.querySelectorAll(".lab-view").forEach((view) => {
    view.hidden = view.id !== `${route}View`;
  });
  document.querySelectorAll(".lab-nav-item").forEach((item) => item.classList.toggle("is-active", item.dataset.route === route));
  if (route === "fifa") renderFifa();
  if (route === "chess") renderChess();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showToast(title, detail) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<span class="toast-mark">&#10003;</span><div><strong>${title}</strong><span>${detail}</span></div>`;
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
      <div class="modal-top"><div><span class="modal-kicker">${kicker}</span><h2 id="modalTitle">${title}</h2></div><button type="button" class="modal-close" data-action="close-modal" aria-label="Close dialog">&times;</button></div>
      ${copy ? `<p>${copy}</p>` : ""}${body}${actions ? `<div class="modal-actions">${actions}</div>` : ""}
    </div>`;
  document.body.classList.add("modal-open");
  window.requestAnimationFrame(() => modalRoot.querySelector(".modal-close")?.focus());
}

function closeModal() {
  if (!modalRoot || modalRoot.hidden) return;
  const returnFocus = modalReturnFocus;
  modalReturnFocus = null;
  modalRoot.hidden = true;
  modalRoot.innerHTML = "";
  modalRoot.className = "modal-root";
  document.body.classList.remove("modal-open");
  if (returnFocus?.isConnected) window.requestAnimationFrame(() => returnFocus.focus());
}

function renderFifa() {
  const cards = [...document.querySelectorAll("[data-fifa-event-card]")];
  let visibleCount = 0;
  cards.forEach((card) => {
    const show = fifaState.filter === "all" || card.dataset.event === fifaState.filter;
    card.hidden = !show;
    if (show) visibleCount += 1;
  });
  document.getElementById("fifaEmptyState").hidden = visibleCount > 0;
  document.getElementById("fifaVisibleCount").textContent = `${visibleCount} event${visibleCount === 1 ? "" : "s"} shown`;
  document.querySelectorAll('[data-action="fifa-filter"]').forEach((button) => {
    const active = button.dataset.filter === fifaState.filter;
    button.classList.toggle("is-active", active);
    if (button.hasAttribute("aria-pressed")) button.setAttribute("aria-pressed", String(active));
  });

  document.getElementById("fifaAlert").hidden = !fifaState.error;
  document.getElementById("fifaReturnNotice").hidden = !fifaState.returnNotice;
  document.querySelector(".refresh-control")?.classList.toggle("is-refreshing", fifaState.refreshing);
  document.getElementById("fifaLastUpdated").textContent = fifaState.lastUpdated;
  document.getElementById("fifaFootFreshness").textContent = `Updated ${fifaState.lastUpdated}`;

  const confirmedCalendar = document.getElementById("fifaCalendarConfirmed");
  if (confirmedCalendar) {
    confirmedCalendar.disabled = false;
    confirmedCalendar.setAttribute("aria-disabled", "false");
    confirmedCalendar.querySelector("strong").textContent = fifaState.calendarAdded ? "Calendar saved" : "Add to calendar";
    confirmedCalendar.querySelector("small").textContent = fifaState.calendarAdded ? "Toronto event saved" : "Save confirmed event";
  }
  const notificationTitle = document.getElementById("fifaNotificationTitle");
  const notificationCopy = document.getElementById("fifaNotificationCopy");
  if (notificationTitle && notificationCopy) {
    notificationTitle.textContent = fifaState.notificationsEnabled ? "Status updates enabled" : "Status updates are off";
    notificationCopy.textContent = fifaState.notificationsEnabled ? "Demo cue only; no live service" : "Enable a demo confirmation cue";
  }
}

function fifaOrderModal() {
  openModal({
    surface: "drawer",
    kicker: "ORDER DETAIL \u00b7 FICTIONAL DEMO RECORD",
    title: "Order FIFA-26-88421",
    copy: "The account order keeps both event records and their current states together.",
    body: `<div class="modal-section-heading"><span>ORDER SUMMARY</span><span>2 saved events</span></div><div class="modal-content-block"><dl><div><dt>ORDER REFERENCE</dt><dd>FIFA-26-88421</dd></div><div><dt>TOURNAMENT</dt><dd>FIFA World Cup 2026</dd></div><div><dt>TICKET QUANTITY</dt><dd>2 tickets</dd></div><div><dt>CURRENT STATUS</dt><dd>1 confirmed \u00b7 1 pending</dd></div></dl></div><ul class="modal-ticket-list"><li class="modal-ticket-item"><span class="modal-ticket-mark">MX</span><span><strong>Mexico City \u00b7 Match 18</strong><small>17 Jun 2026 \u00b7 FIFA confirmation pending</small></span><span class="modal-ticket-state">Pending</span></li><li class="modal-ticket-item"><span class="modal-ticket-mark">CA</span><span><strong>Toronto \u00b7 Match 27</strong><small>21 Jun 2026 \u00b7 mobile ticket available</small></span><span class="modal-ticket-state is-confirmed">Confirmed</span></li></ul><div class="modal-section-heading"><span>COMPACT ORDER HISTORY</span><span>Secondary detail</span></div><div class="modal-timeline"><div class="modal-timeline-row"><span class="timeline-marker">&#10003;</span><div><strong>Order received</strong><span>Reference created \u00b7 08 Jun 2026</span></div></div><div class="modal-timeline-row"><span class="timeline-marker">&#10003;</span><div><strong>Toronto confirmed</strong><span>Ticket available now</span></div></div><div class="modal-timeline-row"><span class="timeline-marker">&#8226;</span><div><strong>Mexico City pending</strong><span>FIFA owns the next confirmation</span></div></div></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-return-overview">Back to dashboard</button>`,
  });
}

function fifaTicketsModal(eventKey = fifaState.selected) {
  const event = fifaEvents[eventKey] || fifaEvents.pending;
  const isPending = event.key === "pending";
  openModal({
    surface: "drawer",
    kicker: `EVENT DETAIL \u00b7 ${event.status.toUpperCase()}`,
    title: event.title,
    copy: event.meaning,
    body: `<div class="ticket-detail-card"><div class="ticket-detail-top"><span>FIFA MOBILE TICKET</span><span class="ticket-detail-state">${isPending ? "Allocation pending" : "Ready for event day"}</span></div><h3>${event.title}</h3><p>${event.subtitle}</p></div><div class="modal-content-block"><dl><div><dt>CURRENT STATE</dt><dd>${event.status}</dd></div><div><dt>OWNER</dt><dd>${event.owner}</dd></div><div><dt>NEXT STEP</dt><dd>${event.next}</dd></div><div><dt>SOURCE</dt><dd>Official FIFA source</dd></div></dl></div>${isPending ? `<div class="availability-panel"><span>!</span><div><strong>Ticket not issued yet</strong><p>No QR code is shown. FIFA owns the next confirmation and no action is required now.</p></div></div>` : `<div class="availability-panel is-ready"><span>&#10003;</span><div><strong>Mobile ticket ready</strong><p>The confirmed event is available for event-day access.</p></div></div>`}`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-return-overview">Back to dashboard</button>${isPending ? "" : `<button type="button" class="modal-primary" data-action="fifa-open-handoff" data-event="confirmed">Transfer tickets safely</button>`}`,
  });
}

function fifaHandoffModal() {
  const event = fifaEvents[fifaState.selected] || fifaEvents.confirmed;
  openModal({
    kicker: "HANDOFF GUARDRAIL \u00b7 EXTERNAL DESTINATION",
    title: "You're leaving FIFA.com",
    copy: `Check the partner identity before transferring the ${event.title} ticket. FIFA remains the source of truth when you return.`,
    body: `<div class="partner-destination"><span class="partner-logo">T</span><div><strong>Official FIFA Ticketing Partner</strong><small>tickets.partner.example/transfer</small></div></div><div class="modal-content-block"><ul class="modal-list"><li><span>Your event and order reference will be preserved for the return path.</span></li><li><span>The partner may ask you to sign in again.</span></li><li><span>Returning to FIFA.com will not claim that the partner completed a transfer.</span></li></ul></div><div class="modal-warning"><span>&nearr;</span><div><strong>You are about to leave FIFA.com.</strong> Continue only if this is the destination you expected.</div></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="fifa-stay">Cancel</button><button type="button" class="modal-primary" data-action="fifa-continue-handoff">Continue to partner</button>`,
  });
}

function fifaHandoffCompleteModal() {
  openModal({
    kicker: isStudyMode() ? "PARTNER HANDOFF" : "PARTNER HANDOFF \u00b7 DEMO STATE",
    title: "Partner boundary understood.",
    copy: isStudyMode() ? "The partner destination would open here. The return path keeps FIFA ticket status visible." : "This offline demonstrator pauses at the external boundary so the safe return can be tested without a transaction.",
    body: `${isStudyMode() ? "" : `<span class="simulation-note">OFFLINE PARTNER SIMULATION</span>`}<div class="modal-success-mark">&nearr;</div><div class="modal-content-block"><dl><div><dt>DESTINATION</dt><dd>Official FIFA Ticketing Partner</dd></div><div><dt>CONTEXT PRESERVED</dt><dd>Order \u00b7 event \u00b7 status</dd></div><div><dt>PARTNER RESULT</dt><dd>Not claimed by FIFA</dd></div></dl></div>`,
    actions: `<button type="button" class="modal-secondary" data-action="close-modal">Stay on FIFA.com</button><button type="button" class="modal-primary" data-action="fifa-return">Return to FIFA dashboard</button>`,
  });
}

function fifaHelpModal() {
  openModal({
    kicker: "FIFA STATUS & SUPPORT",
    title: "Read the state, owner, and safe action.",
    copy: "Every event keeps its status meaning next to the action that is safe in that state.",
    body: `<div class="glossary-grid"><div class="glossary-item"><strong>Pending</strong><span>Awaiting FIFA confirmation. No immediate user action is required.</span></div><div class="glossary-item"><strong>Confirmed</strong><span>The ticket is available and event-day actions are enabled.</span></div><div class="glossary-item"><strong>Official source</strong><span>A FIFA-owned provenance cue for this fictional prototype.</span></div><div class="glossary-item"><strong>Partner handoff</strong><span>A destination preview appears before transfer leaves FIFA.com.</span></div></div>`,
    actions: `<button type="button" class="modal-primary" data-action="close-modal">Return to dashboard</button>`,
  });
}

function applyChessMove(position, move) {
  const next = { ...position };
  const piece = next[move.source] || "";
  next[move.source] = "";
  next[move.destination] = piece;
  return next;
}

function selectedChessMoment() {
  return chessMoments.find((moment) => moment.id === chessState.selectedMoment) || null;
}

function positionForMoment(moment) {
  return (moment?.previewMoves || []).reduce((position, move) => applyChessMove(position, move), chessScenario.startPosition);
}

function chessMoveForPhase(phase) {
  return phase === "practice" ? chessScenario.practiceCorrectMove : chessScenario.betterMove;
}

function chessPositionForPhase(phase) {
  if (phase === "practice") {
    return chessState.practiceDone || chessState.attempt === "correct"
      ? applyChessMove(chessScenario.practicePosition, chessScenario.practiceCorrectMove)
      : chessScenario.practicePosition;
  }
  if (phase === "trial" && chessState.attempt === "correct") return applyChessMove(chessScenario.startPosition, chessScenario.betterMove);
  return positionForMoment(selectedChessMoment());
}

function boardMarkup({ phase = "dashboard", interactive = false } = {}) {
  const position = chessPositionForPhase(phase);
  const moment = selectedChessMoment();
  const selectedSquare = chessState.selectedSquare;
  const highlights = [];
  if (phase === "detail" && moment) highlights.push(chessState.solutionRevealed && moment.id === "queen-safety" ? chessScenario.betterMove.destination : moment.focusSquare);
  const files = ["a", "b", "c", "d", "e", "f", "g", "h"];
  let squares = "";
  for (let rank = 8; rank >= 1; rank -= 1) {
    for (const file of files) {
      const coord = `${file}${rank}`;
      const piece = position[coord] || "";
      const isLight = (files.indexOf(file) + rank) % 2 === 0;
      const classes = ["board-square", isLight ? "light" : "dark"];
      if (highlights.includes(coord)) classes.push(chessState.solutionRevealed ? "is-better" : moment?.tone === "mistake" ? "is-highlight" : "is-selected");
      if (selectedSquare === coord) classes.push("is-source-selected");
      if (chessState.attempt === "correct" && coord === chessMoveForPhase(phase).destination) classes.push("is-better");
      if (interactive) classes.push("is-clickable");
      const pieceClass = piece && piece === piece.toUpperCase() ? "piece-white" : "piece-black";
      const pieceMarkup = piece ? `<span class="piece ${pieceClass}">${chessPieces[piece]}</span>` : "";
      const ariaLabel = `${coord}${piece ? ` ${pieceClass === "piece-white" ? "white" : "black"} piece` : " empty"}`;
      squares += interactive
        ? `<button type="button" class="${classes.join(" ")}" data-action="chess-square" data-square="${coord}" data-coord="${coord}" aria-label="${ariaLabel}">${pieceMarkup}</button>`
        : `<span class="${classes.join(" ")}" data-coord="${coord}" role="img" aria-label="${ariaLabel}">${pieceMarkup}</span>`;
    }
  }
  return `<div class="chess-board-wrap"><div class="chess-board" role="grid" aria-label="Chess position for the current review context">${squares}</div></div>`;
}

function redesignedBoardPanel({ phase = "dashboard", interactive = false } = {}) {
  const moment = selectedChessMoment();
  let legend = "";
  let story = `<div class="move-story"><strong>Completed game context</strong><span>Select any key-moment card to inspect its board context.</span></div>`;
  if (phase === "detail" && moment) {
    const isBetter = chessState.solutionRevealed && moment.id === "queen-safety";
    legend = `<span><i class="legend-swatch ${isBetter ? "legend-better" : moment.tone === "mistake" ? "legend-mistake" : "legend-selected"}"></i>${isBetter ? "safer move" : "selected moment"}</span>`;
    story = `<div class="move-story"><strong>${isBetter ? chessScenario.betterMove.notation : `Move ${moment.moveNumber} \u00b7 ${moment.title}`}</strong><span>${isBetter ? chessScenario.betterMove.summary : moment.summary}</span></div>`;
  } else if (phase === "trial") {
    legend = `<span><i class="legend-swatch legend-selected"></i>selected square</span>`;
    story = `<div class="move-story"><strong>${chessState.attempt === "correct" ? "Move accepted" : "Your move"}</strong><span>${chessState.attempt === "correct" ? `${chessScenario.betterMove.notation} keeps the queen safe.` : "Select the queen first, then choose a safe destination."}</span></div>`;
  } else if (phase === "practice") {
    legend = `<span><i class="legend-swatch legend-selected"></i>selected square</span>`;
    story = `<div class="move-story"><strong>${chessState.attempt === "correct" || chessState.practiceDone ? "Practice move accepted" : "Practice position"}</strong><span>${chessState.attempt === "correct" || chessState.practiceDone ? `${chessScenario.practiceCorrectMove.notation} applies the safety check.` : "Select the queen, then choose a safe square."}</span></div>`;
  }
  return `<div class="board-panel">${boardMarkup({ phase, interactive })}<div class="board-legend">${legend}</div>${story}</div>`;
}

function miniBoardMarkup(moment) {
  const position = positionForMoment(moment);
  const files = ["a", "b", "c", "d", "e", "f", "g", "h"];
  let squares = "";
  for (let rank = 8; rank >= 1; rank -= 1) {
    for (const file of files) {
      const coord = `${file}${rank}`;
      const piece = position[coord] || "";
      const isLight = (files.indexOf(file) + rank) % 2 === 0;
      const pieceClass = piece && piece === piece.toUpperCase() ? "mini-piece-white" : "mini-piece-black";
      squares += `<span class="mini-square ${isLight ? "light" : "dark"}" aria-hidden="true">${piece ? `<i class="${pieceClass}">${chessPieces[piece]}</i>` : ""}</span>`;
    }
  }
  return `<span class="mini-board" role="img" aria-label="Static board preview for move ${moment.moveNumber}, ${moment.title}">${squares}</span>`;
}

function momentsForFilter() {
  if (chessState.filter === "mistake") return chessMoments.filter((moment) => moment.tone === "mistake");
  if (chessState.filter === "good") return chessMoments.filter((moment) => moment.tone === "good");
  if (chessState.filter === "practice") return chessMoments.filter((moment) => moment.supportsPractice);
  return chessMoments;
}

function renderChessDashboard() {
  const moments = momentsForFilter();
  const cards = moments.map((moment) => {
    const reviewed = chessState.reviewedMoments.has(moment.id);
    return `<button type="button" class="moment-card tone-${moment.tone} ${reviewed ? "is-reviewed" : ""}" data-action="chess-select-card" data-moment="${moment.id}" aria-pressed="false"><span class="moment-card-preview">${miniBoardMarkup(moment)}</span><span class="moment-card-content"><span class="moment-card-top"><span class="moment-category">${moment.category}</span><span class="moment-move">Move ${moment.moveNumber}</span></span><h4>${moment.title}</h4><p>${moment.summary}</p><span class="moment-card-footer"><span class="moment-actions-available">${moment.actionLabel}</span><span class="moment-open-mark">&rarr;</span></span>${reviewed ? `<span class="reviewed-mark">Reviewed</span>` : ""}</span></button>`;
  }).join("");
  const count = chessMoments.length;
  const mistakes = chessMoments.filter((moment) => moment.tone === "mistake").length;
  const goodMoves = chessMoments.filter((moment) => moment.tone === "good").length;
  const practice = chessMoments.filter((moment) => moment.supportsPractice).length;
  return `<div class="review-dashboard-header"><div><span class="review-dashboard-kicker">CARD REVIEW MODE</span><h2>Choose a key moment</h2><p>Nothing is selected yet. Scan the previews and open the moment that matters most to you.</p></div><span class="dashboard-choice-state">YOU CHOOSE THE ORDER</span></div><div class="review-dashboard-body"><div class="review-summary-grid" aria-label="Game performance summary"><button type="button" class="review-summary-chip ${chessState.filter === "all" ? "is-active" : ""}" data-action="chess-filter" data-filter="all" aria-pressed="${chessState.filter === "all"}"><strong>${count}</strong><span>Key moments</span></button><button type="button" class="review-summary-chip is-mistake ${chessState.filter === "mistake" ? "is-active" : ""}" data-action="chess-filter" data-filter="mistake" aria-pressed="${chessState.filter === "mistake"}"><strong>${mistakes}</strong><span>Mistakes</span></button><button type="button" class="review-summary-chip is-good ${chessState.filter === "good" ? "is-active" : ""}" data-action="chess-filter" data-filter="good" aria-pressed="${chessState.filter === "good"}"><strong>${goodMoves}</strong><span>Good moves</span></button><button type="button" class="review-summary-chip is-practice ${chessState.filter === "practice" ? "is-active" : ""}" data-action="chess-filter" data-filter="practice" aria-pressed="${chessState.filter === "practice"}"><strong>${practice}</strong><span>Practice available</span></button></div><div class="key-moments-heading"><h3>Review your key moments</h3><span>${moments.length} card${moments.length === 1 ? "" : "s"} shown</span></div><div class="moment-grid">${cards || `<div class="moment-grid-empty">No moments match this filter.</div>`}</div></div>`;
}

function renderMomentDetail() {
  const moment = selectedChessMoment();
  if (!moment) return renderChessDashboard();
  const richMoment = moment.id === "queen-safety";
  const expanded = chessState.expandedDetail ? `<div class="detail-explanation" role="status"><span>ANOTHER WAY TO SEE IT</span><p>${richMoment ? chessScenario.explanation.alternate : moment.why}</p></div>` : "";
  const richContent = richMoment
    ? `<div class="review-callout"><strong>${chessScenario.mistake.notation}</strong><p>${chessScenario.mistake.summary}</p></div><div class="move-readout"><div><span>YOU PLAYED</span><strong>${chessScenario.mistake.notation}</strong><small>${chessScenario.mistake.label}</small></div><div><span>CONSEQUENCE</span><strong>${chessScenario.mistakeConsequence.notation}</strong><small>${chessScenario.mistakeConsequence.summary}</small></div></div><div class="detail-explanation"><span>WHY IT MATTERS</span><p>${chessScenario.explanation.primary}</p></div>${chessState.solutionRevealed ? `<div class="review-callout is-better" role="status"><strong>${chessScenario.betterMove.notation}</strong><p>${chessScenario.betterMove.summary}</p></div>` : ""}${expanded}`
    : `<div class="detail-explanation"><span>WHAT HAPPENED</span><p>${moment.detail}</p></div><div class="detail-explanation"><span>WHY IT MATTERS</span><p>${moment.why}</p></div>${expanded}`;
  const actions = richMoment
    ? `<button type="button" class="primary-chess-button" data-action="chess-reveal-solution">${chessState.solutionRevealed ? "Safer move reviewed" : "Review safer move"}</button><button type="button" class="secondary-chess-button" data-action="chess-try-move">Try this move</button><button type="button" class="ghost-chess-button" data-action="chess-practice">Go to puzzle / practice</button><div class="review-text-links"><button type="button" class="chess-text-link" data-action="chess-toggle-detail">${chessState.expandedDetail ? "Hide extra explanation" : "Explain another way"}</button><button type="button" class="chess-text-link" data-action="chess-back-dashboard">Back to all key moments</button></div>`
    : `<button type="button" class="primary-chess-button" data-action="chess-toggle-detail">${chessState.expandedDetail ? "Hide extra explanation" : "Review explanation"}</button><button type="button" class="ghost-chess-button" data-action="chess-back-dashboard">Choose another card</button>`;
  return `<div class="moment-detail"><div class="moment-detail-top"><button type="button" class="back-to-moments" data-action="chess-back-dashboard">&larr; Back to all key moments</button><span class="selected-moment-state">SELECTED MOMENT</span></div><div class="moment-detail-body"><div class="moment-detail-heading"><span class="moment-category">${moment.category} \u00b7 Move ${moment.moveNumber}</span><h2>${moment.title}</h2><p>${moment.summary}</p></div>${richContent}</div><div class="detail-actions">${actions}</div></div>`;
}

function renderChessTrial() {
  const feedback = chessState.attempt === "correct"
    ? `<div class="review-feedback"><span class="review-feedback-mark">&#10003;</span><span><strong>That move keeps the queen safe.</strong>You found ${chessScenario.betterMove.notation}. The resulting position is shown on the board.</span></div>`
    : chessState.attempt === "wrong-source"
      ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>Select the queen first.</strong>Choose the source piece, then its destination.</span></div>`
      : chessState.attempt === "wrong"
        ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>That destination does not solve the problem.</strong>Select the queen again and retry a safer square.</span></div>`
        : `<div class="detail-explanation"><span>TRY THE IDEA</span><p>Select the queen first, then choose a safe destination. The exact answer stays hidden until you attempt it.</p></div>`;
  const actions = chessState.attempt === "correct"
    ? `<button type="button" class="primary-chess-button" data-action="chess-back-card">Return to selected card</button><button type="button" class="secondary-chess-button" data-action="chess-practice">Open related practice</button><button type="button" class="ghost-chess-button" data-action="chess-back-dashboard">Back to all key moments</button>`
    : `<button type="button" class="secondary-chess-button" data-action="chess-retry">Reset trial</button><button type="button" class="ghost-chess-button" data-action="chess-back-card">Return to selected card</button><button type="button" class="ghost-chess-button" data-action="chess-back-dashboard">Back to all key moments</button>`;
  return `<div class="moment-detail"><div class="moment-detail-top"><button type="button" class="back-to-moments" data-action="chess-back-card">&larr; Back to selected card</button><span class="selected-moment-state">OPTIONAL TRY</span></div><div class="moment-detail-body"><div class="moment-detail-heading"><span class="moment-category">QUEEN SAFETY \u00b7 SAFE EXPERIMENT</span><h2>Find the safer queen move.</h2><p>${chessScenario.reviewPrompt}</p></div>${feedback}</div><div class="detail-actions">${actions}</div></div>`;
}

function renderChessPractice() {
  const solved = chessState.attempt === "correct" || chessState.practiceDone;
  const feedback = chessState.attempt === "correct"
    ? `<div class="review-feedback"><span class="review-feedback-mark">&#10003;</span><span><strong>Good safety check.</strong>${chessScenario.practiceCorrectMove.notation} moves the queen away from the bishop's attack.</span></div>`
    : chessState.attempt === "wrong-source"
      ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>Select the queen first.</strong>Then choose a destination for that piece.</span></div>`
      : chessState.attempt === "wrong"
        ? `<div class="review-feedback is-error"><span class="review-feedback-mark">!</span><span><strong>That square is still unsafe.</strong>Select the queen again and retry.</span></div>`
        : "";
  return `<div class="moment-detail"><div class="moment-detail-top"><button type="button" class="back-to-moments" data-action="chess-back-card">&larr; Back to selected card</button><span class="selected-moment-state">OPTIONAL PRACTICE</span></div><div class="moment-detail-body"><div class="practice-lane ${chessState.practiceDone ? "is-complete" : ""}"><span class="practice-mark">${chessState.practiceDone ? "&#10003;" : "&#10022;"}</span><h3>${chessState.practiceDone ? "Practice complete." : "Find a safe queen square"}</h3><p>${chessState.practiceDone ? "You applied the same safety check in a new position." : chessScenario.practiceGoal}</p></div>${feedback}<div class="detail-explanation"><span>WHY THIS PRACTICE FITS</span><p>It repeats the same idea in a different static position: check the opponent's attack before moving a valuable piece.</p></div></div><div class="practice-actions">${solved && !chessState.practiceDone ? `<button type="button" class="primary-chess-button" data-action="chess-complete-practice">Complete practice</button>` : ""}<button type="button" class="secondary-chess-button" data-action="chess-retry">Reset practice</button><button type="button" class="ghost-chess-button" data-action="chess-back-card">Return to selected card</button><button type="button" class="ghost-chess-button" data-action="chess-back-dashboard">Back to all key moments</button></div></div>`;
}

function renderChess() {
  if (isStudyMode()) queueMicrotask(removeStudyChrome);
  const stage = document.getElementById("chessStage");
  const boardFrame = document.getElementById("chessBoardFrame");
  if (!stage || !boardFrame) return;
  const phase = chessState.view;
  const interactive = ["trial", "practice"].includes(phase) && chessState.attempt !== "correct" && !chessState.practiceDone;
  boardFrame.innerHTML = redesignedBoardPanel({ phase, interactive });
  stage.innerHTML = phase === "dashboard" ? renderChessDashboard() : phase === "detail" ? renderMomentDetail() : phase === "trial" ? renderChessTrial() : renderChessPractice();

  const moment = selectedChessMoment();
  const headerStatus = document.getElementById("chessHeaderStatus");
  const moveLabel = document.getElementById("chessBoardMoveLabel");
  const resultLabel = document.querySelector(".board-game-result");
  if (headerStatus) headerStatus.textContent = phase === "dashboard" ? `Game completed \u00b7 ${chessMoments.length} key moments` : phase === "detail" ? `Selected moment \u00b7 Move ${moment?.moveNumber || chessScenario.moveNumber}` : phase === "trial" ? "Optional try \u00b7 user controlled" : "Optional practice \u00b7 return available";
  if (moveLabel) moveLabel.textContent = phase === "dashboard" ? "NO CARD SELECTED" : phase === "practice" ? "PRACTICE POSITION" : `MOVE ${moment?.moveNumber || chessScenario.moveNumber}`;
  if (resultLabel) resultLabel.textContent = phase === "dashboard" ? "Choose any moment" : phase === "detail" ? "Selected card context" : phase === "trial" ? "Safe experiment" : "Related practice";

  const feedback = chessState.attempt === "correct"
    ? "Move accepted. The resulting position is visible."
    : chessState.attempt === "wrong-source"
      ? "Select the queen first."
      : chessState.attempt === "wrong"
        ? "That destination is still unsafe. Retry when ready."
        : "";
  const boardFeedback = document.getElementById("chessBoardFeedback");
  if (boardFeedback) {
    boardFeedback.hidden = !feedback;
    boardFeedback.className = `board-feedback-overlay ${["wrong", "wrong-source"].includes(chessState.attempt) ? "is-error" : ""}`.trim();
    boardFeedback.textContent = feedback;
  }
}

function chessHelpModal() {
  openModal({
    theme: "chess",
    kicker: "CARD REVIEW MODE",
    title: "Scan first, then choose.",
    copy: "The summary chips filter the same static key-moment cards. No card is selected for you and there is no required review order.",
    body: `<div class="glossary-grid"><div class="glossary-item"><strong>Key moment</strong><span>A recognizable completed-game position with a short learning cue.</span></div><div class="glossary-item"><strong>Review</strong><span>Open the explanation for any card you choose.</span></div><div class="glossary-item"><strong>Try this move</strong><span>An optional source-to-destination experiment inside one selected card.</span></div><div class="glossary-item"><strong>Practice</strong><span>An optional related position with a visible return to the card dashboard.</span></div></div>`,
    actions: `<button type="button" class="modal-primary" data-action="close-modal">Return to cards</button>`,
  });
}

function resetFifa() {
  Object.assign(fifaState, { selected: "pending", filter: "all", calendarAdded: false, notificationsEnabled: false, refreshing: false, error: false, returnNotice: false, lastUpdated: "2 min ago" });
  renderFifa();
  showToast("FIFA dashboard reset", "Both event states are visible again.");
}

function resetChess() {
  Object.assign(chessState, { view: "dashboard", selectedMoment: null, filter: "all", solutionRevealed: false, expandedDetail: false, attempt: null, selectedSquare: null, practiceDone: false, reviewedMoments: new Set() });
  renderChess();
}

function selectFifaEventFromTarget(target) {
  if (target.dataset.event && fifaEvents[target.dataset.event]) fifaState.selected = target.dataset.event;
}

function returnToChessDashboard() {
  Object.assign(chessState, { view: "dashboard", selectedMoment: null, solutionRevealed: false, expandedDetail: false, attempt: null, selectedSquare: null, practiceDone: false });
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
      fifaState.filter = "all";
      navigate("fifa");
      renderFifa();
      break;
    case "fifa-filter":
      fifaState.filter = target.dataset.filter || "all";
      fifaState.returnNotice = false;
      renderFifa();
      break;
    case "fifa-help":
      fifaHelpModal();
      break;
    case "fifa-dismiss-notice":
      fifaState.returnNotice = false;
      renderFifa();
      break;
    case "fifa-view-order":
      selectFifaEventFromTarget(target);
      fifaOrderModal();
      break;
    case "fifa-view-tickets":
      selectFifaEventFromTarget(target);
      fifaTicketsModal(fifaState.selected);
      break;
    case "fifa-calendar":
      selectFifaEventFromTarget(target);
      if (fifaState.selected !== "confirmed") break;
      fifaState.calendarAdded = true;
      renderFifa();
      showToast("Calendar event saved", "Toronto \u00b7 21 Jun 2026 is ready for your calendar.");
      break;
    case "fifa-open-handoff":
      selectFifaEventFromTarget(target);
      fifaHandoffModal();
      break;
    case "fifa-stay":
      closeModal();
      showToast("Still on FIFA.com", "Your ticket context and account states are unchanged.");
      break;
    case "fifa-continue-handoff":
      fifaHandoffCompleteModal();
      break;
    case "fifa-return":
      closeModal();
      fifaState.filter = "all";
      fifaState.returnNotice = true;
      navigate("fifa");
      renderFifa();
      showToast("Returned to FIFA dashboard", "Account context preserved; partner completion was not inferred.");
      break;
    case "fifa-notifications":
      fifaState.notificationsEnabled = !fifaState.notificationsEnabled;
      renderFifa();
      showToast(fifaState.notificationsEnabled ? "Status updates enabled" : "Status updates disabled", "This is a local demo cue only.");
      break;
    case "fifa-refresh":
      if (fifaState.refreshing) break;
      fifaState.refreshing = true;
      fifaState.error = false;
      renderFifa();
      window.setTimeout(() => {
        fifaState.refreshing = false;
        fifaState.lastUpdated = "just now";
        renderFifa();
        showToast("Statuses refreshed", "Both account records now show the latest demo timestamp.");
      }, 700);
      break;
    case "fifa-preview-error":
      if (isStudyMode()) break;
      fifaState.error = true;
      renderFifa();
      break;
    case "fifa-reset":
      if (!isStudyMode()) resetFifa();
      break;
    case "chess-help":
      if (!isStudyMode()) chessHelpModal();
      break;
    case "chess-filter":
      chessState.filter = target.dataset.filter || "all";
      renderChess();
      break;
    case "chess-select-card":
      if (!chessMoments.some((moment) => moment.id === target.dataset.moment)) break;
      chessState.selectedMoment = target.dataset.moment;
      chessState.reviewedMoments.add(target.dataset.moment);
      Object.assign(chessState, { view: "detail", solutionRevealed: false, expandedDetail: false, attempt: null, selectedSquare: null, practiceDone: false });
      renderChess();
      break;
    case "chess-back-dashboard":
      returnToChessDashboard();
      break;
    case "chess-toggle-detail":
      chessState.expandedDetail = !chessState.expandedDetail;
      renderChess();
      break;
    case "chess-reveal-solution":
      chessState.solutionRevealed = true;
      renderChess();
      break;
    case "chess-try-move":
      Object.assign(chessState, { view: "trial", attempt: null, selectedSquare: null, expandedDetail: false });
      renderChess();
      break;
    case "chess-practice":
      Object.assign(chessState, { view: "practice", attempt: null, selectedSquare: null, practiceDone: false, expandedDetail: false });
      renderChess();
      break;
    case "chess-back-card":
      Object.assign(chessState, { view: "detail", attempt: null, selectedSquare: null, practiceDone: false });
      renderChess();
      break;
    case "chess-square": {
      if (!["trial", "practice"].includes(chessState.view)) break;
      const move = chessMoveForPhase(chessState.view);
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
          if (chessState.view === "trial") chessState.solutionRevealed = true;
          showToast("Good move", `${move.notation} addresses the attack on the queen.`);
        }
      }
      renderChess();
      break;
    }
    case "chess-retry":
      chessState.attempt = null;
      chessState.selectedSquare = null;
      if (chessState.view === "practice") chessState.practiceDone = false;
      renderChess();
      break;
    case "chess-complete-practice":
      if (chessState.view !== "practice" || chessState.attempt !== "correct") break;
      chessState.practiceDone = true;
      chessState.selectedSquare = null;
      renderChess();
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
