import { useState, useRef, useEffect } from 'react';
import { useChat } from '../hooks/useChat';
import type {
  ChatRequestMessagesInner,
  ModelRequest,
  ModelResponse,
  ModelResponsePartsInner,
  ModelRequestPartsInner,
  TextPart,
  ToolCallPart,
  ToolReturnPart
} from '../api';
import './Chat.css';

export function Chat() {
  const { messages, streamingText, isStreaming, sendMessage } = useChat();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, streamingText]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isStreaming) return;

    sendMessage(input);
    setInput('');
  };

  const renderPart = (part: ModelResponsePartsInner | ModelRequestPartsInner, idx: number) => {
    if (part.part_kind === 'text') {
      const textPart = part as TextPart;
      return <div key={idx} className="message-part message-part-text">{textPart.content}</div>;
    }

    if (part.part_kind === 'user-prompt') {
      return <div key={idx} className="message-part message-part-text">{(part as any).content}</div>;
    }

    if (part.part_kind === 'tool-call') {
      const toolCall = part as ToolCallPart;
      return (
        <div key={idx} className="message-part message-part-tool-call">
          <strong>🔧 Tool Call:</strong> {toolCall.tool_name}
          {toolCall.args && (
            <pre className="tool-args">{JSON.stringify(toolCall.args, null, 2)}</pre>
          )}
        </div>
      );
    }

    if (part.part_kind === 'tool-return') {
      const toolReturn = part as ToolReturnPart;
      return (
        <div key={idx} className="message-part message-part-tool-return">
          <strong>✅ Tool Result:</strong> {toolReturn.tool_name}
          <pre className="tool-result">{JSON.stringify(toolReturn.content, null, 2)}</pre>
        </div>
      );
    }

    if (part.part_kind === 'thinking') {
      return (
        <div key={idx} className="message-part message-part-thinking">
          <strong>💭 Thinking:</strong>
          <div className="thinking-content">{(part as any).content}</div>
        </div>
      );
    }

    return null;
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>FastAPI + Pydantic AI Chat</h1>
        <p>Streaming chat with tool support</p>
      </div>

      <details>
        <summary>Messages dump</summary>
        <pre className="messages-dump">{JSON.stringify(messages, null, 2)}</pre>
      </details>

      <div className="chat-messages">
        {messages.map((msg, idx) => {
          const role = msg.kind === 'request' ? 'user' : 'assistant';
          const messageObj = msg as ChatRequestMessagesInner;

          return (
            <div key={idx} className={`message message-${role}`}>
              <div className="message-role">{role}</div>
              <div className="message-content">
                {messageObj.parts.map((part, partIdx) => renderPart(part, partIdx))}
              </div>
            </div>
          );
        })}

        {streamingText && (
          <div className="message message-assistant streaming">
            <div className="message-role">assistant</div>
            <div className="message-content">
              {streamingText}
              <span className="cursor">▊</span>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about the weather or anything else..."
          disabled={isStreaming}
          className="chat-input"
        />
        <button type="submit" disabled={isStreaming || !input.trim()} className="chat-submit">
          {isStreaming ? 'Streaming...' : 'Send'}
        </button>
      </form>
    </div>
  );
}
