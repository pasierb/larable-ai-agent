from google.adk.agents import LlmAgent, BaseAgent
from .prompt import system_prompt
from ..product_owner.agent import agent as product_owner_agent
from ..software_architect.agent import agent as software_architect_agent

agent = LlmAgent(
    name="supervisor",
    description="A supervisor agent that oversees the work of the team",
    model="gemini-2.0-flash",
    instruction=system_prompt,
    sub_agents=[
        product_owner_agent,
        software_architect_agent,
    ],
    tools=[],
)
