# AI Web Scraper

A simple and efficient AI Web Scraper built using Selenium for extracting website content. This project allows users to input a website URL, scrape content from the page, and clean the data to make it more readable. It also integrates with Google's API for additional processing.

## Features

- **Web Scraping with Selenium**: Utilizes Selenium to load a webpage and extract the HTML content.
- **Content Cleaning**: Cleans up the scraped HTML to remove unwanted tags like script, style, headers, footers, etc., to focus on meaningful content.
- **Google API Integration**: Uses a Google API key for additional processing or services (e.g., NLP, Translation, or Storage).
- **Easy-to-use Interface**: A simple Python script that can be run locally or deployed as a web app.
- **Customizable**: Modify the scraper to work with different websites and extract specific data.

## Installation

### Requirements:
- Python 3.x
- Selenium
- WebDriver (Chrome, Firefox, etc.)
- BeautifulSoup
- Google API Key (if using Google services)
- ChromeDriver (for Chrome) or corresponding driver for other browsers

### Installation Steps:

1. **Clone the Repository**:

    Clone this repository to your local machine using Git.

2. **Install Dependencies**:

    Install the required Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup WebDriver**:

    If you're using Chrome, make sure to install `chromedriver` with:

    ```bash
    pip install webdriver-manager
    ```

    For other browsers, download the corresponding WebDriver.

4. **Setup Google API Key**:

    - Obtain a Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a `.env` file in the project directory and store your API key:

      ```
      GOOGLE_API_KEY=your_api_key_here
      ```

    - The script will automatically load the key from the `.env` file.

    **Important:** Never share your API key publicly. Add `.env` to `.gitignore` to prevent accidental uploads.

## Usage

### Running Locally

1. **Run the Scraper**:

    Execute the Python script in your terminal.

2. **Provide a URL**:

    The script will prompt you to input the URL of the website you want to scrape.

3. **Scraping Output**:

    The script will output the cleaned text content of the website, removing unnecessary sections such as navigation, footer, and more.

4. **Google API Processing (If Enabled)**:

    If the script is set to use Google services, the extracted content may be processed further (e.g., language translation, sentiment analysis).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Selenium: For browser automation and web scraping.
- BeautifulSoup: For parsing and cleaning HTML.
- Google API: For additional data processing.
- ChromeDriver: Required for Selenium to control Chrome.
