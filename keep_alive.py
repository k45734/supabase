import os
import requests

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    # Supabase REST API를 직접 호출하여 데이터 1건 조회
    # headers에 apikey와 Authorization을 포함해야 합니다.
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}"
    }
    
    # 'players' 테이블에서 1건 조회
    target_url = f"{url}/rest/v1/players?select=name&limit=1"
    
    try:
        response = requests.get(target_url, headers=headers)
        response.raise_for_status()
        print(f"Success: Status Code {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    poke_database()