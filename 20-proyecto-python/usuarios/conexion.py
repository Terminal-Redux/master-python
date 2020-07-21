import mysql.connector

def conectar():
    database = mysql.connector.connect(
    host = "localhost",
    port = "8889",
    user = "root",
    passwd = "root",
    database = "master_python"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]