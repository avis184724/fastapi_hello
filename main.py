from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("메인 페이지에 접속했습니다.")
    return {"message" : "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message" : f"안녕, {name}님!"}