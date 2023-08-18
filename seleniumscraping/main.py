"""
Author : Md Nazish Arman
Description: Automated scraping using selenium
Version : 4.0
Date: 17-Aug-2023
Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3136

"""

import time
import os
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class SeleniumScraper:
    def __init__(self, driver_path):
        # Setting up Chrome driver
        os.environ['PATH'] += os.pathsep + driver_path
        service_obj = Service(driver_path)
        self.driver = webdriver.Chrome(service=service_obj)

    def scrape_data(self, website):
        try:
            if not self.driver:
                raise Exception("Driver not started. Call start_driver() first.")
            
            # Opening the website
            self.driver.get(website)

            # Maximizing the browser window for better visibility
            self.driver.maximize_window()
            
            # Clicking on "All matches" button
            all_matches_button = self.driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
            all_matches_button.click()
            
            # Finding the panel body element
            panel_body_element = self.driver.find_element(By.CLASS_NAME, 'panel-body')

            # Locating the country dropdown and select "Spain"
            country_dropdown = Select(panel_body_element.find_element(By.ID, 'country'))
            country_dropdown.select_by_visible_text('Spain')
            
            # Waiting for elements to load
            time.sleep(5)
            
            # Finding all table rows
            table_rows = self.driver.find_elements(By.CSS_SELECTOR, 'tr')

            # Extracting match details from table rows
            match_details = [row.text for row in table_rows]
            
            return match_details
        except Exception as e:
            print(f"Error in scrape_data: {str(e)}")
            return []

    def close_driver(self):
        try:
            if self.driver:
                # Closing the driver and the browser window
                self.driver.quit()
        except Exception as e:
            print(f"Error in close_driver: {str(e)}")

    def save_to_csv(self, data):
        try:
            # Creating a DataFrame and save to CSV
            df = pd.DataFrame({'match_details': data})
            df.to_csv('seleniumScrapedData.csv', index=False)
        except Exception as e:
            print(f"Error in save_to_csv: {str(e)}")

    def save_to_json(self, data):
        try:
            # Converting data to JSON format and save to a JSON file
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            with open('seleniumScrapedData.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
        except Exception as e:
            print(f"Error in save_to_json: {str(e)}")

# Defining the path to the ChromeDriver executable
driver_executable_path = '/home/shtlp_0043/seleniumscraping/chromedriver'
# Defining the website URL to scrape
target_website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

try:
    # Instantiating the SeleniumScraper class
    scraper = SeleniumScraper(driver_executable_path)
    
    # Scraping data from the website
    scraped_match_data = scraper.scrape_data(target_website)
    
    # Saving scraped data to CSV and JSON files
    scraper.save_to_csv(scraped_match_data)
    scraper.save_to_json(scraped_match_data)
finally:
    # Closing the driver when done
    scraper.close_driver()
