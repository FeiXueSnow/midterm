# Points to Start
points = 0

# Instructions
print("This is a Would - You - Rather - like game. Choose a letter and see if your choice was popular or unpopular.")

# Questions and Answers
# Question 1

question_1 = input("Cats (c) or Dogs (d)? ")
 
if question_1 == "c" or "C":
   print("Unpopular")
elif question_1 == "D" or "d":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()
 
# Question 2

question_2 = input("Toilet Paper Under (u) or Toilet Paper Over (o)? ")
 
if question_2 == "U" or "u":
   print("Unpopular")
elif question_2 == "O" or "o":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()

# Question 1

question_3 = input("Wii (W) or Xbox (X)? ")
 
if question_3 == "X" or "x":
    print("Unpopular!")
elif question_3 == "W" or "w":
   print("Popular!")
   points += 1
else:
   print("...")
   exit()

# Winning, Wosing, and Losing Status
if points == 3:
  print("You are totally in the mainstream!")
elif points == 2:
  print("You've got one outlier, but that's completely fine!")
else:
  print("You wanted to avoid the mainstream, huh?")

