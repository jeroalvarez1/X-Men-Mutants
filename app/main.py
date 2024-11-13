from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.versions.v2.routers import human as v1_human
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def main():
    return RedirectResponse(url="/docs")

app.include_router(v1_human.router, prefix="/api/v2/human", tags=["Human V2"])