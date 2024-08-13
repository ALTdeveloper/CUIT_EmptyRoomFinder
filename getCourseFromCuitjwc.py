import pandas as pd
#打开大课表界面，保存网页为html后拿到这里
# Load the HTML file
import requests
from bs4 import BeautifulSoup

# Load the HTML file
file_path = './202501courseTable1to100.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')

# Use pandas to convert the table to a DataFrame
df = pd.read_html(str(table))[0]

# Save the DataFrame to a CSV file
csv_file_path = './2501course_table1.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
