import psycopg2
from psycopg2 import sql

#---------------------------------------------------------------------------
from clean_data import get_sec
from clean_data import title_keys_clean
from clean_data import dbInsert

#============================================================================

# tags = ['sou brabo', 'é um teste', 'vamos ver se dar certo']
# titulo = title_keys_clean("Vamos ver se isso vai dar certo")
# tempo = get_sec("8:46")
#
# # columns cotains all editable columns names of the Datasheet.
# columns_names = ('href', 'channel', 'title', 'title_key_words', 'views_', 'date_', 'likes', 'deslikes', 'comments_', 'tags', 'time_duration', 'img_common_color', 'img_face')
# columns_value = ('http://www.google.com', 'shape_test', titulo, titulo, 1933444, '21/03/2020 ', 2345, 123, 130, tags, tempo, '10, 10, 255', True)
#
# dbInsert('shape_test', columns_names, columns_value)


