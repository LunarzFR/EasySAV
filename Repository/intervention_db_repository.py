import json
import sqlite3

from Domain.intervention import Intervention
from Domain.list_intervention import ListIntervention
from Repository.intervention_repository import InterventionRepository


class InterventionDbRepository(InterventionRepository):
    def __init__(self, connection_string):
        self.__conn = sqlite3.connect(connection_string)
        self.__cursor = self.__conn.cursor()

    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def create_table(self, sqlCmd):
        self.__execute_commande(sqlCmd)
        return True

    def __execute_commande(self, sqlCommand):
        self.__cursor.execute(sqlCommand)

    def __commit(self):
        self.__conn.commit()

    def save(self, intervention):
        insert_cmd = f"INSERT INTO intervention(client, description) VALUES('{intervention.client}', '{intervention.description}') "
        self.__execute_commande(insert_cmd)
        self.__commit()
        return "True"

    def get_all(self):
        select_cmd = f"SELECT * FROM intervention"
        list_interventions = ListIntervention()
        for row in self.cursor.execute(select_cmd):
            intervention = Intervention(row[0], row[1], row[2])
            list_interventions.add_intervention(intervention.to_dict())

        return list_interventions.interventions
