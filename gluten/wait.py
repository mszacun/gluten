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


def wait_until(fun, max_reps=5, delay=0.5):
    while not fun() and max_reps > 0:
        max_reps -= 1
        sleep(delay)
