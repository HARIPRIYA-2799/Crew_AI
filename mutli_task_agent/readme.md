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


========================================
1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene beauty and the early blooms without the crowds.  
2. Vishvesvaraya Industrial and Technological Museum - Don’t miss the interactive exhibits that make science fun for all ages.  
3. Cubbon Park - Bring a picnic or a book to unwind in this lush green oasis right in the heart of the city.  

**Best Route:**
Start your day at Lalbagh Botanical Garden. You can take the Metro to Lalbagh Station on the Green Line. After enjoying the garden, head towards Vishvesvaraya Industrial and Technological Museum, which is about a 15-minute walk from Lalbagh. 

Next, visit Cubbon Park, which is approximately a 10-minute walk from the museum. To return from Cubbon Park, you can take the Metro from Cubbon Park station (on the Green Line) or MG Road station (on the Purple Line) based on your further travel plans.

Enjoy your trip!
