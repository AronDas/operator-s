print ("put your grades in")

math = int(input("math:"))
english = int(input("English:"))
science = int(input("science:"))
Hindi = int(input("Hindi:"))


sum = math+english+science+Hindi

percentage = (sum / 400)*100
print("your total grade is:", percentage)
print("good job!")