# MCP (Model Context Protocol)

## MCP Workflow

MCP is one of the most popular standard that provides **tools** for LLMs. The general flow of an AI application using LLM and MCP is

```
User Query
    ↓
Your App sends to LLM with:
  - User message
  - Available MCP tools (as function definitions)
    ↓
LLM responds with tool calls
    ↓
Your App executes MCP calls
    ↓
Your App sends results back to LLM
    ↓
LLM synthesizes final response
    ↓
User receives answer
```

There are a few critical points worth noting

1. There are at least 2 LLM queries when using MCP, where the first query make LLM plan for what MCP to call and the second query make LLM consume the MCP call result
2. The MCP calls are executed by the *user host*, while the list of MCP tools to call and their parameters are decided in LLM response
3. Available MCP tools (function definitions) is concatenated with user query, consuming context window
4. To make the AI application able to understand the "MCP list and parameters to call", many new LLMs are trained to use **structured output format** (basically the LLM respond MCP calls with predefined format)

## MCP Communication

In the MCP standard, it defined the serialization format (`JSON-RPC 2.0`) for MCP requests and responses, and some normal ways of communicating the MCP messages.

1. For local MCP server, the response can be communicated via `stdio`
2. For remote MCP calls, the messages are communicated with **HTTP** (and SSE when needed)

So, **an MCP server is a HTTP server** with some customization around other MCP standard requirements. As a result, the MCP SDK for defining a new MCP server is very similar as creating a HTTP server. For example, the experience of `FastMCP` framework is almost identical as `FastAPI`.

## MCP Client Framework

In its very basic, a MCP client is to communicate with the MCP server, which is basically a HTTP client. But to make MCP useful, the AI application needs more than just a MCP client, but a client-side framework that handles the [MCP workflow](#mcp-workflow). And unsurprisingly, there are many such framework like `LangChang`, which handles basically the whole MCP workflow for the AI application.

Basically, the only thing left for the application or the user to do is to **configure available MCP tools**. Some tools can be

- Local scripts (e.g. for code or file search)
- Remote tools (e.g. database queries)
- Other agents (e.g. delegating to other agent)

## References

- [Huggingface MCP Course](https://huggingface.co/learn/mcp-course/en/unit1/hf-mcp-server)