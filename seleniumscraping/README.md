# Selenium Web Scraper

This Python script uses the Selenium library to scrape data from a website and save it in CSV and JSON formats.

## Prerequisites

- Python 3.x installed
- ChromeDriver executable downloaded and its path configured in the script

## Usage

1. **Clone the Repository or Download the Script**

    Clone the repository or download the script to your local machine.

2. **Configure ChromeDriver Path**

    Open the script in a text editor and set the `path` variable to the path of your ChromeDriver executable.

3. **Define the Website URL**

    Define the `website` URL from which you want to scrape data in the `website` variable.

4. **Install Required Python Packages**

    Run the following command to install the necessary packages:
   
    ```bash
    pip install selenium pandas
    ```

5. **Run the Script**

    Execute the script by running:
   
    ```bash
    python scraper.py
    ```

## Steps Explained

1. **Setting Up Environment:**

   - Ensure the Selenium library and ChromeDriver are properly installed.
   - Set the ChromeDriver's path in the `path` variable.

2. **SeleniumScraper Class:**

   - Initialize the `SeleniumScraper` class, which handles web scraping tasks.

3. **Scraping Data:**

   - The `scrape_data` method opens the website, clicks "All matches," and selects "Spain" from the dropdown.
   - Extract data from the table and return it.

4. **Closing the Driver:**

   - Safely close the driver and browser window using the `close_driver` method.

5. **Saving Data:**

   - Convert data to a DataFrame and save it as a CSV file using the `save_to_csv` method.
   - Convert data to JSON format and save it to a JSON file using the `save_to_json` method.

6. **Script Execution:**

   - Instantiate the `SeleniumScraper` class with the ChromeDriver path.
   - Scrape data and save it as CSV and JSON files.

## Notes

- Customize the `website` URL according to your needs.
- Always adhere to the website's terms of use and scraping policies.
- This script serves an educational purpose and might require modifications for different websites.

## Working Video:
- [Screencast from 17-08-23 04:02:21 PM IST.webm](https://github.com/MdNazishArmanShorthillsAI/PracticeRepository/assets/142379599/57e323bd-1323-41b2-9bfc-3e89b19904e3)

