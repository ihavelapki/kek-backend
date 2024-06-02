from fastapi import APIRouter

router = APIRouter()

@router.get("/{item_id}")
async def get_user_info(item_id: int):
    return {"item_id": item_id, "info": "This is a description of the user with {item_id} id"}