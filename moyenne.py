note_eng = float(input("Note en anglais (coff.2) : "))
note_math = float(input("Note en mathématiques (coff.5) : "))
note_info = float(input("Note en informatiques(coff.3) : "))

coff_eng = 2
coff_math = 5 
coff_info = 3

moy = (2*note_eng + 5*note_math + 3*note_info ) /(coff_eng+coff_math+coff_info )
print(f"La moyenne obtenu est : {moy}")