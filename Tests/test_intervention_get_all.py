from unittest import TestCase, mock

import pytest

from Domain.intervention import Intervention
from UseCase.intervention_get_all import InterventionGetAllUseCase


class TestIntervention(TestCase):

    @pytest.fixture()
    def domain_interventions(self):
        interv1 = Intervention(1, "Valentin", "BSOD")
        interv2 = Intervention(2, "Geoffrey", "Test")
        return [interv1, interv2]

    def test_get_all_intervention(self):
        # ARRANGE
        repo = mock.Mock()
        repo.list.list_return = self.domain_interventions
        uc = InterventionGetAllUseCase(repo)

        # ACT
        response = uc.execute()

        # ASSERT
        repo.list.assert_called_with()
        assert response == self.domain_interventions
