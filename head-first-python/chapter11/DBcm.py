import pymysql


class ConnectionError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = pymysql.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except pymysql.OperationalError as err:
            raise ConnectionError(err)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is pymysql.OperationalError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)