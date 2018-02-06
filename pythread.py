import time
from queue import Queue
from threading import Thread


def receive(q):
    data = 1
    while True:
        q.put(data)
        time.sleep(1)
        data += 1
        if data > 5:
            break


def send(q):
    while True:
        data = q.get()
        time.sleep(1)
        print(data)
        if q.empty():
            break


def main():
    q = Queue()
    receive_thread = Thread(target=receive, args=(q,))
    receive_thread.start()
    send_thread = Thread(target=send, args=(q,))
    send_thread.start()


if __name__ == '__main__':
    main()
