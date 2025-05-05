from loguru import logger
import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Execution time for {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper
