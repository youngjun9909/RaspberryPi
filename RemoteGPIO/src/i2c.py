import smbus
from time import sleep

addr = 0x48
ain0 = 0x40
ain1 = 0x41

bus = smbus.SMBus(1)


def read(channel):
  bus.write_byte(addr, channel)
  value = bus.read_byte(addr)
  return value


if __name__ == "__main__":
  try:
    while True:
      data1 = read(ain0)
      data2 = read(ain1)
      print(f"조도센서 값: {data1}")
      print(f"온도센서 값: {data2}")
      sleep(1)
  except KeyboardInterrupt:
    pass