## part 1
x=input("code: ")

if x == "CSC1006":
    print("Mathmatics 2")
elif x == "CSC1007":
    print("Operating Systems")
elif x == "CSC1008":
    print("Data Structures and Algorithms")
elif x == "CSC1009":
    print("Object-Oriented Programming")
elif x == "CSC1010":
    print("Computer networks")
else:
    print("Invalid module code")
    
## part 2
for i in range(102, 66, -1):
    if (i%2==1):
        print(i)