from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import json
from datetime import datetime
import time
import random
import csv
import openpyxl
import os

def get_browser(directory):
    path = r"" + directory
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # If running on a server

    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    
    return driver
def update_excel(data, file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        # Create the file and add the column names
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(list(data.keys()))
        wb.save(file_path)
    else:
        # Load the excel file
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active
    ws.append(list(data.values()))
    wb.save(file_path)
    
def login(browser):
    browser.get('https://www.fxiaoke.com/pc-login/build/login.html?lang=en')
    time.sleep(random.uniform(2,3))
    print('Opened fxiaoke')
    # click span with Account text
    browser.find_element(By.XPATH, '//span[text()="Account"]').click()
    time.sleep(random.uniform(1,2))
    print('Clicked Account')
    # click email account login
    browser.find_element(By.XPATH, '//span[text()="Email Account Login"]').click()
    time.sleep(random.uniform(1,2))
    print('Clicked Email Account Login')
    # send email
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Please enter email account"]').send_keys('xavier.speropoulos@osvaporesso.com')
    time.sleep(random.uniform(1,2))
    print('Sent email')
    # send password
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Please enter the password."]').send_keys('apv123456')
    time.sleep(random.uniform(1,2))
    print('Sent password')
    # click login
    browser.find_element(By.CSS_SELECTOR, 'div.fssdk-email-login').click()
    print('Clicked login')
    time.sleep(random.uniform(5,10))
    print('Logged in')

def get_visit_info(cookies, fs_token):
    main_data = []
    headers = {
    'authority': 'hws.fxiaoke.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en,zh-CN;0.9,zh-TW;0.8',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'guid=fcfceb69-ad11-997e-aab5-2188566dbb6a; mirrorId=0000; originRefer=www.fxiaoke.com; EPXId=3cde6622df6c4dd4b5b80c6838f3fcc7; LoginId=LOGIN_ID_428aacec-c6c6-4568-b93c-dd78252ebf33; fs_token=Dp1YPMCmOJWjOZOmDIqqCZ4pBJWqE30jP6Cs>
    'origin': 'https://hws.fxiaoke.com',
    'referer': 'https://hws.fxiaoke.com/XV/UI/Home',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-trace-id': 'mktest001_22138_1685079770403:502',
    }

    params = {
        '_fs_token': fs_token,
        'traceId': 'E-E.mktest001.22138-1685084717038',
    }

    json_data = {
        'serializeEmpty': False,
        'extractExtendInfo': True,
        'object_describe_api_name': 'object_mZeYu__c',
        'search_template_id': '5d0c806a7cfed91f3e95ba8e',
        'include_describe': False,
        'include_layout': False,
        'need_tag': True,
        'search_template_type': 'default',
        'ignore_scene_record_type': False,
        'search_query_info': '{"limit":100,"offset":0,"filters":[],"orders":[{"fieldName":"last_modified_time","isAsc":false}]}',
        'pageSizeOption': [
            20,
            50,
            100,
        ],
        'list_component': {
            'type': 'list',
            'api_name': 'list_component',
            'header': 'List',
            'nameI18nKey': 'paas.udobj.list_page',
            'view_info': [
                {
                    'name': 'list_view',
                    'is_default': True,
                    'is_show': True,
                },
                {
                    'name': 'split_view',
                    'is_default': False,
                    'is_show': True,
                },
            ],
            'filters_info': [
                {
                    'fields': [],
                    'page_type': 'list',
                },
            ],
            'button_info': [
                {
                    'hidden': [],
                    'page_type': 'list',
                    'render_type': 'list_normal',
                    'order': [             
                        'Add_button_default',
                    ],
                    'exposed_button': 1,
                },
                {
                    'hidden': [],
                    'page_type': 'list',
                    'render_type': 'list_batch',
                    'order': [
                        'ChangeOwner_button_default',
                        'Abolish_button_default',
                        'AddTeamMember_button_default',
                        'DeleteTeamMember_button_default',
                        'Lock_button_default',
                        'Unlock_button_default',
                        'Export_button_default',
                        'ExportFile_button_default',
                        'ChangePartnerOwner_button_default',
                    ],
                    'exposed_button': None,
                },
                {
                    'hidden': [],
                    'page_type': 'list',
                    'render_type': 'list_single',
                    'order': [],
                    'exposed_button': 0,
                },
            ],
            'define_view_info': [
                'list_view',
                'split_view',
            ],
            'scene_info': [
                {
                    'hidden': [],
                    'page_type': 'list',
                    'render_type': 'drop_down',
                    'order': [
                        'All',
                        'Participate',
                        'InCharge',
                        'SubInCharge',
                        'InChargeDept',
                        'Shared',
                        'SubParticipate',
                    ],
                },
            ],
            'attributes': {
                'field_align': None,
                'enable_mobile_layout': None,
            },
            'sourceId': 'object_mZeYu__c',
            'disableLazyload': True,
        },
    }

    response = requests.post(
        'https://hws.fxiaoke.com/FHH/EM1HNCRM/API/v1/object/object_mZeYu__c/controller/List',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    json_response = response.json()
    if json_response is None:
        print("Error: JSON response is None.")
    else:
        print("JSON response: ", json_response)

        if 'Value' not in json_response:
            print("Error: Key 'Value' is not in JSON response.")
        else:
            print("'Value' in JSON response: ", json_response['Value'])

            if 'dataList' not in json_response['Value']:
                print("Error: Key 'dataList' is not in JSON response['Value'].")
            else:
                data = json_response['Value']['dataList']
                print("'dataList' in JSON response['Value']: ", data)
                total = response.json()['Value']['total']
                df = pd.DataFrame(data)
                main_data.append(df)
                print('Total:', total)
                for i in range(100, total, 100):
                    print('Offset:', i)
                    json_data['search_query_info'] = '{"limit":100,"offset":%s,"filters":[],"orders":[{"fieldName":"last_modified_time","isAsc":false}]}' % i
                    response = requests.post(
                        'https://hws.fxiaoke.com/FHH/EM1HNCRM/API/v1/object/object_mZeYu__c/controller/List',
                        params=params,
                        cookies=cookies,
                        headers=headers,
                        json=json_data,
                    )
                    data = response.json()['Value']['dataList']
                    df = pd.DataFrame(data)
                    main_data.append(df)
                df = pd.concat(main_data)
                #df.to_excel('visit_info_data.xlsx', index=False)
                df.to_excel('s3://xavier-visit-info-airflow-bucket/visit_info_data.xlsx', index=False)
  
def scrape_visit_info(browser):
    print('Scraping visit info')
    url = 'https://hws.fxiaoke.com/XV/UI/Home#crm/list/=/object_mZeYu__c'
    browser.get(url)
    time.sleep(random.uniform(8, 9))
    element = browser.find_element(By.CSS_SELECTOR, 'span[data-title="Refresh"]')
    browser.execute_script("arguments[0].click();", element)
    time.sleep(random.uniform(8, 9))
    print('Clicked refresh')
    # click list view
    element = browser.find_element(By.CSS_SELECTOR, 'span[data-title="List View"]')
    browser.execute_script("arguments[0].click();", element)
    time.sleep(random.uniform(8, 9))
    print('Clicked list view')
    # click settings
    element = browser.find_element(By.CSS_SELECTOR, 'span[data-title="Settings"]')
    browser.execute_script("arguments[0].click();", element)
    time.sleep(random.uniform(8, 9))
    print('Clicked settings')
    # click previous label input 100
    input_100  = browser.find_element(By.CSS_SELECTOR, 'input[value="100"]')
    # find previous element of input 100
    previous_element = input_100.find_element(By.XPATH, '..')
    browser.execute_script("arguments[0].click();", previous_element)
    print('Clicked previous element')
    time.sleep(random.uniform(8, 9))

    # close the settings
    #browser.find_element(By.CSS_SELECTOR, 'i[class="el-icon el-icon-close0 fx-icon-close"]').click()
    #print('Closed settings')
    #time.sleep(random.uniform(3, 4))

    # find table
    fs_token = browser.find_element(By.ID, 'fs_token').get_attribute('value')
    cookies = browser.get_cookies()
    cookies = {cookie['name']: cookie['value'] for cookie in cookies}
    get_visit_info(cookies, fs_token)
    print('Extracted visit info data')

def run_visit_info_etl():
    path = os.getcwd()
    browser = get_browser(path)
    login(browser)
    scrape_visit_info(browser)
    browser.quit()
    
if __name__ == '__main__':
    run_visit_info_etl()
