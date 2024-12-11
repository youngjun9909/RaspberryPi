import threading
import time

number = 0

def t1():
    global number
    while True:
        number += 1
        print("스레드 1 실행")
        print(f"Thread1 -> {number}")
        time.sleep(1)

def t2():
    global number
    while True:
        number += 1
        print("스레드 2 실행")
        print(f"Thread1 -> {number}")
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=t1, daemon=True)
    thread2 = threading.Thread(target=t2, daemon=True)

    thread1.start()
    thread2.start()

    while True:
        print("메인 실행 중")
        time.sleep(3)