from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import os
import sys

# user input
channel = "https://www.twitch.tv/" + input("Enter Twitch Channel: ")
situp_count = int(input("Situp Count: "))
interval_1 = float(input("Delay Range (Start): ") + ".0000")
interval_2 = float(input("Delay Range (End): ") + ".0000")
end_msg = input("Completion Message: ")
interval_3 = float(input("Completion Message Delay Range (Start): ") + ".0000")
interval_4 = float(input("Completion Message Delay Range (End): ") + ".0000")
exit_after = input("Shutdown After? (Y/N): ")
user = input("Username: ")
password = input("Password: ")

# login and load channel
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://help.twitch.tv/s/?language=en_US")
time.sleep(2)
login = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/div[5]/div/div/div/div/a/span")
login.click()
userbox = driver.find_element_by_id("username")
userbox.send_keys(user)
passwordbox = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/div[2]/form/div[2]/input")
passwordbox.send_keys(password)
login_confirm = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/div[2]/form/div[3]/button")
login_confirm.click()
time.sleep(2)
driver.get(channel)
time.sleep(2)


def check():
    try:  # timeout banned
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/section/div/div[4]/div[2]/div[1]/div/div[2]/div/div/textarea")
    except NoSuchElementException:
        driver.quit()
        if exit_after == "y" or exit_after == "Y":
            os.system('shutdown -s')
            sys.exit()
        else:
            sys.exit()


def check2():
    c = 0
    while c == 0:
        try:  # emote only mode
            driver.find_element_by_css_selector('<span class="tw-c-text-alt-2 tw-font-size-6 tw-strong tw-word-break-word">スタンプ限定チャット</span>')
        except NoSuchElementException:
            return


def check3():
    b = 0
    while b == 0:
        try:  # slow mode
            driver.find_element_by_css_selector('<textarea class="tw-block tw-border-radius-medium tw-font-size-6 tw-full-width tw-textarea tw-textarea--no-resize" autocomplete="twitch-chat" maxlength="500" placeholder="メッセージを送信（チャットは現在スローモードです）" rows="1" data-a-target="chat-input" data-test-selector="chat-input" style="padding-right: 3.5rem;"></textarea>')
        except NoSuchElementException:
            return


def lie():
    check()
    check2()
    check3()
    slp = random.uniform(interval_1, interval_2)
    time.sleep(slp)
    searchBar = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/section/div/div[4]/div[2]/div[1]/div/div[2]/div/div/textarea")
    searchBar.click()
    searchBar.send_keys("mizkifSleeper")
    searchBar.send_keys(Keys.ENTER)


i = 0
def sit():
    check()
    check2()
    check3()
    slp = random.uniform(interval_1, interval_2)
    time.sleep(slp)
    global i
    i += 1
    searchBar = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/section/div/div[4]/div[2]/div[1]/div/div[2]/div/div/textarea")
    searchBar.click()
    searchBar.send_keys("mizkifSat " + str(i))
    searchBar.send_keys(Keys.ENTER)


def end():
    check()
    check2()
    check3()
    slp = random.uniform(interval_3, interval_4)
    time.sleep(slp)
    searchBar = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/section/div/div[4]/div[2]/div[1]/div/div[2]/div/div/textarea")
    searchBar.click()
    searchBar.send_keys(end_msg)
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.quit()
    if exit_after == "y" or exit_after == "Y":
        os.system('shutdown -s')
        sys.exit()
    else:
        sys.exit()


a = 0
while a == 0:
    if i == situp_count:
        end()
    else:
        lie()
        sit()
