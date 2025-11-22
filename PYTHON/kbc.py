# Questions, options, answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Saturn", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the Indian National Anthem?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Mahatma Gandhi", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "What is the national animal of India?",
        
        "options": ["Lion", "Elephant", "Tiger", "Leopard"],
        "answer": "Tiger"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "Pacific"
    }
]

money = ["₹1,000", "₹5,000", "₹10,000", "₹50,000", "₹1,00,000"]

# Game loop
for i, q in enumerate(questions):
    print(f"\nQuestion for {money[i]}:\n{q['question']}")
    for idx, opt in enumerate(q["options"], start=1):
        print(f"{idx}. {opt}")
    
    user_input = input("Enter your answer (1-4): ").strip()

    if user_input in ["1", "2", "3", "4"]:
        chosen_option = q["options"][int(user_input)-1]
        if chosen_option == q["answer"]:
            print(f"✅ Correct! You won {money[i]}")
        else:
            print("❌ Wrong answer. Game Over!")
            break
    else:
        print("Invalid input. Game Over!")
        break
else:
    print("\n🎉 Congratulations! You won the top prize of ₹1,00,000!")
