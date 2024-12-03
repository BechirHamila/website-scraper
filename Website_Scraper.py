
# %%
import requests
from bs4 import BeautifulSoup
import re
# %%



def scrape(filename,scraped_filename):
# Load URLs from the provided file
    with open(filename, 'r') as file:
        urls = file.readlines()

# Open a file to save the scraped content
    with open(scraped_filename, 'w', encoding='utf-8') as output_file:
        for url in urls:
            url = url.strip()
            try:
                # Fetch the page content
                response = requests.get(url)
                response.raise_for_status()

                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract headings and paragraphs
                content = []
                for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
                    text = tag.get_text(strip=True)
                    # Use regex to remove unwanted content (e.g., JavaScript or placeholders)
                    text = re.sub(r'(\s{2,}|[\r\n]+)', ' ', text)
                    if text and len(text.split()) > 5:  # Keep only meaningful content
                        content.append(text)

                # Write the content to the file
                if content:
                    output_file.write(f"URL: {url}\n\n")
                    output_file.write("\n".join(content))
                    output_file.write("\n\n" + "=" * 50 + "\n\n")
                    print(f"Scraped: {url}")
                else:
                    print(f"No meaningful content found at: {url}")

            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

    print("Scraping completed. Output saved to"+filename+ "_scraped.txt'")



# %%
raw_studierenwerk='studierenwerk_files\\studierenwerk_sitemap.txt'
scrape(raw_studierenwerk,'studierenwerk_files\\studierenwerk_scraped.txt')

# %%
thRo_raw='thRo_files\\thRo_sitemap.txt'
scrape(thRo_raw,'thRo_files\\thRo_scraped.txt')
