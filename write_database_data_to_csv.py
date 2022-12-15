import cx_Oracle
import pandas as pd

try:
    conn =cx_Oracle.connect('SYS','Oracle','localhost:1521/orcl',cx_Oracle.SYSDBA)
    pd_query= pd.read_sql_query("""SELECT * FROM rahul_test""",conn)
    pd_query.to_csv("C:\\Users\Rahul\Downloads\data.csv",index=False)
except Exception as e:
    print("Exception is",e)