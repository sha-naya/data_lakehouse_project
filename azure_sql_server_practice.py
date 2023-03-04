import pyodbc 
conn = pyodbc.connect(
    'DRIVER={Devart ODBC Driver for SQLAzure};Server=tcp:cs779-server.database.windows.net,1433;Database=cs779;Uid=epoch;Pwd=**********;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    )
cursor = conn.cursor()
cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
