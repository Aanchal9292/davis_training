# Function to find student with highest marks
def highest_marks(d):

    max_student = max(d, key=d.get)
    return max_student

marks = {"A":80,"B":95,"C":78}

print(highest_marks(marks))