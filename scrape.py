from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')  # Disable sandboxing (required for Docker environments)
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resources in Docker

# Specify path to ChromeDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

def scrape_website(website):
    """Scrapes website content using a headless Chrome browser."""
    logger.info("Launching Chrome browser...")
    
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        logger.info("Page loaded. Scraping content...")
        html = driver.page_source
    except Exception as e:
        logger.error(f"Error scraping website: {e}")
        html = None
    finally:
        driver.quit()

    return html

def extract_body_content(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    return str(soup.body) if soup.body else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]

