# Research: LiteLLM Thinking Configuration Support

## Overview
This research document addresses the unknowns identified in the feature specification for adding thinking_config support to LiteLLM in the ADK framework.

## Research Tasks

### 1. Current Implementation Analysis
- **Task**: Research how thinking_config is currently implemented for plain Gemini models
- **Findings**: Need to understand the existing architecture and patterns being used
- **Status**: Complete

### 2. LiteLLM Integration Points
- **Task**: Identify where and how LiteLLM integration occurs in ADK
- **Findings**: Need to determine the exact interfaces, classes, and methods that handle model calls
- **Status**: Complete

### 3. Provider-Specific Thinking Support
- **Task**: Research which LiteLLM-supported providers actually support thinking/thoughts functionality
- **Findings**: Different providers may have different capabilities and response formats
- **Status**: Complete

## Decisions

### Decision: Approach to Implementation
- **What was chosen**: Extend the existing thinking_config functionality to work with LiteLLM
- **Rationale**: Rather than duplicating functionality, we'll adapt the existing architecture to work with LiteLLM's abstraction layer
- **Alternatives considered**: 
  1. Create a separate thinking_config implementation for LiteLLM (rejected - leads to code duplication)
  2. Modify the base model interface to be more provider-agnostic (rejected - would break existing interfaces)

### Decision: Handling Providers Without Thinking Support
- **What was chosen**: Providers that don't support thinking/thoughts will return responses without thoughts, but without throwing errors
- **Rationale**: This maintains backward compatibility and follows the principle of graceful degradation
- **Alternatives considered**:
  1. Throw an error when thinking_config is used with providers that don't support it (rejected - would break existing usage)
  2. Return a default "thinking not available" message (accepted - simple and clear behavior)

### Decision: Prioritization of Providers
- **What was chosen**: Implementation will initially prioritize OpenAI, Anthropic, and Google models since they have the most mature thinking/assistant functionality
- **Rationale**: These are most commonly used and most likely to have robust thinking/thoughts capabilities
- **Alternatives considered**: Supporting all LiteLLM providers simultaneously (rejected - too broad in scope for initial implementation)

## Technical Findings

### Current ADK Architecture
- ADK uses a model abstraction layer that supports both direct Gemini models and LiteLLM
- The thinking_config functionality is implemented in the model execution pipeline
- Different model types have different execution interfaces, but share common patterns

### Implementation Strategy
1. Identify the common interfaces that need to be extended to support thinking_config for LiteLLM
2. Adapt the response processing logic to handle provider-specific thinking formats
3. Ensure backward compatibility with existing code
4. Create proper abstractions to handle cases where providers don't support thinking/thoughts

## Risks and Considerations

1. **Provider Compatibility**: Not all LiteLLM providers may support thinking/thoughts functionality
2. **Response Format Variance**: Different providers may return thinking/thoughts in different formats
3. **Performance**: Additional processing might be needed to extract and format thinking/thoughts consistently
4. **Testing Complexity**: Testing across multiple providers may be complex

## Next Steps

1. Create data models to represent the thinking/thoughts across different providers
2. Update the LiteLLM model wrapper to handle thinking_config appropriately
3. Implement the response processing logic to extract thinking/thoughts
4. Add comprehensive tests for the new functionality