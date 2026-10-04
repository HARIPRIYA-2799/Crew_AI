# ✈️ CrewAI AI Travel & Route Planner with 2 agents and 2 tasks

A beginner-friendly **CrewAI multi-agent travel planner** that takes a city name as input and uses two specialized AI agents to plan a trip.

The application:

1. Finds **3 must-visit attractions** in the requested city.
2. Provides a short tip for each attraction.
3. Uses a second AI agent to suggest **2 possible travel routes** between the recommended places.
4. Includes **metro stations, metro changes, and route guidance** where applicable.

---

## 🏗️ Architecture

```text
                 User
                  │
                  │ Enter City
                  ▼
          ┌─────────────────┐
          │   CrewAI Crew   │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          ▼                  ▼
   ┌──────────────┐   ┌──────────────┐
   │   Planner    │   │   Route Map  │
   │    Agent     │   │    Agent     │
   └──────┬───────┘   └──────▲───────┘
          │                  │
          │ Task 1           │ Task 2
          ▼                  │
   3 Tourist Places ─────────┘
          │
          ▼
     Travel Routes
          │
          ▼
       Final Result
```

---

## 🤖 AI Agents

### 1. Expert Local Travel Guide

The first agent is responsible for finding the best attractions.

**Role:**

```text
Expert Local Travel Guide
```

**Responsibilities:**

* Identify 3 must-visit attractions.
* Provide a short tip for each place.
* Recommend authentic attractions rather than tourist traps.

---

### 2. Expert Route Map Suggestor

The second agent uses the output from the first task to plan the travel routes.

**Role:**

```text
Expert route map suggestor
```

**Responsibilities:**

* Suggest 2 possible routes.
* Identify the best order to visit the attractions.
* Consider metro transportation.
* Suggest metro stations to get down at.
* Mention metro line changes where applicable.
* Try to provide shorter and more practical routes.

---

## 🔄 Task Flow

### Task 1 — Find Attractions

The first task asks the `planner` agent to find exactly 3 places.

```text
User enters city
       ↓
Planner Agent
       ↓
Find 3 attractions
       ↓
Place + Travel Tip
```

Example:

```text
1. Marina Beach - Visit around sunset.
2. Kapaleeshwarar Temple - Explore the traditional architecture.
3. Fort St. George - Explore the historical landmarks.
```

---

### Task 2 — Plan Routes

The second task receives the output from the first task and creates travel routes.

```te
```







**OUTPUT:**

python3 multiple_agent.py 
Which city? Bangalore
╭─────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert Local Travel Guide                                                                                               │
│                                                                                                                                 │
│  Task: Suggest exactly 3 places to visit in Bangalore. For each place, give its name and a short 1-line tip.                    │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

[Finalize] todos_count=0, todos_with_results=0
╭───────────────────────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────────────────────────╮
│                                                                                                                                 │
│  Agent: Expert Local Travel Guide                                                                                               │
│                                                                                                                                 │
│  Final Answer:                                                                                                                  │
│  1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene beauty and avoid crowds.                          │
│  2. Bangalore Palace - Don't miss the audio guide for an insightful tour of this majestic heritage site.                        │
│  3. Vidhana Soudha - Capture stunning photos of this architectural marvel during sunset for the best light.                     │
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
│  1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene beauty and avoid crowds.                          │
│  2. Bangalore Palace - Don't miss the audio guide for an insightful tour of this majestic heritage site.                        │
│  3. Vidhana Soudha - Capture stunning photos of this architectural marvel during sunset for the best light.                     │
│                                                                                                                                 │
│  **Best Route to Follow:**                                                                                                      │
│  Start your day at **Lalbagh Botanical Garden**. Take a cab or use the metro to reach the **Lalbagh** station (Green Line).     │
│  After enjoying the garden, head to **Bangalore Palace**. You can take an auto-rickshaw or a cab from the Lalbagh to the        │
│  Palace, which is approximately a 10-minute ride. Finally, make your way to **Vidhana Soudha**. From Bangalore Palace, you can  │
│  take a cab or an auto-rickshaw; it will take about 15-20 minutes. Plan to arrive at Vidhana Soudha before sunset to capture    │
│  the best photos.                                                                                                               │
│                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


========================================
1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene beauty and avoid crowds.  
2. Bangalore Palace - Don't miss the audio guide for an insightful tour of this majestic heritage site.  
3. Vidhana Soudha - Capture stunning photos of this architectural marvel during sunset for the best light.  

**Best Route to Follow:**  
Start your day at **Lalbagh Botanical Garden**. Take a cab or use the metro to reach the **Lalbagh** station (Green Line). After enjoying the garden, head to **Bangalore Palace**. You can take an auto-rickshaw or a cab from the Lalbagh to the Palace, which is approximately a 10-minute ride. Finally, make your way to **Vidhana Soudha**. From Bangalore Palace, you can take a cab or an auto-rickshaw; it will take about 15-20 minutes. Plan to arrive at Vidhana Soudha before sunset to capture the best photos.
