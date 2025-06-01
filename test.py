import math

msg = "Good Morning Python Learners";
temp= '';
for char in msg:
    if char.lower() == "o":
        char = "0" ;
    
    temp += char;



print(msg)
