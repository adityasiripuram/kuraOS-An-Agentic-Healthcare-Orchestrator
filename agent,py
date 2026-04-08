from fastapi import FastAPI, HTTPException
from langchain_google_vertexai import ChatVertexAI
from google.cloud import firestore

app = FastAPI(
    title="Kura OS:  An Agentic Healthcare Orchestrator",
    description="Orchestrator-led system for Appointments and Clinical Notes."
)

# Initialize Firestore - ensures we use the (default) database
db = firestore.Client()

# Initialize Gemini 1.5 Flash
llm = ChatVertexAI(
    model_name="gemini-1.5-flash",
    location="us-central1"
)

# --- 5. TOOLS: EXECUTION LAYER (Write to DB) ---

def calendar_tool_execute(appointment_details: dict):
    """The Tool that specifically handles calendar database writes."""
    doc_ref = db.collection("calendar_slots").document()
    doc_ref.set({
        **appointment_details,
        "status": "booked",
        "created_at": firestore.SERVER_TIMESTAMP
    })
    return doc_ref.id

def notes_tool_execute(note_details: dict):
    """The Tool that specifically handles clinical notes database writes."""
    doc_ref = db.collection("clinical_notes").document()
    doc_ref.set({
        **note_details,
        "created_at": firestore.SERVER_TIMESTAMP
    })
    return doc_ref.id

# --- 4. AGENTS: ACTION LAYER (Decide Structure) ---

def calendar_agent_act(intake_data: str):
    """The Calendar Agent structures the data for the execution tool."""
    action_payload = {
        "event_type": "Doctor Appointment",
        "details": intake_data,
        "duration": "30m"
    }
    slot_id = calendar_tool_execute(action_payload)
    return f"✅ Appointment Slot {slot_id} successfully booked."

def notes_agent_act(intake_data: str):
    """The Notes Agent structures the clinical data for the execution tool."""
    action_payload = {
        "category": "Clinical Observation",
        "content": intake_data
    }
    note_id = notes_tool_execute(action_payload)
    return f"📝 Clinical note {note_id} saved to patient record."

# --- 3. AGENT: INTAKE LAYER (Understand Context) ---

def intake_agent_understand(prompt: str):
    """Analyzes if the request has high priority or specific context."""
    if "urgent" in prompt.lower() or "emergency" in prompt.lower():
        return f"PRIORITY: {prompt}"
    return prompt

# --- 2. ORCHESTRATOR: ROUTING LAYER ---

@app.post("/ask")
async def orchestrator(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Empty prompt.")

    try:
        # Step 1: Intake Agent analyzes the prompt
        refined_context = intake_agent_understand(prompt)
        p_lower = prompt.lower()
        
        # Step 2: Routing Logic
        if any(w in p_lower for w in ["schedule", "appointment", "book", "slot"]):
            # Trigger Calendar Agent
            final_result = calendar_agent_act(refined_context)
            decision_path = "Intake -> Calendar Agent -> Calendar Tool"
            
        elif any(w in p_lower for w in ["note", "record", "observation", "patient says"]):
            # Trigger Notes Agent
            final_result = notes_agent_act(refined_context)
            decision_path = "Intake -> Notes Agent -> Notes Tool"
            
        else:
            # Fallback to General AI (Gemini)
            ai_resp = llm.invoke(prompt)
            final_result = ai_resp.content
            decision_path = "Intake -> General LLM Response"

        # Step 3: Global Audit Log
        db.collection("agent_logs").add({
            "user_input": prompt,
            "decision": decision_path,
            "response": final_result,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        return {
            "orchestrator_decision": decision_path,
            "agent_output": final_result
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Flow Error: {str(e)}")

# --- 1. RETRIEVAL ENDPOINTS ---

@app.get("/calendar")
async def get_calendar():
    docs = db.collection("calendar_slots").order_by("created_at", direction=firestore.Query.DESCENDING).stream()
    return [{"id": d.id, **d.to_dict()} for d in docs]

@app.get("/notes")
async def get_notes():
    docs = db.collection("clinical_notes").order_by("created_at", direction=firestore.Query.DESCENDING).stream()
    return [{"id": d.id, **d.to_dict()} for d in docs]

@app.get("/")
def root():
    return {"status": "Online", "agents": ["Intake", "Calendar", "Notes", "LLM"]}
