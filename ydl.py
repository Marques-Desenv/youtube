from youtube_dl import YoutubeDL

#-----------------------------------------------------------------------------------------------------------------------
# from clean_data import get_sec
from clean_data import keys_clean
# from clean_data import dbInsert
from image_recognition import look_thumb_img, look_for_faces
#-----------------------------------------------------------------------------------------------------------------------
href = "https://www.youtube.com/watch?v=4yOBjknMb-I"
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
    dislikes = content['dislike_count']
    like_rate = content['average_rating']

    try:
        comments_ = content['comment_count']
    except:
        comments_ = 0

    tags = content['tags']
    time_duration = content['duration']
    img_link = content['thumbnails']
    img_common_color = img_link
    img_face = img_link
    categories = content['categories']
    description = content['description']
    description_keys_words = keys_clean(description)

    values = [href, channel, title, title_key_words, views_, date_, likes, dislikes, like_rate, comments_, tags, time_duration,
             look_thumb_img(img_common_color[-1]), look_for_faces(img_face[-1]), categories, description, description_keys_words]

    return values

#TESTANDO
print(youtubedl_scrape(href))