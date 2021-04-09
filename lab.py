import json
from prettytable import PrettyTable

jsn = open("index.json")
data = json.load(jsn)

count = int(input("Введите количество студентов: "))
subject = ["matanaliz", "philosophy"]

x = PrettyTable()

for i in range(1, count+1):
    a = data["students"][str(i)]["grades"]
    grades = []
    stipendiya = None
    for j in range(len(subject)):
        grades.append(a[subject[j]])
    if 3 in grades:
        stipendiya = False
        break
    elif 4 in grades:
        stipendiya = True

for i in range(1, count+1):
    a = data["students"][str(i)]
    x.add_(i,a["firstName"],a["lastName"])
    
# x.add_column("1",[10,3,323,5,6,3,2])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])
print(x)

