import pigpio
from time import sleep

if __name__ == "__main__":
  IP = "192.168.7.102"
  pi = pigpio.pi(IP)

  if not pi.connected:
    print("원격 접속 실패")
    exit()

  try:
    led_pin = 26
    pi.set_mode(led_pin, pigpio.OUTPUT)

    while True:
      pi.write(led_pin, 1)
      sleep(0.1)
      pi.write(led_pin, 0)
      sleep(0.1)

  except KeyboardInterrupt:
    pass

  finally:
    pi.stop()

