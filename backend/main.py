# main.py
from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic_ai import Agent
from pydantic_ai.ui.vercel_ai import VercelAIAdapter
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


@app.post("/chat")
async def chat(request: Request) -> Response:
    """Streaming chat endpoint using Vercel AI protocol."""
    return await VercelAIAdapter.dispatch_request(request, agent=agent)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
