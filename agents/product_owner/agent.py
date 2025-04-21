from google.adk.agents import LlmAgent, BaseAgent
from .prompt import system_prompt
from google.adk.tools import ToolContext


def save_prd(product_requirements_document: str, tool_context: ToolContext):
    """
    Saves the product requirements document.
    """
    tool_context.state["product_requirements_document"] = product_requirements_document


agent = LlmAgent(
    name="product_owner",
    description="A product owner agent that is responsible for the product vision and strategy",
    model="gemini-2.0-flash",
    instruction=system_prompt,
    tools=[save_prd],
)
