# AI Agent Project

> A lightweight, agentic AI coding assistant built with Python, uv, and the Gemini API — inspired by tools like Cursor, OpenCode, and Claude Code.

This project is a simplified agentic AI coding assistant inspired by tools like Cursor, OpenCode, and Claude Code. It was built as part of the Boot.dev "Build an AI Agent".

## 🚀 Overview

The AI Agent is a command-line tool that can take a natural-language coding task, inspect files, modify code, run Python scripts, and iteratively work toward completing the task.

At its core, the agent:

1. Accepts a user instruction (e.g., *"Fix the bug in my calculator app"*)
2. Lets the LLM choose from predefined Python functions, such as:

   * **Scan a directory**
   * **Read a file**
   * **Write/overwrite a file**
   * **Execute a Python file**
3. Repeats these actions until the task is solved or the agent fails


---

## 📌 Example Usage

```
uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly.
```

---

## 🧰 Features

* Natural-language task input
* Automatic file inspection
* Intelligent file editing via LLM
* Ability to run Python scripts to validate changes
* Looping agent that continues until the task is done

---

## 📦 Prerequisites

Before running the project, ensure you have:

* **Python 3.10+** installed
* **uv** Python project/packager installed
* A **Unix-like shell** (bash/zsh)
* **Google Gemini API access** (free tier works)

---



## ▶️ Running the Agent

Use:

```
uv run main.py "your task here"
```

Example:

```
uv run main.py "scan the project and summarize what files contain errors"
```

---

## 🎯 Goals

* Multi-file Python project structure
* Function-calling with LLMs
* Building a basic agent loop
* File manipulation and script execution from Python
* Understanding how modern "AI coding" tools work internally

---
