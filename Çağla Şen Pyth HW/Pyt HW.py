name = "Cagla"
surname ="Sen"
name1 = input("Please enter your name: ")

surname1 = input("Please enter your surname: ")
if (name == name1 and surname == surname1):
    print("Welcome")
else:
        print("Please try again later")

midterm = int(input("Please enter your midterm grade: "))
              
final = int(input("Please enter your final grade: "))

project = int(input("Please enter your project grade: "))
              
              
grade = midterm*0.3 + final*0.5 + project*0.2
            

if grade < 0:
  print("Invalid value")
else:

  if 0 < grade < 30:
      print("FF\nYou failed")
       
  elif 30 < grade < 50:
      print("DD")
      
  elif 50 < grade < 70:
      print("CC")
      
  elif 70 < grade < 90:
      print("BB")
      
  elif 90 < grade < 100:
      print("AA")
