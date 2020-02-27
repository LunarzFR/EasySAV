from unittest import TestCase
from Domain.intervention import Intervention


class TestToDoTask(TestCase):
    def test_to_dict(self):
        task = Intervention("tache 1")
        dict_task = {"client": "Geoffrey", "description": "test description"}
        dic = task.to_dict()
        self.assertEqual(dict_task["description"], dic["description"])
        self.assertEqual(dict_task["client"], dic["client"])

    def test_client(self):
        task = Intervention("tache")
        self.assertEqual(task.client, "geoffrey")

    def test_description(self):
        task = Intervention("tache")
        self.assertEqual(str(task.description), "test de description")