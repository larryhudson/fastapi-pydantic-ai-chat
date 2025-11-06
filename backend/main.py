# main.py
from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.ui.vercel_ai import VercelAIAdapter
from dotenv import load_dotenv
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider

# Load environment variables
load_dotenv()


class Weather(BaseModel):
    """Weather data model."""
    city: str
    condition: str
    temperature: float
    unit: str = "F"


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
def get_weather(city: str) -> Weather:
    """Get the weather for a city."""
    return Weather(city=city, condition="Sunny", temperature=72.0)


@app.get("/tools-schema")
def tools_schema():
    """
    Export JSON schemas for all tool output types with tool name mapping.

    This endpoint enables automatic type generation on the frontend.
    The frontend script (scripts/generate-types.js) fetches this schema and uses
    json-schema-to-typescript to generate TypeScript type definitions.

    Structure:
    {
        "tools": {
            "tool_name": {
                "output": <JSON Schema of the tool's output Pydantic model>
            }
        }
    }

    To add a new tool:
    1. Define a Pydantic model for the tool's output (e.g., Weather class)
    2. Create a @agent.tool_plain function with that return type (e.g., get_weather)
    3. Add an entry to this endpoint mapping tool name to its output schema
    4. Frontend: Run `npm run generate:types` to regenerate TypeScript types
    5. Frontend: Add renderer to toolRenderers.tsx

    Example:
        @agent.tool_plain
        def my_tool(param: str) -> MyOutput:
            '''Tool description.'''
            return MyOutput(...)

        # In /tools-schema return:
        "my_tool": {
            "output": MyOutput.model_json_schema(),
        }
    """
    return {
        "tools": {
            "get_weather": {
                "output": Weather.model_json_schema(),
            }
            # Add more tool schemas here as you add new tools
        }
    }


@app.post("/chat")
async def chat(request: Request) -> Response:
    """Streaming chat endpoint using Vercel AI protocol."""
    return await VercelAIAdapter.dispatch_request(request, agent=agent)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
