# Name: Raymond Zhang
# Program Name: Python Quiz Game
# Date: 9/20/24
# Extra: 

name = input("Hi, what is your name? ")
print("Hi " + name + ", today you will be taking a quiz about Geography.")
while True: # Loop runs infinitely until broken out of.
    score = 0
    print("Question 1: Java is an island located in which of the following countries? ")
    print("1. Malaysia")
    print("2. Indonesia")
    print("3. Thailand")
    print("4. Philippines")
    answer1 = input("Enter an integer as your answer: ")
    if answer1[0] == "2":
        print("Correct!")
        score += 1 # Increments the score by 1.
    else:
        print("Incorrect :(")

    print("Question 2: Dominica is one of the only few countries to have what in their flag? ")
    print("1. The Color Purple")
    print("2. A Human")
    print("3. A Lion")
    print("4. A non-existent Animal")
    answer2 = input("Enter an integer as your answer: ")
    if answer2[0] == "1":
        print("Correct!")
        score += 1
    else:
        print("Incorrect :(")

    print("Question 3: Tirana is the capital of which European country? ")
    print("1. North Macedonia")
    print("2. Kosovo")
    print("3. Montenegro")
    print("4. Albania")
    answer3 = input("Enter an integer as your answer: ")
    if answer3[0] == "4":
        print("Correct!")
        score += 1
    else:
        print("Incorrect :(")
        
    print("Question 4: Super long grass is common in which of the following Brazilian states? ")
    print("1. Goias")
    print("2. Acre")
    print("3. Mato Grosso de Sul")
    print("4. Tocantins")
    answer4 = input("Enter an integer as your answer: ")
    if answer4[0] == "4":
        print("Correct!")
        score += 1
    else:
        print("Incorrect :(")

    print("Question 5: The city of Palma is found in which of the following European countries? ")
    print("1. Spain")
    print("2. Portugal")
    print("3. France")
    print("4. Italy")
    answer5 = input("Enter an integer as your answer: ")
    if answer5[0] == "1":
        print("Correct!")
        score += 1 
    else:
        print("Incorrect :(")

    if score == 0:
        print("You received a score of 0, better luck next time!")
    elif score == 1 or score == 2:
        print("You received a score of " + str(score) + ", still got a bit of work to do!")
    elif score > 2 and score < 5: # Checks if the score is any integer between 2 and 5 excluding both values.
        print("You received a score of " + str(score) + ", you're on your way to becoming an expert Geographer!")
    else:
        print("Well done! You have received the highest score possible on our quiz, that being a 5. Your Geography knowledge exceeds the average person and I officially declare you a pro-Geographer!")

    choice = input("Would you like to play the quiz again? Enter Yes or No: ")
    if choice.lower() == "no":
        break
    elif choice.lower() == "yes":
        continue # Restarts at the beginning of the while loop
    else:
        print("You did not enter one of the options, and as a result this quiz will now end.")
        break # Breaks out of the program