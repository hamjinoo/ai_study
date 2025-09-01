# 평가 리포트 생성(간단)
from pathlib import Path
import json

def main(dataset_path="eval/dataset.jsonl", out="eval/report.md"):
    items = [json.loads(l) for l in Path(dataset_path).read_text(encoding="utf-8").splitlines() if l.strip()]
    n = len(items)
    md = ["# 평가 리포트", f"- 데이터셋: N={n}", "- 결과 요약: (여기에 스코어 표/그래프)"]
    Path(out).write_text("\n".join(md), encoding="utf-8")

if __name__ == "__main__":
    main()
