from Domain.intervention import Intervention
from Repository.intervention_repository import InterventionRepository


class InterventionGetAllUseCase:
    def __init__(self, repo: InterventionRepository):
        self.session = None
        self.repository = repo

    def execute(self):
        return self.repository.get_all()


class ToDoSaveRequestObject:
    def __init__(self, datatask):
        if "description" not in datatask:
            raise Exception("pas de description")
        else:
            self.__description = datatask["description"]

    @property
    def description(self):
        return self.__description

    def get_todo_task(self):
        return Intervention(self.description)
