import math
import multiprocessing
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger(__name__)


def integrate(fun, a, b, steps):
    h = (b - a) / steps
    result = 0
    for i in range(steps):
        result += fun(a + h * i)
    return result * h


def integrate_segment(args):
    fun, a, b, steps = args
    log.info(f"Запуск задачи integrate({fun.__name__}, {a}, {b}, {steps})")
    result = integrate(fun, a, b, steps)
    log.info(f"Завершение задачи integrate({fun.__name__}, {a}, {b}, {steps})")
    return result


def parallel_integrate(fun, a, b, steps, n_jobs, pool_executor):
    step_size = (b - a) / n_jobs
    tasks = [
        (fun, a + i * step_size, a + (i + 1) * step_size, steps // n_jobs)
        for i in range(n_jobs)
    ]

    result = 0
    with pool_executor(max_workers=n_jobs) as executor:
        for partial_result in executor.map(integrate_segment, tasks):
            result += partial_result

    return result


import pandas as pd

def main():
    fn = math.cos
    a = 0
    b = math.pi / 2
    steps = 1000000
    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = list(range(1, cpu_num * 2 + 1))

    results = {
        "n_jobs": n_jobs_list,
        "ThreadPoolExecutor": [],
        "ProcessPoolExecutor": []
    }

    for pool_executor in [ThreadPoolExecutor, ProcessPoolExecutor]:
        print(f"Использование {pool_executor.__name__}:")
        log.setLevel(logging.CRITICAL)
        for n_jobs in n_jobs_list:
            start_time = time.time()
            result = parallel_integrate(fn, a, b, steps, n_jobs, pool_executor)
            end_time = time.time()
            elapsed_time = end_time - start_time
            results[pool_executor.__name__].append(elapsed_time)
            print(f"  n_jobs = {n_jobs}, результат = {result:.5f}, время: {elapsed_time:.2f} секунд")
        print()

    df = pd.DataFrame(data=results)
    print("Таблица времени выполнения для разных n_jobs:")
    print(df)


if __name__ == "__main__":
    main()