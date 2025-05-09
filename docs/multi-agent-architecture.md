# Multi-agent architecture

## Overview

The system implements a hierarchical multi-agent architecture specialized in Laravel application development. The architecture consists of a supervisor agent that coordinates and oversees the work of specialized sub-agents.

## Agent Structure

### Supervisor Agent

The supervisor agent is the top-level coordinator that oversees the entire team's operations. It is implemented using the `LlmAgent` class with the following characteristics:

- Model: gemini-2.0-flash
- Role: Oversees team operations and ensures efficient delivery
- Primary responsibilities:
  - Ensuring team efficiency and effectiveness
  - Verifying adherence to instructions
  - Managing product delivery to clients

### Sub-Agents

The supervisor coordinates with three specialized sub-agents:

1. **Product Owner Agent**

   - Responsible for providing Product Requirements Document (PRD)
   - Handles product-level decisions and requirements

2. **Software Architect Agent**

   - Responsible for providing Technical Design Document (TDD)
   - Handles system architecture and technical decisions

3. **Software Engineer Agent**
   - Handles all codebase-related questions and implementation
   - Responsible for actual code development

## Workflow

The supervisor follows a structured workflow to deliver products:

1. Consults with the Product Owner to obtain the PRD
2. Consults with the Software Architect to obtain the TDD
3. Delegates codebase-related questions to the Software Engineer

## Implementation Details

The architecture is implemented using the Google ADK framework, with each agent being an instance of `LlmAgent`. The supervisor agent maintains direct communication channels with all sub-agents and can delegate tasks based on their expertise.
