from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import webbrowser as web
import time
import random
import gonderilecekMesaj
import pywhatkit
import csv
import pyautogui as pg
import core

pg.FAILSAFE = False

users = []

def start():
    i = 0
    with open(r"bahisRadar.csv", encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows,None)
        for row in rows:
            user = {}
            user['telefon'] = row[0]
            users.append(user)


        for user in users:
            phone_no = user['telefon']
            if i == 0:
                web.open(f'https://web.whatsapp.com/send?phone={phone_no}&text={gonderilecekMesaj.message}')
                time.sleep(10)
                pg.click(button='left',clicks=1,x=916,y=588)

                i = i + 1
                print(f"{phone_no} numaralı kişiye mesaj yollandı. Toplam gönderim adedi: {i}\n")
            else:
                web.open(f'https://web.whatsapp.com/send?phone={phone_no}&text={gonderilecekMesaj.message}')
                time.sleep(9)
                pg.click(button='left',clicks=1,x=916,y=588)
                time.sleep(1)
                pg.click(button='left',clicks=1,x=230,y=26)
                pg.press("enter")
                i = i + 1
                print(f"{phone_no} numaralı kişiye mesaj yollandı. Toplam gönderim adedi: {i}\n")

start()
print("Liste başarıyla bitirildi.")

