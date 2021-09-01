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

    if not book_id:
        return func.HttpResponse(
            "Please provide book_id in the URI",
            status_code=400
        ) 
    
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
    cursor.execute("UPDATE book SET book_name = ?, author = ?, genre = ? WHERE book_id= ?", book_id, author, genre, book_id)
    cursor.commit()
    
    return func.HttpResponse(
        "Book updated",
        status_code=200
    )