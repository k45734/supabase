import os
from supabase import create_client, Client

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    try:
        supabase: Client = create_client(url, key)
        
        # 테이블을 조회하지 않고, 서버의 기본 정보(Health Check)만 요청합니다.
        # 아래 방식은 테이블이 없어도 대답을 주기 때문에 에러가 나지 않습니다.
        response = supabase.auth.get_session() 
        
        print("Success: 데이터베이스 연결 확인 완료 (Auth Session Check)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    poke_database()