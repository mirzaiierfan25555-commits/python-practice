import numpy as np

scores=np.array([
    [18,17,20],
    [15,19,16],
    [20,18,19],
    [17,20,18],
    [14,16,15]

])
students = ["Ali", "Reza", "Sara", "Maryam", "Amir"]
averages=scores.mean(axis=1)
for name,avg in zip(students,averages):
    print(f"{name} | Average: {avg:.2f}")