# AI Web Scraper

A simple and efficient AI Web Scraper built using Selenium for extracting website content. This project allows users to input a website URL, scrape content from the page, and clean the data to make it more readable.

## Features

- **Web Scraping with Selenium**: Utilizes Selenium to load a webpage and extract the HTML content.
- **Content Cleaning**: Cleans up the scraped HTML to remove unwanted tags like script, style, headers, footers, etc., to focus on meaningful content.
- **Easy-to-use Interface**: A simple Python script that can be run locally or deployed as a web app.
- **Customizable**: Modify the scraper to work with different websites and extract specific data.

## Installation

### Requirements:
- Python 3.x
- Selenium
- WebDriver (Chrome, Firefox, etc.)
- BeautifulSoup
- ChromeDriver (for Chrome) or corresponding driver for other browsers

### Installation Steps:

1. **Clone the Repository**:

    Clone this repository to your local machine using Git.

2. **Install Dependencies**:

    Install the required Python libraries by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup WebDriver**:

    If you're using Chrome, make sure to install `chromedriver` with:

    ```bash
    pip install webdriver-manager
    ```

    For other browsers, download the corresponding WebDriver.

4. **Create a .env File** (Optional but recommended):

    For securely storing sensitive information, create a `.env` file to hold API keys or other secrets. Do not push the `.env` file to GitHub (use `.gitignore`).

## Usage

### Running Locally

1. **Run the Scraper**:

    You can run the scraper by executing the Python script in your terminal.

2. **Provide a URL**:

    The script will prompt you to input the URL of the website you want to scrape.

3. **Scraping Output**:

    The script will output the cleaned text content of the website, removing unnecessary sections such as navigation, footer, and more.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Selenium: For browser automation and web scraping.
- BeautifulSoup: For parsing and cleaning HTML.
- ChromeDriver: Required for Selenium to control Chrome.
