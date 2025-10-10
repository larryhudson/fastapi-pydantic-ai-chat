import { useState } from 'react';
import type {
  ChatRequest,
  ChatRequestMessagesInner,
  ModelRequest,
  ModelResponse,
  TextPart
} from '../api';

export function useChat() {
  const [messages, setMessages] = useState<ChatRequestMessagesInner[]>([]);
  const [streamingText, setStreamingText] = useState("");
  const [isStreaming, setIsStreaming] = useState(false);

  const sendMessage = async (userMessage: string) => {
    // Create new user message
    const newUserMessage: ModelRequest & { kind: 'request' } = {
      kind: "request",
      parts: [{
        part_kind: "user-prompt" as const,
        content: userMessage,
        timestamp: new Date().toISOString(),
      }],
    };

    setMessages(prev => [...prev, newUserMessage]);

    // Use all messages for API request
    const apiMessages = [...messages, newUserMessage];

    const requestBody: ChatRequest = {
      messages: apiMessages,
    };

    setIsStreaming(true);
    setStreamingText("");

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody),
      });

      if (!response.body) throw new Error("No response body");

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;

          const data = JSON.parse(line.slice(6));

          if (data.type === "delta") {
            setStreamingText(prev => prev + data.data.text);
          } else if (data.type === "complete") {
            // Replace all messages with the complete history from the backend
            const completeMessages = data.data.messages as ChatRequestMessagesInner[];
            setMessages(completeMessages);
            setStreamingText("");
          }
        }
      }
    } catch (error) {
      console.error("Chat error:", error);
      const errorMessage: ModelResponse & { kind: 'response' } = {
        kind: "response",
        parts: [{
          part_kind: "text" as const,
          content: "Error: Failed to get response",
        }],
        timestamp: new Date().toISOString(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsStreaming(false);
    }
  };

  return {
    messages,
    streamingText,
    isStreaming,
    sendMessage,
  };
}
