# System Prompting

System prompting are the "system message" passed to LLMs, on top of user queries. System prompting can

1. Provide LLM more information about the conversation like "who said each sentence" (user vs LLM)
2. Define specialized role and purpose of the AI application (e.g. "you are a code debugger" or "you are a oncall assistant" etc.)
3. Provide tools to LLM (e.g. MCP function definitions, see [this huggingface course](https://huggingface.co/learn/agents-course/en/unit1/tools) for more about providing tools via system prompt)
4. Provide knowledge bases (e.g. RAG) for LLMs
5. Define input / output structure (format) for LLM
6. More ...

## Modularize System Prompting

All the controls over LLMs are made through system prompts. As aforementioned, the system prompting can get quite complex that it tries to provide things that serves different purposes. For a scalable development of an AI application, it is important to modularize its system prompt so it can be maintained by different team and reused in new AI products.

TODO - what is the best practice for modularize system prompt? with Agent.md?

## Best Practice

WIP https://dev.to/simplr_sh/mastering-system-prompts-for-llms-2d1d 