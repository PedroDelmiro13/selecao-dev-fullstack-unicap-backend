from fastapi import FastAPI
from app.routes import analyze
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#para rodar:
#uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

origins = [  
    "https://curly-journey-69pg45477g4c45xv-8000.app.github.dev", 
    "https://automatic-space-disco-9765q57x47jr29r97-5173.app.github.dev" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router, prefix="/api/v1")

@app.get("/api/v1/healthz")
def healthz():
    return {"status": "ok"}
