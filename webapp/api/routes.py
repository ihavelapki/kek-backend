from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from webapp.models.operations import Operation
from webapp.servises.operations import OperationService
# from webapp.data.database import Session

# from webapp.data.database import get_session
from webapp.data import tables

oper_router = APIRouter(prefix='/operations')


@oper_router.get('/', response_model=List[Operation])
def get_operations(service: OperationService = Depends()):
    return service.get_list()
