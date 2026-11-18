#================================================= Class Check =================================
print("================================================= Class Check =================================")
print("""Sorry guys i know i promised for Squirrelflight and also i just remembered, I havent done any Pantalan dragons oh my moons the entire SlikLeaf Kingdom is going to
 be sooooooooooo mad! But here we are and i think this calls for some serious Firestar action here! (Wierdly i rally don't lke Firestar even though
 he's the 'hero of the prophecy')""")
print("(Note Thunderclan is totally the best and who  hates Ivypool? not me i mean shes soo coool)")
print("Hello. I am Firestar the leader of Thunderclan and today we are going to go through your marks in the Yellowfang medicine cat test- Firestar (I made that up but i mean Yellowfang:) )\n")
print("Another reason that Firestar is perfect for this is HIS daughter Leafpaw!")
Leafpaw = []
print(Leafpaw)
print("You get to decide Leafpaw and Mudfur's marks!")
Leafmark= int(input("Leafpaws marks (1 to 100): "))
Mudmark= int(input("Mudfurs marks (1 to 100): "))
Leafmark2= int(input("Leafpaws 2nd marks (1 to 100): "))
Mudmark2= int(input("Mudfurs 2nd marks (1 to 100): "))
Leafmar3 = int(input("Leafpaws 3rd marks (1 to 100): "))
Mudmark3= int(input("Mudfurs 3rd marks (1 to 100): "))

Yellowfang = [Leafmark, Mudmark, Leafmark2, Mudmark2, Leafmar3, Mudmark3]
print("Student Marks for Leafpaw, and Mudfur:", Yellowfang)

sample_marks = [10, 20, 30] * 2
print("Repeated Random Number:", sample_marks)
 
print("Number of marks:", len(Yellowfang))
 
print("First mark:", Yellowfang[0])
print("Last mark:", Yellowfang[-1])
 
# PART 5: Access a range using slicing
first_three_marks = Yellowfang[0:3]
print("First three marks:", first_three_marks)
 
# PART 6: Reverse the marks list using slicing
reversed_marks = Yellowfang[::-1]
print("Reversed Marks:", reversed_marks)
 
def match_marks(mark_list):
    count = 0
    matched_marks = []
 
    for mark in mark_list:
        mark_text = str(mark)
 
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
 
    print("Marks with first and last digit same:", matched_marks)
    return count
 
same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_digit_count)
 
total = 0
 
for mark in Yellowfang:
    total += mark
 
average = total / len(Yellowfang)
 
print("Sum of marks:", total)
print("Average marks:", average)
 

Yellowfang.sort()
 
print("Smallest mark is:", Yellowfang[0])
print("Largest mark is:", Yellowfang[-1])

print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", Yellowfang)
print("Total Marks:", total)
print("Average Marks:", average)
print("Lowest Mark:", Yellowfang[0])
print("Highest Mark:", Yellowfang[-1])
print("=======================================")
