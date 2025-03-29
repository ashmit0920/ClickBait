from fastapi import APIRouter
import random

router = APIRouter()

variations = ["variation1", "variation2", "variation3"]


@router.get("/variation")
def get_variation():
    selected_variation = random.choice(variations)
    return {"variation": selected_variation}
