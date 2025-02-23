# bible_crawler/crawler.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

ALL_BOOKS = [
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA", "1KI", "2KI",
    "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO", "ECC", "SNG", "ISA", "JER",
    "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP",
    "HAG", "ZEC", "MAL", "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL",
    "EPH", "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE",
    "2PE", "1JN", "2JN", "3JN", "JUD", "REV"
]

def next_verse(prev_verse):
    parts = prev_verse.split('.')
    num = int(parts[1]) + 1
    next_v = f"{parts[0]}.{num}.{parts[2]}"
    return next_v

def get_verses(bible, bible_num):
    """
    Crawl verses for a given Bible version.
    Returns a list of dictionaries mapping chapter identifiers to verse texts.
    """
    first_verses = [f"{book}.1.{bible}" for book in ALL_BOOKS]
    all_bible = []
    for url in first_verses:
        verses = {}
        while True:
            url_sba = f"https://www.bible.com/bible/{bible_num}/{url}"
            print(f"Scraping: {url_sba}")
            try:
                response = requests.get(url_sba)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                # Extract verse text using regex to filter unwanted spans
                text = [span.get_text(strip=True) for span in soup.find_all('span')]
                text = [t for t in text if re.match(r'^[0-9]{1,3}[A-Za-z()“‘]+', t)]
                if text:
                    verses[url] = text
                    print(f"Found {len(text)} verses in {url}")
                else:
                    print(f"No verses found in {url}. Moving to the next book.")
                    break

                # Check for the next chapter
                next_url = next_verse(url)
                next_url_sba = f"https://www.bible.com/bible/{bible_num}/{next_url}"
                next_response = requests.get(next_url_sba)
                if next_response.status_code == 200:
                    print(f"Next chapter {next_url} exists. Continuing...")
                    url = next_url
                else:
                    print("No next chapter. Moving to next book.")
                    break

                # Delay to avoid rate limiting
                time.sleep(1)
            except requests.exceptions.RequestException as e:
                print(f"Error scraping {url_sba}: {e}")
                break
        all_bible.append(verses)
    return all_bible

def remove_crossref(text_list):
    """Remove cross-references from a list of verse texts."""
    return [text for text in text_list if re.match(r'^[0-9]{1,3}[A-Za-z()“‘]+', text)]

def merge_all(data_list):
    """
    Merge the scraped data into a DataFrame with columns:
    ['ChapterID', 'VerseID', 'Content'].
    """
    processed_data = []
    for list_element in data_list:
        for key, value in list_element.items():
            chp_id = '.'.join(key.split('.')[:2])
            content = remove_crossref(value)
            if content:
                try:
                    verse_num = int(re.match(r'([0-9]+)', content[0]).group(1))
                except Exception:
                    verse_num = 0
                chapter = {
                    'ChapterID': chp_id,
                    'VerseID': verse_num,
                    'Content': content[0]
                }
                processed_data.append(chapter)
    return pd.DataFrame(processed_data)
