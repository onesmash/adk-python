# Tasks: LiteLLM Thinking Configuration Support

**Input**: Design documents from `/specs/001-the-thinking-config/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 3.1: Setup
- [ ] T001 Create ThinkingConfig model in src/google/adk/types/thinking_config.py
- [ ] T002 Create ModelResponseWithThinking model in src/google/adk/types/model_response_with_thinking.py

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T003 [P] Contract test for POST /api/litellm/thinking in tests/contract/test_litellm_thinking_contract.py
- [ ] T004 [P] Unit test for ThinkingConfig in tests/unit/test_thinking_config.py
- [ ] T005 [P] Unit test for ModelResponseWithThinking in tests/unit/test_model_response_with_thinking.py
- [ ] T006 [P] Integration test for OpenAI model with thinking in tests/integration/test_litellm_openai_thinking.py
- [ ] T007 [P] Integration test for Anthropic model with thinking in tests/integration/test_litellm_anthropic_thinking.py
- [ ] T008 [P] Integration test for provider without thinking support in tests/integration/test_litellm_no_thinking.py
- [ ] T009 [P] Integration test for backward compatibility in tests/integration/test_litellm_backward_compat.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T010 [P] Implement ThinkingConfig model in src/google/adk/types/thinking_config.py
- [ ] T011 [P] Implement ModelResponseWithThinking model in src/google/adk/types/model_response_with_thinking.py
- [ ] T012 [P] Implement ThinkingExtractor utility in src/google/adk/utils/thinking_extractor.py
- [ ] T013 [P] Implement ProviderThinkingCapabilities enum in src/google/adk/enums/provider_thinking_capabilities.py
- [ ] T014 Update LiteLLMModel class in src/google/adk/models/litellm_model.py to support thinking_config
- [ ] T015 Implement execute_with_thinking method in src/google/adk/models/litellm_model.py
- [ ] T016 Implement validate_thinking_support method in src/google/adk/models/litellm_model.py

## Phase 3.4: Integration
- [ ] T017 Integrate ThinkingExtractor with LiteLLMModel in src/google/adk/models/litellm_model.py
- [ ] T018 Update API endpoint to support thinking_config in src/google/adk/api/litellm_thinking_endpoint.py
- [ ] T019 Add logging for thinking process in src/google/adk/logging/thinking_logger.py

## Phase 3.5: Polish
- [ ] T020 [P] Add unit tests for ThinkingExtractor in tests/unit/test_thinking_extractor.py
- [ ] T021 [P] Add unit tests for ProviderThinkingCapabilities in tests/unit/test_provider_thinking_capabilities.py
- [ ] T022 [P] Update documentation in docs/litellm_thinking.md
- [ ] T023 Performance tests for thinking_config functionality
- [ ] T024 Run quickstart validation tests from quickstart.md

## Dependencies
- Setup (T001-T002) before core implementation (T010-T016)
- Tests (T003-T009) before implementation (T010-T019)
- T010, T011 blocks T014
- T012, T013 blocks T017
- Implementation before polish (T020-T024)

## Parallel Example
```
# Launch T003-T009 together:
Task: "Contract test for POST /api/litellm/thinking in tests/contract/test_litellm_thinking_contract.py"
Task: "Unit test for ThinkingConfig in tests/unit/test_thinking_config.py"
Task: "Unit test for ModelResponseWithThinking in tests/unit/test_model_response_with_thinking.py"
Task: "Integration test for OpenAI model with thinking in tests/integration/test_litellm_openai_thinking.py"
Task: "Integration test for Anthropic model with thinking in tests/integration/test_litellm_anthropic_thinking.py"
Task: "Integration test for provider without thinking support in tests/integration/test_litellm_no_thinking.py"
Task: "Integration test for backward compatibility in tests/integration/test_litellm_backward_compat.py"
```

# Launch T010-T013 together:
Task: "Implement ThinkingConfig model in src/google/adk/types/thinking_config.py"
Task: "Implement ModelResponseWithThinking model in src/google/adk/types/model_response_with_thinking.py"
Task: "Implement ThinkingExtractor utility in src/google/adk/utils/thinking_extractor.py"
Task: "Implement ProviderThinkingCapabilities enum in src/google/adk/enums/provider_thinking_capabilities.py"

```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [ ] All contracts have corresponding tests
- [ ] All entities have model tasks
- [ ] All tests come before implementation
- [ ] Parallel tasks truly independent
- [ ] Each task specifies exact file path
- [ ] No task modifies same file as another [P] task