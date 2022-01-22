from fastapi import APIRouter

from api import schemas
from src import logger

router = APIRouter()


@router.get("/", response_model=schemas.Root)
async def get_root() -> schemas.Root:
    logger.debug("msg='OK!'")
    return schemas.Root.construct(msg="OK!")
