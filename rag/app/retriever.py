# 간단한 하이브리드: 키워드(BM25 유사) + 임베딩(스텁)
from typing import List, Dict
import math

class Doc:
    def __init__(self, text:str, meta:Dict):
        self.text = text
        self.meta = meta

class SimpleRetriever:
    def __init__(self, corpus:List[Doc]):
        self.corpus = corpus

    def score_keyword(self, q, d):
        # 매우 단순한 키워드 매칭
        tokens = q.lower().split()
        return sum(d.text.lower().count(t) for t in tokens)

    def score_dense(self, q, d):
        # 스텁: 길이 기반 가짜 점수
        return 1.0 / (1.0 + abs(len(d.text) - len(q)))

    def search(self, query:str, top_k:int=8)->List[Doc]:
        scores = []
        for d in self.corpus:
            s = 0.7*self.score_keyword(query, d) + 0.3*self.score_dense(query, d)
            scores.append((s, d))
        scores.sort(key=lambda x: x[0], reverse=True)
        return [d for _, d in scores[:top_k]]
