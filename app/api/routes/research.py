from fastapi import APIRouter

router = APIRouter(
    tags=["Research"]
)


@router.get("/research")
async def research_home():

    return {
        "message": "Research agent endpoint"
    }