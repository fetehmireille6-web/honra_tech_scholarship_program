from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return{"message": "Hello! Welcome to my first FastAPI backend!, my name is Feteh Mireille Lareine."}
@app.get("/about")
def get_info():
    return{"course_name": "Generative AI course", "instructor": "Selamo Allen", "student": "Feteh Mireille Lareine", "week": 2, "day": 1, "number_of_weeks": 6}
@app.get("/health")
def health_check():
    return{"status": "healthy"}