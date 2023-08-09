print("Welcome to Okoli's Pigin Quiz ")

play = input("Do you want to play the game? ").lower()

if play != "yes":
    print("Abeg getat")
    quit()

print("Correct guy!!! Let's play :) ")
score = 0


answer = input("What is FTP? ")
if answer == "file transfer protocol":
    print("Sabi guy!")
    score += 1
else: 
    print("Ode!")


answer = input("What is LAN? ")
if answer == "local area network":
    print("Sabi guy!")
    score += 1
else: 
    print("Ode!")


answer = input("What is CPU? ")
if answer == "central processing unit":
    print("Sabi guy!")
    score += 1
else: 
    print("Ode!")


answer = input("What is AWS? ")
if answer == "amazon web service":
    print("Sabi guy!")
    score += 1
else: 
    print("Ode!")

print("You got " + str(score) + " questions correct!" )
print("Which is " + str((score/4) * 100) + "%")