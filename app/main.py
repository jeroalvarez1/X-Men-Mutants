import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.versions.v2.routers import human as v2_human
from app.versions.v3.routers import human as v3_human
from app.database import engine, Base
from dotenv import load_dotenv

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def main():
    return RedirectResponse(url="/docs")

api_version = os.getenv('API_VERSION')

if api_version == 'v2':
    app.include_router(v2_human.router, prefix="/api/v2/human", tags=["Human V2"])
elif api_version == 'v3':
    app.include_router(v3_human.router, prefix="/api/v3/human", tags=["Human V3"])
else:
    app.include_router(v2_human.router, prefix="/api/v2/human", tags=["Human V2"])
    app.include_router(v3_human.router, prefix="/api/v3/human", tags=["Human V3"])