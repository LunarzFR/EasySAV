from unittest import TestCase

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_save import InterventionSaveUseCase
from app import CONNECTION_STRING


class TestIntervention(TestCase):

    def test_save_intervention(self):
        # ARRANGE
        repo = InterventionDbRepository(CONNECTION_STRING)
        uc = InterventionSaveUseCase(repo)
        intervention = Intervention("", "Valentin", "Test")
        # ACT
        response = uc.execute(intervention)
        # ASSERT
        self.assertEqual(response, "True")
