Amount =int(input("Please enter the amount for the withdrawel:"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print ( "notes of dollars", note_1)
print ( "notes of dollars", note_2)
print ( "notes of dollars", note_3)