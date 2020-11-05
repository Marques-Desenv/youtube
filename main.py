import WebOperator
import clean_data
from ydl import youtubedl_scrape
import dbconnection_insert
#-----------------------------------------------------------------------------------------------------------------------
nameYoutubeChannel = "rayra fortunato"
nameDBTable = 'shape test'
#-----------------------------------------------------------------------------------------------------------------------
columns_names = ('href', 'channel', 'title', 'title_key_words', 'views_', 'date_', 'likes', 'dislikes', 'like_rate', 'comments_', 'tags', 'time_duration', 'img_common_color', 'img_face', 'categories', 'description', 'description_keys_words')
#-----------------------------------------------------------------------------------------------------------------------
WebOperator.open_url_video(nameYoutubeChannel)
WebOperator.scroll_down()
links = WebOperator.collectLinks()

for i in links:
    columnsValues = youtubedl_scrape(links[i])

    dbconnection_insert.dbInsert(clean_data.ds_name(nameDBTable), columns_names, columnsValues)