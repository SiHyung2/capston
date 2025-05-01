import bluetooth

# Bluetooth 활성화
ble = bluetooth.BLE()
ble.active(True)

# Bluetooth 장치 검색
print("Scanning for Bluetooth devices...")
devices = ble.gap_scan(5)  # 5초 동안 스캔

if devices:
    print("Found devices:", devices)
else:
    print("No Bluetooth devices found")
