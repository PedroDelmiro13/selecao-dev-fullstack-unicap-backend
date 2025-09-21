import time, uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.sentiment import analyze_sentiment

router = APIRouter()

class AnalyzeRequest(BaseModel):
    task: str
    input_text: str
    use_external: bool = False
    options: dict | None = None

@router.post("/analyze")
def analyze(request: AnalyzeRequest):
    if request.task != "sentiment":
        raise HTTPException(status_code=400, detail="Tarefa nao suportada")

    start = time.time()
    
    #metodo para processar os sentimentos, passa como parâmetro o texto enviado no body
    result = analyze_sentiment(request.input_text)
    elapsed = int((time.time() - start) * 1000)

    return {
        "id": str(uuid.uuid4()),
        "task": request.task,
        "engine": "local:distilbert",
        "result": result,
        "elapsed_ms": elapsed,
        "received_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
