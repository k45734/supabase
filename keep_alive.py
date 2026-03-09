import os
from supabase import create_client, Client

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        print("Error: 환경 변수(URL/KEY)가 설정되지 않았습니다.")
        return

    try:
        supabase: Client = create_client(url, key)
        # 프로젝트 내에 존재하는 아무 테이블이나 조회하세요. 
        # (예: 'users', 'posts' 등 하나라도 데이터가 있는 테이블 권장)
        # 만약 테이블이 하나도 없다면 가벼운 쿼리라도 날려야 합니다.
        response = supabase.table('profiles').select("*").limit(1).execute()
        print("Success: 데이터베이스에 신호를 보냈습니다.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    poke_database()