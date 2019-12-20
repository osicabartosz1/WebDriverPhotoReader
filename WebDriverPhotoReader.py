import os
import time
import urllib.request
from selenium import webdriver

def createPath(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

def getTimeStamp():
    now = time.time()
    name = str(now).replace("/", "").replace(".", "").replace(":", "")

    return str(name)

print("Creation of ChromeOptions")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--block-new-web-contents")
#--disable-popup-blocking
#--suppress-message-center-popups
print("Creation of ChromeDriver")
browser = webdriver.Chrome(executable_path=r"C:\Users\Bartek\Documents\ChromeWebDrive\79\chromedriver.exe", chrome_options=chrome_options)

print("Get Desktop path")
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

print("Get Desktop path and currentPath")
currentPath = os.getcwd()

print("Create a folder")
desctinationFolderName = desktop + "\\" + getTimeStamp() + "\\"
createPath(desctinationFolderName)

for pageNumber in range(10):
    browser.get('https://faktopedia.pl/page/' + str(pageNumber+1))

    try:
        submit_button = browser.find_elements_by_xpath("//*/span[text()='OK, przejdź do strony' ]")[0]
        submit_button.click()
    except:
        print("optional " + str(pageNumber) )

    print("Find all photos page = " + str(pageNumber))
    try:
        image_table = browser.find_elements_by_xpath("//*/img[@class='pic']")
        for image in image_table:
            #time.sleep(2)
            src = image.get_attribute('src')
            name = str(src).replace("/", "").replace(".", "").replace(":", "").replace("?","")
            name = getTimeStamp() + name
            urllib.request.urlretrieve(src, desctinationFolderName + name + ".png")
    except:
        print("error")

browser.close()