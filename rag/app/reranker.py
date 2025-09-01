# 선택: Cross-encoder/ColBERT 대체 자리. 지금은 길이/키워드 가중치로 더미 재순위.
from typing import List
from .retriever import Doc

def rerank(query:str, docs:List[Doc], top_k:int=4)->List[Doc]:
    scored = []
    for d in docs:
        # 더미: 짧고 질의 길이와 유사하면 가점
        score = 1.0/(1+abs(len(d.text)-len(query))) + d.text.lower().count(query.lower())*0.1
        scored.append((score, d))
    scored.sort(key=lambda x:x[0], reverse=True)
    return [d for _, d in scored[:top_k]]
