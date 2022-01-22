from fastapi import FastAPI

from api.endpoints import router
from src import logger


def create_app() -> FastAPI:
    app = FastAPI(
        title="API", openapi_url="/api/openapi.json", version="0.1.0"
    )
    app.include_router(router, prefix="/api")
    logger.debug("App created.")
    return app


app = create_app()
