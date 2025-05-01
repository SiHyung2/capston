import network

# AP 모드 활성화
ap = network.WLAN(network.AP_IF)
ap.active(True)

# AP 설정 (SSID, 비밀번호, 최대 연결 개수)
ap.config(essid="ESP32-C3-AP", password="12345678", authmode=network.AUTH_WPA_WPA2_PSK, max_clients=5)

print("Wi-Fi AP 시작됨!  'ESP32-C3-AP' 연결하려면 비밀번호 '12345678'를 입력 ")
print("IP Address:", ap.ifconfig()[0])
