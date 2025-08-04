from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Optional

# Create MCP server instance
mcp = FastMCP("TodoMCP")

# In-memory mock database
tasks: List[Dict] = []
task_counter = 0

# Tool: Add a new task
@mcp.tool()
def add_task(task: str, due: Optional[str] = None) -> str:
    """Add a new task with an optional due date"""
    global task_counter
    task_counter += 1
    tasks.append({"id": task_counter, "task": task, "due": due, "done": False})
    return f"✅ Task added: {task} (ID: {task_counter})"

# Tool: List all tasks
@mcp.tool()
def list_tasks() -> List[str]:
    """List all tasks with their status"""
    if not tasks:
        return ["No tasks available."]
    return [
        f"{t['id']}. {t['task']} "
        f"{'(Done)' if t['done'] else '(Pending)'}"
        + (f" [Due: {t['due']}]" if t['due'] else "")
        for t in tasks
    ]

# Tool: Mark a task as done
@mcp.tool()
def mark_done(task_id: int) -> str:
    """Mark a task as completed"""
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return f"✅ Task {task_id} marked as done."
    return f"❌ Task with ID {task_id} not found."

# Resource: Get a specific task by ID
@mcp.resource("todo://task/{task_id}")
def get_task(task_id: int) -> str:
    """Return the task details by ID"""
    for t in tasks:
        if t["id"] == task_id:
            status = "Done" if t["done"] else "Pending"
            due_str = f", Due: {t['due']}" if t["due"] else ""
            return f"Task {task_id}: {t['task']} ({status}{due_str})"
    return f"Task with ID {task_id} not found."

# Resource: Get all tasks summary
@mcp.resource("todo://all")
def get_all_tasks() -> str:
    """Return a summary of all tasks"""
    if not tasks:
        return "No tasks available."
    summary = "\n".join(
        [
            f"{t['id']}. {t['task']} ({'Done' if t['done'] else 'Pending'})"
            + (f" [Due: {t['due']}]" if t['due'] else "")
            for t in tasks
        ]
    )
    return f"📋 All Tasks:\n{summary}"

# Resource: Get today's tasks
@mcp.resource("todo://today")
def get_today_tasks() -> str:
    """Return a summary of today's tasks"""
    if not tasks:
        return "No tasks for today."
    summary = "\n".join(
        [f"- {t['task']} ({'Done' if t['done'] else 'Pending'})" for t in tasks]
    )
    return f"📋 Today's Tasks:\n{summary}"

# Prompt: Generate motivational message
@mcp.prompt()
def motivate_user() -> str:
    """Generate a motivational message based on tasks"""
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    if total == 0:
        return "You have no tasks today — enjoy your free time! 🎉"
    return f"Keep going! 💪 You’ve finished {done}/{total} tasks. {pending} left to conquer!"

# Run the MCP server
if __name__ == "__main__":
    mcp.run()
