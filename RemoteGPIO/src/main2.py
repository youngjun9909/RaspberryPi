import pigpio
from time import sleep

if __name__ == "__main__":
  IP = "192.168.7.102"
  pi = pigpio.pi(IP)

  if not pi.connected:
    print("원격 접속 실패")
    exit()

  try:
    btn_pin = 17
    pi.set_mode(btn_pin, pigpio.INPUT)
    pi.set_pull_up_down(btn_pin, pigpio.PUD_DOWN)

    led_pin = 26
    pi.set_mode(led_pin, pigpio.OUTPUT)

    while True:
      if pi.read(btn_pin) == 1:
        pi.write(led_pin, 1)
        sleep(0.1)
        pi.write(led_pin, 0)
        sleep(0.1)

  except KeyboardInterrupt:
    pass

  finally:
    pi.stop()

