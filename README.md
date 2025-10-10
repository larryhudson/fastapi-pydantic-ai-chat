# FastAPI + Pydantic AI Streaming Chat

A minimal demonstration of end-to-end type-safe streaming chat using:
- **FastAPI + Pydantic AI** backend with tool support
- **Server-Sent Events** for streaming responses
- **OpenAPI → TypeScript** code generation for type safety
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

### Type Safety Flow
1. Backend defines `ChatRequest` with `List[ModelMessage]` (Pydantic AI types)
2. Export OpenAPI schema: `uv run python export_openapi.py`
3. Generate TypeScript client: `npx @openapitools/openapi-generator-cli generate ...`
4. Frontend uses generated types - **no manual type definitions needed**

### Streaming Implementation
- **Backend**: `StreamingResponse` with SSE format (`data: {json}\n\n`)
- **Frontend**: `ReadableStream` with `getReader()` to process deltas
- **Real-time**: Text appears character-by-character as it's generated

### Message Handling
- **Full history**: Entire conversation sent with each request
- **Tool calls**: Automatically tracked in message history
- **Type-safe**: Frontend and backend share identical message structure

## Project Structure

```
├── backend/
│   ├── main.py              # FastAPI app with streaming endpoint
│   ├── export_openapi.py    # Schema generator
│   └── openapi.json         # Generated OpenAPI schema
└── frontend/
    ├── src/
    │   ├── api/             # Generated TypeScript client
    │   ├── hooks/useChat.ts # Chat hook with SSE handling
    │   └── components/Chat.tsx
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
