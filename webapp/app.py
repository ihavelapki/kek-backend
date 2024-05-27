from fastapi import FastAPI
from api import router

# import uvicorn

app = FastAPI()
app.include_router(router)


@app.get('/')
def index():
    return {'aaaaa': 'bbbb'}


# if __name__ == '__main__':
#     uvicorn.run(app)

