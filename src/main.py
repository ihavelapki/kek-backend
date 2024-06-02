from fastapi import FastAPI
from .api.v1.router import api_router

# import uvicorn

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


@app.get('/')
async def index():
    return {'response': 'This is a FastApi backnd app'}


# if __name__ == '__main__':
#     uvicorn.run(app)
