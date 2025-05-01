import network
import urequests
import time


# 코드 출처 : https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board/micropython-setup?utm_source=chatgpt.com
# 이해 안되면 위 주소로 들어가서 다시 공부하자


# 코드 설명
# (주의) urequests를 패키지 관리자를 통해서 설치해야 실행 가능!
# (주의) HTTP get 주소는 실제 있는 주소로 바꿔야 작동한다!
# 1. WIFI 설정
#    + SSID에 WI-FI의 이름을, PASSWORD에 WI-FI 비밀번호를  넣는다
# 2. WIFI 연결 시도
#    + network.WLAN(network.STA_IF): ESP32를 "클라이언트(STAtion 모드)"로 설정 (AP 모드 아님).
#       - WLAN(무선 LAN)은 무선 통신을 사용하여 모든 유형의 네트워크 클라이언트나 장치를 연결하는 일종의 LAN(근거리 통신망)
#       - WLAN(무선 LAN) 기술은 IEEE 802.11 표준을 주로 사용하며 IEEE 802.11표준의 브랜드명이 "WI-FI"임
#    + active(True): Wi-Fi 기능 켜기
#    + connect(): 지정한 SSID와 비밀번호로 실제 Wi-Fi에 접속 시도
# 3. WIFI 연결 대기
#    + Wi-Fi가 연결될 때까지 1초 간격으로 기다리는 반복문
#    + wlan.isconnected()가 True가 될 때까지 무한 대기
#    + 연결 안 되면 계속 "Wi-Fi 연결 중..." 출력함
# 4. 연결 성공 후 메시지 출력
#    + wlan.ifconfig()는 네트워크 정보(IP, Subnet, Gateway 등)를 튜플로 반환
#    + [0]은 IP 주소 (예: '192.168.0.12')
# 5. HTTP GET 요청
#    + HTTP GET 요청 : 서버로부터 정보를 요청할 때 사용되는 HTTP 메서드이다.
#       - 청할 때 필요한 데이터를 Body에 담지 않고, 쿼리 스트링(주소 뒤에 "?"를 붙여서)을 통해 전송한다.
#       - HTTP 헤더에서 cache-control 헤더를 통해 캐시 옵션을 지정할 수 있음
#       - GET 요청은 브라우저 히스토리에 남는다.
#    + HTTP POST 요청
#       - GET과 달리 전송할 데이터를 HTTP 메세지의 Body에 담아서 전송
#       - Body의 타입은 요청 헤더의 Content-Type에서 설정해주어야 한다
#       - 전송할 데이터는 크롬 개발자 도구 등으로 확인할 수 있기 때문에 민감한 정보는 반드시 암호화가 필요
#    + url 변수에 인터넷에서 시간 정보를 가져올 API 주소를 넣는다
#    + 이 API는 서울 표준시 기준의 현재 시간을 JSON 형태로 응답함
#    + urequests.get()으로 HTTP GET 요청 보내기
#    + 인터넷에 연결되어 있어야 정상 작동
#    + 반환된 response는 서버 응답 객체
# 6. 응답 데이터의 상태 확인 및 출력
#    + response.status_code == 200 → HTTP 성공 코드 (OK)
#    + 성공이면 response.text로 실제 응답 내용을 출력 (문자열, JSON 형식)
# 7. 연결된 HTTP 세션 정리
#    + 안 닫으면 메모리 누수나 오류 날 수 있음 (메모리가 작은 기기 특성상 MicroPython에선 중요함)

# 1. WIFI 설정
SSID = 'No.205'
PASSWORD = '20001129'

# 2. WIFI 연결 시도
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# 3. WIFI 연결 대기
while not wlan.isconnected():
    print("Wi-Fi 연결 중...")
    time.sleep(1)

# 4. 연결 성공 후 메시지 출력
print("연결 완료!")
print("IP 주소:", wlan.ifconfig()[0])

# 5. HTTP GET 요청
url = 'http://www.google.com'
response = urequests.get(url)

# 6. 응답 데이터의 상태 확인 및 출력
if response.status_code == 200:
    print("응답 데이터:")
    print(response.text)
else:
    print("요청 실패, 상태 코드:", response.status_code)

# 7. 연결된 HTTP 세션 정리
response.close()
