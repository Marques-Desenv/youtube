from selenium import webdriver
from clean_data import channel_search_name
import time
driver = ""
#----------------------------------------------------------------------------------------------------------------------


def open_url_video(nameYoutubeChannel):
    global driver

    driver = webdriver.Chrome(r"C:\Users\marqu\Documents\Coding\Youtube\Files\chromedriver.exe")
    driver.maximize_window()  # Maximiza a tela do navegador
    driver.get(r"https://www.youtube.com/results?search_query=%s" %(channel_search_name(nameYoutubeChannel)))  # get the driver to the url search page on youtube
    driver.find_element_by_xpath("//div[@id='avatar']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//paper-tab[2]//div[1]").click()
    driver.implicitly_wait(2)  # espera itens aparecerem na tela por tempo determinado em segundos

def scroll_down():
    global driver

    # driver = webdriver.Chrome(r"C:\Users\marqu\Documents\Coding\Youtube\Files\chromedriver.exe")
    # driver.maximize_window()  # Maximiza a tela do navegador
    # driver.get(r"https://www.youtube.com/results?search_query=")  # entra no site especificado
    # driver.implicitly_wait(2)  # espera itens aparecerem na tela por tempo determinado em segundos

    # # This "While" scrolls down the channel video list till the botton.
    # while True:
    #     hrefs = driver.find_elements_by_css_selector('#thumbnail')
    #
    #     driver.execute_script("window.scrollBy(0,document.body.scrollHeight || document.documentElement.scrollHeight)", "")
    #     time.sleep(2)
    #     last_hrefs = driver.find_elements_by_css_selector('#thumbnail')
    #
    #     print(len(hrefs))
    #     print(len(last_hrefs))
    #
    #     if len(hrefs) == len(last_hrefs):
    #         break

    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(height)
    while True:
        driver.execute_script("window.scrollTo(0, " + str(height) + ");")
        time.sleep(2)
        newHeight = driver.execute_script("return document.documentElement.scrollHeight")
        print(newHeight)
        if newHeight == height:
            break
        height = newHeight


    print('Collecting links')
    links = driver.find_elements_by_xpath('//*[@id="video-title"]')
    href = []

    for link in links:
        href.append(link.get_attribute("href"))

    print(href)

    # hrefs = []
    # href = driver.find_elements_by_xpath("//a[@href]")
    # for href in hrefs:
    #     hrefs.append(str(href.get_attribute('href')))
    # return print(hrefs)

def collectLinks():
    global driver

    print('Collecting links')
    hrefs = []
    href = driver.find_elements_by_xpath("//a[@href]")
    for href in hrefs:
        hrefs.append(str(href.get_attribute("href")))
    driver.quit()
    return hrefs



nameYoutubeChannel = "rayra fortunato"

open_url_video(nameYoutubeChannel)
scroll_down()
collectLinks()


