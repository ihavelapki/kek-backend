from fastapi import APIRouter
from webapp.api.routes import oper_router

router = APIRouter()
router.include_router(oper_router)
