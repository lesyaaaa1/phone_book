from unittest import TestCase
from file import read_dataset, write_dataset
from manager import create, update, delete
from search import search_record
import json

class Test(TestCase):
    def setUp(self) -> None:
        self.dict_1 = {}
        self.file = 'file.json'
        self.info = {"0678817737": {"first_name": "lesya", "last_name": "kiriliuk", "city": "rivne", "country": "ukraine"}}
    def test_create(self):
        create(self.dict_1, self.info)
        self.assertIn("0678817737", self.dict_1)
        self.assertEqual(self.dict_1["0678817737"], {"first_name": "lesya", "last_name": "kiriliuk", "city": "rivne", "country": "ukraine"})

    def test_update(self):
        create(self.dict_1, self.info)
        update(self.dict_1, {"0678817737": {"first_name": "", "last_name": "", "city": "kiyv", "country": ""}})
        self.assertEqual(self.dict_1["0678817737"], {"first_name": "lesya", "last_name": "kiriliuk", "city": "kiyv", "country": "ukraine"})
    def test_delete(self):
        create(self.dict_1, self.info)
        delete(self.dict_1) # але там сам тест як запуститься, то треба ввести 0678817737, щоб все виконалось без помилок
        self.assertNotIn("0678817737", self.dict_1)

    def test_search_record(self):
        create(self.dict_1, self.info)
        self.assertEqual(search_record(self.dict_1, 'sp', '000'), {})
        self.assertEqual(search_record(self.dict_1, 'sf', 'lesya'), self.info)
        self.assertEqual(search_record(self.dict_1, 'sl', 'aaaaaaa'), {})
        self.assertEqual(search_record(self.dict_1, 'sfl', 'lesya kiriliuk'), self.info)
        self.assertEqual(search_record(self.dict_1, 'sct', 'kiyv'), {})
        self.assertEqual(search_record(self.dict_1, 'sc', 'ukraine'), self.info)

    def test_read_dataset(self):
        read_dataset({"0678817737": {"first_name": "lesya", "last_name": "kiriliuk", "city": "rivne", "country": "ukraine"}})
        self.assertIn({"0678817737": {"first_name": "lesya", "last_name": "kiriliuk", "city": "rivne", "country": "ukraine"}}, )

    def test_write_and_read_dataset(self):
        write_dataset(self.info, 'file_test.json')
        self.assertEqual(self.info, read_dataset('file_test.json'))

