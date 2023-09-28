import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright

# TESTING
if __name__ == "__main__":
    token_limit = 1000

    # News sites mostly have <span> tags to scrape
    cnn_url = "https://www.cnn.com"
    wsj_url = "https://www.wsj.com"
    nyt_url = "https://www.nytimes.com/ca/"
    ecommerce_url = "https://appsumo.com"
    amazon_url = "https://www.amazon.ca/s?k=computers&crid=1LUXGQOD2ULFD&sprefix=%2Caps%2C94&ref=nb_sb_ss_recent_1_0_recent"

    async def scrape_with_playwright(url: str, **kwargs):
        html_content = await ascrape_playwright(url)

        print("Extracting content with LLM")

        # print(html_content)

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(**kwargs,
                                    content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_playwright(
        url=ecommerce_url,
        # schema_pydantic=SchemaNewsWebsites
        schema=ecommerce_schema
    ))
