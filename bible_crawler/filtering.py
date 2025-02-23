# bible_crawler/filtering.py

import pandas as pd
import numpy as np
import re
from crawler import get_verses, merge_all
from config import source_bible, source_bible_num, target_translation, target_bible_num

def filter_df(df, lower=False):
    """
    Filter and clean a DataFrame with 'Source' and 'Target' columns.
    Returns a cleaned DataFrame.
    """
    print("Initial DataFrame shape:", df.shape)
    
    # Remove rows with missing values
    df = df.dropna()
    print("--- After dropping NaNs:", df.shape[0], "rows")
    
    # Drop duplicate rows
    df = df.drop_duplicates()
    print("--- After dropping duplicates:", df.shape[0], "rows")
    
    # Remove rows where Source equals Target
    df["Source-Copied"] = df['Source'] == df['Target']
    df = df[df["Source-Copied"] == False].drop(["Source-Copied"], axis=1)
    print("--- After removing source-copied rows:", df.shape[0], "rows")
    
    # Remove rows where one side is too long relative to the other or exceeds 200 words
    df["Too-Long"] = ((df['Source'].str.count(' ') + 1) > (df['Target'].str.count(' ') + 1) * 2) | \
                     ((df['Target'].str.count(' ') + 1) > (df['Source'].str.count(' ') + 1) * 2) | \
                     ((df['Source'].str.count(' ') + 1) > 200) | \
                     ((df['Target'].str.count(' ') + 1) > 200)
    df = df[df["Too-Long"] == False].drop(["Too-Long"], axis=1)
    print("--- After removing too-long rows:", df.shape[0], "rows")
    
    # Remove HTML tags and normalize whitespace
    df = df.replace(r'<.*?>|&lt;.*?&gt;|&?(amp|nbsp|quot);', ' ', regex=True)
    df = df.replace(r'  ', ' ', regex=True)
    print("--- After removing HTML:", df.shape[0], "rows")
    
    # Optionally lower-case the text
    if lower:
        df['Source'] = df['Source'].str.lower()
        df['Target'] = df['Target'].str.lower()
        print("--- After lower-casing:", df.shape[0], "rows")
    else:
        print("--- Keeping original casing:", df.shape[0], "rows")
    
    # Remove any remaining empty cells
    df = df.replace(r'^\s*$', np.nan, regex=True).dropna()
    print("--- After removing empty cells:", df.shape[0], "rows")
    
    # Shuffle the DataFrame
    df = df.sample(frac=1).reset_index(drop=True)
    print("--- After shuffling:", df.shape[0], "rows")
    
    return df

def main():
    # Crawl the source Bible
    print("Crawling source Bible...")
    source_data = get_verses(source_bible, source_bible_num)
    df_source = merge_all(source_data)
    
    # Crawl the target translation
    print("Crawling target translation...")
    target_data = get_verses(target_translation, target_bible_num)
    df_target = merge_all(target_data)
    
    # Merge the two datasets on ChapterID and VerseID
    merged_df = pd.merge(df_source, df_target, on=['ChapterID', 'VerseID'], how='outer', suffixes=('', '_translation'))
    
    # Rename columns to align with filtering:
    # "Content" from source becomes "Source" and "Content_translation" from target becomes "Target"
    merged_df.rename(columns={'Content': 'Source', 'Content_translation': 'Target'}, inplace=True)
    print("Merged DataFrame shape:", merged_df.shape)
    
    # Filter the merged DataFrame
    filtered_df = filter_df(merged_df, lower=False)
    
    # Save the filtered DataFrame as a single CSV file with columns "Source" and "Target"
    output_csv = "filtered_bible.csv"
    filtered_df.to_csv(output_csv, index=False)
    print("Filtered data saved to:", output_csv)

if __name__ == "__main__":
    main()
