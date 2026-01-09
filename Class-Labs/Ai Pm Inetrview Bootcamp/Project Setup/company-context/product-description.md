# LegalGraph Product Overview

**Your complete guide to the LegalGraph product**

---

## What is LegalGraph?

LegalGraph is an AI-powered contract review platform for in-house legal teams. Think **"Ironclad meets ChatGPT"** - enterprise-grade like Ironclad, AI-intelligent like ChatGPT, but built specifically for pre-signature contract review at mid-market companies.

### Core Value Proposition

**For in-house legal teams overwhelmed by contract volume,** LegalGraph is an AI contract review platform **that automatically extracts clauses, scores risk, and enforces legal playbooks.** Unlike Ironclad (expensive, full CLM) or LawGeex (limited to basic contracts), LegalGraph **provides clause-level precision with customizable AI, at 60% lower cost.**

---

## Product Philosophy

### Key Principles

**1. AI augments lawyers, never replaces them**
- Lawyers make final decisions
- AI handles tedious extraction and analysis
- Human expertise + machine speed = better outcomes
- Confidence scores on everything

**2. Accuracy is non-negotiable**
- 95%+ accuracy or we don't ship
- Clear "AI uncertain" flags
- Validated on thousands of contracts
- Transparency on model limitations

**3. Customization is critical**
- Every legal team has different playbooks
- Train on YOUR contracts, YOUR standards
- One-size-fits-all AI doesn't work in legal
- Continuous learning from feedback

**4. Security is table stakes**
- SOC 2 Type II certified
- Data encryption at rest and in transit
- Zero-retention policy option
- On-premise deployment available

**5. Speed unlocks value**
- Contracts reviewed in minutes, not hours
- Real-time collaboration
- Instant playbook updates
- No 6-month implementations

---

## Core Features

### 1. Contract Upload & Processing

**What users can do:**
- Drag-and-drop upload (PDF, Word, images)
- OCR for scanned documents
- Batch processing (up to 100 contracts at once)
- Auto-detect contract type (MSA, NDA, lease, etc.)
- Version comparison (track redlines)

**Our differentiation:**
- **Smart OCR:** 99%+ accuracy even on poor scans
- **Instant processing:** 50-page contract processed in 30 seconds
- **15+ document types:** Not just NDAs - MSAs, leases, employment, vendor, customer contracts
- **No file size limits:** Handle 1,000-page real estate portfolios

**Technical details:**
- Supports: PDF, DOCX, DOC, images (JPG, PNG)
- Max batch size: 100 contracts or 2GB
- Processing speed: ~2 seconds per page
- OCR engine: Custom-trained on legal documents

### 2. AI-Powered Clause Extraction

**What users can do:**
- Automatically identify and extract 200+ clause types
- Custom clause definitions (train AI on your clauses)
- Clause comparison across contracts
- Search extracted clauses portfolio-wide
- Export clauses to spreadsheet

**Supported clause types (examples):**
- **Liability:** Indemnification, limitation of liability, warranty disclaimers
- **IP:** Ownership, licensing, assignment, work-for-hire
- **Compliance:** Data privacy, GDPR, CCPA, confidentiality
- **Financial:** Payment terms, pricing, penalties, late fees
- **Termination:** Termination for cause, termination for convenience, notice periods
- **Dispute:** Governing law, jurisdiction, arbitration, class action waivers
- **Operational:** Service levels, support, training, implementation

**Our differentiation:**
- **Clause-level precision:** Extract exact text, page number, section reference
- **Confidence scores:** 0-100% confidence on every extraction
- **Custom training:** Add your own clause types (takes 10 examples)
- **Context awareness:** Understands clause relationships (e.g., indemnity caps tied to liability limits)

**Accuracy:**
- Standard clauses: 96% precision, 94% recall
- Custom clauses (after training): 92% precision, 89% recall
- OCR + extraction combined: 94% end-to-end accuracy

### 3. Risk Scoring & Analysis

**What users can do:**
- Multi-dimensional risk assessment across 15+ risk categories
- Overall risk score: Low / Medium / High / Critical
- Risk explanations (why is this risky?)
- Compare contract risk to company standards
- Portfolio risk heatmaps

**Risk dimensions:**
- **Liability Risk:** Uncapped indemnity, broad liability, no exclusions
- **IP Risk:** Unclear ownership, broad licensing, assignment clauses
- **Compliance Risk:** Missing data privacy, GDPR gaps, no confidentiality
- **Financial Risk:** Unfavorable payment terms, high penalties, auto-renewal
- **Termination Risk:** Difficult exit, long notice periods, no termination for convenience
- **Vendor Lock-in:** Long term, auto-renewal, high switching costs
- **Data Security:** No security standards, no breach notification
- **Operational Risk:** Unrealistic SLAs, no support, implementation risk

**Our differentiation:**
- **Explainable AI:** Every risk score includes specific reasons
- **Customizable thresholds:** Define what "high risk" means for your company
- **Benchmarking:** Compare to industry standards (coming Q2 2025)
- **Trend analysis:** Track risk over time across contract portfolio

**Example risk output:**
```
Overall Risk: HIGH (73/100)

Liability Risk: CRITICAL
- Unlimited indemnification (Section 8.1)
- No liability cap (missing)
- No mutual indemnification (one-way, we indemnify them)

IP Risk: MEDIUM
- Work product ownership unclear (Section 5.2)
- Broad license grant to vendor (Section 5.3)

Recommendation: Negotiate liability cap and mutual indemnification before signing.
```

### 4. Playbook Management

**What users can do:**
- Create digital legal playbooks (approval matrix, fallback positions)
- Define approved clause language
- Set risk thresholds per clause type
- Approval workflows (who approves what risk level)
- Deviation detection and flagging

**Playbook components:**
- **Preferred language:** "We prefer X clause language"
- **Acceptable alternatives:** "We can accept Y as fallback"
- **Red lines:** "Never accept Z"
- **Approval matrix:** "High risk requires GC approval"
- **Context:** "Why this matters: [explanation]"

**Our differentiation:**
- **Version control:** Track playbook changes over time
- **A/B testing:** Test different negotiation strategies
- **Learning:** AI learns from accepted deviations
- **Templates:** Start with industry-standard playbooks

**Example playbook rule:**
```
Clause: Limitation of Liability
Preferred: "Liability capped at 12 months of fees paid"
Acceptable: "Liability capped at 6 months of fees paid"
Red line: "No cap or less than 3 months of fees"
Approval: High risk = GC approval required
Rationale: Protects company from unlimited liability exposure
```

### 5. Collaboration & Workflow

**What users can do:**
- Real-time commenting on specific clauses
- @mention team members
- Assign contracts for review
- Approval workflows (multi-stage)
- Slack/Teams/email notifications
- Activity log (who did what, when)

**Our differentiation:**
- **Clause-level comments:** Comment on specific clauses, not entire document
- **Threaded discussions:** Organized conversations, not scattered
- **Decision tracking:** Mark comments as "Approved" or "Needs negotiation"
- **Audit trail:** Complete history for compliance

**Workflow example:**
1. Contract uploaded → Auto-assigned to junior attorney (based on type)
2. Junior reviews → Flags high-risk clauses
3. Senior reviews → Approves or escalates to GC
4. GC reviews → Approves or sends to business for negotiation
5. Business negotiates → Tracks in LegalGraph
6. Final approval → Audit trail complete

### 6. Analytics & Reporting

**What users can do:**
- Contract portfolio dashboard
- Risk heatmaps (which contracts are riskiest?)
- Processing time savings calculator
- Clause compliance rates
- Custom reports (filter by anything)
- Executive dashboards for GC

**Key reports:**
- **Volume report:** Contracts reviewed per week/month
- **Risk report:** High-risk contracts requiring attention
- **Velocity report:** Time from upload to approval
- **Compliance report:** % of contracts meeting playbook standards
- **ROI report:** Time saved × attorney hourly rate

**Our differentiation:**
- **Automatic insights:** "30% of vendor contracts have uncapped indemnity"
- **Predictive analytics:** "At current pace, backlog will clear in 3 weeks"
- **Benchmarking:** Compare to industry averages (coming Q2 2025)

**Example dashboard:**
```
Portfolio Summary (Last 30 days)
- Contracts reviewed: 127
- Average processing time: 18 minutes (vs 3.5 hours manual)
- Time saved: 408 hours ($122,400 at $300/hour)
- High-risk contracts: 23 (18%)
- Playbook compliance: 87%
```

### 7. Integrations

**What users can do:**
- **DocuSign:** Import signed contracts, trigger review before signing
- **Adobe Sign:** Same as DocuSign
- **Salesforce:** Pull contracts from opportunities, push review status
- **NetSuite/SAP:** Link contracts to vendors/customers
- **Slack:** Notifications, alerts, approvals
- **Microsoft Teams:** Same as Slack
- **Box/Google Drive/SharePoint:** Sync contracts automatically
- **Email:** Forward contracts to LegalGraph for review

**Our differentiation:**
- **Two-way sync:** Changes in LegalGraph update connected systems
- **Workflow automation:** "When contract uploaded to Salesforce → auto-review in LegalGraph"
- **API-first:** Build custom integrations (REST API)

**Coming integrations (Q2 2025):**
- Ironclad (pre-review integration)
- Clio (law firm management)
- Jira (for legal teams using Jira)

---

## Product Roadmap (Simplified)

### Already Shipped (Current Product)

- Contract upload & OCR processing
- AI clause extraction (200+ types)
- Risk scoring (15+ dimensions)
- Playbook management
- Collaboration (comments, @mentions)
- Basic analytics dashboard
- Integrations (DocuSign, Salesforce, Slack)
- SOC 2 Type II certification

### In Progress (Q4 2024 - Q1 2025)

- **Contract Negotiation Assistant** (AI-powered redline suggestions)
- **Advanced risk analytics** (predictive, portfolio-level)
- **Multi-language support** (Spanish, French, German)
- **Custom clause training** (10-example learning)
- **Bulk playbook updates** (change rules across all contracts)

### Planned (Q2-Q3 2025)

- **Benchmarking** (compare terms to industry standards)
- **Contract drafting assistant** (AI-generated first drafts)
- **Law firm edition** (firm-specific features)
- **Advanced integrations** (Ironclad, Clio, NetSuite, SAP)
- **Mobile app** (iOS and Android, review-on-the-go)

### Research Phase (Exploring)

- **Automated negotiation** (AI negotiates routine terms)
- **Contract lifecycle management** (full CLM, not just review)
- **Legal research integration** (link to case law, statutes)
- **Multi-party contracts** (3+ party agreements)
- **Regulatory compliance alerts** (new laws affecting contracts)

---

## Product Metrics

### North Star Metric

**Contracts Reviewed Per Month** - Number of contracts processed through LegalGraph

**Why this metric?**
- Indicates actual usage (not just logins)
- Measures value delivery (time saved)
- Leading indicator of retention
- Correlates with revenue (more contracts = higher value)

**Current:** 12,500 contracts/month
**Goal (Q1 2025):** 18,000 contracts/month

---

### Product Health Metrics

**Activation:**
- **Definition:** User reviews first contract within 7 days of signup
- **Current:** 55%
- **Target:** 70%
- **Why it matters:** Activated users are 8x more likely to become paying customers

**AI Accuracy:**
- **Definition:** Clause extraction precision (% of extracted clauses that are correct)
- **Current:** 94%
- **Target:** 96%+
- **Why it matters:** Accuracy drives trust, trust drives adoption

**Time Saved Per Contract:**
- **Definition:** Manual review time minus LegalGraph review time
- **Current:** 3.5 hours saved per contract
- **Target:** 4+ hours
- **Why it matters:** Time saved = ROI = retention

**Retention:**
- **Definition:** % of customers active in month N who are active in month N+12
- **Current:** 92% (enterprise), 68% (SMB)
- **Target:** 95% (enterprise), 80% (SMB)
- **Why it matters:** Retention drives LTV and revenue growth

**Playbook Compliance:**
- **Definition:** % of contracts meeting playbook standards
- **Current:** 72%
- **Target:** 85%
- **Why it matters:** Compliance = risk reduction = value delivery

---

## Pricing & Packaging

### Current Plans

**Starter Plan ($8,000/year):**
- 1-3 users
- 100 contracts/month
- Standard clause extraction (200+ types)
- Risk scoring (all dimensions)
- Email support
- 30-day data retention

**Professional Plan ($25,000/year):**
- 5-10 users
- 500 contracts/month
- Custom clause training
- Playbook management
- Integrations (DocuSign, Salesforce, Slack)
- Priority support
- 2-year data retention

**Enterprise Plan ($45,000+/year):**
- Unlimited users
- Unlimited contracts
- Everything in Professional
- Advanced analytics dashboard
- Custom integrations (API access)
- Dedicated customer success manager
- On-premise deployment option
- Unlimited data retention
- SLA guarantees (99.9% uptime)

### Competitive Pricing

| Tool | Entry Price | Mid-tier | Enterprise |
|------|------------|----------|------------|
| **LegalGraph** | $8k/year | $25k/year | $45k/year |
| Ironclad | $50k/year | $150k/year | $300k+/year |
| Kira Systems | $30k/year | $80k/year | $150k/year |
| LawGeex | $15k/year | $50k/year | $80k/year |
| Evisort | $40k/year | $100k/year | $180k/year |

**Our strategy:** 40-60% lower cost than enterprise competitors, premium positioning vs point solutions.

---

## Technology Stack

**Frontend:**
- React + TypeScript
- Tailwind CSS
- React Query (data fetching)
- WebSockets (real-time collaboration)

**Backend:**
- Python + FastAPI
- PostgreSQL (primary database)
- Redis (caching, job queues)
- S3 (contract storage, encrypted)
- Elasticsearch (full-text search)

**AI/ML:**
- Custom NLP models (transformer-based)
- GPT-4 and Claude 3 (fine-tuned on legal corpus)
- spaCy, Hugging Face Transformers
- 500k+ contracts in training dataset
- Continuous learning from user feedback

**Infrastructure:**
- AWS (hosting: US East, EU West)
- CloudFront (CDN)
- Docker + Kubernetes
- Terraform (infrastructure as code)

**Security:**
- SOC 2 Type II certified
- GDPR and CCPA compliant
- AES-256 encryption (at rest and in transit)
- SSO (SAML, OAuth)
- Role-based access control (RBAC)
- Audit logs (immutable)

---

## Product Principles in Action

### Example: How we built Risk Scoring

**Principle: AI augments lawyers, never replaces**
- AI flags risks, lawyers decide what to do
- Confidence scores on every risk (transparency)
- "AI uncertain" warnings (honesty about limitations)
- Final decision always with lawyer

**Principle: Accuracy is non-negotiable**
- 94%+ accuracy validated on 10,000 test contracts
- Monthly accuracy audits (internal + external)
- User feedback loop (report incorrect extractions)
- Model retraining every quarter

**Principle: Customization is critical**
- Risk thresholds customizable per company
- Custom risk dimensions (add your own)
- Playbook defines what "risky" means
- AI learns from your decisions

**Result:** 92% of users trust risk scores, 78% follow AI recommendations

---

## Your Projects This Quarter

As the Senior PM for AI/ML and Contract Review, you're working on:

**Project 1: Contract Negotiation Assistant**
- Goal: Launch AI-powered redline suggestions
- Timeline: Q1 2025
- Status: PRD in progress (you'll write this!)

**Project 2: Advanced Risk Analytics**
- Goal: Portfolio-level risk insights for GCs
- Timeline: Q1 2025
- Status: Research phase

**Project 3: Multi-language Support**
- Goal: Support Spanish, French, German contracts
- Timeline: Q2 2025
- Status: Planning

---

## Product Documentation

All product documentation lives in:
- **Notion:** Product specs, PRDs, research, roadmap
- **Figma:** Designs, mockups, design system
- **GitHub:** Technical specs, API docs, ML model docs
- **LegalGraph:** Dogfooding! (we review our own contracts)

---

## Key Use Cases in Detail

### Use Case 1: High-Volume NDA Review

**User:** Associate General Counsel
**Scenario:** Review 50 NDAs per week from vendors

**Before LegalGraph:**
- 30 minutes per NDA × 50 = 25 hours/week
- Manual extraction of key terms (mutual/one-way, term, exceptions)
- Inconsistent risk assessment
- Missed edge cases

**After LegalGraph:**
- Upload batch of 50 NDAs
- AI processes all 50 in 15 minutes
- Auto-extracts: mutual/one-way, term length, exceptions, return/destroy language
- Flags 8 as "high risk" (one-way, short term, no carve-outs)
- Attorney reviews only the 8 high-risk (30 minutes total)
- Approves 42 standard NDAs in batch (5 minutes)

**Result:** 25 hours → 50 minutes (97% time savings)

---

### Use Case 2: Complex MSA Negotiation

**User:** Senior Counsel
**Scenario:** Negotiate Master Service Agreement with Fortune 500 customer

**Before LegalGraph:**
- 6 hours over 3 days (manual review, spreadsheet tracking)
- Compare 50-page MSA to company standards (mentally)
- Miss subtle risk issues
- Negotiation strategy reactive (respond to their redlines)

**After LegalGraph:**
- Upload 50-page MSA (processing: 2 minutes)
- AI extracts all key terms, flags 12 deviations from playbook
- Risk score: HIGH (liability uncapped, IP rights unclear, auto-renewal)
- Negotiation assistant suggests: "Add liability cap of 12 months fees (our standard)"
- Precedent search: "We've accepted 6-month cap with similar customers"
- Generate redline with suggested changes (exports to Word)

**Result:** 6 hours → 45 minutes (88% time savings), proactive negotiation strategy

---

### Use Case 3: Real Estate Portfolio Due Diligence

**User:** Real Estate Counsel (law firm serving client)
**Scenario:** Review 200 commercial leases for acquisition due diligence

**Before LegalGraph:**
- 2 associates × 80 hours each = 160 billable hours ($80k at $500/hour)
- Manual spreadsheet of key lease terms
- Risk analysis subjective, inconsistent
- 2 weeks turnaround time

**After LegalGraph:**
- Upload 200 leases (batch processing: 45 minutes)
- AI extracts: rent, term, renewal options, early termination, tenant improvements, subleasing
- Risk scoring: 23 leases flagged as high-risk (unfavorable terms)
- Portfolio analytics: Average lease term 7.2 years, 34% have co-tenancy clauses, 12% missing estoppel rights
- Associates review only high-risk leases (30 hours)
- Export complete due diligence report

**Result:** 160 hours → 30 hours (81% savings), $80k → $15k billable, 2 weeks → 3 days

---

**Throughout this course, you'll write PRDs, conduct user research, analyze competitors, and plan features for LegalGraph. You're not learning in a vacuum - you're working on a real (fictional) AI legal tech product!**