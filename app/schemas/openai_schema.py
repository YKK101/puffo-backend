from pydantic import BaseModel

class OpenAIChatMessage(BaseModel):
    role: str
    content: str

class OpenAIImageResponse(BaseModel):
    b64_json: str | None
    revised_prompt: str | None
    url: str | None

class OpenAIChatCompletionResponse(BaseModel):
    content: str
    refusal: str | None
    role: str
    audio: str | None
    function_call: str | None
    tool_calls: str | None
