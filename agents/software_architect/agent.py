from google.adk.agents import LlmAgent
from .prompt import system_prompt
from google.adk.tools import ToolContext


def save_tdd(technical_design_document: str, tool_context: ToolContext):
    """
    Saves the technical design document.
    """
    tool_context.state["technical_design_document"] = technical_design_document


agent = LlmAgent(
    name="software_architect",
    description="A software architect agent specialized in Laravel applications",
    model="gemini-2.0-flash",
    instruction=system_prompt,
    tools=[save_tdd],
)
