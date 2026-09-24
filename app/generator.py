import httpx
import uuid

def create_guest_account():
    # Generates a random device ID to mimic a mobile phone registration
    device_id = str(uuid.uuid4()).replace('-', '')[:16]
    
    url = "https://freefiremobile.com"
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Build/RP1A.200720.011)",
        "Content-Type": "application/json"
    }
    payload = {
        "device_id": device_id,
        "device_model": "CPH2127",
        "os_version": "30",
        "region": "EU"  # This automatically routes to the Middle East & Africa layer
    }
    
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {
                    "uid": data.get("uid"),
                    "password": data.get("access_token")
                }
    except Exception:
        return None
      
