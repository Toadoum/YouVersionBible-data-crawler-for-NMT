# Bible Crawler and Data Filtering Package

This package is designed to crawl Bible texts from [bible.com](https://www.bible.com/bible/), merge two Bible versions into a parallel dataset, filter and clean the data, and finally output a CSV file containing two columns ("Source" and "Target"). This CSV file is ideal for training neural machine translation models.

## Features

- **Web Crawling:** Scrapes Bible texts for a specified source Bible version and its target translation.
- **Data Merging:** Combines crawled data based on common chapter and verse identifiers.
- **Data Filtering:** Cleans the merged dataset by removing duplicates, empty cells, overly long entries, HTML tags, and more.
- **CSV Output:** Saves the final, cleaned dataset as a single CSV file with "Source" and "Target" columns.

## Project Structure

bible_crawler/
├── init.py # Makes this folder a Python package.
├── config.py # Contains user-defined configuration parameters.
├── crawler.py # Functions to crawl and merge Bible texts.
├── filtering.py # Filtering functions and main integration code.
├── main.py # Entry point to run the package.
requirements.txt # Lists all Python dependencies.
README.md # This file.bashCopierModifier
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/bible_crawler.git
   cd bible_crawler
Install the dependencies:bashCopierModifierpip install -r requirements.txt
ConfigurationUser-specific parameters are stored in the config.py file. By default, the parameters are set as follows:pythonCopierModifier# bible_crawler/config.py

source_bible = "SBA2015"
source_bible_num = 516

target_translation = "NIV"
target_bible_num = 111
You can modify these values as needed.UsageTo run the package from the command line, execute one of the following commands in the parent directory of the bible_crawler folder:Using the module approach:bashCopierModifierpython -m bible_crawler.filtering
Or by running the main entry point:bashCopierModifierpython bible_crawler/main.py
The script will:Crawl the specified source Bible and target translation from bible.com.Merge the crawled data on chapter and verse identifiers.Filter and clean the data.Save the final clean CSV file as filtered_bible.csv with columns "Source" and "Target".RequirementsThe required Python packages are listed in the requirements.txt file:shellCopierModifierrequests&gt;=2.25.1
beautifulsoup4&gt;=4.9.3
pandas&gt;=1.1.5
numpy&gt;=1.19.5
Install them using:bashCopierModifierpip install -r requirements.txt
ContributingContributions to improve the package are welcome! To contribute:Fork this repository.Create a new branch for your feature or bug fix:bashCopierModifiergit checkout -b my-feature-branch
Commit your changes with clear commit messages.Push your changes to your fork:bashCopierModifiergit push origin my-feature-branch
Open a Pull Request on GitHub with a detailed description of your changes.If you have any questions, suggestions, or bug reports, please open an issue on GitHub.LicenseThis project is licensed under the MIT License.