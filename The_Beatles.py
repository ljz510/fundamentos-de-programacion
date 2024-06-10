"""Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list."""

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3

for members in ["Stu Sutcliffe", "Pete Best"]: 
    new_members = input(f"Please add {members} to the list beatles: ")
    beatles.append(new_members)
print("Step 3:", beatles)

# step 4

del beatles[-1]
del beatles[-1] 

print("Step 4:", beatles)

# step 5

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

