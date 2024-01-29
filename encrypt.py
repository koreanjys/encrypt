from passlib import hash

async def encrypt(data: str, algorithm:str, salt: str = None):
    try:
        crypt = getattr(hash, f"{algorithm}_crypt")  # 선택한 해싱 알고리즘에 따라 사용하는 크립트가 바뀜
        hashed_data = crypt.using(salt=salt).hash(data)
        return hashed_data
    except AttributeError:
        print(f"Unsupported algorithm: {algorithm}")
        return None