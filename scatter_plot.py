import matplotlib.pyplot as plt

# Study hours and exam scores for Class A
class_a_hours = [2, 4, 6, 8]
class_a_scores = [45, 95, 65, 85]
v
# Study hours and exam scores for Class B
class_b_hours = [1, 3, 5, 7, 9]
class_b_scores = [40, 50, 60, 70, 95]

# Scatter plot for both classes
plt.scatter(class_a_hours, class_a_scores, label='Class A', color='blue')
plt.scatter(class_b_hours, class_b_scores, label='Class B', color='orange')

plt.title('Scatter Plot: Class A vs Class B')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()
