from fastapi import FastAPI
# from api import router

# import uvicorn

app = FastAPI()
# app.include_router(router)


@app.get('/')
async def index():
    return {'response': 'This is a FastApi backnd app'}


# if __name__ == '__main__':
#     uvicorn.run(app)

