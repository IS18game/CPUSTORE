from fastapi import APIRouter

router = APIRouter(prefix="/promotions", tags=["promotions"])

@router.get("/")
def get_promotions():
    return {"message": "Promotion endpoint is working"}
