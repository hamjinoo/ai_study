from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .schema import AnswerSchema, SourceItem
from .retriever import SimpleRetriever, Doc
from .reranker import rerank
from .utils import make_citations_block

app = FastAPI(title="Evidence‑Grounded RAG (Template)")

# 데모용 코퍼스
CORPUS = [
    Doc("RAG는 검색과 생성을 결합해 최신성과 근거성을 높이는 기법이다.", {"id":"doc-1", "title":"RAG intro"}),
    Doc("롱컨텍스트는 대용량 문맥을 한 번에 처리하도록 모델을 확장한다.", {"id":"doc-2", "title":"Long Context"}),
    Doc("OWASP LLM Top-10은 보안 체크리스트로 인젝션 방어 등을 포함한다.", {"id":"doc-3", "title":"OWASP LLM"}),
]
retriever = SimpleRetriever(CORPUS)

class AskIn(BaseModel):
    question: str

@app.post("/ask", response_model=AnswerSchema)
def ask(in_: AskIn):
    # 1) 검색
    cands = retriever.search(in_.question, top_k=8)
    # 2) 재순위
    top = rerank(in_.question, cands, top_k=3)
    # 3) 근거 블록
    ctx = make_citations_block(top)
    # 4) (여기서 실제 LLM 호출이 들어가야 하나, 템플릿이므로 더미 생성)
    body = f"질문: {in_.question}\n\n근거:\n{ctx}\n\n답변: [1][2]를 참고하면 RAG와 보안 체크리스트가 핵심입니다."
    sources = [SourceItem(id=f"[{i+1}]", title=d.meta.get("title",""), location=d.meta.get("id",""), quote=d.text[:120]) for i, d in enumerate(top)]
    return AnswerSchema(
        one_line="출처가 있는 답변 템플릿(데모)",
        answer_md="RAG는 검색+생성 결합으로 **근거성**을 높입니다. 자세한 내용은 [1][2][3]을 참고하세요.",
        sources=sources,
        limits="데모 코퍼스/더미 생성. 실제 LLM 연결 필요.",
        next_questions=["실제 문서 폴더를 인덱싱하세요.", "리트리버 파라미터를 표로 비교하세요."]
    )
