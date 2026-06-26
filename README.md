# AI Job Application Copilot

## Problem Statement
Job seekers spend hours every day manually reading job descriptions, tailoring resumes, and tracking applications across dozens of tabs and spreadsheets — most of that time goes into repetitive work, not into actually improving the quality of each application. AI Job Application Copilot helps users parse their resume into structured data, score how well it matches a given job description, generate tailored content grounded in their real experience, and track every application in one place — with a human approving every submission, not a bot applying on their behalf.


## Tech Stack
- **Backend:** Django + Django REST Framework (auth, data models, business logic)
- **ML/AI Service:** FastAPI (resume parsing, embeddings, RAG pipeline, LLM calls)
- **Database:** PostgreSQL
- **Frontend:** React (application tracker, dashboard)
- **LLM Provider:** [OpenAI / Anthropic — fill in once decided]

## AI Architecture: How the RAG Pipeline Works

This project uses **Retrieval-Augmented Generation (RAG)** rather than relying on an LLM's raw output, specifically to prevent hallucination — the system never lets the model invent experience the user doesn't have.

1. **Ingestion** — resume text is extracted (PDF/DOCX) and parsed into structured fields (skills, projects, experience) via an LLM call with a strict output schema.
2. **Embedding** — each structured experience/project entry is converted into a vector embedding and stored, so it can be retrieved by semantic similarity later (not just keyword match).
3. **Retrieval** — when a job description is provided, it's also embedded, and compared against the user's stored experience entries using cosine similarity. This produces the match score and surfaces the most relevant pieces of the user's real background for that specific job.
4. **Grounded generation** — only the retrieved, real experience entries are passed into the LLM's context when generating tailored bullets/cover-letter content. The model is explicitly instructed not to introduce skills or claims that aren't present in the retrieved data — this is the core hallucination-prevention mechanism.
5. **Human review** — every generated output is shown to the user for approval/edit before it's used anywhere. No content or application is sent without human sign-off.

## Key AI/ML Concepts Used
- **LLM (Large Language Model)** — used for structured resume parsing and grounded content generation
- **Embeddings & semantic similarity** — used for JD-to-resume match scoring
- **RAG (Retrieval-Augmented Generation)** — retrieval step grounds every generation in the user's real data
- **Hallucination prevention** — strict grounding + human-in-the-loop review, not just prompt instructions
- **Structured output parsing** — Pydantic schema validation on all LLM outputs

## Status
🚧 In active development. Architecture, setup instructions, and evaluation metrics will be added as features are built out.