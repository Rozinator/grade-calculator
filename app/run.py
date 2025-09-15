# run.py

from pathlib import Path
from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

def main():
    # Instantiate Grade and Weights objects
    my_grades = Grades()
    weights = GradeWeights()

    # Load grades from JSON (file should be next to this script)
    json_path = Path(__file__).with_name("grades.json")
    if not json_path.exists():
        raise FileNotFoundError(
            f"grades.json not found at {json_path}. "
            "Create this file with keys: quiz_1, quiz_2, midterm, project, final."
        )
    my_grades.load_from_json(str(json_path))

    # Print out the grades to console
    print(my_grades)

    # Calculate course grade based on the grades set above
    percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
    if percentage_grade is None:
        print("Can't calculate overall course grade without all individual grades.")
    else:
        letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
        print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

    # Calculate the grade assuming that all assignments not turned in yet will be 100%
    optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
    optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
    print(
        f'If all other assignments are 100%, the overall course would be '
        f'{optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}'
    )

if __name__ == "__main__":
    main()


