import os
from supabase import create_client, Client

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    try:
        supabase: Client = create_client(url, key)
        
        # 1. 실제 테이블에서 아주 적은 양의 데이터를 조회합니다.
        # 'profiles'나 'users' 등 본인의 프로젝트에 실제 존재하는 테이블 이름을 넣으세요.
        # .limit(1)을 붙여 부하를 최소화합니다.
        response = supabase.table("players").select("name").limit(1).execute()
        
        print(f"Success: 데이터베이스 쿼리 완료 ({len(response.data)} rows fetched)")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    poke_database()