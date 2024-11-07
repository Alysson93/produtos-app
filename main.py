from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import api, frontend

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(api.router)
app.include_router(frontend.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
