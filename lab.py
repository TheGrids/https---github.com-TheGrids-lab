import json
from prettytable import PrettyTable
jsa = open("index.json", encoding='utf-8')
data = json.load(jsa)

n = len(data["students"]) # Количество студентов
subject = ["Мат. Анализ","Философия"]
x = PrettyTable(["Номер", "Имя", "Фамилия","Мат. анализ","Философия", "Средняя оценка"])
y = PrettyTable()
z = PrettyTable(["Имя", "Фамилия", "Повышенная стипендия","Обычная стипендия","Без стипендии"])

# Средняя оценка
def averageScore(i):
    score = data["students"][str(i+1)]["grades"]
    average = (int(score["Мат. Анализ"]) + int(score["Философия"]))/2
    return average
    


for i in range(n):
    x.add_row(
        [
            i+1,
            data["students"][str(i+1)]["firstName"],
            data["students"][str(i+1)]["lastName"],
            data["students"][str(i+1)]["grades"]["Мат. Анализ"],
            data["students"][str(i+1)]["grades"]["Философия"],
            averageScore(i),
        ])
print(x)

for j in range(len(subject)):
    gradesSubject = []
    for i in range (1,n+1):
        gradesSubject.append(int(data["students"][str(i)]["grades"][str(subject[j])]))
    y.add_column(subject[j],[sum(gradesSubject)/len(gradesSubject)])

print(y)

def checkGrades(student,ss):
    for i in range(len(subject)):
        check = None
        if data["students"][str(student)]["grades"][str(subject[i])] == "3":
            check = False
            break
        elif data["students"][str(student)]["grades"][str(subject[i])] == "4":
            check = True
            break
    if ss == check: return "✓"
    else: return "-"

for i in range(1,n+1):
    z.add_row([
        data["students"][str(i)]["firstName"],
        data["students"][str(i)]["lastName"],
        checkGrades(i,None),
        checkGrades(i,True),
        checkGrades(i,False)
    ])

print(z)


