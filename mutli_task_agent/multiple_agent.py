import os

# Disable CrewAI telemetry reporting
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Automatically reads key-value pairs from your .env file
load_dotenv()

# 1. Ask the user for the city
city = input("Which city? ")

# 2. Define the Agent
planner = Agent(
    role="Expert Local Travel Guide",
    goal="Suggest the top 3 must-visit attractions in any requested city and also you should know the best route to follow to visit all 3 places",
    backstory=(
        "You are a seasoned travel curator known for giving concise, practical, "
        "and authentic recommendations rather than tourist traps."
        "you also the shortest and best routes to visit these places"
    ),
    verbose=True
)
routemap = Agent(
    role="Expert route map suggestor",
    goal="suggest the best 2 routes to be followed to visit the places that are outputed from the above agent",
    backstory=(
        "You are a seasoned travel curator known for giving concise, practical, "
        "you are very well versed in metro travel and you know to suggest on which metro you should get down at and suggest if we have to change metro lanes as well"
        "you also the shortest and best routes to visit these places"
    ),
    verbose=True
)

# 3. Define the Task
task1 = Task(
    description="Suggest exactly 3 places to visit in {city}. For each place, give its name and a short 1-line tip.",
    expected_output=(
        "A numbered list of exactly 3 places formatted as:\n"
        "1. [Place Name] - [Short 1-line tip]\n"
        "2. [Place Name] - [Short 1-line tip]\n"
        "3. [Place Name] - [Short 1-line tip]"
    ),
    agent=planner
)
task2 = Task(
    description="take the input from the above task and suggest the best travel route to follow for the same",
    expected_output=(
        "A numbered list of exactly 3 places formatted as:\n"
        "1. [Place Name] - [Short 1-line tip]\n"
        "2. [Place Name] - [Short 1-line tip]\n"
        "3. [Place Name] - [Short 1-line tip]\n"
        "the best route to be followed to accomplish visiting all the 3 places"
    ),
    agent=routemap
)

# 4. Assemble the Crew
crew = Crew(
    agents=[planner,routemap],
    tasks=[task1,task2]
)

# 5. Run the Crew
result = crew.kickoff(inputs={"city": city})
print("\n" + "=" * 40)
print(result)