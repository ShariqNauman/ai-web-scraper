from google import genai
from google.genai.types import GenerateContentConfig
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
import random
import streamlit as st

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Gemini API
client = genai.Client(api_key=st.secrets["api"]["key"])


template = """
You are tasked with extracting specific information from the following text content: {dom_content}. 
Please follow these instructions carefully:

1. Extract Information: Extract the information that matches the provided description: {parse_description}.
2. Mixed Format: Your response can include both text and tables as needed.
3. Table Format: When presenting lists or tabular data, use Markdown tables with | characters. Include a header row and a separator row.
4. Text Formatting: Use Markdown formatting for text sections to improve readability (e.g., headers, bold, italic).
5. No Extra Content: Do not include any additional explanations or comments outside of the extracted information.
6. Empty Response: If no information matches the description, return an empty string ('').
"""

# Initialize Gemini model
def create_model():
    return client.chats.create(
            model="gemini-2.0-flash", 
        )

def parse_chunk(chunk, parse_description, max_retries=3):
    """Parses a single chunk of text with Gemini API and retries if needed."""
    retries = 0
    while retries < max_retries:
        try:
            model = create_model()
            prompt = template.format(dom_content=chunk, parse_description=parse_description)
            response = model.send_message(prompt)

            if response and response.text:
                return response.text
            
            return ""  # Return empty if no response

        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e):
                wait_time = 2 ** retries + random.uniform(0, 1)  # Exponential backoff
                logger.warning(f"Quota exceeded. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
                retries += 1
            else:
                logger.error(f"Error parsing chunk: {e}")
                break

    return ""  # Return empty if all retries fail

def parse_with_gemini(dom_chunks, parse_description):
    """Processes multiple chunks with Gemini API in parallel (rate-limited)."""
    parsed_results = []
    total_chunks = len(dom_chunks)

    with ThreadPoolExecutor(max_workers=5) as executor:  # Reduced concurrency
        future_to_chunk = {executor.submit(parse_chunk, chunk, parse_description): i 
                           for i, chunk in enumerate(dom_chunks, start=1)}

        for future in as_completed(future_to_chunk):
            chunk_index = future_to_chunk[future]
            try:
                result = future.result()
                parsed_results.append(result)
                logger.info(f"Parsed batch: {chunk_index} of {total_chunks}")
            except Exception as e:
                logger.error(f"Error processing chunk {chunk_index}: {e}")

    return "\n".join(parsed_results)