#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import digits
from PIL import Image,ImageOps
import time

def scrapeClimbs(angle,minAscents,minGrade,maxGrade):
    #angle = multiple of 5 between 0 and 70
    #minAscents >=1
    #minGrade <= maxGrade 4a/V0 = 10, 4b/V0 = 11,..., 7c/V9 = 26, 7c+/V10 = 27
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get(f"https://climbdex.fly.dev/results?name=&angle={angle}&minAscents={minAscents}&minGrade={minGrade}&maxGrade={maxGrade}&sortBy=ascents&sortOrder=desc&minRating=1.0&gradeAccuracy=1&settername=&holds=&mirroredHolds=&board=kilter&layout=1&size=7&set=1&set=20&roleMatch=strict")
    time.sleep(3)

    try:
        climb_results = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"header-results-count")))
        num_climbs = int(''.join(c for c in climb_results.text if c in digits))
        first_climb_button = WebDriverWait(driver,10.).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#div-results-list > button:nth-child(1)")))
        first_climb_button.click()
        climb_count = 1

        for i in range(num_climbs):
            climb_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"header-climb-name")))
            climb_stats = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"paragraph-climb-stats")))
            climb_grade = climb_stats.text.split()[0]
            climb_fontgrade = climb_grade.split('/')[0]
            climb_vgrade = climb_grade.split('/')[1]
            try:
                driver.find_element(By.ID,"paragraph-climb-description")
                climb_description = driver.find_element(By.ID,"paragraph-climb-description")
                outlier = False
                if 'none' not in climb_description.get_attribute('class'):
                    climb_text = climb_description.text.lower()
                    if "match" in climb_text or "campus" in climb_text:
                        outlier = True
                if not outlier:
                    climb_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#svg-climb")))
                    climb_box.screenshot(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                    with Image.open(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png') as im:
                        width,height = im.size
                        im_cropped = im.crop(((0, 158, width, height)))
                        im_cropped.save(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                        im_resized = im_cropped.resize((258, 283), Image.ANTIALIAS)
                        im_resized.save(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png',quality=95)
                if outlier:
                    climb_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#svg-climb")))
                    climb_box.screenshot(rf'{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                    with Image.open(rf'{climb_fontgrade}-{climb_vgrade}-{climb_count}.png') as im:
                        width,height = im.size
                        im_cropped = im.crop(((0, 158, width, height)))
                        im_cropped.save(rf'{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                        im_resized = im_cropped.resize((258, 283), Image.ANTIALIAS)
                        im_resized.save(rf'{climb_fontgrade}-{climb_vgrade}-{climb_count}.png',quality=95)
                climb_count+=1
                right_arrow = WebDriverWait(driver,10.).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#button-next")))
                right_arrow.click()
                time.sleep(2)
                
            except:
                climb_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#svg-climb")))
                climb_box.screenshot(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                with Image.open(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png') as im:
                    width,height = im.size
                    im_cropped = im.crop(((0, 158, width, height)))
                    im_cropped.save(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png')
                    im_resized = im_cropped.resize((258, 283), Image.ANTIALIAS)
                    im_resized.save(rf'{climb_vgrade}/{climb_fontgrade}-{climb_vgrade}-{climb_count}.png',quality=95)
                climb_count+=1
                right_arrow = WebDriverWait(driver,10.).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#button-next")))
                right_arrow.click()
                time.sleep(2)
                
                
    except:
            driver.quit()
    driver.quit() 
    

