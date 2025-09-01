# 간단 지표: Exact Match 유사/근거 포함 여부
from typing import List, Dict

def exact_match(pred:str, gold:str)->float:
    return 1.0 if pred.strip().lower()==gold.strip().lower() else 0.0

def contains_any(pred:str, targets:List[str])->float:
    return 1.0 if any(t.lower() in pred.lower() for t in targets) else 0.0

def score_batch(items:List[Dict])->Dict:
    ems, faith = [], []
    for it in items:
        ems.append(exact_match(it["pred"], it["gold"]))
        faith.append(contains_any(it["pred"], it.get("gold_spans", [])))
    return {"EM": sum(ems)/len(ems), "Faithfulness": sum(faith)/len(faith)}
