# ADK-Python Project Context

## Project Overview

The Agent Development Kit (ADK) is an open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic and deployment-agnostic, built for compatibility with other frameworks. ADK was designed to make agent development feel more like software development, making it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.

### Key Features
- **Rich Tool Ecosystem**: Utilize pre-built tools, custom functions, OpenAPI specs, or integrate existing tools
- **Code-First Development**: Define agent logic directly in Python for ultimate flexibility, testability, and versioning
- **Modular Multi-Agent Systems**: Design scalable applications by composing multiple specialized agents
- **Deploy Anywhere**: Easily containerize and deploy agents on Cloud Run or with Vertex AI Agent Engine

## Project Architecture

The ADK project follows a modular architecture with the following key components:

- `agents/` - Core agent functionality and definitions (LlmAgent, BaseAgent, etc.)
- `tools/` - Tool implementations for agents to interact with external systems
- `models/` - Model integrations (primarily Google GenAI models)
- `flows/` - Agent execution flows and connection management
- `cli/` - Command-line interface for ADK tools
- `evaluation/` - Agent evaluation and testing capabilities
- `sessions/` - Session management and storage
- `memory/` - Agent memory and state management
- `artifacts/` - File and artifact handling
- `code_executors/` - Code execution environments
- `events/` - Event handling for agent interactions
- `runners.py` - Core runner functionality

## Building and Running

### Development Setup
1. Clone the repository: `gh repo clone google/adk-python`
2. Install development tools (uv recommended)
3. Create a virtual environment: `uv venv --python "python3.11" ".venv"`
4. Activate virtual environment: `source .venv/bin/activate`
5. Install dependencies: `uv sync --all-extras`
6. Run unit tests: `pytest ./tests/unittests`

### Build Commands
- Format code: `./autoformat.sh`
- Build package: `uv build`
- Run tests: `pytest tests/unittests`
- Install in development mode: `uv sync --all-extras`

### CLI Usage
The package provides an `adk` command-line tool for various operations:
- `adk web` - Launch the development UI
- `adk eval` - Evaluate agents
- `adk deploy` - Deployment commands

## Development Conventions

### Code Style
- Follows Google Python Style Guide
- Uses 2-space indentation
- Maximum 80 character line length
- Use `pylint` and `pyink` for formatting (enforced via `./autoformat.sh`)
- In ADK source: use relative imports, `from __future__ import annotations`
- In ADK tests: use absolute imports

### Testing
- Unit tests in `tests/unittests/` using pytest
- Integration tests in `tests/integration/`
- Tests must cover new features, edge cases, and error conditions
- End-to-end tests required for complex changes

### Versioning
- Follows Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH)
- Breaking changes require MAJOR version bump
- Public API includes Python interfaces, data schemas, CLI, and API formats
- Use conventional commits format for commit messages

### Public API Surface
The public API includes:
- All public classes, methods, and functions in the `google.adk` namespace
- Built-in tools' names, parameters, and expected behavior
- Persisted data schemas (Session, Memory, Evaluation datasets)
- JSON request/response format for ADK API server
- CLI commands, arguments, and flags
- Expected file structure for agent definitions

## Key Files and Directories

- `pyproject.toml` - Project configuration, dependencies, and build settings
- `README.md` - Main project documentation and usage examples
- `CONTRIBUTING.md` - Contribution guidelines and development setup
- `AGENTS.md` - Detailed development context for LLM assistance
- `src/google/adk/` - Main source code
- `tests/` - Unit and integration tests
- `contributing/` - Contribution resources
- `assets/` - Project images and assets

## Dependencies

The project has extensive dependencies for AI/ML development, including:
- Google GenAI SDK and AI Platform
- FastAPI for web interface
- Pydantic for data validation
- Various Google Cloud services
- Testing and development tools (pytest, mypy, etc.)
- Optional dependencies for special features (a2a, evaluation, etc.)

## Documentation

Full documentation is available at: https://google.github.io/adk-docs/
Key documentation topics include:
- Building single and multi-agent systems
- Using built-in and custom tools
- Evaluation capabilities
- Deployment options
- Development UI