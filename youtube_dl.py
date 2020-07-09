from youtube_dl import YoutubeDL
from youtube_dl import extractor
#-----------------------------------------------------------------------------------------------------------------------
from clean_data import get_sec
from clean_data import title_keys_clean
from clean_data import dbInsert
#-----------------------------------------------------------------------------------------------------------------------
href = "https://www.youtube.com/watch?v=cw0MskC4Izo"
#-----------------------------------------------------------------------------------------------------------------------
def youtubedl_scrape(href):
    ydl = YoutubeDL()
    content = ydl.extract_info(href, download=False)
    return content

#TESTANDO
print(youtubedl_scrape(href))