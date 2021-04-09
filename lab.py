import json
from prettytable import PrettyTable
jsa = open("index.json")
data = json.load(jsa)

n = len(data["students"]) # Количество студентов
x = PrettyTable(["Номер", "Имя", "Фамилия","Мат. анализ","Философия", "Средняя оценка", "Средний балл группы"])

# Средняя оценка
def averageScore(i):
    score = data["students"][str(i+1)]["grades"]
    average = (int(score["matanaliz"]) + int(score["philosophy"]))/2
    return average
def averageGroup(i):
    s=0
    for j in range(n):
        s+= averageScore(j)
    answer = s/n
    return answer
    


for i in range(n):
    x.add_row(
        [
            i+1,
            data["students"][str(i+1)]["firstName"],
            data["students"][str(i+1)]["lastName"],
            data["students"][str(i+1)]["grades"]["matanaliz"],
            data["students"][str(i+1)]["grades"]["philosophy"],
            averageScore(i),
            averageGroup(i),
        ])
print(x)



