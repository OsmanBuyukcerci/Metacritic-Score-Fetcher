from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

clear = lambda: os.system('cls')

file = open("C:\\Users\\Osman\\Desktop\\metacritic\\games.txt" , "r")
games = file.read().split('\n')

PATH = "C:\\Users\\Osman\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_position(-10000, 0)
driver.get("https://www.metacritic.com/")

Action = ActionChains(driver)

clear()
print('Oyunlar taranıyor...')
sleep(2)
clear()

for i in range(len(games)):
    try:
        searchBox = driver.find_element(By.ID , "primary_search_box")
        searchBox.send_keys(games[i])
        global type_el
        type_el = driver.find_elements(By.CLASS_NAME , "title")
        sleep(2)
        for i in range(len(type_el)):
            x = i+1
            type = driver.find_element(By.XPATH , '//*[@id="primary_search_results"]/a[%d]/div/span[1]' %(x)).text
            if type == "PC Game":
                type = driver.find_element(By.XPATH , '//*[@id="primary_search_results"]/a[%d]/div/span[1]' %(x))
                break
            else:
                pass
        type.click()
        gameName = driver.find_element(By.XPATH , '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/a/h1').text
        metaScore = driver.find_element(By.XPATH , '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span').text
        userScore = driver.find_element(By.XPATH , '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div').text
        scoreFile = open("C:\\Users\\Osman\\Desktop\\metacritic\\Scores.txt" , "a")
        scoreFile.write('%s:\nMetascore = %s\nUserscore = %s\n'%(gameName, metaScore, userScore))
        print('%s skorları kaydedildi.'%(gameName))
        sleep(2)
    except:
        Action.key_down(Keys.CONTROL).perform()
        searchBox.send_keys('a')
        Action.key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
    finally:
        pass
        
clear()
print('İşlem başarıyla tamamlandı.')


