import pathlib

from flask import Flask, jsonify

from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_get_all import InterventionGetAllUseCase

app = Flask(__name__)

CONNECTION_STRING = f"{pathlib.Path(__file__).parent.absolute()}\\database.db"


@app.route('/')
def get_all_interventions():
    repo = InterventionDbRepository(CONNECTION_STRING)
    uc = InterventionGetAllUseCase(repo)
    return jsonify(uc.execute())


@app.route('/add', methods=['POST'])
def add_intervention():
    return ""


if __name__ == '__main__':
    app.run()


