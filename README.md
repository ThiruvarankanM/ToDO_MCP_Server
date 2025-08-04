# Todo MCP Server

This project implements a To-Do List Manager using the MCP (Machine Cognition Platform) framework with Python.

---

## Prerequisites

- Python 3.13 installed (or compatible version)
- Git (for cloning and version control)
- Basic command line familiarity (Terminal on macOS/Linux or PowerShell on Windows)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
````

---

### 2. Create and activate a virtual environment

> This isolates project dependencies and avoids conflicts

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

---

### 3. Upgrade pip and install required packages

```bash
pip install --upgrade pip
pip install mcp uv typer
```

---

### 4. Initialize the MCP project (if not already initialized)

```bash
uv init MCP_Server
cd MCP_Server
```

> If this step is already done, just ensure you are inside the `MCP_Server` folder

---

### 5. Add MCP CLI dependencies to your project

```bash
uv add "mcp[cli]"
```

---

### 6. Install the MCP Server app from your `main.py`

```bash
uv run mcp install main.py
```

---

### 7. Run the MCP server

```bash
uv run mcp run main.py
```

---

## Usage Instructions

* Once running, you can use the Todo MCP commands via Claude Desktop or CLI interface.

* Example commands you may have implemented:

  * `add_task "Buy groceries"`
  * `list_tasks`
  * `mark_done 1`

---

## Notes

* If you get a warning about virtual environment path mismatch, you can ignore it or use the `--active` flag as shown:

  ```bash
  uv add "mcp[cli]" --active
  ```

* Always activate your virtual environment before running MCP commands to ensure the correct Python environment.

---

## Troubleshooting

* If a command is not found, check your Python version and that the `.venv` is activated.

* To deactivate the virtual environment:

  ```bash
  deactivate
  ```

---

## License

[MIT License](LICENSE)

---



If you want, I can also help you generate a **LICENSE** file or create example commands for testing! Would you like me to?
```
