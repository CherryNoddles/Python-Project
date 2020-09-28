
print("Title of program: MCQ revision program")
print()
​
counter = 0
score = 0
total_num_of_qn = 3
​
​
counter +=1
tracker = 0
​
while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which European power got control over Malacca in 1511?")
  print("   a) British")
  print("   b) Spanish")
  print("   c) Portugese")
  print("   d) Dutch")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. The British took control over Singapore in 1819."
    score -=1
  elif answer == "b":
    output = "Wrong. Spain was not a European power in Southeast Asia during that time."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. The Dutch wrestled Malacca from the Portugese in 1641."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
​
​
counter +=1
tracker = 0
​
while tracker !=1:
  
  print("Q"+str(counter)+") "+ "以下哪一个不是一种修辞手法？")
  print("   a) 肖像描写")
  print("   b) 排比句")
  print("   c) 夸张")
  print("   d) 比喻")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "你答对了！"
    tracker =1
    score +=1
  elif answer == "b":
    output = "错。排比句是一种修辞手法。"
    score -=1
  elif answer == "c":
    output = "错。夸张是一种修辞手法。"
    score -=1
    
  elif answer == "d":
    output = "错。夸张是一种修辞手法。"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
​
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
​
counter +=1
tracker = 0
​
while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."
​
  
​
  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
  
​


