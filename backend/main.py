from fastapi import FastAPI

from modules.community.router import router as community_router
from modules.user.router import router as user_router
from modules.auth.router import router as auth_router
from modules.division.router import router as division_router
from modules.member_category.router import (router as member_category_router,)
from modules.member.router import router as member_router

app = FastAPI(
    title="Community Accounting Management System",
    version="1.0.0",
)

app.include_router(community_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(division_router)
app.include_router(member_category_router)
app.include_router(member_router)


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