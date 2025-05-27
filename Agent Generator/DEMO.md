# n8n Workflow Generator Agent - Live Demo

This demonstration shows the complete process of generating an n8n workflow using the agent.

## Demo Scenario

**Business Requirement**: 
"I need a customer feedback workflow that triggers when feedback is submitted via a webhook, analyzes the sentiment using AI, stores positive feedback in Google Sheets, sends negative feedback alerts to Slack, and emails a thank you message to the customer."

## Step 1: Agent Analysis

The agent would analyze this requirement and identify:

### Trigger
- **Type**: Webhook (for receiving feedback submissions)
- **Configuration**: POST endpoint to receive feedback data

### Data Processing
- **Sentiment Analysis**: AI node to analyze feedback sentiment
- **Data Extraction**: Extract customer info and feedback text
- **Conditional Logic**: Route based on sentiment (positive vs negative)

### Integrations
- **Google Sheets**: Store positive feedback
- **Slack**: Alert for negative feedback  
- **Email**: Thank you messages to customers

### Error Handling
- **Validation**: Check required fields
- **Fallback**: Handle API failures gracefully

## Step 2: Generated Workflow Architecture

```
Webhook Trigger → Extract Data → AI Sentiment Analysis
                                         ↓
                                    IF (Sentiment)
                                    ↙         ↘
                            [Positive]    [Negative]
                                 ↓           ↓
                          Google Sheets   Slack Alert
                                 ↓           ↓
                           Email Thanks  Email Thanks
```

## Step 3: Generated n8n JSON

Here's what the agent would generate (example structure):

```json
{
  "name": "Customer Feedback Processing Workflow",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "customer-feedback",
        "responseMode": "onReceived"
      },
      "id": "feedback-webhook",
      "name": "Feedback Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "extract-customer",
              "name": "customerEmail",
              "value": "={{ $json.email }}",
              "type": "string"
            },
            {
              "id": "extract-feedback", 
              "name": "feedbackText",
              "value": "={{ $json.feedback }}",
              "type": "string"
            }
          ]
        }
      },
      "id": "extract-data",
      "name": "Extract Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [460, 300]
    },
    {
      "parameters": {
        "agent": "conversationalAgent",
        "text": "={{ $json.feedbackText }}",
        "options": {
          "systemMessage": "Analyze the sentiment of this customer feedback. Respond with only 'positive', 'negative', or 'neutral'."
        }
      },
      "id": "sentiment-analysis",
      "name": "AI Sentiment Analysis", 
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 0.1,
      "position": [680, 300]
    }
  ],
  "connections": {
    "Feedback Webhook": {
      "main": [[{"node": "Extract Data", "type": "main", "index": 0}]]
    },
    "Extract Data": {
      "main": [[{"node": "AI Sentiment Analysis", "type": "main", "index": 0}]]
    }
  }
}
```

## Step 4: Setup Instructions

The agent would provide these setup steps:

### 1. Import Workflow
1. Copy the generated JSON
2. Open n8n
3. Go to Workflows → Import from URL/Text
4. Paste JSON and save

### 2. Configure Credentials
- **OpenAI**: For sentiment analysis
- **Google Sheets**: For storing positive feedback
- **Slack**: For negative feedback alerts
- **Gmail/SMTP**: For thank you emails

### 3. Test Configuration
1. Use the webhook URL from n8n
2. Send test feedback via POST request
3. Verify sentiment analysis works
4. Check data flows to correct destinations

### 4. Deployment
1. Activate the workflow
2. Share webhook URL with your feedback system
3. Monitor execution logs
4. Set up error notifications

## Step 5: Validation

Using our validation script:

```bash
python validation/validate_workflow.py workflows/customer-feedback.json
```

Expected output:
```
✅ Workflow 'customer-feedback.json' is valid!
```

## Real-World Usage

To use this system:

1. **Describe your workflow** in natural language
2. **Specify all requirements** clearly
3. **Review the generated JSON** for completeness
4. **Import into n8n** and configure credentials
5. **Test thoroughly** before production use

## Benefits Demonstrated

- **Speed**: Generate complex workflows in minutes
- **Accuracy**: Follows n8n best practices automatically
- **Completeness**: Includes error handling and validation
- **Maintainability**: Well-structured and documented code
- **Flexibility**: Easy to modify and extend

## Next Steps

After seeing this demo:

1. Try the system with your own requirements
2. Start with simple workflows and build complexity
3. Use the templates as starting points
4. Validate all generated workflows
5. Share successful patterns with the team

This demonstration shows how the n8n workflow generator agent transforms business requirements into functional automation workflows quickly and reliably. 