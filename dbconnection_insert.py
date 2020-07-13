import psycopg2
import clean_data
import beautiful_data
#-----------------------------------------------------------------------------------------------------------------------
from clean_data import get_sec
from clean_data import title_keys_clean
from clean_data import dbInsert
#-----------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------
# columns cotains all editable columns names of the Datasheet.
columns_names = (  'href', 'channel', 'title', 'title_key_words', 'views_', 'date_', 'likes', 'dislikes', 'like_rate', 'comments_', 'tags', 'time_duration',
                   'img_common_color', 'img_face', 'autoplay_href', 'autoplay_channel', 'autoplay_title', 'autoplay_title_key_words', 'autoplay_views',
                   'autoplay_date', 'autoplay_likes', 'autoplay_dislikes', 'autoplay_like_rate','autoplay_comments', 'autoplay_tags', 'autoplay_time_duration',
                   'autoplay_img_common_color', 'autoplay_img_face', 'secondary1_href', 'secondary1_channel', 'secondary1_title',
                   'secondary1_title_key_words', 'secondary1_views', 'secondary1_date', 'secondary1_likes', 'secondary1_dislikes', 'secondary1_like_rate',
                   'secondary1_comments', 'secondary1_tags', 'secondary1_time_duration', 'secondary1_img_common_color', 'secondary1_img_face',
                   'secondary2_href', 'secondary2_channel', 'secondary2_title', 'secondary2_title_key_words', 'secondary2_views', 'secondary2_date',
                   'secondary2_likes', 'secondary2_dislikes', 'secondary2_like_rate','secondary2_comments', 'secondary2_tags', 'secondary2_time_duration',
                   'secondary2_img_common_color', 'secondary2_img_face', 'secondary3_href', 'secondary3_channel', 'secondary3_title',
                   'secondary3_title_key_words', 'secondary3_views', 'secondary3_date', 'secondary3_likes', 'secondary3_dislikes', 'secondary3_like_rate',
                   'secondary3_comments', 'secondary3_tags', 'secondary3_time_duration', 'secondary3_img_common_color', 'secondary3_img_face',)
#-----------------------------------------------------------------------------------------------------------------------
columns_values = [,]
#-----------------------------------------------------------------------------------------------------------------------
nameYoutubeChannel = "shape inexplicavel"
#-----------------------------------------------------------------------------------------------------------------------



dbInsert(clean_data.ds_name(nameYoutubeChannel), columns_names, columns_values)


