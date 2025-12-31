from langchain.agents import create_agent

class RavenAgent:
    _agent = None

    def get_agent(self):
        if self._agent is None:
            self._agent = create_agent(
                name="raven",
                description="An agent that excels in problem-solving and decision-making tasks.",
                tools=["search", "data_analysis", "report_generation"],
                llm_model="gpt-4"
            )
        return self._agent

    def get_system_prompt(self):
        return (
            "You are Raven, an advanced AI agent designed to assist with complex tasks. "
            "Utilize your tools effectively to provide accurate and efficient solutions."
        )
