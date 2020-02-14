class Intervention:
    def __init__(self, ref, client, description):
        self.ref = ref
        self.client = client
        self.description = description

    def to_dict(self):
        return {
            "ref": self.ref,
            "client": self.client,
            "description": self.description
        }