

# app/grades.py

import json
from typing import Optional, Dict, Any


class Grades:
    """
    Stores all individual class grades and can load them from a JSON file.
    Expected JSON format (keys are optional):
    {
      "quiz_1": 85,
      "quiz_2": 90,
      "midterm": 88,
      "project": 95,
      "final": 92
    }
    """

    def __init__(
        self,
        quiz_1: Optional[float] = None,
        quiz_2: Optional[float] = None,
        midterm: Optional[float] = None,
        project: Optional[float] = None,
        final: Optional[float] = None,
    ) -> None:
        """
        This constructor declares instance variables with the self prefix and
        sets them to the provided values (or None by default).
        """
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final

    # --- New: load from JSON file -------------------------------------------------

    def load_from_json(self, file_path: str) -> None:
        """
        Populate grade fields from a JSON file. Missing keys remain as-is.
        """
        with open(file_path, "r") as f:
            data = json.load(f)
        self._apply_dict(data)

    # --- Helper(s) ----------------------------------------------------------------

    def _apply_dict(self, data: Dict[str, Any]) -> None:
        """
        Applies values from a dict to known fields if present.
        """
        # Use .get so missing keys don't overwrite existing values
        self.quiz_1 = data.get("quiz_1", self.quiz_1)
        self.quiz_2 = data.get("quiz_2", self.quiz_2)
        self.midterm = data.get("midterm", self.midterm)
        self.project = data.get("project", self.project)
        self.final = data.get("final", self.final)

    # --- Existing API kept intact -------------------------------------------------

    def set_all(
        self,
        quiz_1: Optional[float] = None,
        quiz_2: Optional[float] = None,
        midterm: Optional[float] = None,
        project: Optional[float] = None,
        final: Optional[float] = None,
    ) -> None:
        """
        Sets the grades all at once. When calling this function, the caller can specify
        the parameters to be set like so:
        Grades().set_all(midterm=88, project=95)
        """
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final

    def __str__(self) -> str:
        """
        This method gets called whenever this object is printed to string (e.g., standard out).
        """
        grades = []
        if self.quiz_1 is not None:
            grades.append(f"Quiz 1: {self.quiz_1}")
        if self.quiz_2 is not None:
            grades.append(f"Quiz 2: {self.quiz_2}")
        if self.midterm is not None:
            grades.append(f"Midterm Exam: {self.midterm}")
        if self.project is not None:
            grades.append(f"Project: {self.project}")
        if self.final is not None:
            grades.append(f"Final Exam: {self.final}")

        if len(grades) <= 0:
            return "No grades submitted yet."
        else:
            # Create a string in which each element of the list is separated by a comma
            return "GRADES --- " + ", ".join(grades)
