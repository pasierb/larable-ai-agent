import os
import subprocess
from typing import List
from pathlib import Path
from google.adk.agents import LlmAgent
from .prompt import system_prompt
from google.adk.tools import ToolContext

CODEBASE_PATH = Path("/Users/mpasierbski/work/larable")


def browse_codebase(tool_context: ToolContext) -> List[str]:
    """
    Browse the codebase to find the files that need to be updated.
    
    Returns:
        List[str]: List of file paths relative to the codebase root
    """
    try:
        # Use pathlib for more idiomatic path handling
        result = subprocess.run(
            ["find", "app", "config", "database", "routes", "resources", "-type", "f"],
            cwd=CODEBASE_PATH,
            capture_output=True,
            text=True,
            check=True  # Raises CalledProcessError if command fails
        )
        files = result.stdout.splitlines()
        tool_context.state["codebase"] = files
        return files
    except subprocess.CalledProcessError as e:
        tool_context.state["codebase"] = []
        return []


def get_file_content(file_path: str, tool_context: ToolContext) -> str:
    """
    Get the content of a file.
    
    Args:
        file_path: Path to the file relative to the codebase root
        tool_context: Tool context for state management
        
    Returns:
        str: Content of the file or error message if file cannot be read
    """
    try:
        full_path = os.path.join(CODEBASE_PATH, file_path)
        with open(full_path, 'r') as file:
            return file.read()
    except (FileNotFoundError, PermissionError) as e:
        return f"Error reading file {file_path}: {str(e)}"


def update_file(file_path: str, content: str, tool_context: ToolContext) -> str:
    """
    Update a file with the given content.
    
    Args:
        file_path: Path to the file relative to the codebase root
        content: New content to write to the file
        tool_context: Tool context for state management
        
    Returns:
        str: Success message or error message if file cannot be updated
    """
    try:
        full_path = os.path.join(CODEBASE_PATH, file_path)
        with open(full_path, 'w') as file:
            file.write(content)
        return f"File {file_path} updated successfully"
    except (FileNotFoundError, PermissionError) as e:
        return f"Error updating file {file_path}: {str(e)}"


def run_artisan_command(command_parts: List[str], tool_context: ToolContext) -> str:
    """
    Run a Laravel artisan command.

    Args:
        command_parts: list of strings, the command to run. Executed as `php artisan <command_parts[0]> <command_parts[1]> ...`

    Returns:
        The output of the command.
    """

    result = subprocess.run(
        ["php", "artisan", *command_parts],
        cwd=CODEBASE_PATH,
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error running artisan command {command_parts}: {result.stderr}"

def check_rules(file_path: str, tool_context: ToolContext):
    """
    Check if any of the rules for AI apply to the file.
    """
    pass


agent = LlmAgent(
    name="software_engineer",
    description="A software engineer agent specialized in Laravel applications",
    model="gemini-2.0-flash",
    instruction=system_prompt,
    tools=[
        browse_codebase,
        get_file_content,
        update_file,
    ],
)
