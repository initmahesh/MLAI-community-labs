# Integrating Langflow with Lovable

This guide explains how to integrate Langflow with your Lovable application. You can watch the detailed video tutorial [here](https://pragyaallc-my.sharepoint.com/:v:/g/personal/sachin_parmar_legalgraph_ai/EU8bby8ZCgJHqcAISsIKnqUB2JIlXQu_khe82IS2xJFUog?e=wqZvDq&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D).

## Configuration

### 1. Vite Configuration

Set up your `vite.config.ts` to proxy requests to the Langflow API:

```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";

export default defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
    proxy: {
      "/langflow": {
        target: "YOUR_LANGFLOW_API_ENDPOINT",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/langflow/, ""),
      },
    },
  },
  plugins: [react(), mode === "development" && componentTagger()].filter(
    Boolean
  ),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
}));
```

### 2. API Integration

Here's how to implement the API calls in your application:

```typescript
interface ChatMessage {
  content: string;
  role: "user" | "ai" | "assistant";
  timestamp: Date;
}

export const sendMessage = async (message: string): Promise<ChatMessage> => {
  try {
    const response = await fetch("/langflow", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer YOUR_AUTH_TOKEN",
      },
      body: JSON.stringify({
        input_value: message,
        output_type: "chat",
        input_type: "chat",
      }),
      signal: AbortSignal.timeout(5 * 60 * 1000), // 5 minute timeout
    });

    if (!response.ok) {
      throw new Error(`API responded with status: ${response.status}`);
    }

    const data = await response.json();

    const aiResponse =
      data?.outputs?.[0]?.outputs?.[0]?.outputs?.message?.message ||
      data?.outputs?.[0]?.outputs?.[0]?.results?.message?.text ||
      "I'm not sure how to respond to that.";

    return {
      content: aiResponse,
      role: "assistant",
      timestamp: new Date(),
    };
  } catch (error) {
    console.error("Failed to send message:", error);
    throw error;
  }
};
```

## Important Notes

1. Make sure to replace `YOUR_LANGFLOW_API_ENDPOINT` in the Vite configuration with your actual Langflow API endpoint.
2. Replace `YOUR_AUTH_TOKEN` with your actual authentication token.
3. The API endpoint and token in the example code are placeholders and need to be updated with your actual credentials.

