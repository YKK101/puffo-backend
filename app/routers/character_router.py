from fastapi import APIRouter
from app.schemas import Element
from app.services import create_character

router = APIRouter()


@router.post("/characters")
async def create_characters(ingredients: list[Element]):
    res = await create_character(ingredients)
    return res
