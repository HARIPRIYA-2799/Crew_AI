# ✈️ CrewAI Travel Planner



**So this is single agent but multi tasking program**



A simple **CrewAI-based AI travel planner** that takes a city name from the user and uses an AI agent to:

1. Recommend exactly **3 must-visit attractions**.
2. Provide a short travel tip for each attraction.
3. Suggest a **route to visit all 3 places**.

This project demonstrates the basic concepts of **Agents, Tasks, Crew, and Task Flow in CrewAI**.

---

## 🏗️ Project Flow

```text
User
  │
  │ Enter City
  ▼
CrewAI Agent
  │
  ├── Task 1: Find 3 Attractions
  │
  └── Task 2: Suggest Travel Route
  │
  ▼
Final Result
```

---

## 📁 Project Structure

```text
travel-planner/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* CrewAI
* Python-dotenv
* LLM API

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd travel-planner
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install crewai python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

Add the API key required by your configured LLM:

```env
OPENAI_API_KEY=your_api_key_here
```

> Never commit your `.env` file or API keys to GitHub.

Add `.env` to `.gitignore`:

```text
.env
.env.*
```

---

## ▶️ Run the Application

Run the Python script:

```bash
python main.py
```

The application will ask:

```text
Which city?
```

For example:

```text
Which city? Bangalore
```

The CrewAI agent will then generate:

* 3 recommended places
* A short tip for each place
* A suggested route to visit them

---

## 🧠 CrewAI Concepts Demonstrated

### Agent

The `planner` agent represents an **AI travel expert**.

```python
planner = Agent(
    role="Expert Local Travel Guide",
    goal="Suggest the top 3 must-visit attractions...",
    backstory="You are a seasoned travel curator...",
    verbose=True
)
```

The agent is responsible for performing the assigned tasks.

### Task

The project contains two tasks.

**Task 1 — Attractions**

```text
Suggest exactly 3 places to visit.
```

**Task 2 — Route**

```text
Use the places from Task 1 and suggest the best route.
```

### Crew

The crew brings the agent and tasks together:

```python
crew = Crew(
    agents=[planner],
    tasks=[task1, task2]
)
```

### Kickoff

The workflow starts with:

```python
result = crew.kickoff(inputs={"city": city})
```

The user's city is passed into the CrewAI workflow.

---

## 📤 Example

Input:

```text
Which city? Chennai
```

Possible output:

```text
1. Marina Beach - Visit early morning or around sunset.
2. Kapaleeshwarar Temple - Explore the traditional Dravidian architecture.
3. Fort St. George - Visit to learn about Chennai's colonial history.

Suggested Route:

Kapaleeshwarar Temple
        ↓
Fort St. George
        ↓
Marina Beach
```

---

## 📌 Key Learning

This project demonstrates a basic **multi-task AI workflow**:

```text
User Input
    ↓
Agent
    ↓
Task 1
    ↓
Task 2
    ↓
Crew
    ↓
Final Result
```

It is a beginner-level example of how **CrewAI can coordinate an AI agent across multiple tasks**.


**OUTPUT:**

(course_venv) blr-mp6ov:W4D4 hads$ python3 multiple_agent.py 
Which city? bangalore
╭─────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert Local Travel Guide                                                                                               │
│                                                                                                                                 │
│  Task: Suggest exactly 3 places to visit in bangalore. For each place, give its name and a short 1-line tip.                    │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

[Finalize] todos_count=0, todos_with_results=0
╭───────────────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert Local Travel Guide                                                                                               │
│                                                                                                                                 │
│  Final Answer:                                                                                                                  │
│  1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene atmosphere and avoid the crowds.                  │
│  2. Bangalore Palace - Don’t miss the beautiful woodwork and the stunning gardens that surround this historic site.             │
│  3. Vidhana Soudha - Admire its majestic architecture from the outside, especially lit up at night for a breathtaking view.     │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert route map suggestor                                                                                              │
│                                                                                                                                 │
│  Task: take the input from the above task and suggest the best travel route to follow for the same                              │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

[Finalize] todos_count=0, todos_with_results=0
╭───────────────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert route map suggestor                                                                                              │
│                                                                                                                                 │
│  Final Answer:                                                                                                                  │
│  1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene atmosphere and avoid the crowds.                  │
│  2. Vidhana Soudha - Admire its majestic architecture from the outside, especially lit up at night for a breathtaking view.     │
│  3. Bangalore Palace - Don’t miss the beautiful woodwork and the stunning gardens that surround this historic site.             │
│                                                                                                                                 │
│  Best Route to Follow:                                                                                                          │
│  Start at Lalbagh Botanical Garden. After enjoying the gardens, take the Metro from Lalbagh Station (Green Line) towards        │
│  Mysore Road Station. Change at Cubbon Park Station to the Purple Line and travel to Vidhana Soudha Station. After visiting     │
│  Vidhana Soudha, return to Cubbon Park Station and take the Purple Line towards Baiyappanahalli Station, getting off at the     │
│  next stop, which is the Bangalore Palace Station. This route minimizes travel time while allowing you to visit all three       │
│  locations efficiently.                                                                                                         │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


========================================
1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene atmosphere and avoid the crowds.  
2. Vidhana Soudha - Admire its majestic architecture from the outside, especially lit up at night for a breathtaking view.  
3. Bangalore Palace - Don’t miss the beautiful woodwork and the stunning gardens that surround this historic site.  

Best Route to Follow:  
Start at Lalbagh Botanical Garden. After enjoying the gardens, take the Metro from Lalbagh Station (Green Line) towards Mysore Road Station. Change at Cubbon Park Station to the Purple Line and travel to Vidhana Soudha Station. After visiting Vidhana Soudha, return to Cubbon Park Station and take the Purple Line towards Baiyappanahalli Station, getting off at the next stop, which is the Bangalore Palace Station. This route minimizes travel time while allowing you to visit all three locations efficiently.
(course_venv) blr-mp6ov:W4D4 hads$ 
