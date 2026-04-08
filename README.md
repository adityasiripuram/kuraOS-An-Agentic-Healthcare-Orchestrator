# kuraOS-An-Agentic-Healthcare-Orchestrator

🩺 Kuro OS: Med-AI Multi-Agent System 

Kuro OS is an intelligent orchestrator-led medical assistant designed to streamline clinical workflows. It utilizes a Multi-Agent System (MAS) architecture to handle patient intake, automated scheduling, clinical documentation, and prescription drafting.

🏗️ High-Level Architecture Kuro OS operates on a layered architecture that separates intent understanding from tool execution. This ensures scalability, modularity, and medical auditability.

The Agent LineupIntake Agent (The Front Desk): Analyzes patient sentiment, triage urgency, and identifies intent.

Calendar Agent (The Coordinator): Interface for scheduling logic; interacts with the Calendar Tool via MCP.

Notes Agent (The Scribe): Captures raw consultation dialogue and converts it into structured clinical observations.

Scribe Agent (The Assistant): Processes clinical notes to generate draft prescriptions (Rx) and treatment plans.

🚀 Deployment The system is containerized using Docker and deployed to Google Cloud Run for serverless scalability.Quick Deploy CommandBashgcloud run deploy kuro-os \
    --source . \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_CLOUD_PROJECT=[YOUR_PROJECT_ID]
    
Note: Ensure a .gcloudignore file is present to exclude large local environments (like venv/) to keep deployment fast and lean.

🛠️ Tech Stack Layer Technology Framework FastAPI (Python 3.12)AI EngineVertex AI - Gemini 1.5 FlashDatabaseGoogle Cloud Firestore (Native Mode)DeploymentGoogle Cloud Run & Artifact RegistryConnectivity 

Model Context Protocol (MCP)🚦 Usage & Sample PromptsOnce deployed, you can interact with the system via the /ask endpoint.

1. Scheduling Prompt: "I need to book an urgent appointment for my heart pain. 
"Workflow: Intake (Urgency Flag) ➔ Calendar Agent ➔ Firestore Tool.

2. Clinical DocumentationPrompt: "Note: Patient reports persistent dry cough and mild fever for 3 days.
"Workflow: Intake ➔ Notes Agent ➔ Firestore Clinical Notes.

3. Medical Inquiry (Fallback) Prompt: "What are the common symptoms of high blood pressure?"Workflow: Intake ➔ General LLM (Gemini).


📊 Workflow DiagramCode snippetgraph LR
    A[User Input] --> B{Orchestrator}
    B --> C[Intake Agent]
    C --> D{Routing Logic}
    D -- Scheduling --> E[Calendar Agent]
    D -- Observation --> F[Notes Agent]
    D -- General Qs --> G[Gemini 1.5 Flash]
    E --> H[(Firestore: Slots)]
    F --> I[(Firestore: Notes)]
    I --> J[Scribe Agent: Draft Rx]

📜 Database Collections

calendar_slots: Stores confirmed appointments and timestamps.

clinical_notes: Stores structured medical observations.
agent_logs: A global audit log of every system decision and path taken.
Live link

Gemini said
For your demo of Kuro OS, you want to showcase the "intelligence" of the orchestrator—how it distinguishes between a logistics task (scheduling), a clinical task (note-taking), and a knowledge task (medical AI).

Here are the best sample prompts categorized by the "Success Path" they demonstrate.

1. The Scheduling Path (The "Efficiency" Demo)
Goal: Show how the system handles the front-office workload.

Standard Request: "I'd like to book a follow-up appointment for next Tuesday at 2 PM."

The "Urgency" Test: "I need to book an urgent appointment, I've had a sharp pain in my chest for the last hour."

Demo Tip: Point out how the Intake Agent identifies the word "urgent" and flags it in the backend logs.

2. The Clinical Scribe Path (The "Doctor's Assistant" Demo)
Goal: Show how the system captures data during a consultation.

Observation: "Record a note: Patient's blood pressure is 140/90, and they report recurring migraines."

Patient History: "Take a record: Patient has a history of seasonal allergies and was prescribed antihistamines in 2024."

Demo Tip: Show the Firestore "clinical_notes" collection immediately after this to prove the data was structured and saved.

3. The Medical Knowledge Path (The "Expert" Demo)
Goal: Show the fallback to the LLM (Gemini) for unstructured medical queries.

General Inquiry: "What is the typical recovery timeline for a laparoscopic gallbladder surgery?"

Comparative: "Explain the difference between Type 1 and Type 2 diabetes to a patient who was just diagnosed."

4. The "Stress Test" (The Routing Logic Demo)
Goal: Show that the system doesn't get confused by overlapping keywords.

Complex Intent: "I need to schedule a visit because the note I took earlier about my fever says it's getting worse."

What to watch for: See if the Orchestrator prioritizes the Schedule action (Calendar) or the Note action (Clinical). In your current code, it will trigger the Calendar Agent.

Live Link:
 
 [![Live Demo](https://img.shields.io/badge/Demo-Live_on_Cloud_Run-blue?style=for-the-badge&logo=googlecloud)](https://kuro-os-220370152341.us-central1.run.app/docs)

📥 Demo Script Flow
If you are presenting this to an audience, follow this 3-step sequence to tell a story:

Step	 Action	 The Story


Step 1	Scheduling Prompt	"First, Kuro OS handles the patient's entry into the system without human intervention."

Step 2	Clinical Note Prompt	"Once the patient is with the doctor, the system acts as a scribe, capturing vital signs and observations."

Step 3	Check the DB	"Finally, we see that all this data is securely stored in Firestore, ready for the Scribe Agent to draft a prescriptio


Developed for clinical efficiency and AI-driven healthcare assistance.
