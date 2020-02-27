from unittest import TestCase

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_save import InterventionSave
from app import CONNECTION_STRING


class TestIntervention(TestCase):

    def test_save_intervention(self):
        # ARRANGE
        repo = InterventionDbRepository(CONNECTION_STRING)
        uc = InterventionSave(repo)
        intervention = Intervention("2000", "Valentin", "Test")
        # ACT
        response = uc.execute(intervention)
        # ASSERT
        self.assertDictEqual(response[-1], {
            "ref": 2000,
            "client": "Valentin",
            "description": "Test"
        })
