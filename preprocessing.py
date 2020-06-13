import pandas as pd


def process():

    # import data
    df = pd.read_csv("./data/UkTiersponsors_All.csv")

    # rename cols
    df.columns = ["company", "city", "industry", "main_tier", "sub_tier", "date"]

    # datetime
    df["date"] = pd.to_datetime(df["date"])
    # df['date'] = df['date'].dt.strftime('%d/%m/%Y') # date format
    df["year"] = df["date"].apply(lambda x: x.year) # year

    # lowercased city
    df["city"] = df["city"].apply(str.lower)
    df["city"] = df["city"].apply(str.capitalize)

    return df

    