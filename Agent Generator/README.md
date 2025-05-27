# n8n Workflow Generator Agent

An intelligent agent that generates n8n workflow JSON files from natural language descriptions using Claude and comprehensive documentation context.

## Overview

This project creates a specialized AI agent that can understand workflow requirements described in natural language and generate valid n8n workflow JSON files. The agent leverages:

- **Cursor Rules**: Defines the agent's role as an n8n workflow expert
- **Documentation Context**: Complete n8n documentation for accurate code generation
- **XML Prompt Engineering**: Structured prompts for precise workflow generation
- **Template System**: Pre-built patterns for common workflow types
- **Validation**: Ensures generated workflows are valid n8n JSON

## Features

- 🤖 **Natural Language to Workflow**: Describe what you want, get a working n8n workflow
- 📚 **Documentation-Aware**: Uses comprehensive n8n docs for accurate generation
- 🎯 **Template-Based**: Leverages proven patterns for reliable results
- ✅ **Validation**: Ensures generated JSON is valid for n8n import
- 🔧 **Extensible**: Easy to add new templates and patterns

## Project Structure

```
├── .cursorrules                 # Agent behavior and role definition
├── docs/                       # n8n documentation and references
├── templates/                  # Pre-built workflow templates
├── prompts/                    # XML prompt templates
├── examples/                   # Example workflows and use cases
├── validation/                 # JSON schema and validation tools
└── workflows/                  # Generated workflow outputs
```

## How It Works

1. **Input**: Natural language description of desired workflow
2. **Processing**: Agent uses docs, templates, and XML prompts
3. **Generation**: Creates valid n8n workflow JSON
4. **Validation**: Checks JSON structure and node compatibility
5. **Output**: Ready-to-import n8n workflow file

## Usage

1. Describe your workflow in natural language
2. The agent analyzes requirements against n8n capabilities
3. Generates structured XML prompt with context
4. Produces valid n8n workflow JSON
5. Import the JSON directly into n8n

## Quick Start

1. Open this project in Cursor
2. Use the `.cursorrules` to activate the agent
3. Describe your workflow needs
4. Get a working n8n JSON file
5. Import into n8n and test

## Example Workflows

- **Data Processing**: ETL pipelines, data transformation
- **API Integration**: Connect services, webhooks, automation
- **Notifications**: Email, Slack, Discord alerts
- **Monitoring**: Error handling, status checks
- **Reporting**: Generate and distribute reports

## Contributing

Add new templates, improve documentation, or enhance the prompt system by following the established patterns in this repository. 