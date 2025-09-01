# 리트리버 파라미터 탐색(템플릿)
import itertools, json

def grid(params):
    keys = params.keys()
    for vals in itertools.product(*params.values()):
        yield dict(zip(keys, vals))

if __name__ == "__main__":
    params = {"k":[4,8], "chunk":[256,512], "max_tokens":[1024,2048]}
    for cfg in grid(params):
        print(json.dumps(cfg))
