# Agent Raven

Raven is an AI agent for news list management and summarizing. The agent manages the new list by keeping a local database with the "already read" pagination token. The agent reads the subscribed news list and summarize new articles haven't been read yet.

## Usage

### Subscribe News Source

```
agent-raven subscribe <news-url>
```

### Unsubscribe News Source

```
agent-raven unsubscribe <news-url>
```

### List Subscribed Source

```
agent-raven list <regex match>
```

### Generate Summarize

```
agent-raven summary
```

Available option for summary generation

1. `--date YYYY/MM/DDTHH:MM:SS` : setting the start date to consider the summarization, default is the "last time summary generated" or "date subscribed" if no summary has been generated for this source
2. `--incognido` : do NOT remember that a summary has been generated (does not update the "last time summarized" info)
3. `--target "regex match"` : only generate summary for the target news source URLs that matches the input target 
4. `--time-suffix` : add UTC time (second granularity) to the suffix of summary file, by default the summary is stored to `out/summary.html` file

## Design

Raven be built with LangChain using locally hosted LLMs (with ollama). It will use a database tool (a script) to access persistent information including the subscription list and last access time of each URL page. It will use a web loading tool to access the target URL for content retrival (**TODO** for making it work for pages that is blocked behind CAPTCHA or login)