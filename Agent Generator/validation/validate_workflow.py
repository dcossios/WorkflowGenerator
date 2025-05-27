#!/usr/bin/env python3
"""
n8n Workflow Validator

This script validates n8n workflow JSON files against the schema
and performs additional logical checks.
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import jsonschema
from jsonschema import validate, ValidationError

class N8nWorkflowValidator:
    def __init__(self, schema_path: str = "validation/n8n-workflow-schema.json"):
        """Initialize the validator with the JSON schema."""
        self.schema_path = Path(schema_path)
        self.schema = self._load_schema()
        
    def _load_schema(self) -> Dict[str, Any]:
        """Load the JSON schema from file."""
        try:
            with open(self.schema_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in schema file: {e}")
    
    def validate_workflow(self, workflow_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate a workflow against the schema and perform logical checks.
        
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Schema validation
        try:
            validate(instance=workflow_data, schema=self.schema)
        except ValidationError as e:
            errors.append(f"Schema validation error: {e.message}")
        
        # Additional logical validations
        errors.extend(self._validate_connections(workflow_data))
        errors.extend(self._validate_trigger_nodes(workflow_data))
        errors.extend(self._validate_node_positions(workflow_data))
        errors.extend(self._validate_expressions(workflow_data))
        
        return len(errors) == 0, errors
    
    def _validate_connections(self, workflow: Dict[str, Any]) -> List[str]:
        """Validate that all connections reference existing nodes."""
        errors = []
        
        # Get all node names
        node_names = {node['name'] for node in workflow.get('nodes', [])}
        
        # Check connections
        connections = workflow.get('connections', {})
        for source_node, connection_types in connections.items():
            if source_node not in node_names:
                errors.append(f"Connection source node '{source_node}' does not exist")
                continue
            
            for connection_type, connection_arrays in connection_types.items():
                for connection_array in connection_arrays:
                    for connection in connection_array:
                        target_node = connection.get('node')
                        if target_node and target_node not in node_names:
                            errors.append(
                                f"Connection target node '{target_node}' does not exist "
                                f"(referenced from '{source_node}')"
                            )
        
        return errors
    
    def _validate_trigger_nodes(self, workflow: Dict[str, Any]) -> List[str]:
        """Validate trigger node requirements."""
        errors = []
        
        trigger_types = {
            'n8n-nodes-base.manualTrigger',
            'n8n-nodes-base.webhook',
            'n8n-nodes-base.scheduleTrigger',
            'n8n-nodes-base.chatTrigger',
            'n8n-nodes-base.emailTrigger'
        }
        
        nodes = workflow.get('nodes', [])
        trigger_nodes = [node for node in nodes if node.get('type') in trigger_types]
        
        if not trigger_nodes:
            errors.append("Workflow must have at least one trigger node")
        
        # Check for multiple manual triggers (usually not recommended)
        manual_triggers = [
            node for node in trigger_nodes 
            if node.get('type') == 'n8n-nodes-base.manualTrigger'
        ]
        if len(manual_triggers) > 1:
            errors.append("Multiple manual trigger nodes found - consider using only one")
        
        return errors
    
    def _validate_node_positions(self, workflow: Dict[str, Any]) -> List[str]:
        """Validate node positioning for good visual layout."""
        errors = []
        
        nodes = workflow.get('nodes', [])
        positions = []
        
        for node in nodes:
            position = node.get('position', [])
            if len(position) != 2:
                errors.append(f"Node '{node.get('name')}' has invalid position format")
                continue
            
            x, y = position
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                errors.append(f"Node '{node.get('name')}' has non-numeric position values")
                continue
            
            positions.append((x, y, node.get('name')))
        
        # Check for overlapping nodes
        for i, (x1, y1, name1) in enumerate(positions):
            for x2, y2, name2 in positions[i+1:]:
                if abs(x1 - x2) < 50 and abs(y1 - y2) < 50:
                    errors.append(f"Nodes '{name1}' and '{name2}' may be too close together")
        
        return errors
    
    def _validate_expressions(self, workflow: Dict[str, Any]) -> List[str]:
        """Validate n8n expressions in node parameters."""
        errors = []
        
        def check_expressions_recursive(obj: Any, path: str = ""):
            """Recursively check for expression syntax."""
            if isinstance(obj, str):
                if '={{' in obj and '}}' in obj:
                    # Basic expression syntax check
                    expression_count = obj.count('={{')
                    closing_count = obj.count('}}')
                    if expression_count != closing_count:
                        errors.append(f"Malformed expression at {path}: {obj}")
            elif isinstance(obj, dict):
                for key, value in obj.items():
                    check_expressions_recursive(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    check_expressions_recursive(item, f"{path}[{i}]")
        
        nodes = workflow.get('nodes', [])
        for node in nodes:
            node_name = node.get('name', 'Unknown')
            parameters = node.get('parameters', {})
            check_expressions_recursive(parameters, f"Node '{node_name}' parameters")
        
        return errors
    
    def validate_file(self, file_path: str) -> Tuple[bool, List[str]]:
        """Validate a workflow file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            return self.validate_workflow(workflow_data)
        except FileNotFoundError:
            return False, [f"File not found: {file_path}"]
        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON in file: {e}"]
        except Exception as e:
            return False, [f"Unexpected error: {e}"]

def main():
    """Command line interface for the validator."""
    if len(sys.argv) != 2:
        print("Usage: python validate_workflow.py <workflow_file.json>")
        sys.exit(1)
    
    workflow_file = sys.argv[1]
    
    try:
        validator = N8nWorkflowValidator()
        is_valid, errors = validator.validate_file(workflow_file)
        
        if is_valid:
            print(f"✅ Workflow '{workflow_file}' is valid!")
            sys.exit(0)
        else:
            print(f"❌ Workflow '{workflow_file}' has validation errors:")
            for error in errors:
                print(f"  • {error}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 