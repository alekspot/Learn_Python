# swapy.exe Утилита для упрощения нахождения окон приложений и получения готового кода для pywinauto
from pywinauto import Application 
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select

def vpnOn():
    app = Application().Start(cmd_line=u'"C:\\Program Files\\ShrewSoft\\VPN Client\\ipsecc.exe" -r "VPN.pcf"')
    vpnWindow = app.SHREWSOFT_CON
    vpnWindow.wait('ready')

    usernameInput = vpnWindow.Edit1
    passwordInput = vpnWindow.Edit2
    connectBtn = vpnWindow.Connect
    usernameInput.set_text('apotkin')
    passwordInput.set_text('bzgH8b5SA')
    connectBtn.click()
    time.sleep(4)

#app.Kill_()

def getLink():
    now = datetime.date.today()
    day = now.day
    month = now.month

    dayStr = '0' + str(day) if day < 10 else str(day)
    monthStr = '0' + str(month) if month < 10 else str(month)
    yearStr = str(now.year)

    return f"https://reporter.corp.local/report_new?date={yearStr}-{monthStr}-{dayStr}"


def authReporter():
    link = getLink()
    # Для запуска тестирующего браузера необходим драйвер chromedriver.exe
    browser = webdriver.Chrome(r'C:\Users\aleksandr\Desktop\myPython\utils\chromedriver')

    browser.get("https://reporter.corp.local/login")    # перейти на страницу
    browser.find_element_by_id("details-button").click()     # клик по найденному элементу
    browser.find_element_by_id("proceed-link").click()
    browser.find_element_by_id("username").send_keys("apotkin") # печать в найденный <input>
    browser.find_element_by_id("password").send_keys("bzgH8b5SA")
    browser.find_element_by_id("_submit").click()
    
    browser.get(link)
    select1 = Select(browser.find_element_by_id("projects"))    # ссылаемся на найденный <select>
    select2 = Select(browser.find_element_by_id("task_types"))

    select1.select_by_value("10001937") # Название проекта      # выбираем <option value="10001937">
    select2.select_by_value("30") # Тип задачи

    browser.find_element_by_id("form_minutes").send_keys("8")
    browser.find_element_by_id("form_description").send_keys("Разработка.Написание скриптов.Доработка")
    browser.find_element_by_id("button_submit").click()
  
vpnOn()
authReporter()



