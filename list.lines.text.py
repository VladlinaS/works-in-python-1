from os import system

text_lines = [
    'Programming is the implementation of logic to facilitate specified computing operations and ',
    'functionality. It occurs in one or more languages, which differ by application, domain and ',
    'programming model.'
]

system("cls")

for i in range(len(text_lines)):
    print(i, text_lines [i])
#print(text_lines [0])
#print(text_lines [1])
#print(text_lines [2])