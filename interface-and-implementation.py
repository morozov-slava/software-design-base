
from abc import ABC, abstractmethod
from dataclasses import dataclass

import oracledb


class Storage(ABC):

	@abstractmethod
	def save(data: str) -> None:
		raise NotImplementedError("Method must be implemented in child class")

	@abstractmethod
	def retrieve(id: int) -> str:
		raise NotImplementedError("Method must be implemented in child class")


@dataclass
class OracleConfigDTO:
    username: str
    password: str
    dsn: str


class OracleDatabaseStorage(Storage):
    def __init__(self, tablename: str, config: OracleConfigDTO):
	    self.tablename = tablename
        self.connection = oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn
        )
        self.cursor = self.connection.cursor()
        
    def save(self, data: str) -> None:
        self.cursor.execute(f"INSERT INTO {self.tablename} VALUES ({data})")
        self.connection.commit()

    def retrieve(self, id: int) -> str:
        self.cursor.execute(f"SELECT data FROM {self.tablename} WHERE id = {id}")
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            raise ValueError(f"No data found for ID {id}")

    def close(self):
        self.cursor.close()
        self.connection.close()


def main():
	# Variables
	database_configs = OracleConfigDTO(
		username="admin",
		password="Qwerty12345",
		dsn="localhost:1521/ORACLE_DATABASE"
	)
	tablename = "TestTable"

	# Storage operations
	storage = OracleDatabaseStorage(config, tablename)
	storage.save("Пользователь-4356")
	data = storage.retrieve(1)
	storage.close()
