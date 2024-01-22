import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# URL of the Flipkart page you want to scrape
product = "iphone14"
url = "https://www.flipkart.com/search?q="+product

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_info_elements = soup.find_all("div", class_="_4rR01T")

    # Create a new Excel workbook
    wb = Workbook()
    sheet = wb.active

    # Write the headers
    sheet["A1"] = "Product Name"
    #sheet["B1"] = "Product ID"

    # Write the data to the Excel sheet
    for i, product_info in enumerate(product_info_elements, start=1):
        product_name_element = product_info.find("div",class_='_4rR01T')
        product_name = product_name_element.text.strip() if product_name_element else "N/A"
        sheet[f"A{i}"] = product_name
        #sheet[f"B{i}"] = product_id

    # Save the workbook to an Excel file
    wb.save("flipkart_products.xlsx")
    print("Data scraped and saved successfully.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
