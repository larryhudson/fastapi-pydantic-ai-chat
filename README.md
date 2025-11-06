# FastAPI + Pydantic AI Streaming Chat

A minimal demonstration of end-to-end type-safe streaming chat using:
- **FastAPI + Pydantic AI** backend with tool support
- **Vercel AI Data Stream Protocol** for streaming responses
- **Vercel AI SDK** frontend with automatic type safety
- **React** frontend with real-time streaming UI

## Quick Start

### Using Makefile (Recommended)

```bash
# Install all dependencies
make install

# Run both backend and frontend together
make dev
```

### Manual Setup

**Backend** (uses [uv](https://docs.astral.sh/uv/))

```bash
cd backend
uv sync
cp .env.example .env  # Add your AWS credentials
uv run fastapi dev main.py
```

Backend runs at `http://localhost:8000`

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

## Key Features

### Type Safety
- **Pydantic AI** validates and serializes messages
- **Vercel AI Data Stream Protocol** provides standardized message format
- **Frontend types** automatically align with backend types
- No manual type definitions or code generation needed

### Streaming Implementation
- **Backend**: Uses `VercelAIAdapter.dispatch_request()` to handle Vercel AI protocol
- **Frontend**: Uses `@ai-sdk/react` `useChat()` hook for automatic streaming handling
- **Real-time**: Text appears character-by-character as it's generated

### Message Handling
- **Tool support**: Backend `@agent.tool_plain` decorated functions
- **Message history**: Automatically maintained by Vercel AI SDK
- **Type-safe**: Pydantic AI messages automatically converted to Vercel AI format

## Project Structure

```
├── backend/
│   ├── main.py              # FastAPI app with Pydantic AI
│   └── pyproject.toml       # Dependencies
└── frontend/
    ├── src/
    │   ├── hooks/useChat.ts      # Wrapper around Vercel AI's useChat
    │   ├── components/Chat.tsx    # Chat UI component
    │   └── App.tsx               # Main app
    └── package.json
```

## How It Works

**Backend** (`backend/main.py:52-80`):
```python
@app.post("/chat")
async def chat(request: ChatRequest):
    async def generate():
        async with agent.run_stream(...) as response:
            # Stream text deltas
            async for delta in response.stream_text(delta=True):
                yield f"data: {json}\n\n"
            # Send complete message history
            yield f"data: {complete_messages}\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")
```

**Frontend** (`frontend/src/hooks/useChat.ts:39-73`):
```typescript
const reader = response.body.getReader();
while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  // Parse SSE events
  if (data.type === "delta") {
    setStreamingText(prev => prev + data.data.text);
  } else if (data.type === "complete") {
    setMessages(data.data.messages);
  }
}
```

## Regenerate Types After Backend Changes

```bash
# Using Makefile
make generate-api

# Or manually:
cd backend
uv run python export_openapi.py

cd ../frontend
npx @openapitools/openapi-generator-cli generate \
  -i ../backend/openapi.json \
  -g typescript-axios \
  -o ./src/api
```

## Available Commands

- `make dev` - Run both backend and frontend
- `make backend` - Run backend only
- `make frontend` - Run frontend only
- `make install` - Install all dependencies
- `make generate-api` - Regenerate TypeScript client
- `make clean` - Clean generated files
- `make help` - Show all commands

## Documentation

See [GUIDE.md](./GUIDE.md) for detailed tutorial with step-by-step implementation guide.
