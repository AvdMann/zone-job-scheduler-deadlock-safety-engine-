import threading
import time

counter = 100


def subtract_credits():
    global counter
    temp = counter
    time.sleep(0.001)
    temp -= 40
    counter = temp


def add_credits():
    global counter
    temp = counter
    time.sleep(0.001)
    temp += 25
    counter = temp


def run_without_sync():
    global counter

    print("WITHOUT SYNCHRONIZATION")

    for i in range(5):
        counter = 100

        t1 = threading.Thread(target=subtract_credits)
        t2 = threading.Thread(target=add_credits)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print(f"Run {i + 1}: Final Value = {counter}")


flag = [False, False]
turn = 0


def peterson_worker(thread_id, operation):
    global counter, turn

    other = 1 - thread_id

    flag[thread_id] = True
    turn = other

    while flag[other] and turn == other:
        pass

    temp = counter
    time.sleep(0.001)

    if operation == "subtract":
        temp -= 40
    else:
        temp += 25

    counter = temp

    flag[thread_id] = False


def run_with_peterson():
    global counter, flag, turn

    print("\nWITH PETERSON'S ALGORITHM")

    for i in range(5):
        counter = 100
        flag = [False, False]
        turn = 0

        t1 = threading.Thread(
            target=peterson_worker,
            args=(0, "subtract")
        )

        t2 = threading.Thread(
            target=peterson_worker,
            args=(1, "add")
        )

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print(f"Run {i + 1}: Final Value = {counter}")


if __name__ == "__main__":
    run_without_sync()
    run_with_peterson()
