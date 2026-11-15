def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "answer": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A) Venus", "B) Mercury", "C) Earth", "D) Mars"],
            "answer": "B"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == q['answer']:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The answer is {q['answer']}")
    
    print(f"\n\nQuiz Complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()