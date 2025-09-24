# Data Model: LiteLLM Thinking Configuration Support

## Overview
This document defines the data entities needed to support thinking_config functionality in LiteLLM models within the ADK framework.

## Entities

### ThinkingConfig
- **Purpose**: Configuration object that controls whether thoughts are included in model responses
- **Fields**: 
  - include_thoughts: bool (default: False) - Whether to include AI thoughts in the response
  - thought_format: str (optional) - The format in which to return thoughts (e.g., 'raw', 'structured')
- **Validation**: The configuration should be validated to ensure valid thought_format values

### LiteLLMModel
- **Purpose**: Model class that wraps LiteLLM functionality with thinking_config support
- **Fields**:
  - model_name: str - The name of the underlying model (e.g., "openai/gpt-4", "anthropic/claude-3-opus")
  - api_key: str - API key for the provider
  - base_url: str (optional) - Base URL if using custom endpoint
  - thinking_config: ThinkingConfig (optional) - Configuration for thinking/thoughts
  - provider_specific_params: dict (optional) - Additional parameters specific to the provider
- **Methods**:
  - execute_with_thinking(input: str) -> ModelResponseWithThinking
  - validate_thinking_support() -> bool

### ModelResponseWithThinking
- **Purpose**: Response object that extends standard model response to include thinking/thoughts
- **Inherits from**: BaseModelResponse
- **Fields**:
  - response: str - The final response from the model
  - thinking: Optional[str] - The internal reasoning/thoughts of the model
  - raw_response: dict - The original response from the provider (for debugging)
  - provider: str - The provider that generated the response
- **Validation**: If thinking is present, it should be non-empty

### ThinkingExtractor
- **Purpose**: Utility class to extract thinking/thoughts from provider-specific response formats
- **Methods**:
  - extract_thinking(response: dict, provider: str) -> Optional[str]: Extracts thinking from provider response
  - normalize_thinking(thinking: str, provider: str) -> str: Normalizes thinking format across providers
- **Implementation note**: This class will have provider-specific extraction strategies

### ProviderThinkingCapabilities
- **Purpose**: Enum/Configuration that defines thinking/thoughts capabilities for different providers
- **Values**:
  - OPENAI: Supports thinking in function call or structured output format
  - ANTHROPIC: Supports thinking in messages API within <thinking> tags
  - GOOGLE: Supports thinking in function calling or structured output
  - OTHER: May or may not support thinking (fallback to no thinking)
- **Usage**: Used to determine how to process responses from different providers

## Relationships

- ThinkingConfig is associated with LiteLLMModel as an optional configuration parameter
- ModelResponseWithThinking is the output of LiteLLMModel execution when thinking_config is enabled
- ThinkingExtractor is used by LiteLLMModel to process provider-specific response formats
- ProviderThinkingCapabilities is referenced by ThinkingExtractor to determine extraction strategy

## State Transitions (if applicable)

- The thinking extraction process moves from: Raw Provider Response → Extracted Thinking → Normalized Thinking
- The model response goes through: Request Input → Provider Processing → Thinking Extraction → Final Response

## Validation Rules

1. If thinking_config is provided and include_thoughts is True, the response should attempt to include thinking data
2. If a provider doesn't support thinking, the response should return with no thinking field (not null) and no error
3. Thinking content should be properly formatted according to the provider's format