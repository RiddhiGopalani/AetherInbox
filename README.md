# AetherInbox

An autonomous email classification and dynamic priority-ranking engine. AetherInbox integrates machine learning for semantic intent triage with a relational database tracking thread density and domain signatures to eliminate inbox noise and prevent high-stakes notification loss.

## The Problem
Standard email clients sort messages chronologically, causing critical, time-sensitive communications (such as recruitment updates, coding assessments, and urgent academic notices) to get buried beneath high-volume marketing broadcasts, platform alerts, and automated newsletters. Furthermore, rigid global spam filters frequently misclassify legitimate outreach from new professional domains, resulting in missed opportunities.

## The Solution
AetherInbox decouples email streaming from simple keyword matching by implementing a dual-layered architectural triage pipeline:
1. **DBMS Layer (The Context Graph):** Utilizes a relational schema to autonomously track global ATS infrastructure domains, parse multi-tiered conversation threads, and calculate a dynamic Sender Reputation Matrix without manual whitelisting.
2. **AI Layer (Semantic Intent Triage):** Employs natural language processing to extract the underlying transactional intent of a message (e.g., direct human outreach vs. automated broadcast) rather than relying on surface keywords.

## Core Tech Stack
* **Backend:** FastAPI (Asynchronous Python)
* **Database:** PostgreSQL (via Supabase) with Row-Level Security (RLS)
* **Task Queue:** Celery + Redis (Asynchronous Background Pipeline)
* **AI/ML Layer:** Hugging Face Transformers & Sentence-Transformers
* **Frontend:** Streamlit (Data-Centric UI Dashboard)
* **Authentication:** Google OAuth 2.0
