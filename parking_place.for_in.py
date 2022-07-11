parking_places = 7
free_places    = 3

print("#"*parking_places*5)

for place_index in range (1, parking_places + 1):
   if place_index == free_places:
      print("| |", end ="")
   else:
      print("|X|", end="")
  
print("\n", "#"*parking_places*5, sep ="")
 #sep — это может быть строка, которую необходимо вставлять между значениями, по умолчанию — пробел.

        