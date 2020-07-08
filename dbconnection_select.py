import psycopg2

def dbSelect(db, ds):
    # connect to the db
    try:
        con = psycopg2.connect( host = "localhost",
                                database = "youtubedb",
                                user = "postgres",
                                password = "metralha",
                                port = "5432")

            print("Database connected successfully.")
    except:
        print("Database not connected")
    #
    # # cursor
    # cur = con.cursor()
    # cur.execute("select id, name from employees")
    # row = cur.fetchall()
    #
    # # close the connection
    con.close()







