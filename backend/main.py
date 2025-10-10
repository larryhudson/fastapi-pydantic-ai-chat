# main.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessage
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

# Load environment variables
load_dotenv()

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Bedrock model with co2-develop profile
bedrock_model = BedrockConverseModel(
    "eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
    provider=BedrockProvider(
        profile_name="co2-develop",
    ),
)

# Create agent with tools
agent = Agent(model=bedrock_model)

@agent.tool_plain
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"Weather in {city}: Sunny, 72°F"


class ChatRequest(BaseModel):
    messages: List[ModelMessage]  # Pydantic AI's native type

class ChatEvent(BaseModel):
    type: str  # 'delta' | 'complete'
    data: dict


@app.post("/chat")
async def chat(request: ChatRequest):
    """Simple streaming chat endpoint."""
    async def generate():
        print("request is here")
        print(request)

        # Extract the user's text from the last message
        user_prompt = request.messages[-1].parts[0].content if request.messages[-1].parts else ""

        # Run agent with message history (excluding the current message to avoid duplication)
        async with agent.run_stream(
            user_prompt,  # Current user prompt
            message_history=request.messages[:-1]  # Previous messages only
        ) as response:
            print("response is here")
            print(response)
            # Stream text deltas
            async for delta in response.stream_text(delta=True):
                event = ChatEvent(type="delta", data={"text": delta})
                yield f"data: {event.model_dump_json()}\n\n"

            # Send all messages when complete
            event = ChatEvent(
                type="complete",
                data={"messages": response.all_messages()}
            )
            yield f"data: {event.model_dump_json()}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
