# 1.Students marks list
# STORE
# name   |  s1  | s2  | gen
# -------------------------
# John   | 9.0  | 8.0 |10.0 |
# Mary   | 8.0  | 9.0 |9.0  |
# ...
from os import system

#data = ["Name:", "sem 1:",  "sem 2:",  "gen:"]
students_data = [ 
       ["John" ,  9.0 , 8.0 , 10.0 ],  # 0 
       ["Marry",  8.0 , 9.0 , 9.0  ],  # 1
       ["Peter",  8.0 , 8.0 , 10.0 ],  # 2
    #  0        1     2     3
]

system('cls')
print("     Name:             sem 1: sem 2:  gen:")
#print (data)
#for d in range (len(data)):
    #f"{data [d] [0]} | {data [d] [0] } | {data [d] [0]} | {data [d] [0] }
    #print(d, data)

for i in range (len(students_data)):
    print(f"{i + 1 : 3} | {students_data [i] [0] :15} | {students_data [i] [1] :4.1f} | {students_data [i] [2] :4.1f} | {students_data [i] [3] :4.1f}")

