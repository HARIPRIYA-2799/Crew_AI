import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Disable telemetry SSL issues
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

load_dotenv()

app = FastAPI(title="Travel Planner API")

class TravelRequest(BaseModel):
    city: str

@app.post("/plan")
def generate_itinerary(req: TravelRequest):
    if not req.city.strip():
        raise HTTPException(status_code=400, detail="City name cannot be empty.")
    
    # 1. Define Agent
    planner = Agent(
        role="Expert Local Travel Guide",
        goal="Suggest the top 3 must-visit attractions in any requested city",
        backstory=(
            "You are a seasoned travel curator known for giving concise, "
            "practical, and authentic recommendations rather than tourist traps."
        ),
        verbose=False  # Keep logs clean in production
    )

    # 2. Define Task
    task = Task(
        description="Suggest exactly 3 places to visit in {city}. For each place, give its name and a short 1-line tip.",
        expected_output=(
            "A numbered list of exactly 3 places formatted as:\n"
            "1. [Place Name] - [Short 1-line tip]\n"
            "2. [Place Name] - [Short 1-line tip]\n"
            "3. [Place Name] - [Short 1-line tip]"
        ),
        agent=planner
    )

    # 3. Assemble and Run Crew
    crew = Crew(agents=[planner], tasks=[task])
    result = crew.kickoff(inputs={"city": req.city})

    return {"city": req.city, "recommendations": str(result)}