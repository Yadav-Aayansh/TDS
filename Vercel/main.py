from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/api")
def api(name: list[str] = Query(...)):
    with open("students.json", 'r') as file:
        students = json.load(file)

    marks = list()
    for n in name:
        for student in students:
            if student["name"] == n:
                marks.append(student["marks"])

    result = {"marks": marks}
    return result
