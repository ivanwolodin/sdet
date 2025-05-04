from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from dotenv import load_dotenv

from app.api.v1.auth import router as auth_router
from app.core.config import config

load_dotenv(dotenv_path=".env-test")

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)


@app.get("/api/main")
async def main():
    return {"message": "ok"}


app.include_router(auth_router, prefix='/api/v1')
