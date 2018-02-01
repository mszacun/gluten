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
