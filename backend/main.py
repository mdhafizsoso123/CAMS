from fastapi import FastAPI

from modules.community.router import router as community_router

app = FastAPI(
    title="Community Accounting Management System",
    version="1.0.0",
)

app.include_router(community_router)


@app.get("/")
def root():
    return {
        "application": "Community Accounting Management System",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
    }