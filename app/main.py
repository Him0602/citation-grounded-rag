from fastapi import FastAPI

app = FastAPI(title="Citation Grounded RAG")


@app.get("/")
def root():
    return {"message": "Citation Grounded RAG API is running"}