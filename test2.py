import unittest
import threading
from test1 import TestAPI
import getData


rps = 6

latency80 = True


class TestRun(unittest.TestCase):
    def test_rps(self):
        global rps
        self.assertGreater(rps, 5)

    def test_latency80(self):
        global latency
        self.assertTrue(latency80)


# Python выполняет выполнение одного потока с блокировкой остальных потоков.
# Global Interprete Lock (GIL). Именно эта блокировка и вызывает такое поведение.
# Однако GIL решает множество проблем с разделяемой памятью.
# При отключении GIL код, в лучшем случает, будет работать также, а в худшем - дольше.

latency = []


def calc_lat80(latency):  # 80% ответов от ресурса <= 450 мс
    li = []
    for i in latency:
        if i > 450:
            li.append(i)
    if len(li) >= 2:
        latency80 = False
    else:
        latency80 = True


if __name__ == "__main__":
    for i in range(8):
        my_thread = threading.Thread(target=unittest.main)
        my_thread.start()
        my_thread.join()
        latency.append(getData.time_resp)
    calc_lat80(latency)
