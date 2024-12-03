import asyncio
from openai import AsyncOpenAI
from app.schemas import BaseModel, OpenAIChatMessage, OpenAIChatCompletionResponse, OpenAIImageResponse
import app.config as config

class OpenAIConnector:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)

    async def create_chat_completion(self, messages: list[OpenAIChatMessage], model: str = "gpt-3.5-turbo") -> OpenAIChatCompletionResponse:
        """
        Create a chat completion using OpenAI's API.

        Args:
        - messages (list[OpenAIChatMessage]): A list of messages to be used for the chat model.
        - model (str): The model to be used for generating chat completion.
        - response_format (BaseModel): An optional Pydantic model to format the response.

        Returns:
        - dict: A dictionary containing the chat completion result.
        """
        completion = await self.client.chat.completions.create(
            model=model,
            messages=[m.dict() for m in messages]
        )

        return OpenAIChatCompletionResponse(**completion.choices[0].message.dict())

    async def create_image(self, prompt: str, size: str = "1024x1024", model: str = "dall-e-2") -> list[OpenAIImageResponse]:
        """
        Create an image using OpenAI's API.

        Args:
        - prompt (str): The prompt to be used for generating the image.
        - size (str): The size of the image to be generated.

        Returns:
        - dict: A dictionary containing the image result.
        """
        response = await self.client.images.generate(prompt=prompt, size=size, model=model)
        return [OpenAIImageResponse(**image.dict()) for image in response.data]
