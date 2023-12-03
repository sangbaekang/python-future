import concurrent.futures
import time


def add_and_print(x):
    time.sleep(1.234)

    print(f"x print: {x}")
    return x + 1


def execute_thread():
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            executor.submit(add_and_print, i)

    return "Success"


if __name__ == "__main__":
    print("Hello World")
