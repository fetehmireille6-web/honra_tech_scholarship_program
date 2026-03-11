def calculate_grade(score):
    if score < 0 and score > 100:
        return "Enter a valid score"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 55:
        return "C+"
    elif score >= 50:
        return "C"
    else:
        return "F" 

students = [
    {"name": "Mireille", "score": 95},
    {"name": "Cabrol", "score": 40},
    {"name": "Emperd", "score": 73},
    {"name": "Success", "score": 50},
    {"name": "Alexis", "score": 63},
]

print("Student Report Card")
for i in students:
    grade = calculate_grade(i["score"])
    print(f"Student: {i["name"]} scored: {i["score"]}, {grade} Grade in the exam")
    
