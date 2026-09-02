# AGENTS.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

※ Don't use '~': It might make strikethrough. Instead, use '-'.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

---

# 2026 연고전 해커톤

## 목적

고려대학교와 연세대학교 양교 단과대학의 전문성과 특색을 살린 새로운 대표 교류 행사를 만들고, 학생들이 AI 소프트웨어 분야의 역량을 바탕으로 경쟁하고 교류하는 장을 만들고자 함.

## 일정

대회 기간 : 9/27 ~ 10/1
중간 집계 : 대회 기간 중 매일 오전 10시 / 오후 10시
파이널 데이(발표 및 시상) : 10/6 19시 → 상위 12팀 발표 진행

※ 시상식을 제외한 일정은 모두 온라인으로 진행

## 개요

해커톤 종목 : **격자 기반 턴제 전략 게임 → <깃발 대항전>**

- 참가자들은 신촌과 안암 캠퍼스를 배경으로 주요 건물에 깃발을 꽂아 거점을 점령하고 점수를 획득하는 전략 Agent를 개발하게 됨.
- 완성된 Agent들은 자동 대전 환경에서 서로 맞붙으며, 각 팀은 자신만의 전략과 기술을 바탕으로 치열한 승부를 펼침.
- 개발 경험이 많지 않은 학우들도 부담 없이 참여할 수 있도록 구성했으며, Agent의 기획부터 개발•개선과 대전까지 전 과정을 경험 가능.
- 한 팀당 2~3인 구성 (우리 팀은 3인 구성)

## 진행 방식

신촌과 안암 캠퍼스를 배경으로, 각 건물에 깃발을 꽂아 거점을 점령하고, 점수를 획득하는 전략 시뮬레이션 Agent 개발

1. 대회 준비 및 환경 제공
- 참가팀 대상 시뮬레이터 환경 및 베이스라인 코드 제공
- 규칙 가이드 및 테스트용 대전 환경 오픈
2. Agent 개발 및 전략 수립 (해커톤 기간)
- 팀별 전략에 맞춘 점령•방어 알고리즘 개발
- 시뮬레이터 환경에서 자유로운 테스트 및 모델 고도화
3. 최종 제출 및 대전 평가
- 개발 완료된 최종 Agent 코드 제출
- 전 팀 스위스 토너먼트 및 본선 진출자 대상 종합평가를 통한 평가 진행

※ 상세 대회 일정 및 제출 가이드는 추후 별도 안내 예정

## 평가

최종 평가는 제출 마감 후 일괄 진행.

- 1차 예선 : 스위스 토너먼트 형식 → 모든 참가팀의 Agent를 대상으로 중간 탈락 없이 여러 라운드 대전을 진행하여 상위 팀을 선발
- 2차 본선 : 상위 팀 종합 평가 → 풀 리그 대전 결과(70%) + 보고서(20%) + 발표(10%)

1차에서 선발된 본선 진출 팀을 대상으로 풀 리그의 대전 결과와 보고서 및 발표 평가를 종합하여 최종 수상 순위를 결정

※ 2차 본선에 대한 내용은 추후 상위 팀 대상으로 안내 예정

---
---

# 연습 계획

plan.md를 참고하여 사용자의 상황에 맞게 해커톤 연습을 진행한다.