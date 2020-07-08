import psycopg2
from psycopg2 import sql

def get_sec(time_str): # turns the time of the video into seconds
    """Get Seconds from time."""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)


def title_keys_clean(titulo): # turns the title of the video to a splited list
    titleKeys = titulo.lower()
    titleKeys = titleKeys.split()
    return titleKeys


def dbInsert(ds, columns_names, columns_values): #It querys an insert to Database
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

    cur = con.cursor()
    columns = ', '.join(columns_names)    # Where column names is a tuple or list of all the column headings you want in your query.
    query = """ INSERT INTO %s (%s) VALUES %%s; """ % (ds, columns)
    params = [columns_values]
    cur.execute(query, params)
    con.commit()
    con.close()


def ds_name(nameYoutubeChannel): # changes the name of the channel to data sheet name standard
    dsChannel = nameYoutubeChannel.split()
    ds = ""
    for i in dsChannel:
        ds = (ds + i + "_")
    ds = ds[:-1]
    return ds


def channel_search_name(nameYoutubeChannel):
    nameSplit = nameYoutubeChannel.split()
    print(nameSplit)
    name = ''
    for i in nameSplit:
        name = (name + i + "+")
    name = name[:-1]
    return name


