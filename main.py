
def getGradePoint(lettergrade):
    if lettergrade == "A":
      return 4.0
    elif lettergrade == "A-":
      return 3.67
    elif lettergrade == "B+":
      return 3.33
    elif lettergrade == "B":
      return 3.0
    elif lettergrade == "B-":
      return 2.67
    elif lettergrade == "C+":
      return 2.33
    elif lettergrade == "C":
      return 2.0
    elif lettergrade == "D":
      return 1.0
    elif lettergrade == "F":
      return 0.0
    else: 
      return 0.0

def run():
  lettergrade1 = input("Enter your course 1 letter grade: ")
  credit1 = int(input("Enter your course 1 credit: "))
  gpa1 = getGradePoint(lettergrade1)
  print(f"Grade point for course 1 is: {gpa1}")
  lettergrade2 = input("Enter your course 2 letter grade: ")
  credit2 = int(input("Enter your course 2 credit: "))
  gpa2 = getGradePoint(lettergrade2)
  print(f"Grade point for course 2 is: {gpa2}")
  lettergrade3 = input("Enter your course 3 letter grade: ")
  credit3 = int(input("Enter your course 3 credit: "))
  gpa3 = getGradePoint(lettergrade3)
  print(f"Grade point for course 3 is: {gpa3}")

  GPA = (gpa1 * credit1 + gpa2 * credit2 + gpa3 * credit3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()
    


