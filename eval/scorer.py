import json, sys
from rag.app.eval import score_batch

def main(path):
    items = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            it = json.loads(line)
            # 데모: pred는 gold로 대체(실사용 시 모델 예측으로 교체)
            it["pred"] = it["gold"]
            items.append(it)
    print(score_batch(items))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "dataset.jsonl")
