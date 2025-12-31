# AI Agent

The major difference between AI agents and traditional LLM applications (e.g. the initial ChatGPT webpage) is that agent is capable of "iterating on itself" with the use of tooling and observing/verifying result. An agent is able to close the loop of "plan --> execute --> verify" independently with the support of sufficient tools, and only present the final result to the user.

## Define An Agent

Below is an example of defining an AI agent with SDK (it is likely even simpler to define a customized agent in an application supporting agent mode already, like Amazon Q)

```
final_answer = FinalAnswerTool()
model = InferenceClientModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
# We're creating our CodeAgent
agent = CodeAgent(
    model=model,
    tools=[final_answer], # add your tools here (don't remove final_answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)

GradioUI(agent).launch()
```

And the **critical input** for the agent are

- description of the agent
- tools
- prompt template (basically the system prompts)

## References

- [Huggingface Agent Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)
- [LangChain Agent](https://docs.langchain.com/oss/python/langchain/agents)