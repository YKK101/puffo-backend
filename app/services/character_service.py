import asyncio
from app.schemas import Element
from app.constants import MAX_INGREDIENTS, MIN_INGREDIENTS
from app.libs import OpenAIConnector
from app.schemas import OpenAIChatMessage

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

    messages = [
        OpenAIChatMessage(
            role="system",
            content="You are a creative assistant who designs unique monsters based on chemical reactions. For each monster, respond in the following format: {\"name\": [Monster's Name], \"personality\": [Traits based on reaction characteristics like volatile = short-tempered, steady = calm], \"highlight_feature\": [Monster's standout ability]} Be concise but imaginative."
        ),
        OpenAIChatMessage(
            role="user",
            content=f"Here are the ingredients: {', '.join([f'{el.element_name} ({el.element_symbol})' for el in ingredients])}. What's the monster like?"
        )
    ]

    openai = OpenAIConnector()
    response = await openai.create_chat_completion(messages=messages)

    return { "test": response.content }

