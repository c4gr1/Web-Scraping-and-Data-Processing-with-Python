# Python Web Scraping and Data Processing Projects

This repository contains three different Python projects: downloading an image from a URL, scraping data from a web page, and calculating word frequency.

## Projects

### 1. Downloading an Image from a URL

This project prompts the user for a URL, downloads the image from the given URL, and saves it with the specified filename. Using the `urllib.request` library, the project downloads the image based on the provided URL and filename.

### 2. Web Scraping Wikipedia and Processing Data with Pandas

This project scrapes data from the Wikipedia page "List of largest companies in the United States by revenue," converts it into a Pandas DataFrame, and saves the data to a CSV file. The `requests` and `BeautifulSoup` libraries are used to scrape the data from the web page, and the Pandas library is used to process and save the data.

### 3. Calculating Word Frequencies on a Wikipedia Page

This project scrapes content from a specified Wikipedia page, calculates word frequencies, and sorts the words from most to least frequent. Using the `requests` and `BeautifulSoup` libraries, the project scrapes the data from the web page, removes symbols, and calculates word frequencies.

## Requirements

To run these projects, you need the following Python libraries:
- `requests`
- `pandas`
- `beautifulsoup4`

To install these libraries, run:
```
pip install requests pandas beautifulsoup4
