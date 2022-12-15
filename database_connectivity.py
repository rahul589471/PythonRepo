import cx_Oracle

try:
    # create connection
    # conn = cx_Oracle.connect('SYS/Oracle@localhost:1521/orcl')
    conn = cx_Oracle.connect('SYS', 'Oracle', 'localhost:1521/orcl', cx_Oracle.SYSDBA)

    # create a cursor
    cursor = conn.cursor()

    # create a table
    sql_create_table = """
    declare
    nCount NUMBER;
    v_sql LONG;
    begin
    SELECT count(*) into nCount FROM dba_tables where lower(table_name) = 'rahul_test';
    IF(nCount <= 0)
    THEN
    v_sql:='
    CREATE TABLE rahul_test(a number, b varchar2(250), c number)';
    execute immediate v_sql;
    END IF;
    end;
    """
    cursor.execute(sql_create_table)
    print("Table created")

#Delete record
    delete_query= """   DELETE FROM rahul_test"""
    cursor.execute(delete_query)
#Inserting records
    insert_statement = """
    INSERT INTO rahul_test values(:1,:2,:3)"""
    # cursor.execute(insert_statement,[1,'Rahul',10])
    # cursor.execute(insert_statement,[2,'Mittal',20])
    # cursor.execute(insert_statement,[3,'Abc',30])
    data =[ (5,'Rahul',10),(6,'Mittal',20),(7,'Abc',30)]
    cursor.executemany(insert_statement,data)
    print("Rows inserted")

    #Fetch Records
    select_query ="""select * from rahul_test """

    cursor.execute(select_query)
    row =cursor.fetchall()  # it will return a list of tuples
    
    for index,record in enumerate(row):
        print("index is ", index, "Record is", record)


except Exception as e:
    print("Error while creating the connection")
    print(e)
else:
    print(conn.version)
    conn.commit()
finally:
    cursor.close()
    conn.close()
