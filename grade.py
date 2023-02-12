user_input = input("Name of the exam: ")
max_marks = int(input("Please enter maximum marks of the exam: "))
marks = int(input("please enter your marks: "))

percentage = marks / max_marks * 100
print(percentage)

if percentage >= 80:
    print("You got an A grade")
elif percentage >= 60:
    print("You got an B grade")

elif percentage >= 35:
    print("you got an C grade")

else:
    print("You got F in exam")
