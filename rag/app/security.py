BLOCK_PATTERNS = [
    'ignore previous', 'disregard instructions', 'system override',
    'format drive', 'delete all', 'exfiltrate'
]

ALLOWED_DOMAINS = {'example.com', 'wikipedia.org'}

def is_prompt_injection(text:str)->bool:
    low = text.lower()
    return any(p in low for p in BLOCK_PATTERNS)

def can_execute_external(url:str)->bool:
    # 화이트리스트 도메인만 허용
    return any(url.endswith(d) or (f".{d}" in url) for d in ALLOWED_DOMAINS)
