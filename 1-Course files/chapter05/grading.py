
k = int(input("enter your grade score: "))

grade_rubric = ["A","B","C","D","F"]

if k == 0:
    print("Your final grade is F")
    quit()
final_score = 5 - int(k)

print("Your final grade is "+grade_rubric[final_score])

scores = [(5, "A"), (4, "B"), ((3, "C"))]
d = dict()
d[5] = "Sprite"
d[4] = "Coke"
d[3] = "Fanta"


