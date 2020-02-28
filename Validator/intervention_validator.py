from Domain.intervention import Intervention


class InterventionValidator:
    def __init__(self, data):
        try:
            self.ref = data["ref"]
            self.client = data["client"]
            self.description = data["description"]
        except Exception as exc:
            raise Exception(exc.args[0])

    def valid_intervention(self):
        return Intervention(self)
