import re
import scrapetube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dateutil import parser

# https://scrapetube.readthedocs.io/en/latest/

def get_all_video_in_channel(channel_id):
    channel_id = re.sub("https://www.youtube.com/channel/", "", channel_id)
    scraped_videos = scrapetube.get_channel(channel_id)
    processed_videos = []

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    for video in scraped_videos:
        processed_videos.append(format_video_info(video, driver))

    driver.quit()

    for video in processed_videos:
        print(video)

    return processed_videos

def format_video_info(old_video, driver):
    new_video = {
        'video_url': old_video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'],
        'thumbnail': old_video['thumbnail']['thumbnails'][-1]['url'],
        'title': old_video['title']['runs'][0]['text'],
        'published': None
    }

    new_video['published'] = get_video_date_time(new_video['video_url'], driver)

    return new_video

def get_video_date_time(video_url, driver):
    driver.get(f"https://www.youtube.com{video_url}")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span#dot+yt-formatted-string[class$='ytd-video-primary-info-renderer']")))

    date = driver.find_element_by_css_selector("span#dot+yt-formatted-string[class$='ytd-video-primary-info-renderer']")

    return parser.parse(date.text, fuzzy=True)

def get_channel_name_from_url(channel_url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"{channel_url}")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string")))

    date = driver.find_element_by_xpath(
            "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string")

    return_thing = date.text

    driver.quit()

    return return_thing
