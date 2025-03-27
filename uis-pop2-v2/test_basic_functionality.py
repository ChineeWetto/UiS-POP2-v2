import asyncio
import sys
import os
from tools.search_engine import search_with_retry
from tools.web_scraper import process_urls

async def main():
    print("Testing search functionality...")
    # Perform a simple search
    search_results = search_with_retry("Python programming language")
    
    if not search_results:
        print("No search results found!")
        return
    
    # Take the first result URL
    first_url = search_results[0]['href']
    print(f"\nFirst search result URL: {first_url}")
    print(f"Title: {search_results[0]['title']}")
    print(f"Snippet: {search_results[0]['body']}")
    
    print("\nTesting web scraping functionality...")
    # Scrape the first URL
    scraped_results = await process_urls([first_url], max_concurrent=1)
    
    if scraped_results and scraped_results[0]:
        print("\nSuccessfully scraped content from:", first_url)
        # Print first 500 characters of content
        content = scraped_results[0]
        print("\nFirst 500 characters of content:")
        print(content[:500] + "...")
    else:
        print("Failed to scrape content!")

if __name__ == "__main__":
    asyncio.run(main()) 