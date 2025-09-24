#!/usr/bin/env python3
"""
Simple example demonstrating LiteLLM thinking_config support.

Usage:
    python thinking_example.py
"""

import os
import asyncio

# Example of how to use thinking_config with LiteLLM
async def main():
    """Main function demonstrating the feature."""
    
    try:
        from google.genai import types
        from google.adk.models.lite_llm import LiteLlm
        from google.adk.models.llm_request import LlmRequest
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure you have the required dependencies installed.")
        return
    
    print("=== LiteLLM Thinking Config Example ===")
    
    # Example 1: Using Gemini via LiteLLM with thinking (low effort)
    print("\n1. Gemini via LiteLLM with thinking_config (low effort):")
    model = LiteLlm(model="gemini/gemini-2.0-flash-thinking-exp")
    
    request_low = LlmRequest(
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text("What is 15 × 23? Think step by step.")]
            )
        ],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                include_thoughts=True,
                thinking_budget="low"  # 轻量级推理
            )
        )
    )
    
    try:
        async for response in model.generate_content_async(request_low, stream=False):
            if response.content and response.content.parts:
                for part in response.content.parts:
                    if part.text:
                        print(f"Response: {part.text}")
            break
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using Anthropic with high effort thinking
    print("\n2. Anthropic with thinking_config (high effort):")
    model2 = LiteLlm(model="anthropic/claude-3-7-sonnet-20250219")
    
    request_high = LlmRequest(
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text("解释量子计算的基本原理，要详细思考。")]
            )
        ],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                include_thoughts=True,
                thinking_budget="high"  # 高强度推理
            )
        )
    )
    
    try:
        async for response in model2.generate_content_async(request_high, stream=False):
            if response.content and response.content.parts:
                for part in response.content.parts:
                    if part.text:
                        print(f"Response: {part.text}")
            break
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Using medium effort thinking with token budget
    print("\n3. Medium effort thinking with token budget:")
    request_medium = LlmRequest(
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_text("分析一下股市投资的风险和机会。")]
            )
        ],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                include_thoughts=True,
                thinking_budget=2000  # 数值映射到 medium
            )
        )
    )
    
    try:
        async for response in model.generate_content_async(request_medium, stream=False):
            if response.content and response.content.parts:
                for part in response.content.parts:
                    if part.text:
                        print(f"Response: {part.text}")
            break
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Without thinking config (baseline)
    print("\n4. Without thinking_config (baseline):")


if __name__ == "__main__":
    asyncio.run(main())