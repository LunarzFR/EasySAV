from Domain.intervention import Intervention
from Repository.intervention_repository import InterventionRepository


class InterventionSave:
    def __init__(self, repo: InterventionRepository):
        self.session = None
        self.repository = repo

    def execute(self, intervention: Intervention):
        return self.repository.save(intervention)
