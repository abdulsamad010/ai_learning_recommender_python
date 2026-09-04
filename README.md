# 🤖 AI Learning Recommender — Python

<p align="center">
  <img src="https://img.shields.io/badge/DevSphere-Internship-blue?style=for-the-badge" alt="DevSphere Internship">
  <img src="https://img.shields.io/badge/Week-1-green?style=for-the-badge" alt="Week 1">
  <img src="https://img.shields.io/badge/Task-1-orange?style=for-the-badge" alt="Task 1">
  <img src="https://img.shields.io/badge/Artificial%20Intelligence-AI-purple?style=for-the-badge" alt="Artificial Intelligence">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Rule--Based%20AI-Decision%20Logic-FF6F00?style=for-the-badge" alt="Rule-Based AI">
  <img src="https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge" alt="Completed">
</p>

> **DevSphere Internship Program | Week 1 | Task 1 — Artificial Intelligence (AI)**

A beginner-friendly **rule-based Artificial Intelligence system built with Python** that recommends suitable learning activities based on a user's preferred subject, skill level, and learning goal.

---

## 📌 Project Overview

The **AI Learning Recommender** is a simple decision-making system designed to demonstrate fundamental Artificial Intelligence concepts using Python.

The system collects three inputs from the user:

- 🎯 Preferred subject
- 📈 Current skill level
- 🚀 Learning goal

It then processes these inputs through a structured set of rules using Python's conditional logic and produces:

- A personalized learning recommendation
- A clear explanation for the recommendation

The project demonstrates how a basic AI system can use predefined rules to transform user inputs into useful decisions.

---

## 🎯 Task Objective

The objective of this Week 1 task is to:

- Understand basic Artificial Intelligence concepts
- Practice Python programming fundamentals
- Implement a simple decision-making system
- Use `if`, `elif`, and `else` logic
- Accept and validate user input
- Build a practical rule-based AI application
- Generate recommendations based on multiple inputs

---

## 🧠 AI Approach

This project uses a **rule-based AI approach**.

Instead of machine learning, the system relies on predefined rules created by the developer.

### Decision Process

```text
User Input
    │
    ├── Preferred Subject
    │
    ├── Skill Level
    │
    └── Learning Goal
            │
            ▼
     Rule-Based Engine
            │
            ▼
     Conditional Logic
      if / elif / else
            │
            ▼
     AI Recommendation
            │
            ▼
       Explanation
```

### Example

```text
Subject = AI
Level = Intermediate
Goal = Build Projects

            ↓

Rule Evaluation

            ↓

Recommendation:
Build a Python recommendation system using
multiple user preferences.
```

---

## ✨ Features

### 🔹 User Input

The system collects:

1. Preferred subject
2. Skill level
3. Learning goal

### 🔹 Input Validation

Invalid selections are rejected and the user is asked to enter a valid option.

### 🔹 Rule-Based Decision Making

The recommendation engine evaluates different combinations of user inputs.

### 🔹 Personalized Recommendations

Different combinations of preferences can produce different learning recommendations.

### 🔹 Recommendation Explanation

The system explains why a particular learning activity was selected.

### 🔹 Modular Structure

The application uses reusable Python functions to keep the code organized and maintainable.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🤖 **Rule-Based AI** | Decision-making logic |
| 💻 **VS Code** | Development environment |
| 🔧 **Git** | Version control |
| 🐙 **GitHub** | Repository hosting |

### Dependencies

No external Python packages are required.

The project uses Python's built-in functionality.

---

## 📂 Project Structure

```text
ai_learning_recommender_python/
│
├── src/
│   └── ai_recommender.py
│
├── tests/
│   └── test_recommender.py
│
├── screenshots/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ How It Works

### 1️⃣ Select a Subject

The user chooses one of the available subjects:

```text
Python
AI
Data Analysis
Other
```

### 2️⃣ Select Skill Level

The available levels are:

```text
Beginner
Intermediate
Advanced
```

### 3️⃣ Select Learning Goal

The available goals are:

```text
Practice
Build Projects
Learn Concepts
```

### 4️⃣ Rule Evaluation

The system evaluates the selected values through predefined decision rules.

### 5️⃣ Recommendation

The AI system returns a suitable learning activity and explains the reason behind the recommendation.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/abdulsamad010/ai_learning_recommender_python.git
```

### Navigate to the Project

```bash
cd ai_learning_recommender_python
```

### Run the Application

```bash
python src/ai_recommender.py
```

---

## 🧪 Running Tests

The project includes basic tests for the recommendation engine.

Run:

```bash
python tests/test_recommender.py
```

Expected output:

```text
All AI recommendation tests passed successfully.
```

---

## 💻 Example

### User Input

```text
Preferred subject: AI
Skill level: Intermediate
Learning goal: Build Projects
```

### System Output

```text
=================================================================
             AI LEARNING RECOMMENDATION
=================================================================

Preferred Subject : AI
Skill Level       : Intermediate
Learning Goal     : Build Projects

Recommendation:
Build a Python recommendation system using multiple user preferences.

Why this recommendation?
A recommendation system demonstrates practical rule-based AI functionality.

=================================================================
```

---

## 📸 Screenshots

Screenshots of the working application can be added to the:

```text
screenshots/
```

Recommended screenshots include:

- Application startup
- User input
- Generated AI recommendation
- Successful test execution

---

## 🧩 Core Python Concepts

This project demonstrates:

- Variables
- Strings
- Lists
- Functions
- Function parameters
- Return values
- User input
- Input validation
- `if` statements
- `elif` statements
- `else` statements
- Nested conditions
- Rule-based decision making
- Modular programming
- Basic software testing

---

## 🤖 Why This Is AI

The project demonstrates a basic form of **rule-based Artificial Intelligence**.

The system:

1. Receives information from the user.
2. Evaluates the information against predefined rules.
3. Makes a decision based on those rules.
4. Produces an appropriate recommendation.
5. Provides an explanation for the decision.

### AI vs Machine Learning

This project does **not** train a machine learning model.

The intelligence comes from explicitly defined rules.

```text
Rule-Based AI
      │
      ├── User Input
      │
      ├── Predefined Rules
      │
      └── Decision
```

Machine Learning, on the other hand, learns patterns from data.

The current project focuses specifically on the **AI Basics + Python** requirements of the DevSphere Week 1 task.

---

## 📈 Future Improvements

Possible future improvements include:

- More learning categories
- More recommendation rules
- Recommendation scoring
- User profiles
- Graphical user interface
- Web-based interface
- Database integration
- Natural Language Processing
- Machine Learning-based recommendations

These improvements are outside the scope of the current Week 1 task.

---

## 🎓 Learning Outcomes

Through this project, the following skills were practiced:

- Python programming fundamentals
- Conditional decision-making
- Rule-based Artificial Intelligence
- User input handling
- Input validation
- Function-based programming
- Basic software testing
- Project organization
- Technical documentation

---

## 🏢 Internship Information

| Field | Details |
|---|---|
| **Organization** | DevSphere |
| **Program** | Internship Program |
| **Week** | Week 1 |
| **Task** | Task 1 |
| **Domain** | Artificial Intelligence (AI) |
| **Topic** | AI Basics + Python |
| **Project** | AI Learning Recommender |
| **Technology** | Python |
| **Approach** | Rule-Based AI |

---

## 👨‍💻 Author

**Abdul Samad Abbasi**

GitHub: [@abdulsamad010](https://github.com/abdulsamad010)

---

## 📄 License

This project was developed as part of the **DevSphere Internship Program** for educational and internship purposes.
