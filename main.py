import WebOperator
import clean_data
import beautiful_data
import dbconnection_insert
#-----------------------------------------------------------------------------------------------------------------------
nameYoutubeChannel = ""
#-----------------------------------------------------------------------------------------------------------------------
WebOperator.open_url_video(nameYoutubeChannel)
WebOperator.scroll_down()
links = WebOperator.collectLinks()

for i in links:
    columnsValues = beautiful_data.beautiful_scrape(links[i])

    dbconnection_insert.dbInsert(clean_data.ds_name(nameYoutubeChannel), columns_names, columnsValues)