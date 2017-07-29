from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import os


def downloader(driver):
    arr = ["간장 파스타","알리오올리오","차돌박이 파스타"]

    for x in arr:
        driver.get("https://www.google.co.kr/search?site=&tbm=isch&q="+x)
        driver.implicitly_wait(3)
        menu = str(x)
        os.makedirs(menu)

        for i in range(1,101):
            img = driver.find_element_by_xpath('//*[@id="rg_s"]/div['+ str(i) +']/a/img')
            img_src = img.get_attribute("src")
            
            try:
                path = os.path.dirname(os.path.abspath(__file__))
                urllib.request.urlretrieve(img_src, path + "/" + menu +"/"+ menu + str(i) + ".jpg")
            except:
                continue
        
if __name__ == "__main__":
  driver = webdriver.Chrome()
  downloader(driver)
  driver.quit()
