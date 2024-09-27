questions = [
    ["When do we celebrate Independence Day?", "14 August", "15 August", "15 July", "26 January", 2],
    ["Sun rises in which direction?", "East", "West", "North", "South", 1],
    ["What is the capital of India?", "Jharkhand", "Odisha", "New Delhi", "Maharashtra", 3],
    ["How many days are there in a week?", "10", "7", "5", "6", 2],
    ["Which planet do we live on?", "Earth", "Mars", "Venus", "Pluto", 1],
    ["How many colors are there in a rainbow?", "10", "7", "8", "12", 2],
    ["How many legs does a spider have?", "10", "7", "8", "5", 3],
    ["What is the opposite of 'UP'?", "Side", "below", "Under", "Down", 4],
    ["What is 5 + 3?", "8", "2", "15", "0", 1],
    ["What is the color of the sky?", "White", "Pink", "Blue", "Yellow", 3],
    ["How many months are there in a year?", "11", "14", "10", "12", 4],
    ["Which is the fastest land animal?", "Lion", "Tiger", "Cheetah", "Zebra", 3]
]

levels = [10000, 20000, 50000, 100000, 200000, 800000, 1600000, 3200000, 5000000, 10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a. {question[1]}                    b. {question[2]}")   
    print(f"c. {question[3]}                      d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    
    if reply == question[-1]:  # Correct answer
        print(f"Correct answer! You have won Rs.{levels[i]}")
        
        if i == 3:
            money = 50000
        elif i == 6:
            money = 800000
        elif i == 10:
            money = 10000000
    else:  # Incorrect answer
        print("Wrong Answer!")
        break

print(f"Your take home money is Rs. {money}")