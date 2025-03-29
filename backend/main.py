from fastapi import FastAPI
from api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app = FastAPI(title="ClickBait API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routes
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to ClickBait API!"}
