from contextlib import contextmanager

from icecream import ic


@contextmanager
def safe():
    try:
        ic("safe:")
        yield
    except Exception as e:
        ic(e)
    finally:
        ic("/safe")
