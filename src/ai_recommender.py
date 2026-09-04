def get_valid_choice(prompt, options):
    normalized_options = {option.lower(): option for option in options}

    while True:
        choice = input(prompt).strip().lower()

        if choice in normalized_options:
            return normalized_options[choice]

        print(f"Invalid choice. Please select one of: {', '.join(options)}")


def generate_recommendation(subject, level, goal):
    if subject == "Python":
        if level == "Beginner":
            if goal == "Practice":
                return (
                    "Practice Python fundamentals through small programming exercises.",
                    "Beginner learners benefit from practicing core syntax and basic problem-solving."
                )
            elif goal == "Build Projects":
                return (
                    "Build a simple Python calculator or command-line application.",
                    "A small project helps beginners apply fundamental Python concepts in a practical way."
                )
            else:
                return (
                    "Study Python fundamentals including variables, data types, conditions, and loops.",
                    "Understanding the fundamentals creates a strong foundation for further Python development."
                )

        elif level == "Intermediate":
            if goal == "Practice":
                return (
                    "Solve intermediate Python problems using functions, lists, dictionaries, and file handling.",
                    "These concepts strengthen practical Python problem-solving skills."
                )
            elif goal == "Build Projects":
                return (
                    "Build a Python automation or data-processing project.",
                    "A practical project helps connect multiple intermediate Python concepts."
                )
            else:
                return (
                    "Explore object-oriented programming, modules, exceptions, and advanced data structures.",
                    "These topics help an intermediate learner move toward more structured Python development."
                )

        else:
            return (
                "Develop an advanced Python application involving automation, APIs, or data processing.",
                "Advanced projects provide opportunities to apply Python concepts to realistic problems."
            )

    elif subject == "AI":
        if level == "Beginner":
            if goal == "Practice":
                return (
                    "Practice basic AI decision-making by building rule-based programs.",
                    "Rule-based systems provide an accessible introduction to how AI can make decisions."
                )
            elif goal == "Build Projects":
                return (
                    "Build a simple rule-based chatbot or recommendation system.",
                    "A small AI project demonstrates how inputs can be processed into intelligent decisions."
                )
            else:
                return (
                    "Study AI fundamentals, including intelligent agents, decision-making, and rule-based systems.",
                    "These concepts establish a foundation for understanding AI."
                )

        elif level == "Intermediate":
            if goal == "Practice":
                return (
                    "Create a multi-factor AI decision-making system.",
                    "Combining multiple conditions provides practical experience with structured AI logic."
                )
            elif goal == "Build Projects":
                return (
                    "Build a Python recommendation system using multiple user preferences.",
                    "A recommendation system demonstrates practical rule-based AI functionality."
                )
            else:
                return (
                    "Explore search algorithms, knowledge representation, and intelligent decision systems.",
                    "These concepts expand understanding beyond basic AI conditional logic."
                )

        else:
            return (
                "Design a more complex intelligent decision system with multiple interacting rules.",
                "Advanced rule-based systems require careful organization of knowledge and decision paths."
            )

    elif subject == "Data Analysis":
        if level == "Beginner":
            return (
                "Load a dataset with Pandas and explore its rows, columns, and missing values.",
                "Dataset exploration is an important first step in understanding data."
            )

        elif level == "Intermediate":
            return (
                "Clean a dataset and calculate descriptive statistics using Pandas.",
                "Data cleaning and statistics are essential skills for practical data analysis."
            )

        else:
            return (
                "Perform exploratory data analysis and identify meaningful patterns in a dataset.",
                "Advanced analysis focuses on interpreting data and extracting useful insights."
            )

    else:
        if goal == "Build Projects":
            return (
                "Build a small Python project related to your interests.",
                "Project-based learning helps convert programming knowledge into practical experience."
            )
        elif goal == "Practice":
            return (
                "Practice programming through small problem-solving exercises.",
                "Regular practice helps improve logical thinking and programming confidence."
            )
        else:
            return (
                "Start with fundamental programming and AI concepts.",
                "A strong foundation makes it easier to progress toward advanced topics."
            )


def display_recommendation(subject, level, goal, recommendation, reason):
    print("\n" + "=" * 65)
    print("             AI LEARNING RECOMMENDATION")
    print("=" * 65)
    print(f"Preferred Subject : {subject}")
    print(f"Skill Level       : {level}")
    print(f"Learning Goal     : {goal}")
    print("\nRecommendation:")
    print(recommendation)
    print("\nWhy this recommendation?")
    print(reason)
    print("=" * 65)


def main():
    print("=" * 65)
    print("             AI LEARNING RECOMMENDER")
    print("                 DevSphere - Week 1")
    print("=" * 65)

    print(
        "\nThis rule-based AI system recommends a learning activity "
        "based on your preferences."
    )

    subjects = [
        "Python",
        "AI",
        "Data Analysis",
        "Other"
    ]

    levels = [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    goals = [
        "Practice",
        "Build Projects",
        "Learn Concepts"
    ]

    subject = get_valid_choice(
        "\nPreferred subject (Python / AI / Data Analysis / Other): ",
        subjects
    )

    level = get_valid_choice(
        "Skill level (Beginner / Intermediate / Advanced): ",
        levels
    )

    goal = get_valid_choice(
        "Learning goal (Practice / Build Projects / Learn Concepts): ",
        goals
    )

    recommendation, reason = generate_recommendation(
        subject,
        level,
        goal
    )

    display_recommendation(
        subject,
        level,
        goal,
        recommendation,
        reason
    )

    print("\nThank you for using the AI Learning Recommender!")


if __name__ == "__main__":
    main()