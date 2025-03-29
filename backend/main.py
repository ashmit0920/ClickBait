from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="ClickBait API")

# Include API routes
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to ClickBait API!"}
