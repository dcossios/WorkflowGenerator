# n8n Node Reference Guide

This document provides a comprehensive reference for n8n nodes, their parameters, and common configurations.

## Trigger Nodes

### Manual Trigger
- **Type**: `n8n-nodes-base.manualTrigger`
- **TypeVersion**: 1.1
- **Use Case**: Manual workflow execution for testing or one-off tasks
- **Parameters**: None required
- **Example**:
```json
{
  "parameters": {},
  "id": "manual-trigger",
  "name": "Manual Trigger",
  "type": "n8n-nodes-base.manualTrigger",
  "typeVersion": 1.1,
  "position": [240, 300]
}
```

### Webhook
- **Type**: `n8n-nodes-base.webhook`
- **TypeVersion**: 1.1
- **Use Case**: Receive HTTP requests from external systems
- **Key Parameters**:
  - `httpMethod`: GET, POST, PUT, DELETE, etc.
  - `path`: URL path for the webhook
  - `responseMode`: onReceived, onLastNode, responseNode
- **Example**:
```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook-endpoint",
    "responseMode": "onReceived",
    "options": {}
  },
  "id": "webhook-trigger",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 1.1,
  "position": [240, 300],
  "webhookId": "webhook-trigger"
}
```

### Schedule Trigger
- **Type**: `n8n-nodes-base.scheduleTrigger`
- **TypeVersion**: 1.1
- **Use Case**: Time-based workflow execution
- **Key Parameters**:
  - `rule.interval`: Array of timing rules
  - `cronExpression`: Cron format timing
- **Example**:
```json
{
  "parameters": {
    "rule": {
      "interval": [
        {
          "field": "cronExpression",
          "cronExpression": "0 9 * * 1-5"
        }
      ]
    }
  },
  "id": "schedule-trigger",
  "name": "Schedule Trigger",
  "type": "n8n-nodes-base.scheduleTrigger",
  "typeVersion": 1.1,
  "position": [240, 300]
}
```

### Chat Trigger
- **Type**: `n8n-nodes-base.chatTrigger`
- **TypeVersion**: 1.1
- **Use Case**: Interactive chat interfaces
- **Key Parameters**:
  - `public`: Boolean for public access
  - `options`: Additional configuration
- **Example**:
```json
{
  "parameters": {
    "public": true,
    "options": {}
  },
  "id": "chat-trigger",
  "name": "Chat Trigger",
  "type": "n8n-nodes-base.chatTrigger",
  "typeVersion": 1.1,
  "position": [240, 300]
}
```

## Data Processing Nodes

### Set (Data Transformation)
- **Type**: `n8n-nodes-base.set`
- **TypeVersion**: 3.2
- **Use Case**: Transform and structure data
- **Key Parameters**:
  - `assignments.assignments`: Array of field assignments
- **Example**:
```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "field1",
          "name": "newFieldName",
          "value": "={{ $json.originalField }}",
          "type": "string"
        }
      ]
    },
    "options": {}
  },
  "id": "set-node",
  "name": "Set",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3.2,
  "position": [460, 300]
}
```

### Code (JavaScript/Python)
- **Type**: `n8n-nodes-base.code`
- **TypeVersion**: 2
- **Use Case**: Custom logic implementation
- **Key Parameters**:
  - `jsCode`: JavaScript code
  - `pythonCode`: Python code (if supported)
- **Example**:
```json
{
  "parameters": {
    "jsCode": "const items = $input.all();\nconst results = [];\n\nfor (const item of items) {\n  results.push({\n    json: {\n      processed: true,\n      data: item.json\n    }\n  });\n}\n\nreturn results;"
  },
  "id": "code-node",
  "name": "Code",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [680, 300]
}
```

### IF (Conditional Logic)
- **Type**: `n8n-nodes-base.if`
- **TypeVersion**: 2
- **Use Case**: Conditional branching
- **Key Parameters**:
  - `conditions.conditions`: Array of conditions
  - `conditions.combinator`: "and" or "or"
- **Example**:
```json
{
  "parameters": {
    "conditions": {
      "options": {
        "caseSensitive": true,
        "leftValue": "",
        "typeValidation": "strict"
      },
      "conditions": [
        {
          "id": "condition1",
          "leftValue": "={{ $json.status }}",
          "rightValue": "active",
          "operator": {
            "type": "string",
            "operation": "equals"
          }
        }
      ],
      "combinator": "and"
    },
    "options": {}
  },
  "id": "if-node",
  "name": "IF",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2,
  "position": [900, 300]
}
```

### Switch (Multiple Conditions)
- **Type**: `n8n-nodes-base.switch`
- **TypeVersion**: 3
- **Use Case**: Multi-way branching
- **Key Parameters**:
  - `rules`: Array of condition rules
  - `fallbackOutput`: Default output
- **Example**:
```json
{
  "parameters": {
    "rules": {
      "rules": [
        {
          "conditions": {
            "conditions": [
              {
                "leftValue": "={{ $json.priority }}",
                "rightValue": "high",
                "operator": {
                  "type": "string",
                  "operation": "equals"
                }
              }
            ]
          },
          "output": 0
        },
        {
          "conditions": {
            "conditions": [
              {
                "leftValue": "={{ $json.priority }}",
                "rightValue": "medium",
                "operator": {
                  "type": "string",
                  "operation": "equals"
                }
              }
            ]
          },
          "output": 1
        }
      ]
    },
    "fallbackOutput": 2
  },
  "id": "switch-node",
  "name": "Switch",
  "type": "n8n-nodes-base.switch",
  "typeVersion": 3,
  "position": [900, 300]
}
```

## Integration Nodes

### HTTP Request
- **Type**: `n8n-nodes-base.httpRequest`
- **TypeVersion**: 4.1
- **Use Case**: API calls and web requests
- **Key Parameters**:
  - `method`: HTTP method
  - `url`: Target URL
  - `authentication`: Auth configuration
  - `sendHeaders`: Boolean for custom headers
  - `sendBody`: Boolean for request body
- **Example**:
```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/endpoint",
    "authentication": "genericCredentialType",
    "genericAuthType": "httpHeaderAuth",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {
          "name": "Content-Type",
          "value": "application/json"
        }
      ]
    },
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={{ $json }}",
    "options": {}
  },
  "id": "http-request",
  "name": "HTTP Request",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4.1,
  "position": [680, 300]
}
```

### Gmail
- **Type**: `n8n-nodes-base.gmail`
- **TypeVersion**: 2.1
- **Use Case**: Send emails via Gmail
- **Key Parameters**:
  - `operation`: send, reply, etc.
  - `fromEmail`: Sender email
  - `toEmail`: Recipient email
  - `subject`: Email subject
  - `message`: Email content
- **Example**:
```json
{
  "parameters": {
    "operation": "send",
    "fromEmail": "sender@company.com",
    "toEmail": "recipient@company.com",
    "subject": "Automated Notification",
    "message": "This is an automated message from n8n workflow.",
    "options": {}
  },
  "id": "gmail-node",
  "name": "Gmail",
  "type": "n8n-nodes-base.gmail",
  "typeVersion": 2.1,
  "position": [1120, 300]
}
```

### Slack
- **Type**: `n8n-nodes-base.slack`
- **TypeVersion**: 2.1
- **Use Case**: Send Slack messages
- **Key Parameters**:
  - `operation`: postMessage, etc.
  - `select`: channel, user
  - `channelId`: Target channel
  - `text` or `content`: Message content
- **Example**:
```json
{
  "parameters": {
    "operation": "postMessage",
    "select": "channel",
    "channelId": {
      "__rl": true,
      "value": "general",
      "mode": "name"
    },
    "content": "Workflow notification: {{ $json.message }}",
    "otherOptions": {}
  },
  "id": "slack-node",
  "name": "Slack",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2.1,
  "position": [1120, 300]
}
```

### Google Sheets
- **Type**: `n8n-nodes-base.googleSheets`
- **TypeVersion**: 4.2
- **Use Case**: Read/write Google Sheets data
- **Key Parameters**:
  - `operation`: append, read, update, etc.
  - `documentId`: Spreadsheet ID
  - `sheetName`: Sheet name
  - `columns`: Column mapping
- **Example**:
```json
{
  "parameters": {
    "operation": "appendOrUpdate",
    "documentId": {
      "__rl": true,
      "value": "SPREADSHEET_ID",
      "mode": "id"
    },
    "sheetName": {
      "__rl": true,
      "value": "Sheet1",
      "mode": "name"
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": {
        "name": "={{ $json.name }}",
        "email": "={{ $json.email }}",
        "status": "={{ $json.status }}"
      }
    },
    "options": {}
  },
  "id": "sheets-node",
  "name": "Google Sheets",
  "type": "n8n-nodes-base.googleSheets",
  "typeVersion": 4.2,
  "position": [1340, 300]
}
```

## AI & Language Model Nodes

### AI Agent
- **Type**: `@n8n/n8n-nodes-langchain.agent`
- **TypeVersion**: 0.1
- **Use Case**: Intelligent task automation
- **Key Parameters**:
  - `agent`: Agent type
  - `text`: Input text
  - `options.systemMessage`: System prompt
- **Example**:
```json
{
  "parameters": {
    "agent": "conversationalAgent",
    "text": "={{ $json.userInput }}",
    "hasOutputParser": true,
    "options": {
      "systemMessage": "You are a helpful assistant that processes user requests."
    }
  },
  "id": "ai-agent",
  "name": "AI Agent",
  "type": "@n8n/n8n-nodes-langchain.agent",
  "typeVersion": 0.1,
  "position": [900, 300]
}
```

### OpenAI Chat Model
- **Type**: `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- **TypeVersion**: 1
- **Use Case**: Language model for AI agents
- **Key Parameters**:
  - `model`: Model name (gpt-4o-mini, gpt-4, etc.)
  - `options.temperature`: Creativity level
  - `options.maxTokens`: Response length limit
- **Example**:
```json
{
  "parameters": {
    "model": "gpt-4o-mini",
    "options": {
      "temperature": 0.7,
      "maxTokens": 1000
    }
  },
  "id": "openai-model",
  "name": "OpenAI Chat Model",
  "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
  "typeVersion": 1,
  "position": [900, 180]
}
```

## Common n8n Expressions

### Data Access
- **Current item**: `{{ $json.fieldName }}`
- **Previous node**: `{{ $('Node Name').item.json.field }}`
- **All items**: `{{ $('Node Name').all() }}`
- **Item by index**: `{{ $('Node Name').item(0).json.field }}`

### Date/Time
- **Current timestamp**: `{{ new Date().toISOString() }}`
- **Format date**: `{{ new Date().toLocaleDateString() }}`
- **Add days**: `{{ new Date(Date.now() + 24*60*60*1000).toISOString() }}`

### Conditional Logic
- **Ternary operator**: `{{ $json.value > 100 ? 'high' : 'low' }}`
- **Null check**: `{{ $json.field || 'default' }}`
- **Type check**: `{{ typeof $json.field === 'string' }}`

### String Operations
- **Concatenation**: `{{ $json.firstName + ' ' + $json.lastName }}`
- **Uppercase**: `{{ $json.text.toUpperCase() }}`
- **Substring**: `{{ $json.text.substring(0, 10) }}`

### Array Operations
- **Length**: `{{ $json.items.length }}`
- **Join**: `{{ $json.array.join(', ') }}`
- **Filter**: `{{ $json.items.filter(item => item.active) }}`

## Node Connection Patterns

### Basic Linear Flow
```
Trigger → Process → Transform → Output
```

### Conditional Branching
```
Trigger → Process → IF → [Success Path]
                      └→ [Error Path]
```

### Parallel Processing
```
Trigger → Process → [Branch A]
                 └→ [Branch B]
                 └→ [Branch C]
```

### AI Integration
```
Chat Trigger → Extract Context → AI Agent ← Language Model
                                      ↓
                              Format Response
```

## Best Practices

1. **Node Naming**: Use descriptive names that explain the node's purpose
2. **Error Handling**: Include IF nodes to check for errors and provide fallback paths
3. **Data Validation**: Validate inputs before processing
4. **Positioning**: Arrange nodes left-to-right in execution order
5. **Expressions**: Use proper n8n expression syntax with {{ }}
6. **Authentication**: Configure proper credentials for external services
7. **Testing**: Use manual triggers for testing before automation 