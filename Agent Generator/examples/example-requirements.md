# Example Workflow Requirements

This document contains example workflow descriptions that can be used to test the n8n workflow generator agent.

## 1. Simple Data Processing Pipeline

**Requirement**: "I need a workflow that runs every morning at 9 AM, fetches sales data from our REST API endpoint, processes the data to calculate daily totals, and sends a summary email to the management team."

**Expected Components**:
- Schedule Trigger (daily at 9 AM)
- HTTP Request to fetch data
- Code node for data processing
- Email notification
- Error handling

## 2. Customer Support Webhook

**Requirement**: "Create a workflow that receives customer support tickets via webhook, categorizes them based on priority (high, medium, low) using keywords, and automatically creates tickets in our project management tool while sending notifications to the appropriate teams."

**Expected Components**:
- Webhook trigger
- Data extraction and validation
- IF/Switch nodes for categorization
- API calls to project management tool
- Conditional notifications (Slack/email)
- Error handling

## 3. AI-Powered Content Moderation

**Requirement**: "I want an automated content moderation system that receives user submissions via webhook, uses AI to analyze the content for inappropriate material, flags suspicious content for manual review, and automatically approves safe content while logging all decisions."

**Expected Components**:
- Webhook trigger
- AI content analysis
- Decision logic (IF nodes)
- Database logging
- Notification system
- Audit trail

## 4. Social Media Monitoring

**Requirement**: "Build a workflow that monitors social media mentions of our brand every hour, analyzes sentiment using AI, stores the results in a Google Sheet, and sends alerts to the marketing team when negative sentiment is detected."

**Expected Components**:
- Schedule trigger (hourly)
- Social media API integration
- AI sentiment analysis
- Google Sheets integration
- Conditional alerting
- Data aggregation

## 5. E-commerce Order Processing

**Requirement**: "Create an order processing workflow that triggers when a new order is received via webhook, validates inventory levels, calculates shipping costs, sends confirmation emails to customers, updates inventory systems, and creates shipping labels."

**Expected Components**:
- Webhook trigger
- Multiple API integrations
- Data validation
- Email notifications
- Error handling and rollback
- External service integrations

## 6. Document Processing Pipeline

**Requirement**: "I need a workflow that processes uploaded documents: extracts text using OCR, categorizes documents using AI, stores metadata in a database, and moves files to appropriate folders based on category."

**Expected Components**:
- File upload trigger
- OCR processing
- AI categorization
- Database operations
- File management
- Status tracking

## 7. Meeting Scheduler Assistant

**Requirement**: "Build an AI assistant that helps schedule meetings by receiving requests via chat, checking calendar availability, suggesting optimal times, sending calendar invites, and confirming with all participants."

**Expected Components**:
- Chat trigger
- AI agent for conversation
- Calendar API integration
- Email/notification system
- Context management
- Confirmation workflows

## 8. Data Quality Monitoring

**Requirement**: "Create a data quality monitoring system that runs daily, checks various data sources for inconsistencies, generates quality reports, identifies anomalies using statistical analysis, and alerts data engineers when issues are found."

**Expected Components**:
- Schedule trigger
- Multiple data source connections
- Data analysis code
- Quality checks and validations
- Report generation
- Alert system

## 9. Customer Onboarding Automation

**Requirement**: "Automate customer onboarding by triggering when a new user signs up, sending welcome emails, creating accounts in various systems, setting up initial configurations, and scheduling follow-up communications."

**Expected Components**:
- Webhook/email trigger
- Multi-step sequence
- User account creation
- Email sequences
- System integrations
- Follow-up scheduling

## 10. IoT Data Processing

**Requirement**: "Process IoT sensor data by receiving telemetry via webhook, validating data ranges, storing time-series data, detecting anomalies using thresholds, and triggering maintenance alerts when sensors report critical values."

**Expected Components**:
- Webhook trigger
- Data validation
- Time-series processing
- Threshold monitoring
- Alert system
- Data storage

## Testing Instructions

To test the workflow generator with these examples:

1. Choose an example requirement
2. Provide the requirement text to the agent
3. Verify the generated workflow includes all expected components
4. Check that the JSON is valid and can be imported into n8n
5. Validate that the workflow logic matches the requirements

## Customization Guidelines

When creating custom requirements:

- Be specific about trigger conditions
- Define clear business logic
- Specify required integrations
- Include error handling needs
- Mention any compliance requirements
- Describe expected outputs and notifications 