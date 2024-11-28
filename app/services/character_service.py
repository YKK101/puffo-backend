import asyncio
from app.schemas import Element
from app.constants import MAX_INGREDIENTS, MIN_INGREDIENTS

async def create_character(ingredients: list[Element]) -> dict:
    """
    Create a new character based on the given ingredients.

    Args:
    - ingredients (list[Element]): A list of ingredients to be used for creating the new character.
      The length of the list must be between MIN_INGREDIENTS and MAX_INGREDIENTS.

    Returns:
    - dict: A dictionary containing the newly created character.
    """
    if len(ingredients) < MIN_INGREDIENTS or len(ingredients) > MAX_INGREDIENTS:
        raise ValueError(
            f"Expected the length of ingredients to be between {MIN_INGREDIENTS} and {MAX_INGREDIENTS}"
        )

    return { "test": ingredients }

