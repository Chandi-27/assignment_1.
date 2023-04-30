string=input("Enter a name : ")
unique_letters=[]
for x in string:
    if x not in unique_letters:
        unique_letters.append(x)
print("Unique letters: "+",".join(unique_letters))
print("Number of unique letters: "+ str(len(unique_letters)))