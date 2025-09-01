# 참고: 템플릿(학습용 개념). 실제 학습 코드는 프레임워크/리소스에 맞게 대체하세요.
import random

def policy_answer(prompt:str)->str:
    # 베이스 정책(모델)을 흉내내는 더미
    return "기본 응답: " + prompt[:50]

def preference_pairs():
    # (prompt, better, worse) 예시 데이터
    data = [
        ("요약: 문장 3줄", "세 줄 요약 A", "긴 산문"),
        ("JSON으로 출력", '{"ok": true}', "ok"),
    ]
    for d in data:
        yield d

def dpo_train(epochs=3):
    weight = 0.0
    logs = []
    for ep in range(epochs):
        correct = 0
        total = 0
        for (p, better, worse) in preference_pairs():
            # 더미: 가중치가 오를수록 올바른 형식을 낼 확률 증가
            prob_better = min(0.5 + weight, 0.95)
            ans = better if random.random() < prob_better else worse
            correct += int(ans == better)
            total += 1
        acc = correct/total
        logs.append({"epoch": ep+1, "acc": acc})
        weight += 0.1
    return logs

if __name__ == "__main__":
    print(dpo_train())
