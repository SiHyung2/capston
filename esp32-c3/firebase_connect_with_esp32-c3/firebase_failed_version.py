# 다음 주소를 보면서 공부중..
# 출처 : https://github.com/ckoever/micropython-firebase-realtime-database

# 실패 원인 : esp32-c3에 ussl 모듈이 없는 것을 확인함.. 하

import os
import network
import ufirebase as firebase

wlan = network.WLAN(network.STA_IF)
if not wlan.active() or not wlan.isconnected():
  wlan.active(True)
  wlan.connect("No.205", "20001129")
  while not wlan.isconnected():
    pass


