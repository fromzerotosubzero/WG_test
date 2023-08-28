import pytest
import pandas as pd
from dataclasses import dataclass

@dataclass
class Websites:
    title: str
    popularity: int
    front_end: str
    back_end: str
    database: str
    note: str
    
@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    # getting table from url, saving into dataframe
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    dfs = pd.read_html(url)
    progLang = dfs[0]

    # adjusting dataframe to create dataclass later
    progLang.fillna("N/A", inplace=True) 
    progLang.columns = ["title", "popularity", "front_end", "back_end", "database", "note"]

    # cleans wikirefs for all data in columns
    for column in progLang.columns:
        progLang[column] = progLang[column].str.replace("\[\d+\]", "", regex=True)

    # cleaning junk from popularity column & converting dtype object to numeric
    progLang["popularity"] = progLang["popularity"].str.replace("\[\d+\]","", regex=True) \
        .str.replace("\D", "", regex=True) 
    progLang["popularity"] = pd.to_numeric(progLang["popularity"]) #convert dtype object to numeric

    # saving clean csv for future usage
    progLang.to_csv("progLang.csv", index=False)