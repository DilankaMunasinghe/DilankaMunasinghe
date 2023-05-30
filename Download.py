import requests
import os

# List of URLs
urls = [
    'https://example.com/file1.txt',
    'https://example.com/file2.txt',
    'https://example.com/file3.txt'
]

# Directory to save the downloaded files
directory = 'downloads'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Download files from each URL
for url in urls:
    response = requests.get(url)
    filename = os.path.join(directory, url.split('/')[-1])  # Extract filename from URL
    with open(filename, 'wb') as file:
        file.write(response.content)
        print(f"Downloaded {filename}")
