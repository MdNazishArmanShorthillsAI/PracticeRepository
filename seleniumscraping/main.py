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
        # Configure the environment path and create a Chrome driver instance
        os.environ['PATH'] += os.pathsep + driver_path
        service_obj = Service(driver_path)
        self.driver = webdriver.Chrome(service=service_obj)

    def scrape_data(self, website):
        try:
            if not self.driver:
                raise Exception("Driver not started. Call start_driver() first.")
            
            # Open the website
            self.driver.get(website)
            
            # Maximize the browser window for better visibility
            self.driver.maximize_window()
            
            # Click on "All matches" button
            all_matches_button = self.driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
            all_matches_button.click()
            
            # Locate the dropdown and select "Spain"
            caja = self.driver.find_element(By.CLASS_NAME, 'panel-body')
            dropdown = Select(caja.find_element(By.ID, 'country'))
            dropdown.select_by_visible_text('Spain')
            
            # Wait for elements to load
            time.sleep(5)
            
            # Select elements in the table
            matches = self.driver.find_elements(By.CSS_SELECTOR, 'tr')
            partidos = [match.text for match in matches]
            
            return partidos
        except Exception as e:
            print(f"Error in scrape_data: {str(e)}")
            return []

    def close_driver(self):
        try:
            if self.driver:
                # Close the driver and the browser window
                self.driver.quit()
        except Exception as e:
            print(f"Error in close_driver: {str(e)}")

    def save_to_csv(self, data):
        try:
            # Create a DataFrame and save it as a CSV file
            df = pd.DataFrame({'goals': data})
            df.to_csv('seleniumScrapedData.csv', index=False)
        except Exception as e:
            print(f"Error in save_to_csv: {str(e)}")

    def save_to_json(self, data):
        try:
            # Convert data to JSON format and save it to a JSON file
            json_data = json.dumps(data, indent=4, ensure_ascii=False)
            with open('seleniumScrapedData.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
        except Exception as e:
            print(f"Error in save_to_json: {str(e)}")

# Define the path to the ChromeDriver executable
path = '/home/shtlp_0043/seleniumscraping/chromedriver'

# Define the website URL to scrape
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Instantiate the SeleniumScraper class
try:
    scraper = SeleniumScraper(path)
    
    # Scrape data from the website
    scraped_data = scraper.scrape_data(website)
    
    # Save scraped data to CSV and JSON files
    scraper.save_to_csv(scraped_data)
    scraper.save_to_json(scraped_data)
finally:
    # Close the driver when done
    scraper.close_driver()
