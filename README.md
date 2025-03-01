# YouVersion Bible Data Crawler for NMT

In this project, we aim to crawl Bible texts from [bible.com](https://www.bible.com/bible/), merge two Bible versions into a parallel dataset, filter and clean the data, and output a CSV file suitable for training neural machine translation models. </br>

# Run the project

To run the project, follow the steps below. This will guide you through setting up your environment, installing dependencies, and running the data crawling and filtering steps.

If you do not have `venv` package, please refer to this [link](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/) for installation instructions.

## Create virtual environment
```
$ python3 -m venv ENV_NAME
```
## Activate your environment
```
$ source ENV_NAME/bin/activate
```

## Install requirements

To run this project, you must install all the necessary dependencies:
```
$ pip install -r requirements.txt
```

## Data Extraction and Cleaning

After setting up your environment and installing dependencies, you can proceed with running the main script.

### Run the crawler and data filter

Run the following command to start the data crawling and filtering process:
```
$ python3 bible_crawler/main.py
```

This command will:

1. Crawl the specified source Bible and target translation from [bible.com](https://www.bible.com/bible/).
2. Merge the crawled data on chapter and verse identifiers.
3. Clean the data by removing duplicates, empty cells, and unnecessary HTML tags.
4. Output the cleaned dataset to a CSV file called `filtered_bible.csv` with "Source" and "Target" columns.

## Example of running the script

To specify the source and target Bible versions and start the process, use the following:
```
$ python bible_crawler/main.py 
```

This will crawl the specified source Bible version (`SBA2015`) and target translation (`NIV`) (english). You can change these values based on your requirements in the `config.py`. For French, one can use Louis Second Bible version (`LSB`), the target bible number will be 93 (`target_bible_num = 93`)

# Results Presentation

### Cleaned Bible Data (Example)

Once the data has been filtered, you can visualize the cleaned dataset:

| Chapter | Verse | Source (SBA2015)                  | Target (NIV)                   |
|---------|-------|-----------------------------------|--------------------------------|
| EXO.20  | 1     | 1Togə́bè ɓa Ala pa taje neelé lai pana: | 1And God spoke all these words: |
| EXO.36  | 1     | 1Besaleel gə Oholiab gə diŋgamje lai gə́ njégo... | 1So Bezalel, Oholiab and every skilled person ... |


## Features

- **Web Crawling:** Scrapes Bible texts for a specified source Bible version and its target translation.
- **Data Merging:** Combines crawled data based on common chapter and verse identifiers.
- **Data Filtering:** Cleans the merged dataset by removing duplicates, empty cells, overly long entries, HTML tags, and more.
- **CSV Output:** Saves the final, cleaned dataset as a single CSV file with "Source" and "Target" columns.

# Project Structure

```bash
bible_crawler/
├── __init__.py          # Makes this folder a Python package.
├── config.py            # Contains user-defined configuration parameters.
├── crawler.py           # Functions to crawl and merge Bible texts.
├── filtering.py         # Filtering functions and main integration code.
├── main.py              # Entry point to run the package.
data/
├── filtered_bible.csv   # The output of the crawled and filtered Bible data.
requirements.txt         # Lists all Python dependencies.
README.md               # This file.
.gitignore               # Ignores unnecessary files/folders in version control.
LICENSE                 # Project's license file.
            # This file.
```

# License

This project is licensed under the MIT License.

# Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes or improvements.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## Guidelines for Contributions

- Ensure that the code is well-documented.
- Write tests for new features or bug fixes.
- Follow the coding style used in the project.
- If you fix a bug or add a feature, please update the `README.md` file accordingly.

Thank you for your contributions!
```