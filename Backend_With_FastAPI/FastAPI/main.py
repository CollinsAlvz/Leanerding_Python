from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}


@app.get("/url")
async def root():
    return {"url_curso": "http://localhost"}


@app.get("/prueba")
async def root():
    return {"prueba": "Esta verga funciona"}

# Run the live server: uvicorn main:app --reload
