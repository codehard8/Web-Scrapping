from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


#url_1 = "https://www.zillow.com/az/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.00426%2C%22south%22%3A31.332177%2C%22east%22%3A-109.045223%2C%22west%22%3A-114.816591%7D%2C%22mapZoom%22%3A6%2C%22usersSearchTerm%22%3A%22Arizona%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A8%2C%22regionType%22%3A2%7D%5D%2C%22schoolId%22%3Anull%7D"

#Base_URL="https://www.zillow.com/co/{page}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page}%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-131.392035125%2C%22east%22%3A-62.310003875000014%2C%22south%22%3A16.455500906135853%2C%22north%22%3A55.27187241368884%7D%2C%22mapZoom%22%3A4%2C%22usersSearchTerm%22%3A%22Colorado%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10%2C%22regionType%22%3A2%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# i used multiple urls could be better to scrape first to a list but ------

url_1="https://www.zillow.com/nm/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.000293%2C%22south%22%3A31.332172%2C%22east%22%3A-103.001964%2C%22west%22%3A-109.050173%7D%2C%22mapZoom%22%3A6%2C%22usersSearchTerm%22%3A%22New%20Mexico%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41%2C%22regionType%22%3A2%7D%5D%2C%22schoolId%22%3Anull%7D"
Base_URL="https://www.zillow.com/nm/{page}_p/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.000293%2C%22south%22%3A31.332172%2C%22east%22%3A-103.001964%2C%22west%22%3A-109.050173%7D%2C%22mapZoom%22%3A6%2C%22usersSearchTerm%22%3A%22New%20Mexico%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41%2C%22regionType%22%3A2%7D%5D%2C%22schoolId%22%3Anull%2C%22pagination%22%3A%7B%22currentPage%22%3A{page}%7D%7D"

headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Eowyancoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://example.com",
    "Upgrade-Insecure-Requests": "1"
}

Houses=[]
columns = ["link","address","dealer","price","beds","baths","area"]


for page in range(1,23):

    
    if page == 1:
        url = url_1 # Use the unique first page URL
    else:
        url = Base_URL.format(page=page)  # the other pags folow pattren (pagination)
    
    # Send the request to get the page content
    r = requests.get(url, headers=headers)

    time.sleep(5)

    # Ensure that the request is successful
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')

        # Find the listing container
        listing_container = soup.find('ul', class_='List-c11n-8-107-0__sc-1smrmqp-0 StyledSearchListWrapper-srp-8-107-0__sc-1ieen0c-0 jBzkcM gagHXc photo-cards photo-cards_extra-attribution')

        # Find all <li> elements inside the <ul>
        listings = listing_container.find_all('li', class_='ListItem-c11n-8-107-0__sc-13rwu5a-0 StyledListCardWrapper-srp-8-107-0__sc-wtsrtn-0 dAZKuw xoFGK')

       #print(len(listings))

        for listing in listings:
            # Find the 'data-container' div inside each <li>
            data_container = listing.find('div', class_='StyledPropertyCardDataWrapper-c11n-8-107-0__sc-hfbvv9-0 cdQcZn property-card-data')

            if data_container:
                # Extract the link
                link = data_container.find('a')['href'] if data_container.find('a') else 'N/A'

                # Extract the address
                address = data_container.find('address', {'data-test': 'property-card-addr'}).text.strip() if data_container.find('address', {'data-test': 'property-card-addr'}) else 'N/A'

                # Extract the dealer/agent info
                dealer = data_container.find('div', class_='StyledPropertyCardDataArea-c11n-8-107-0__sc-10i1r6-0 bziRDw').text.strip() if data_container.find('div', class_='StyledPropertyCardDataArea-c11n-8-107-0__sc-10i1r6-0 bziRDw') else 'N/A'

                # Extract the price
                price = data_container.find('span', {'data-test': 'property-card-price'}).text.strip() if data_container.find('span', {'data-test': 'property-card-price'}) else 'N/A'
                
                
                ######

                # Locate the ul element directly
                details_list = soup.find('ul', class_='StyledPropertyCardHomeDetailsList-c11n-8-107-0__sc-1j0som5-0 ewlWmM')

                # Initialize an empty list to store extracted values
                extracted_values = []

                if details_list:
                    # Find all li elements within the ul
                    list_items = details_list.find_all('li')
                    for li in list_items:
                        # Extract the <b> tag inside the li
                        b_tag = li.find('b')
                        if b_tag:
                           extracted_values.append(b_tag.text.strip())  # Clean and append the value

                beds=extracted_values[0] if len(extracted_values) > 0 else 'N/A'
                baths=extracted_values[1] if len(extracted_values) > 1 else 'N/A'
                area=extracted_values[2] if len(extracted_values) > 2 else 'N/A'


                # Print the extracted data
                Houses.append([link,address,dealer,price,beds,baths,area])
                
    else:
        print(f"Failed to retrieve the page. Status code: {r.status_code}")


# Convert list of lists to DataFrame
new_dat = pd.DataFrame(Houses, columns=columns)

output_file = "houses_for_sale_Colorado.csv"
new_dat.to_csv(output_file, mode='a', index=False, header=False)