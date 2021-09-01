import logging
import json
import pyodbc

import azure.functions as func

server = 'datagrokr.database.windows.net'
driver = '{ODBC Driver 17 for SQL Server}'

database = 'de-intern-apr'
username = "dgadmin"
password = "dingding@ding1"


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    book_id = req.route_params.get('book_id')

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM book WHERE book_id= ?", book_id)
    row = cursor.fetchone()

    book_id = str(row[0])
    book_name = str(row[1])
    author = str(row[2])
    genre = str(row[3])

    json_list = list()
    json_list.append({"book_id": book_id, "book_name": book_name, "author": author, "genre": genre})

    response = json.dumps(json_list)

    return func.HttpResponse(response)