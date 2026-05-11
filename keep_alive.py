import os
import requests

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    table_url = f"{url}/rest/v1/keep_alive"
    
    try:
        # 1. 데이터 삽입 (POST)
        print("상태 신호 전송 중...")
        insert_res = requests.post(table_url, headers=headers, json={})
        insert_res.raise_for_status()
        print("성공: 데이터 삽입 완료 (DB 활성화)")

        # 2. 데이터 삭제 (DELETE)
        # 'id가 null이 아닌 모든 행'이라는 조건을 추가 (neq.null)
        delete_url = f"{table_url}?id=neq.null" 
        delete_res = requests.delete(delete_url, headers=headers)
        delete_res.raise_for_status()
        print("성공: 데이터 정리 완료 (Clean up)")
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    poke_database()