import pathlib

from flask import Flask, jsonify, request

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_get_all import InterventionGetAllUseCase
from UseCase.intervention_save import InterventionSaveUseCase
from Validator.intervention_validator import InterventionValidator

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
    uc = InterventionSaveUseCase(repo)
    data = request.get_json()
    intervention = InterventionValidator.valid_intervention(data)
    return uc.execute(intervention)


if __name__ == '__main__':
    app.run()
