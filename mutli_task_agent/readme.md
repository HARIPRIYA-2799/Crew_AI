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
1. Lalbagh Botanical Garden - Visit early in the morning to enjoy the serene beauty and avoid the crowds.  
2. Bengaluru Palace - Take a guided tour to fully appreciate the history and architectural details of this stunning palace.  
3. Brigade Road - Explore the vibrant shopping scene and local eateries; be sure to try some South Indian snacks while you're there.

**Best Route to Visit:**

1. Start your day at **Lalbagh Botanical Garden**. Take the Myers Square bus stop to the Near Lalbagh main gate.
2. After exploring Lalbagh, take the bus or a short taxi ride to **Bengaluru Palace**. From Lalbagh, it’s about a 15-minute drive.
3. Finally, for **Brigade Road**, take a cab from the Bengaluru Palace. Brigade Road is roughly a 10-minute drive away, and you’ll be right in the heart of shopping and dining. 

**Metro Travel Tips:** 
- If using the metro, you can start at the Lalbagh Metro Station (Purple Line), travel to the Vidhana Soudha Station (change to the Green Line), and then reach Brigade Road by getting off at the Brigade Road Metro Station. 
- For Bengaluru Palace, a cab will be necessary from either Lalbagh or Brigade Road as it is not on a direct metro line.

Enjoy your trip!
