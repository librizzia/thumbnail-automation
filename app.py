#!/usr/bin/python3

from email.mime import image
from glob import glob
import requests
import io
import time
import os
import glob
import shutil
from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image, ImageFont, ImageDraw

SCREENSHOT = './PAUSED_VIDEO.png'
EXISTING_THUMBNAIL = './OLD_THUMBNAIL.png'
NEW_THUMBNAIL = './destination/NEW_THUMBNAIL.png'
TITLE_FONT_FILE = './fonts/Maximum Impact.ttf'
DATE_FONT_FILE = './fonts/BebasNeue-Regular.ttf'
THUMBNAIL_OUTPUT = "./THUMBNAIL.png"

# Image Directories
# existing_thumbnail_image_path = '/home/anthony/Code/thumbnail-automation/img'
# INITLAIZE TITLE VARIABLES
# sermon_title = None
# sermon_date = None
# church = None

# # LINKS
# youtube_screenshot_site = 'https://www.youtubescreenshot.com/'
# youtube_metadata_site = 'https://mattw.io/youtube-metadata/'
# # Chrome Options
# chrome_options = ChromeOptions()
# chrome_options.add_argument('user-agent=fake-useragent')
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_extension('ublock_origin_extension.crx')
# chrome_options.add_extension('extensions/automatic_max_quality.crx')

# driver = webdriver.Chrome('./chromedriver', options=chrome_options)

# # Setup Webdriver
# driver.implicitly_wait(3)

# youtube_link = input('Enter YouTube Link: ')


def menu():
    print("Would you like to:")
    print("[1] Use the existing thumbnail?")
    print("[2] Create a new thumbnail?")
    print("[0] Quit")


def moveMostRecentDownload():
    # get list of files that matches pattern
    destination = "/home/anthony/Code/scripts/thumbnail-python/destination"
    pattern = "/home/anthony/Downloads/*"
    files = list(filter(os.path.isfile, glob.glob(pattern)))

    # sort by modified time
    files.sort(key=lambda x: os.path.getmtime(x))

    # get last item in list
    lastfile = files[-1]

    # print("Most recent file matching {}: {}".format(pattern, lastfile))
    # print("Most recent file is : " + lastfile)

    shutil.copy2(
        lastfile, destination)

    os.chdir(destination)
    for file in os.listdir():
        # print(file)
        new_name = "NEW_THUMBNAIL.png"
        os.rename(file, new_name)


def printTitle():
    driver.get(youtube_link)

    driver.implicitly_wait(2)

    videoTitle = driver.find_element(
        By.XPATH, '//*[@id="container"]/h1/yt-formatted-string')
    scrapped_title = videoTitle.text

    # Printing the title of this URL
    print("The YouTube title is " + scrapped_title), "\n"
    time.sleep(1)
    driver.quit


def getTitle():
    driver.get(youtube_metadata_site)
    driver.find_element(By.ID, "value").send_keys(youtube_link)
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    video_title = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div[1]/pre/code/span[12]')
    replaced_text = video_title.text
    youtube_video_title = replaced_text.replace('"', '')

    print("The YouTube title is " + youtube_video_title), "\n"
    title_array = youtube_video_title.split(" - ")

    global sermon_title
    global sermon_date
    global church

    sermon_title = title_array[0]
    sermon_date = title_array[1]
    church = title_array[2]

    print("Sermon is " + sermon_title)
    print("Date is " + sermon_date)
    print("Church is " + church)

    print(youtube_video_title)
    driver.quit

    return sermon_title, sermon_date, church


def downloadImage(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name

    with open(file_path, "wb") as f:
        image.save(f, "JPEG")


def makeTempFolder():
    Path("tmp").mkdir(exist_ok=True)


def makeOutputFolder():
    Path("output").mkdir(exist_ok=True)


def changeResolution(thumbnail):
    size = 1920, 1080
    im = Image.open(thumbnail)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("./tmp/THUMBNAIL_1080p.png", "PNG")
    print("Resolution of thumbnail changed")


def trim():
    # Trim new thumbnail
    img = Image.open('./tmp/THUMBNAIL_1080p.png')

    (left, upper, right, lower) = (0, 0, 1540, 1080)
    cropped_image = img.crop((left, upper, right, lower))

    base_image = Image.open('./assets/base_image.png').convert("RGBA")
    cropped_image.save('./tmp/cropped_image.png')

    new_cropped_image_image = Image.open(
        './tmp/cropped_image.png').convert("RGBA")
    base_image.paste(new_cropped_image_image,
                     (380, 0), new_cropped_image_image)
    base_image.save('./tmp/TEST_IMAGE.png')
    print("Image cropped")


def overlayGradient():
    pass


def addTitles():
    # Set photo variables
    SCREENSHOT = 'TEST_IMAGE.png'
    GRADIENT = 'gradient.png'
    THUMBNAIL = './output/base_thumbnail.png'

    # getTitle

    # Image that goes on top
    img = Image.open("./assets/gradient.png").convert("RGBA")

    # Image on bottom
    background = Image.open("./tmp/TEST_IMAGE.png").convert("RGB")

    # Overlays image
    new_image = background.paste(img, (0, 0), img)

    # Font selection from the downloaded file
    # TITLE_FONT_FILE = './fonts/Maximum Impact.ttf'
    # DATE_FONT_FILE = './fonts/BebasNeue-Regular.ttf'
    # image = Image.open(SCREENSHOT)

    # Add Titlesthumbnail
    # Decide the text location, color and font
    # date_font = ImageFont.truetype(DATE_FONT_FILE, 100)
    # drawing = ImageDraw.Draw(background)
    # drawing.text((90, 918), sermon_date, font=date_font, fill="#FFFFFF")

    # Main Title
    # title_font = ImageFont.truetype(TITLE_FONT_FILE, 140)
    # drawing.text((196, 192), sermon_title, font=title_font, fill="#FFFFFF")

    # Save
    background.save(THUMBNAIL)
    # background.show()
    # print("Thumbnail created")
    # time.sleep(2)

    pass


def captureNewThumbnail():
    # Add timestamp
    # timestamp = '&t=59m55s'thumbnail

    # Play video
    youtube_video = driver.find_element(By.ID, 'movie_player')
    time.sleep(6)
    youtube_video.screenshot(NEW_THUMBNAIL)
    # driver.execute_script('youtube_sceengrab.js')
    time.sleep(1)
    youtube_video.click()  # mouse clickbackground.save(THUMBNAIL)
    time.sleep(2)
    driver.quit

    # makeThumbnail(NEW_THUMBNAIL)


def existingThumbnail():
    watchCode = youtube_link.replace('https://www.youtube.com/', '')
    print("Watch Code is " + watchCode)

    screenshot_site_with_watch_code = youtube_screenshot_site + watchCode
    driver.get(screenshot_site_with_watch_code)

    image_url = driver.find_element(By.ID, "mainshot").get_attribute("src")
    driver.get(image_url)
    downloadImage("", image_url, EXISTING_THUMBNAIL)
    print("Previous thumbnail captured")
    driver.quit

    makeThumbnail(EXISTING_THUMBNAIL)


def makeThumbnail(thumbnail):
    # getTitle()
    makeTempFolder()
    makeOutputFolder()
    changeResolution(thumbnail)
    trim()
    addTitles()
    print("Thumbnail created!")
    pass


# makeThumbnail(NEW_THUMBNAIL)


def moveThumbnail():
    # get list of files that matches pattern
    destination = "/home/anthony/Code/scripts/thumbnail-python/destination"
    pattern = "/home/anthony/Code/scripts/thumbnail-python/output/*"
    files = list(filter(os.path.isfile, glob.glob(pattern)))

    # sort by modified time
    files.sort(key=lambda x: os.path.getmtime(x))

    # get last item in list
    lastfile = files[-1]

    # print("Most recent file matching {}: {}".format(pattern, lastfile))
    # print("Most recent file is : " + lastfile)

    shutil.copy2(
        lastfile, destination)

    os.chdir(destination)
    for file in os.listdir():
        # print(file)
        new_name = "NEW_THUMBNAIL.png"
        os.rename(file, new_name)


# moveMostRecentDownload()
# time.sleep(6)
makeThumbnail(NEW_THUMBNAIL)
moveThumbnail()
