# kuraOS-An-Agentic-Healthcare-Orchestrator

🩺 Kuro OS: Med-AI Multi-Agent System 

Kuro OS is an intelligent orchestrator-led medical assistant designed to streamline clinical workflows. It utilizes a Multi-Agent System (MAS) architecture to handle patient intake, automated scheduling, clinical documentation, and prescription drafting.

🏗️ High-Level ArchitectureKuro OS operates on a layered architecture that separates intent understanding from tool execution. This ensures scalability, modularity, and medical auditability.

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

Developed for clinical efficiency and AI-driven healthcare assistance.
