print("  Student Grade Calculator  ")

# Enter marks for 5 subjects
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))
mark4 = float(input("Enter mark for Subject 4: "))
mark5 = float(input("Enter mark for Subject 5: "))

# Calculate total and average
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

# Show results
print("\n--- Your Results ---")
print("Total marks:", total)
print("Average marks:", average)

# Give grade based on average
if average >= 90:
    print("Grade: A+ 🏆 Excellent!")
elif average >= 80:
    print("Grade: A 😊 Very Good!")
elif average >= 70:
    print("Grade: B 👍 Good!")
elif average >= 60:
    print("Grade: C 📚 Keep Studying!")
else:
    print("Grade: F ❌ Please work harder!")