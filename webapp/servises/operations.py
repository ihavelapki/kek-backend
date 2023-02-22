from typing import List
from fastapi import Depends

from sqlalchemy.orm import Session

from webapp.data import tables
from webapp.data.database import get_session


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Operation]:
        operations = (
            self.session
            .query(tables.Operation)
            .all())
        return operations