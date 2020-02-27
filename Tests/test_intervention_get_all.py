from unittest import TestCase

from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_get_all import InterventionGetAllUseCase
from app import CONNECTION_STRING


class TestIntervention(TestCase):

    def test_get_all_intervention(self):
        # ARRANGE
        repo = InterventionDbRepository(CONNECTION_STRING)
        uc = InterventionGetAllUseCase(repo)
        # ACT
        response = uc.execute()
        # ASSERT
        self.assertDictEqual(response[0], {
            "ref": 1,
            "client": "Geoffrey Soulaques",
            "description": "Problème ordinateur portable"
        })
