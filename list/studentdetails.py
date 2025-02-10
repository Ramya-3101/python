# Function to get student details from user
def get_details():
    student = {}
    
    student['name'] = input("Enter student's name: ")
    student['age'] = int(input("Enter student's age: "))
    student['gender'] = input("Enter student's gender: ")
    student['city'] = input("Enter student's grade: ")
    student['country'] = input("Enter student's favorite subject: ")

    return student

# Get details and store in dictionary
details = get_details()

# Display the stored details
print("\nDetails:")
for key, value in details.items():
    print(f"{key.capitalize()}: {value}")
