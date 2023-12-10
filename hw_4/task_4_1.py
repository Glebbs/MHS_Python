import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def worker(number):
    fib_num = fibonacci(number)
    print(f"Поток/процесс {threading.current_thread().name}: Фибоначчи({number}) = {fib_num}")


def main():
    number = 35
    repetitions = 10
    sync_start = time.time()
    for _ in range(repetitions):
        worker(number)
    sync_end = time.time()

    threads = [threading.Thread(target=worker, args=(number,)) for _ in range(repetitions)]
    async_threads_start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    async_threads_end = time.time()

    processes = [multiprocessing.Process(target=worker, args=(number,)) for _ in range(repetitions)]
    async_processes_start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    async_processes_end = time.time()

    print(f"Синхронное выполнение: {sync_end - sync_start} секунд")
    print(f"Асинхронное выполнение с потоками: {async_threads_end - async_threads_start} секунд")
    print(f"Асинхронное выполнение с процессами: {async_processes_end - async_processes_start} секунд")


if __name__ == "__main__":
    main()