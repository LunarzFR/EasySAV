import pathlib

from flask import Flask, jsonify, request

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_get_all import InterventionGetAllUseCase
from UseCase.intervention_save import InterventionSave

app = Flask(__name__)

CONNECTION_STRING = f"{pathlib.Path(__file__).parent.absolute()}\\db.sqlite"


@app.route('/')
def get_all_interventions():
    repo = InterventionDbRepository(CONNECTION_STRING)
    uc = InterventionGetAllUseCase(repo)
    return jsonify(uc.execute())


@app.route("/add", methods=['POST'])
def save_intervention():
    repo = InterventionDbRepository(CONNECTION_STRING)
    uc = InterventionSave(repo)
    data = request.get_json()
    intervention = Intervention(data.get('ref'), data.get('client'), data.get('description'))
    return uc.execute(intervention)


if __name__ == '__main__':
    app.run()
