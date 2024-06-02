# Backend project on FAST API for kek-online-cinema-hall

* [Documents](./docs)
    * [kek architect plan]()



## Poetry



## Arch

```
fastapi-project
├── etc
├── docs
├── src
│   ├── auth
│   │   ├── router.py
│   └── main.py
├── tests/
├── templates/
├── .env
├── .gitignore
├── poetry.lock
└── pyproject.toml
```


```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'response': 'This is a FastApi backend app'}
```




## API




## Run:

```
uvicorn main:app --reload
```