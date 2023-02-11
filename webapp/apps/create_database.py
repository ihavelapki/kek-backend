from webapp.apps.database import engine
from webapp.apps.tables import Base

Base.metadata.create_all(engine)

