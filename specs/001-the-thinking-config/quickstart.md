# Quickstart: LiteLLM Thinking Configuration Support

## Overview
This document provides a quick guide to test the new thinking_config functionality with LiteLLM models in ADK.

## Prerequisites
- ADK framework installed (version >= 1.x.x)
- Appropriate API keys for the LiteLLM provider you want to test (OpenAI, Anthropic, etc.)
- Understanding of the basic ADK model usage

## Setup

### 1. Install ADK
```bash
pip install google-adk
```

### 2. Prepare API Keys
Set environment variables for your chosen provider:
```bash
# For OpenAI
export OPENAI_API_KEY=your_openai_api_key

# For Anthropic
export ANTHROPIC_API_KEY=your_anthropic_api_key

# For Google
export GEMINI_API_KEY=your_google_api_key
```

## Basic Usage

### Using thinking_config with LiteLLM

```python
from google.adk.models import LiteLLMModel
from google.adk.types import ThinkingConfig

# Configure a LiteLLM model with thinking_config
model = LiteLLMModel(
    model_name="openai/gpt-4",
    api_key=os.getenv("OPENAI_API_KEY"),
    thinking_config=ThinkingConfig(include_thoughts=True)
)

# Execute with thinking
result = model.execute_with_thinking("Explain how to solve a Rubik's cube")
print("Final answer:", result.response)
print("Thinking process:", result.thinking)
```

## Test Scenarios

### Test 1: OpenAI Model with Thinking
**Input**: Complex problem requiring reasoning
```python
model = LiteLLMModel(
    model_name="openai/gpt-4",
    api_key=os.getenv("OPENAI_API_KEY"),
    thinking_config=ThinkingConfig(include_thoughts=True)
)

result = model.execute_with_thinking("A farmer has 17 sheep, all but 9 die. How many are left?")
```
**Expected**: Result should contain both a response ("9 sheep are left") and thinking (the reasoning process)

### Test 2: Anthropic Model with Thinking
**Input**: Question requiring logical reasoning
```python
model = LiteLLMModel(
    model_name="anthropic/claude-3-opus",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    thinking_config=ThinkingConfig(include_thoughts=True)
)

result = model.execute_with_thinking("Calculate the sum of all numbers from 1 to 100")
```
**Expected**: Result should contain the answer (5050) and the thinking process showing how it was calculated

### Test 3: Provider without Thinking Support
**Input**: Using a provider that doesn't support thinking
```python
model = LiteLLMModel(
    model_name="provider/without-thinking-support",
    api_key=os.getenv("PROVIDER_API_KEY"),
    thinking_config=ThinkingConfig(include_thoughts=True)
)

result = model.execute_with_thinking("Simple question")
```
**Expected**: Result should contain the response but thinking should be None or empty, with no errors

### Test 4: Backward Compatibility
**Input**: Using LiteLLM without thinking_config (default behavior)
```python
model = LiteLLMModel(
    model_name="openai/gpt-4",
    api_key=os.getenv("OPENAI_API_KEY")
    # No thinking_config provided
)

result = model.execute("Simple question")
```
**Expected**: Result should behave exactly as before, without any thinking information

## Validation Steps

1. Run Test 1 and verify that thinking is included in the response
2. Run Test 2 and verify that thinking from Anthropic is properly handled
3. Run Test 3 and verify that no errors occur with providers that don't support thinking
4. Run Test 4 and verify that backward compatibility is maintained
5. Compare the results with the same prompts using plain Gemini models to ensure consistency in responses

## Troubleshooting

### Issue: Thinking not returned when expected
- Verify that the model provider actually supports thinking/thoughts functionality
- Check that API keys are valid and have the required permissions

### Issue: Error when using thinking_config
- Ensure all required dependencies are installed
- Verify that the model name is correctly formatted (e.g., "provider/model-name")

### Issue: Different thinking format across providers
- This is expected behavior; the implementation normalizes the thinking format as much as possible
- The content of the thinking may differ based on how each provider implements this functionality