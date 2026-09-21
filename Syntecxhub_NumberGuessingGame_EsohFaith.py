import random

print ("Welcome to number guessing game")
best_score = None
ch = 0

while ch < 4:
    print ("1. Easy")
    print ("2. Medium")
    print ("3. Hard")
    print ("4. Exit")

    ch = int(input("Enter your choice (1, 2, 3, or 4): "))
    if ch ==1:
        print("Easy mode: the computer has selected a number between 1 and 100 (inclusive), now it's your turn." )
        num1 = random.randint(1, 100)
        turns = 0
        while True:
            guess = int(input("Enter your guess number:"))
            turns +=1
            if guess < num1:
             print("Go higher")
            elif guess > num1:
             print("Go lower")
            elif guess == num1:
             print("Congratulations!!! you guessed the right number in", turns, "turns.")
             if best_score is None or turns < best_score:
                    best_score = turns
                    print ("Best score:", best_score)
             if not input("Do you want to play again? (yes/no): ").lower() == "yes":
                print("Thank you for playing the game, see you next time!!")
                break 
            else:
             print("thank you for playing the game, see you next time!!")
        break
    
    elif ch == 2:
         print("Medium mode: the computer has selected a number between 100 and 300 (inclusive), now it's your turn." )
         num2 = random.randint(100, 300)
         turns = 0
         while True:
          guess = int(input("Enter your guess number:"))
          turns +=1
          if guess < num2:
            print("Go higher")
          elif guess > num2:
            print("Go lower")
          elif guess == num2:
            print("Congratulations!!! you guessed the right number in", turns, "turns.")
            if best_score is None or turns < best_score:
              best_score = turns
            print ("Best score:", best_score)
            if not input("Do you want to play again? (yes/no): ").lower() == "yes":
              print("Thank you for playing the game, see you next time!!")
            break
          else:
             print("thank you for playing the game, see you next time!!")
         break
    elif ch == 3:
         print("Hard mode: the computer has selected a number between 300 and 500 (inclusive), now it's your turn." )
         num3 = random.randint(300, 500)
         turns = 0
         while True:
          guess = int(input("Enter your guess number:"))
          turns +=1
          if guess < num3:
            print("Go higher")
          elif guess > num3:
            print("Go lower")
          elif guess == num3:
            print("Congratulations!!! you guessed the right number in", turns, "turns.")
            if best_score is None or turns < best_score:
             best_score = turns
             print ("Best score:", best_score)
            if not input("Do you want to play again? (yes/no): ").lower() == "yes":
             print("Thank you for playing the game, see you next time!!")
             break
            else:
             print("thank you for playing the game, see you next time!!")   
            break
    elif ch == 4:
        print("Invalid choice.")
        break
else:
    print("Thank you for playing the game, see you next time!!")  
      
