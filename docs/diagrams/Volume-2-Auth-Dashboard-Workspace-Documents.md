# Multi-Agent Financial Research System
## UI/UX Design Specification — Volume 2 of 4
### Authentication · Onboarding · Dashboard · Workspace · Document Management · Upload Flow

References Volume 1 for all named components, colors, and tokens (e.g. "Primary Button," "Metric Card").

---

## Screen 1 — Landing Page

**Purpose:** Convert a first-time visitor (finance student/analyst) into a registered user by making the value proposition ("upload a report, ask a question, get a cited answer") viscerally obvious in under 5 seconds.

**Layout:** Full-bleed hero, single column, centered content, max-width 1200px container.
- Top: transparent nav bar (Logo left, "Login" + "Get Started" primary button right).
- Hero: H1 headline ("Ask your financial reports anything"), subheadline, primary CTA button, secondary "Watch demo" ghost button.
- Hero visual: the 3D orbiting-agents scene (Volume 1 §4.7.4), right-aligned on desktop, stacked below text on mobile.
- Below fold: 3-column "How it works" (Upload → Ask → Cite), 6-icon agent showcase strip, testimonial/stat band ("Zero hallucinated figures" trust badge), footer.

**Components:** Nav bar, Primary/Secondary buttons, 3D hero scene, Icon cards (agent showcase), Footer with Help Center link.

**Interactions:** CTA scrolls or routes to Register. "Watch demo" opens a modal video player. Agent icons on hover show a 1-line tooltip of that agent's job.

**States:** Static marketing page; only loading state is the 3D scene lazy-loading (static image fallback until interaction-ready).

**Animations:** 3D scene has slow (12s loop) ambient rotation; on-scroll fade-up (200ms) for each section, staggered 80ms per card.

**Responsive:** Mobile stacks hero text above visual; 3-column "how it works" becomes vertical stack; nav collapses to hamburger.

**Design Rationale:** Establishes the "trust through transparency" principle immediately via the citation-focused headline, before any feature list — this is the product's core differentiator and must lead.

---

## Screen 2 — Login

**Purpose:** Authenticate a returning user with minimal friction.

**Layout:** Centered card (max-width 400px) on a subtly branded `Neutral/100` background (small static 3D motif, low-opacity, top corner only — no distraction).
- Logo, "Welcome back" H2, email field, password field (with visibility toggle), "Forgot password?" link, Primary "Log In" button, divider "or", Google + GitHub OAuth buttons, footer link to Register.

**Components:** Text input ×2, Primary Button, Ghost link, OAuth buttons (icon + label, outline style), Toast (error).

**Interactions:** Submit on Enter key or button click. OAuth buttons route to Screen 4 bridge.

**States:** Default · Field focus · Field error (inline caption, red border) · Submitting (button shows spinner, disabled) · Auth failed (toast: "Invalid email or password").

**Animations:** Card fade+scale-in on load (200ms). Error shake (subtle, 2px, 150ms) on failed submit.

**Responsive:** Card becomes full-width with 16px side margins on mobile; OAuth buttons stack full-width.

**Design Rationale:** Single, unambiguous path with no distracting content — login should be the fastest screen in the product.

---

## Screen 3 — Register

**Purpose:** Create a new account with clear expectation-setting (email verification if applicable).

**Layout:** Same card pattern as Login, extended with Name field and a password-strength meter beneath the password field.

**Components:** Text input ×3 (Name, Email, Password), password strength meter (4-segment bar), checkbox ("I agree to Terms"), Primary Button, OAuth buttons.

**Interactions:** Real-time password strength feedback. Checkbox required before Primary Button enables (button disabled/40% opacity until checked).

**States:** Default · Validation errors per field (e.g., "Email already registered" inline, not just toast) · Submitting · Success (auto-redirect to Onboarding).

**Animations:** Strength meter segments fill with color transition (Danger → Warning → Success) over 150ms as password improves.

**Responsive:** Identical stacking pattern to Login.

**Design Rationale:** Surfacing "already registered" inline (not a generic toast) reduces user confusion and directs them to Login without a dead end.

---

## Screen 4 — OAuth Bridge Screen (Google / GitHub)

**Purpose:** Brief, reassuring transitional screen shown while the OAuth redirect/callback completes.

**Layout:** Centered, minimal: provider icon, "Connecting to Google…" text, indeterminate progress bar.

**Components:** Progress bar (indeterminate), provider logo.

**States:** Connecting · Success (auto-forwards to Dashboard or Onboarding if first login) · Failed (error card: "We couldn't connect your Google account" + Retry + Back to Login).

**Animations:** Provider logo subtle pulse while connecting.

**Responsive:** Identical across breakpoints (simple centered layout).

**Design Rationale:** OAuth redirects can feel like the app "broke" without an explicit bridge screen; this removes ambiguity.

---

## Screen 5 — Forgot / Reset Password

**Purpose:** Self-service password recovery.

**Layout:** Two sequential states in one route: (a) email entry card, (b) after email sent, a confirmation card with "check your email" illustration (2D icon, not 3D — utility screen). Reset link leads to a New Password card (password + confirm password fields).

**Components:** Text input, Primary Button, confirmation illustration, password fields with match-validation.

**States:** Email submitted · Link expired (error card with "Request new link") · Password reset success (redirects to Login with success toast).

**Design Rationale:** Kept deliberately plain/utilitarian — recovery flows should never introduce delight elements that slow the user down during a stressful moment (locked out of account).

---

## Screen 6 — Onboarding: Welcome Carousel

**Purpose:** Set expectations for the 6-agent system and the citation-grounding promise before the user's first upload.

**Layout:** Full-screen, 3-slide horizontal carousel, dot indicators, "Skip" top-right, "Next"/"Get Started" bottom-right.
- Slide 1: 3D illustration — document transforming into structured chunks. Headline: "Upload once, ask anything."
- Slide 2: 3D agent-badge lineup (all 6, small, in identity colors). Headline: "Six specialized AI agents work together."
- Slide 3: Chat bubble mockup with a citation pill highlighted. Headline: "Every answer traces back to the page."

**Components:** Carousel, dot pagination, Ghost "Skip" button, Primary "Next"/"Get Started" button.

**Interactions:** Swipe (touch) or arrow-key navigation; clicking a dot jumps to that slide.

**States:** N/A (linear, no error states) — "Skip" available at every slide.

**Animations:** Slide transition: horizontal slide 280ms ease. 3D illustrations have their idle ambient loop active throughout.

**Responsive:** Identical structure; illustrations scale down proportionally on mobile, text remains legible at 16px minimum.

**Design Rationale:** Establishing the agent mental model here (rather than discovering it ad hoc in the product) reduces confusion later in Agent Activity Monitor and chat attribution.

---

## Screen 7 — Onboarding: First Workspace Setup

**Purpose:** Get the user to their first tangible result (a processed document) as fast as possible.

**Layout:** Centered card with two clear paths, presented as large selectable tiles:
- Tile A: "Start with a sample company" (uses pre-loaded seed data — icon: building) → skips straight to a populated Workspace Overview.
- Tile B: "Upload my own report" → routes to Create Workspace (Screen 10) then Upload Documents (Screen 12).

**Components:** Selectable Tile card ×2 (icon, title, one-line description, chevron), Ghost "I'll do this later" link (routes to empty Dashboard).

**States:** Default · Tile hover (E2 elevation lift) · Tile selected (brief check animation before route transition).

**Design Rationale:** Removes the classic empty-state cold-start problem — a student can experience full value before ever finding/uploading their own document.

---

## Screen 8 — Dashboard (Home)

**Purpose:** Single-glance overview of the user's research activity: which workspaces need attention, what red flags exist, and quick actions.

**Layout:** 12-column grid.
- Row 1 (full width): Greeting header ("Good afternoon, Priya") + global "New Workspace" primary button, right-aligned.
- Row 2 (3 columns × 4): Summary Metric Cards — "Active Workspaces," "Documents Processed," "Open Red Flags" (color-coded by severity), "Reports Generated."
- Row 3 (8 col + 4 col split): Left — "Recent Workspaces" list (Workspace Cards, max 5, "View all" link to Workspace List). Right — "Agent Activity" mini-feed (last 5 agent completions across all workspaces, each a compact Agent Output Card).
- Row 4 (full width): "Attention Needed" band — surfaces any High-severity red flags across all workspaces as a horizontally scrollable card row, so risk is visible without opening each workspace.

**Components:** Metric Card ×4, Workspace Card, Agent Output Card (compact), Severity Badge, Primary Button.

**Interactions:** Clicking a Workspace Card routes to Workspace Overview. Clicking a red-flag attention card routes directly to that workspace's Red Flag Analysis tab (deep link).

**States:**
- **Populated** (described above).
- **Empty** (new user, no workspaces): replaces Rows 2–4 with a single centered Empty State (3D illustration + "Create your first workspace" CTA — see Volume 4 Empty States spec).
- **Loading:** Skeleton cards matching exact grid shape.

**Animations:** Cards stagger-fade-in (40ms delay increments) on first load only, not on every navigation return.

**Responsive:** Metric Cards collapse to 2×2 grid on tablet, single column on mobile. "Recent Workspaces" and "Agent Activity" stack vertically (Workspaces first) on mobile.

**Design Rationale:** The "Attention Needed" band operationalizes UX Goal #4 (confidence in AI activity) and Goal #1 (trust) by surfacing risk proactively rather than requiring the user to remember to check each workspace.

---

## Screen 9 — Workspace List

**Purpose:** Full management view of all workspaces (search, sort, bulk actions).

**Layout:** Header with search input (scoped) + sort dropdown (Recent/Name/Most Documents) + view toggle (grid/list) + "New Workspace" primary button. Below: grid of Workspace Cards (or list rows in list view).

**Components:** Workspace Card, Search input, Sort dropdown, view-toggle icon buttons, contextual menu (⋯) per card: Rename, Duplicate, Delete.

**Interactions:** Delete triggers a confirmation Modal ("This will permanently delete 3 documents, 12 chat messages, and 1 report. Type the workspace name to confirm.") — high-friction confirmation for destructive action per Principle 1.4.

**States:** Populated · Empty (see Volume 4) · Filtered-empty ("No workspaces match 'xyz'" with Clear Search action) · Loading (skeleton grid).

**Responsive:** Grid becomes 2-column (tablet) then 1-column (mobile); list view remains single column with condensed rows.

**Design Rationale:** Explicit typed-confirmation for delete reflects the "reversible, forgiving" principle — financial research data loss is high-stakes for a student's coursework.

---

## Screen 10 — Create Workspace (Stepper Modal)

**Purpose:** Guided creation of a new research workspace.

**Layout:** Modal, 2-step Stepper.
- Step 1: Workspace name input + optional description.
- Step 2: "Add documents now?" — either drag-and-drop zone (routes into Upload flow inline) or "Skip, I'll upload later" ghost button.

**Components:** Stepper, Text input, File Dropzone component, Primary/Ghost buttons.

**Interactions:** Name field validates uniqueness within the user's account in real time (debounced). Drag-and-drop accepts multi-file drop directly into Step 2.

**States:** Step 1 validation error (duplicate name) · Step 2 file-type rejected (non-PDF) inline error under dropzone.

**Animations:** Step transition slides horizontally 200ms; dropzone highlights with a dashed-border color shift + subtle scale (1.01) on drag-over.

**Responsive:** Modal becomes full-screen sheet on mobile.

**Design Rationale:** Combining creation + first upload into one flow reduces the multi-navigation friction of "create empty workspace, then separately find upload button."

---

## Screen 11 — Workspace Overview (Shell + Tabs)

**Purpose:** The persistent frame for all workspace-scoped work; hosts the tab strip (Chat, Documents, Metrics, Comparison, Red Flags, Agent Activity, Reports) detailed as their own tabs/screens.

**Layout:** Top Bar (Volume 1 §3.1: workspace name + switcher, tab strip, Upload icon button, "Generate Report" primary button). Below: active tab content fills remaining viewport.
- A persistent right-edge **Agent Status Rail** (collapsible, 280px) shows live status chips for all 6 agents relevant to the current workspace — visible from every tab, reinforcing "confidence in AI activity" globally, not just on the dedicated monitor screen.

**Components:** Top Bar, Tab Strip, Agent Status Rail (Agent Status Chip × 6), Icon Button, Primary Button.

**States:** Any agent in the rail can be `Idle/Running/Complete/Failed`; a `Failed` state shows a small red dot + "Retry" affordance directly in the rail without leaving the current tab.

**Responsive:** Agent Status Rail collapses to a single summary chip ("2 agents running") that expands as a bottom sheet on tap, on tablet/mobile.

**Design Rationale:** Making agent status ambient (always-visible rail) rather than confined to one monitor screen is the single highest-leverage trust-building UI decision in the product.

---

## Screen 12 — Upload Documents

**Purpose:** Add one or more financial PDFs to the active workspace.

**Layout:** Modal or dedicated tab state (accessible via Upload icon button in Top Bar). Large centered drag-and-drop zone with a subtle 3D document-stack illustration inside it at rest; "Browse files" secondary link beneath. Below: a list of files currently queued/uploading with per-file progress bars.

**Components:** File Dropzone, Progress Bar (per file), file-type/size validation caption, Primary "Upload" button (if manual confirm step is used) or auto-start on drop.

**Interactions:** Multi-file drag-and-drop; per-file remove (×) before upload starts; clicking a completed file routes into Document Processing (Screen 13) for that file.

**States:** Idle (empty dropzone) · Drag-over (highlighted) · Uploading (progress per file) · Upload error (invalid type/size — red inline message, file chip marked with error icon, "Remove" and "Try again") · All complete (success toast + auto-transition into Document Processing view).

**Animations:** Dropzone idle 3D illustration has a very slow (6s) breathing/float loop; on successful drop, illustration briefly "absorbs" the file icon (400ms) before switching to the upload list.

**Responsive:** Dropzone remains prominent but reduces height on mobile; file browsing via native file picker only (no drag-and-drop requirement on touch).

**Design Rationale:** The absorb animation is the one moment 3D motion directly communicates system behavior (file → data), satisfying the brief's 3D requirement without becoming decorative noise.

---

## Screen 13 — Document Processing (Live Status)

**Purpose:** Show the Document Agent's real-time pipeline progress (parse → clean → chunk → embed → index) so the wait feels transparent, not opaque.

**Layout:** Centered vertical stepper-timeline (not a generic progress bar) with 5 stages, each with an icon, label, and status. Above it, the 3D "document → particles → vector nodes" animation (Volume 1 §4.7.3) plays in sync with the current stage.

**Components:** Vertical Stepper (5 nodes: Parsing, Cleaning, Chunking, Embedding, Indexing), 3D processing animation, Agent Status Chip.

**States:**
- **In progress** — current stage pulses in its Agent-Document-Agent identity color (blue); completed stages show a green check; upcoming stages are greyed.
- **Complete** — full green stepper, auto-transition (after 1.5s dwell so user can register success) into Workspace Overview → Documents tab, with a success toast: "Report indexed. Extraction and Red Flag analysis starting automatically."
- **Failed at a stage** — that node turns red with an inline reason ("Could not extract text — file may be a scanned image without OCR support") + "Retry" and "Contact Support" actions.

**Animations:** Each stage transition triggers a small 3D "pulse" synced to the stepper node completing (600ms). This is the primary showcase moment for the 3D brief requirement — it should feel satisfying, not just informative.

**Responsive:** Stepper becomes horizontal-compact on mobile (icons only, label on tap) to fit viewport width; 3D animation scales down but stays present.

**Design Rationale:** Naming the actual pipeline stages (rather than a vague "Processing…") directly operationalizes Principle "Never a naked wait" and teaches the user the underlying RAG concept passively.

---

## Screen 14 — Document Library

**Purpose:** Manage all documents within a workspace (view status, delete, re-view metrics per document).

**Layout:** Table/grid toggle. Columns: Document name + thumbnail, Pages, Upload date, Status chip (Processing/Ready/Failed), quick actions (View Metrics, View Red Flags, Delete).

**Components:** Document Card (grid mode) or Table row (list mode), Status Chip, contextual menu, Search/filter bar (filter by status, company).

**Interactions:** Clicking a "Ready" document opens a contextual side panel summarizing its extracted metrics + red-flag count with links into the full Metrics/Red Flags tabs pre-filtered to that document. Delete opens a confirmation Modal warning that associated metrics, red flags, and citations tied only to this document will be removed.

**States:** Populated · Empty (see Volume 4) · A document mid-processing shows an inline mini-progress bar directly in its row/card (not just a static "Processing" label) so the library itself feels alive.

**Responsive:** Table collapses to card list on mobile; thumbnails hidden below `md` breakpoint to save space.

**Design Rationale:** Surfacing a live mini-progress bar in the library (rather than requiring a trip to Screen 13) keeps users oriented if they navigate away mid-processing — a common real-world behavior.

---

*End of Volume 2. Continue to Volume 3: AI Chat, Research Agent, Citations, Financial Analysis, Comparison, Red Flag Detection, Agent Activity Monitor.*
