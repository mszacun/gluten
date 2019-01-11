import time


def do_it(fun, max_reps=5, delay=0.5):
    while True:
        max_reps -= 1
        try:
            fun()
            return
        except:
            if max_reps == 0:
                raise
            time.sleep(delay)


def wait_until(fun, max_reps=10, delay=1):
    while not fun():
        max_reps -= 1
        time.sleep(delay)
        if max_reps == 0:
            raise Exception('Specified conditions was not met')

