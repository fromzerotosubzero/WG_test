import pytest
import pandas as pd

@pytest.fixture(scope='module')
def df():
    return pd.read_csv('progLang.csv')

min_popularity = [15*10**6, 10**7, 5*10**7,10**8, 5*10**8, 15*10**8, 10**9]  
@pytest.mark.parametrize("item",min_popularity)
def test_popularity(df, item):
    has_min = df.query(f"popularity < {item}")
    out = ""
    for index, row in has_min.iterrows():
        out += f"{row['title']} (Frontend:{row['front_end']}|Backend:{row['back_end']}) has {row['popularity']} unique visitors per month. Expected more than {item}\n"
    assert len(has_min) == 0, out
    