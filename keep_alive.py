import os
import requests

def poke_database():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    # 공통 헤더 설정
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    # 1. 테이블이 있는지 확인하거나 데이터를 삽입 시도
    # (테이블이 없다면 여기서 404 에러가 발생하므로 이를 통해 상태 확인 가능)
    table_url = f"{url}/rest/v1/keep_alive"
    
    try:
        # 데이터 삽입 시도 (이 작업이 실질적인 Heartbeat 역할)
        print("상태 신호 전송 중...")
        insert_res = requests.post(table_url, headers=headers, json={})
        
        if insert_res.status_code == 404:
            print("알림: keep_alive 테이블이 없습니다. SQL Editor에서 테이블을 먼저 생성해주세요.")
            print("SQL: create table keep_alive (id uuid default gen_random_uuid() primary key, created_at timestamptz default now());")
            return

        insert_res.raise_for_status()
        print("성공: 데이터 삽입 완료 (DB 활성화)")

        # 2. 방금 넣은 데이터 또는 오래된 데이터 삭제 (용량 정리)
        # 모든 데이터를 삭제하여 테이블을 비워둡니다.
        delete_res = requests.delete(table_url, headers=headers)
        delete_res.raise_for_status()
        print("성공: 데이터 정리 완료 (Clean up)")
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    poke_database()