import faiss
print(faiss.__version__)

# GPU 사용 가능 여부 확인
print(faiss.get_num_gpus())
