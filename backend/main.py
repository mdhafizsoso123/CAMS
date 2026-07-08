from fastapi import FastAPI

app = FastAPI(
    title="Community Accounting Management System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Community Accounting Management System API"}

@app.get("/health")
def health():
    return {"status": "healthy"}