import logging
import pyodbc

import azure.functions as func

server = 'datagrokr.database.windows.net'
driver = '{ODBC Driver 17 for SQL Server}'

database = 'de-intern-apr'
username = "dgadmin"
password = "dingding@ding1"

def main(req: func.HttpRequest) -> func.HttpResponse:

    book_id = req.route_params.get('id')
    if not book_id:
        return func.HttpResponse(
            "Please provide book_id in the URI",
            status_code=400
        )

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM book WHERE book_id= ?", book_id)
    cursor.commit()
    
    return func.HttpResponse(
        "Book deleted",
        status_code=200
    )