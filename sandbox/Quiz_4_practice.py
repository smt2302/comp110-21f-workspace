"""The function writing problems."""


def average_grades(a: dict[str, list[int]]) -> dict[str, float]:
    student_grades: dict[str, float] = {}
    for key in a:
        i: int = 0
        sum = int
        total = float
        while i > len(a[key]):
            sum = sum + a[key[i]]
            i += 1
        total = sum / len(a[key])
        student_grades[key] = total
    return student_grades