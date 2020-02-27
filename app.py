import pathlib

from flask import Flask, jsonify, request

from Domain.intervention import Intervention
from Repository.intervention_db_repository import InterventionDbRepository
from UseCase.intervention_get_all import InterventionGetAllUseCase, ToDoSaveRequestObject

app = Flask(__name__)

CONNECTION_STRING = f"{pathlib.Path(__file__).parent.absolute()}\\database.db"


@app.route('/')
def get_all_interventions():
    repo = InterventionDbRepository(CONNECTION_STRING)
    uc = InterventionGetAllUseCase(repo)
    return jsonify(uc.execute())


@app.route("/add", methods=['POST'])
def add():
    try:
        data_task = request.get_json(force=True)
        task_request = ToDoSaveRequestObject(data_task)
        # repo = TodoJsonRepository()
        repo = InterventionDbRepository(CONNECTION_STRING)
        uc = InterventionGetAllUseCase(repo)
        response = uc.execute(task_request.get_todo_task())
        return "{}".format(int(response.return_value)), {"Content-Type": "application/plaintext"}
    except Exception as exc:
        return str(exc), 400, {}


if __name__ == '__main__':
    app.run()
