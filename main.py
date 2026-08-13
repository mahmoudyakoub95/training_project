def greet():
    return "Hello from main"


def grade_result(score):
    if score >= 50:
        return "pass"
    else:
        return "fail"


print(greet())
print(grade_result(80))