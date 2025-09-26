def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if grades == None:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        # counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    #Sentencias
    students = [
        {'name': 'Ana', 'grades': [80, 90, 85]}
    ]

    #Decisiones y caminos TC2
    #     students = [
    #     {'name': 'Ana', 'grades': [80, 90, 85]},   # aprobado
    #     {'name': 'Luis', 'grades': [60, 60, 60]},  # recuperación
    #     {'name': 'Marta', 'grades': [40, 45, 50]},  # reprobado
    #     {'name': 'Jorge', 'grades': []}, #Nulo
    # ]


    result = process_grades(students)
    print("\nFinal processing result:")
    print(result)

# TC2 -> Truena el codigo al poner estudiante sin calificaciones, requisito RF4, Por lo tanto no se puede cubrir la sentencia de sin notas