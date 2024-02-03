import psycopg2

db_host= '127.0.0.1'
db_user = 'postgres'
db_password = 'Hjcnjd11'
db_database = 'Test'

connection = psycopg2.connect(host=db_host,user=db_user,password=db_password,dbname=db_database)

connection.autocommit=True

with connection.cursor() as cursor:
    cursor.execute("insert into qwerty(first_name,last_name,year) values('Ivan+','Petrov+',45),('I+','P+',55)")
    # print(cursor.fetchall())
    # results = cursor.fetchall()
    #
    # for result in results:
    #     print(result)