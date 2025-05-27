# n8n Workflow Generator Agent - Usage Guide

This guide explains how to effectively use the n8n workflow generator agent to create functional workflows from natural language descriptions.

## Quick Start

### 1. Setup
1. Open this project in Cursor
2. Ensure you have the `.cursorrules` file active
3. Optionally install Python dependencies: `pip install -r requirements.txt`

### 2. Basic Usage
Simply describe your workflow needs in natural language:

> "I need a workflow that triggers every weekday at 9 AM, fetches data from our sales API, calculates daily totals, and emails a summary to the management team."

The agent will analyze your requirements and generate a complete n8n workflow JSON.

## How It Works

### Agent Process
1. **Requirement Analysis**: Breaks down your description into components
2. **Architecture Design**: Plans the workflow structure and data flow
3. **Node Selection**: Chooses appropriate n8n nodes
4. **JSON Generation**: Creates valid n8n workflow JSON
5. **Validation**: Ensures the workflow meets n8n standards

### Context Sources
The agent leverages:
- **n8n Documentation**: Comprehensive node reference
- **Templates**: Pre-built workflow patterns
- **Best Practices**: Proven workflow design patterns
- **Validation Rules**: Ensures JSON compatibility

## Writing Effective Prompts

### Be Specific About Triggers
❌ **Vague**: "I want automation"
✅ **Clear**: "I need a webhook that triggers when customers submit forms"

❌ **Vague**: "Run periodically"
✅ **Clear**: "Run every Monday at 9 AM"

### Define Data Flow Clearly
❌ **Vague**: "Process some data"
✅ **Clear**: "Fetch sales data from REST API, calculate totals by region, filter for amounts > $1000"

### Specify Integrations
❌ **Vague**: "Send notifications"
✅ **Clear**: "Send Slack messages to #alerts channel and email notifications to team@company.com"

### Include Business Logic
❌ **Vague**: "Handle different cases"
✅ **Clear**: "If order value > $500, send to priority queue; otherwise, standard processing"

## Example Workflows

### 1. Simple Automation
**Prompt**: "Create a daily report workflow that runs at 8 AM, fetches yesterday's orders from our API, counts them, and emails the total to admin@company.com"

**Generated Components**:
- Schedule Trigger (8 AM daily)
- HTTP Request to fetch orders
- Code node to count and process
- Gmail node for email notification

### 2. Conditional Processing
**Prompt**: "Build a customer support workflow that receives tickets via webhook, categorizes them as urgent/normal based on keywords, sends urgent tickets to Slack immediately, and creates all tickets in our project management system"

**Generated Components**:
- Webhook trigger
- Data extraction and validation
- IF/Switch nodes for categorization
- Conditional Slack notifications
- API integration for ticket creation

### 3. AI-Powered Workflow
**Prompt**: "Create an AI content moderator that receives posts via webhook, analyzes content for inappropriate material using AI, automatically approves safe content, flags suspicious content for review, and logs all decisions"

**Generated Components**:
- Webhook trigger
- AI agent for content analysis
- Decision logic with IF nodes
- Multiple output paths
- Logging and audit trail

## Working with Generated Workflows

### 1. Review the Output
The agent provides:
- **Workflow Overview**: High-level description
- **Architecture Summary**: Design explanation
- **Node Breakdown**: Each node's purpose
- **Setup Requirements**: External services needed
- **Complete JSON**: Ready-to-import workflow
- **Import Instructions**: Step-by-step guide

### 2. Import into n8n
1. Copy the generated JSON
2. Open n8n
3. Go to Workflows → Import from URL/Text
4. Paste the JSON
5. Review and save

### 3. Configure Credentials
Set up required credentials for:
- API integrations (HTTP Request nodes)
- Email services (Gmail, SMTP)
- Communication tools (Slack, Discord)
- Cloud services (Google Sheets, Airtable)

### 4. Test the Workflow
1. Use Manual Trigger for initial testing
2. Check data flow between nodes
3. Verify expressions work correctly
4. Test error handling paths
5. Activate when ready

## Customization Tips

### Modifying Generated Workflows
- **Node Parameters**: Adjust URLs, credentials, timing
- **Expressions**: Customize data transformations
- **Error Handling**: Add or modify error paths
- **Positioning**: Rearrange nodes for clarity

### Adding Features
- **Monitoring**: Add logging and status checks
- **Scalability**: Include batch processing
- **Security**: Add validation and sanitization
- **Reporting**: Include analytics and metrics

## Validation and Quality Assurance

### Automatic Validation
The system includes:
- JSON schema validation
- Node connection verification
- Expression syntax checking
- Best practices compliance

### Manual Validation
Use the validation script:
```bash
python validation/validate_workflow.py workflows/generated-workflow.json
```

### Common Issues
- **Missing Credentials**: Ensure all integrations are configured
- **Invalid Expressions**: Check n8n expression syntax
- **Node Connections**: Verify all connections are properly mapped
- **Trigger Configuration**: Ensure triggers are properly set up

## Advanced Features

### Template Customization
Leverage existing templates in `templates/`:
- **Basic Webhook**: Simple webhook-to-API integration
- **Scheduled Processing**: Time-based data processing
- **AI Chat Agent**: Conversational AI workflows

### Prompt Engineering
Use the XML prompt template in `prompts/` for:
- Consistent output format
- Comprehensive context inclusion
- Quality validation checks

### Extension Patterns
Common workflow extensions:
- **Error Monitoring**: Add error tracking workflows
- **Data Backup**: Include backup and recovery
- **Performance Monitoring**: Add execution time tracking
- **Audit Logging**: Include comprehensive logging

## Troubleshooting

### Common Problems

**Problem**: "Generated workflow doesn't import"
**Solution**: Check JSON syntax and schema compliance

**Problem**: "Nodes are missing parameters"
**Solution**: Review node documentation and add required fields

**Problem**: "Expressions are not working"
**Solution**: Verify n8n expression syntax and data paths

**Problem**: "Workflow executes but fails"
**Solution**: Check credentials, URLs, and API endpoints

### Getting Help
1. Check the node reference in `docs/`
2. Review example workflows in `examples/`
3. Validate using the validation script
4. Consult n8n documentation for specific nodes

## Best Practices

### Workflow Design
- Start with simple, linear flows
- Add complexity gradually
- Include error handling from the beginning
- Use descriptive node names
- Comment complex logic

### Maintenance
- Version control your workflows
- Document external dependencies
- Test regularly with real data
- Monitor execution performance
- Keep credentials secure

### Performance
- Minimize API calls where possible
- Use batching for large datasets
- Implement proper error handling
- Consider execution time limits
- Monitor resource usage

## Contributing

To improve the system:
1. Add new templates to `templates/`
2. Enhance documentation in `docs/`
3. Improve validation in `validation/`
4. Share example requirements in `examples/`
5. Refine the prompt template in `prompts/`

## Support

For issues or questions:
1. Check this usage guide
2. Review the documentation
3. Validate your workflow JSON
4. Test with simple examples first
5. Gradually add complexity

The n8n workflow generator agent is designed to make automation accessible and efficient. Start with simple workflows and gradually build more complex automation as you become familiar with the system. 