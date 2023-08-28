import unittest
import requests

class TestAPI(unittest.TestCase):
    url = "http://0.0.0.0:5000/"

    data = {
        "text": "something wicked this way comes"
    }

    def test_post(self):
        resp = requests.post(self.url, json = self.data)
        self.assertEqual(resp.status_code, 200)
        print("Test 2 completed. Status: PASSED")

if __name__ == '__main__':
    tester = TestAPI()

    tester.test_post()