import network
import socket

# Wi-Fi AP 설정
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP32_AP", password="12345678")

# UDP 서버 소켓 설정
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('0.0.0.0', 12345))

print("UDP Server Started at 192.168.4.1:12345")

while True:
    data, addr = udp.recvfrom(1024)
    print("Received from {}: {}".format(addr, data.decode()))
    
    # 클라이언트(핸드폰)에게 응답
    udp.sendto(b'ESP32 received your message!', addr)
