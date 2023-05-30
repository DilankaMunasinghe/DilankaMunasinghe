import requests
import os
from concurrent.futures import ThreadPoolExecutor

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

# Function to download a file from a given URL
def download_file(url):
    response = requests.get(url)
    filename = os.path.join(directory, url.split('/')[-1])
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename

# Download files using multiple threads
with ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        future = executor.submit(download_file, url)
        futures.append(future)
    
    # Wait for all the download tasks to complete
    for future in futures:
        filename = future.result()
        print(f"Downloaded {filename}")
