import unittest
import getData
import datetime


class TestAPI(unittest.TestCase):
    def test_request_time(self):  # ответ от ресурса < 500мс
        self.assertLess(getData.time_resp, 500)

    def test_date(self):  # актуальность полученных данных
        self.assertEqual(
            getData.date, datetime.datetime.now().strftime("%Y-%m-%d"))

    def test_data_size(self):  # размер пакета данных < 10кб
        self.assertLess(getData.size, 10000)


if __name__ == '__main__':
    unittest.main()
