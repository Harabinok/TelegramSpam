import os
import webbrowser
import pyautogui as pag
from  time import  sleep
import pyperclip
import json
from pprint import pprint

default_size = [1920, 1080];
size = [pag.size().width, pag.size().height]

width = default_size[0] / size[0]
height = default_size[1] / size[1]

telegram_string = [700,992]
telegram_button_send = [1299,992]
telegram_button_members = [1545,1028]
telegram_button_search = [159,135]
telegram_button_element_in_search = [155,280]
telegram_button_url = [278,50]

json_settings = "None"
json_settings_button = "None"

json_data = "None"
json_Name_group = "None"
json_SMS = "None"

test = "https://web.telegram.org/k/#@chanterelle_08".split('#')

id = test[1]

print(id)

with open('Settings.json', 'r', encoding= 'utf-8') as f:
    text = json.load(f)
    json_settings = text['Settings']


for settings in json_settings:
    json_settings_button = settings['Button']
    for button in json_settings_button:
        telegram_string = button['telegram_string']
        telegram_button_send = button['telegram_button_send']
        telegram_button_members = button['telegram_button_members']
        telegram_button_search = button['telegram_button_search']
        telegram_button_element_in_search = button['telegram_button_element_in_search']
        telegram_button_url = button['telegram_button_url']

with open('Data.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    json_data = text['Data']


for data in json_data:
    json_Name_group = data['Name_group']
    json_SMS = data['SMS']


def main():
    os.startfile("C:/Users/Александр/AppData/Local/Programs/Opera GX/launcher.exe")
    sleep(5)
    webbrowser.open_new("https://web.telegram.org/k/#@Omsk_help")
    sleep(3)
    add_user_in_data_base()
    pass

def add_user_in_data_base():
    pag.click(telegram_button_url)
    pag.hotkey('Ctrl','c')
    with open("Data.json",'r', encoding= "utf-8") as file:
        data_json = json.load(file)
        data = data_json['Data']
        add_id_for_send_SMS = "None"
        for add_data_base in json_data:
            add_id_for_send_SMS = add_data_base['add_id_for_send_SMS']
            add_data_base['add_id_for_send_SMS'].append('https://web.telegram.org/k/#@Omsk_help')
        with open('Data.json', encoding= 'utf-8') as outfile:
            json.dump(data_json, outfile, ensure_ascii=False, indent=2)

    pass

def send_sms():
    pag.click(telegram_string[0],telegram_string[1])
    pag.hotkey('ctrl', 'v')
    pag.click(telegram_button_send[0],telegram_button_send[1])
    pass
def copy_in_pyperclip_name_group():

    pyperclip.copy(json_SMS)
    pass

def settings():
    print("add offset for button_members")
if __name__ == "__main__":
    add_user_in_data_base()