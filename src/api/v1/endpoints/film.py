from fastapi import APIRouter

router = APIRouter()

@router.get("/{item_id}")
async def get_film_info(item_id: int):
    return {"item_id": item_id, "info": "This is a description of the film with {item_id} id"}