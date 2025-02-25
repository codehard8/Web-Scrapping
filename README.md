
---

# Web Scrapping Project

This repository contains a web scraping project that utilizes BeautifulSoup to extract data. The repository includes the following key files:

## Files

- **`housing_dta_scrapping.py`**: This script is intended for scraping housing data from the web using BeautifulSoup.
- **`houses_for_sale_US.csv`**: This CSV file contains data of houses for sale in the US, including details such as link, address, dealer, price, beds, baths, and area.

## Project Description

This project demonstrates how to scrape web data using BeautifulSoup in Python. The primary focus is on extracting real estate data and saving it in a structured format for further analysis.

## Requirements

- Python 3.x
- BeautifulSoup
- Requests

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/codehard8/Web-Scrapping.git
    cd Web-Scrapping
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the scraping script (assuming the script name is `housing_dta_scrapping.py`):
    ```bash
    python housing_dta_scrapping.py
    ```

4. The results will be saved in `houses_for_sale_US.csv`.

## Data Fields in `houses_for_sale_US.csv`

- **link**: URL of the house listing.
- **address**: Physical address of the house.
- **dealer**: Real estate dealer or agent.
- **price**: Listing price of the house.
- **beds**: Number of bedrooms.
- **baths**: Number of bathrooms.
- **area**: Area of the house in square feet.

## License

This project is licensed under the MIT License.

---
