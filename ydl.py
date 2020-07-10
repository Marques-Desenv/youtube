from youtube_dl import YoutubeDL

#-----------------------------------------------------------------------------------------------------------------------
# from clean_data import get_sec
from clean_data import keys_clean
# from clean_data import dbInsert
#-----------------------------------------------------------------------------------------------------------------------
href = "https://www.youtube.com/watch?v=cw0MskC4Izo"
#-----------------------------------------------------------------------------------------------------------------------
def youtubedl_scrape(href):
    ydl = YoutubeDL()
    content = ydl.extract_info(href, download=False)

    channel = content['uploader']
    title = content['title']
    title_key_words = keys_clean(title)
    views_ = content['view_count']
    date_ = content['upload_date']
    likes = content['like_count']
    deslikes = content['dislike_count']
    comments_ = content['comment_count']
    tags = content['tags']
    time_duration = content['duration']
    img_common_color = '255,255,255'
    img_face = True
    categories = content['categories']
    description = content['description']
    description_keys_words = keys_clean(description)

    values = [href, channel, title, title_key_words, views_, date_, likes, deslikes, comments_, tags, time_duration,
              img_common_color, img_face, description, description_keys_words]

    return values

#TESTANDO
print(youtubedl_scrape(href))