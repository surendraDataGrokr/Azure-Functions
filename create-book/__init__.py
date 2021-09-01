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

    try:
        request_json = req.get_json()
        book_name = request_json.get('book_name')
        author = request_json.get('author')
        genre = request_json.get('genre')
    except:
        return func.HttpResponse(
            "Please put a valid JSON in the request",
            status_code=400
        )

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO book VALUES (?, ?, ?)", book_name, author, genre)
    cursor.commit()
    
    return func.HttpResponse(
        "Book added",
        status_code=201
    )