attendance = int(input())
assignment_submitted = int(input())
Sports_player = (input("If you are a sports playes Press y "))


print(f"attendance criteria met? : {attendance>= 75}")
print(f"assignmet criteria met?  :{assignment_submitted >= 70}")
print(f"sports criteria met? : {Sports_player}")

if attendance >=75 and assignment_submitted >=70:
     print("You are passed")
     if Sports_player == "y" :
      print("You are eligible to get 10 marks Extra")
     else:
      print("You Won't get any extra Marks")
else:
 print("You are not eligible")
