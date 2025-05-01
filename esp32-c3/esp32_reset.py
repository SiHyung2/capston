from machine import Pin, UART
import time

# esp32-c3-mini-1 의 datasheet에서 11번째 페이지의 pin definitions를 찾아서 tx, rx의 GPIO 핀을 찾았음
# https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf


# UART 객체 설정 (TX: GPIO 21, RX: GPIO 20)
uart = UART(1, baudrate=9600, tx=21, rx=20)

#while True:
#    if uart.any():  # 데이터가 수신되었으면
#        data = uart.read()  # 데이터 읽기
#        print("Received:", data)  # 수신한 데이터 출력
#    time.sleep(0.1)  # 100ms 대기



while True:
    uart.write("Hello, ESP32!\n")  # 데이터 송신
    time.sleep(1)  # 1초 대기