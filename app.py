from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import logging

logging.basicConfig(
    filename='app_log.log',  # Set the log file name
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)



app = Flask(__name__)

# Define a function to initialize the Chrome WebDriver
def initialize_webdriver():
    service = Service('chromedriver.exe')
    # Set Chrome options for headless mode
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('--disable-gpu')  # Disable GPU usage, which can cause issues in headless mode
    options.add_argument('--no-sandbox')  # Disable sandboxing for headless mode (useful in some environments)

    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=service, options=options)

# Define a function to scrape video data
def scrape_video_data(channel_url):
    logging.info('Scraping video data for channel URL: %s', channel_url)

    driver = initialize_webdriver()
    driver.get(channel_url)
    driver.implicitly_wait(1)
    time.sleep(9)

    # Extract video links
    video_links = driver.find_elements(By.ID, 'video-title-link')
    video_links_list = [f" {video_link.get_attribute('href')}" for i, video_link in enumerate(video_links[:5], start=1)]

    # Extract video thumbnails
    thumbnail_elements = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
    video_thumbnail_list = [f" {thumbnail_element.find_element(By.TAG_NAME, 'img').get_attribute('src')}" for i, thumbnail_element in enumerate(thumbnail_elements[:5], start=1)]

    # Extract video titles
    video_titles = driver.find_elements(By.XPATH, './/*[@id="video-title-link"]')
    video_titles_list = [f"{title.get_attribute('title')}" for i, title in enumerate(video_titles[:5], start=1)]

    # Extract video views
    video_views = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-video-meta-block')
    video_views_list = [f"{view.find_element(By.TAG_NAME, 'span').text}" for i, view in enumerate(video_views[:5], start=1)]

    # Extract video timings
    video_timings = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]')
    video_timings_list = []
    for i, video_time in enumerate(video_timings[:5], start=1):
        spans = video_time.find_elements(By.TAG_NAME, 'span')
        time_of_posting = None
        for span in spans:
            text = span.text
            if "ago" in text:
                time_of_posting = text
                break
        video_timings_list.append(f"{time_of_posting}")
        logging.info('Scraping completed for channel URL: %s', channel_url)


    driver.quit()

    return video_titles_list, video_links_list, video_thumbnail_list, video_views_list, video_timings_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    channel_url = request.form.get('channel_url')
    logging.info('Scraping data for channel URL: %s', channel_url)
    video_titles_list, video_links_list, video_thumbnail_list, video_views_list, video_timings_list = scrape_video_data(channel_url)
    logging.info('Scraping completed for channel URL: %s', channel_url)
    # Combine the lists using zip
    data = [
        {
            "title": title,
            "link": link,
            "thumbnail": thumbnail,
            "view_count": view,
            "time_posted": time
        }
        for title, link, thumbnail, view, time in zip(
            video_titles_list, video_links_list, video_thumbnail_list, video_views_list, video_timings_list
        )
    ]

    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
