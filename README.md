# AI Portfolio Template — Evidence‑Grounded RAG & Eval (v2025-09-01)

**한 줄 핵심:** “모델을 새로 발명”이 아니라, **검색(RAG)·근거·평가·보안**을 **작동**하게 만들어 _출처가 있는 AI_ 를 만드는 템플릿입니다.

## 폴더 구조
```
ai-portfolio/
  README.md
  requirements.txt
  paper_notes/
  replications/
  rag/
  mm_rag/
  long_context/
  eval/
  ux/
  docs/
  scripts/
  prompt_templates/
  tests/
  security.md
  .gitignore
  LICENSE
```
## 빠른 시작
1) Python 3.10+
2) 가상환경 생성 후 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
3) API 서버 실행:
   ```bash
   uvicorn rag.app.main:app --reload
   ```
4) 프런트 데모(정적): `ux/demo/index.html` 열기 → 서버는 `http://127.0.0.1:8000`

## 목표 산출물(포트폴리오 신호)
- **출처가 있는 답변**(본문 [1][2] 각주 + 근거 하이라이트)
- **HELM식 간단 평가 리포트**(정확성·근거성)
- **OWASP LLM Top-10 대응 체크리스트**(인젝션 방어/권한·출처 정책)
- **튜닝 전후 그래프**(비용·지연·정확성 프론티어)

> ⚠️ 이 템플릿은 학습·포트폴리오용 뼈대입니다. 상용 배포 전에는 데이터/보안/비용 검토가 필수입니다.
