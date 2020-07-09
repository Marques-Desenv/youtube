from bs4 import BeautifulSoup
import requests
#-----------------------------------------------------------------------------------------------------------------------
from clean_data import get_sec
from clean_data import title_keys_clean
from clean_data import dbInsert

#-----------------------------------------------------------------------------------------------------------------------

def beautiful_scrape(href):
    source = requests.get(href).text
    soup = BeautifulSoup(source,'lxml')
    div_s = soup.findAll('div')
    print(div_s)

    channel = div_s[1].find('a',class_="yt-uix-sessionlink spf-link").text.strip()
    title = div_s[1].find('span',class_='watch-title').text.strip()

    # views_ = soup.find("div", attrs={'class': 'watch-view-count'}).text
    # date_ = soup.select('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton:nth-child(2) div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(5) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) div.style-scope.ytd-video-primary-info-renderer:nth-child(2) > yt-formatted-string.style-scope.ytd-video-primary-info-renderer:nth-child(2)').text
    # likes = soup.select('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton:nth-child(2) div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(5) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(3) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-menu-renderer ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-default-active:nth-child(1) > a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer').text
    # deslikes = soup.select('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton:nth-child(2) div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(5) div.style-scope.ytd-watch-flexy ytd-video-primary-info-renderer.style-scope.ytd-watch-flexy div.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-video-primary-info-renderer:nth-child(6) div.style-scope.ytd-video-primary-info-renderer:nth-child(3) div.style-scope.ytd-video-primary-info-renderer:nth-child(1) ytd-menu-renderer.style-scope.ytd-video-primary-info-renderer div.style-scope.ytd-menu-renderer ytd-toggle-button-renderer.style-scope.ytd-menu-renderer.force-icon-button.style-text:nth-child(2) > a.yt-simple-endpoint.style-scope.ytd-toggle-button-renderer').text
    # comments_ = soup.select('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton:nth-child(2) div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy ytd-comments.style-scope.ytd-watch-flexy:nth-child(9) ytd-item-section-renderer.style-scope.ytd-comments:nth-child(2) div.style-scope.ytd-item-section-renderer:nth-child(1) ytd-comments-header-renderer.style-scope.ytd-item-section-renderer div.style-scope.ytd-comments-header-renderer:nth-child(1) h2.style-scope.ytd-comments-header-renderer:nth-child(1) > yt-formatted-string.count-text.style-scope.ytd-comments-header-renderer').text
    # tags = soup.find.has_attr("property='og:video:tag'").text
    # time_duration = soup.select('div.style-scope.ytd-app:nth-child(12) ytd-page-manager.style-scope.ytd-app:nth-child(4) ytd-watch-flexy.style-scope.ytd-page-manager.hide-skeleton:nth-child(2) div.style-scope.ytd-watch-flexy:nth-child(8) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy:nth-child(1) div.style-scope.ytd-watch-flexy div.style-scope.ytd-watch-flexy ytd-player.style-scope.ytd-watch-flexy div.style-scope.ytd-player div.html5-video-player.ytp-transparent.ytp-exp-marker-tooltip.ytp-iv-drawer-enabled.ad-created.ytp-hide-info-bar.paused-mode div.ytp-chrome-bottom:nth-child(32) div.ytp-chrome-controls div.ytp-left-controls div.ytp-time-display.notranslate:nth-child(5) > span.ytp-time-duration').text

    values = [href, channel, title]#, title_keys_clean(title), views_, date_, likes, deslikes, comments_, tags, get_sec(time_duration), img_common_color = '255, 255, 255', img_face = True]
    return values



#TESTANDO
href = "https://www.youtube.com/watch?v=cw0MskC4Izo"
print(beautiful_scrape(href))