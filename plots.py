import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# import data
df = pd.read_csv("UkTiersponsors_All.csv")

# rename cols
df.columns = ["company", "city", "industry", "main_tier", "sub_tier", "date"]

# datetime
df["date"] = pd.to_datetime(df["date"])
# df['date'] = df['date'].dt.strftime('%d/%m/%Y') # date format
df["year"] = df["date"].apply(lambda x: x.year) # year

# lowercased city
df["city"] = df["city"].apply(str.lower)
df.head()

# year count
df_year = df.groupby("year").count()


def get_plot():
    # total number of registers per year
    f_years = df_year[df_year.index>2013] # filter unwanted years

    fig = go.Figure()
    fig.add_trace(go.Bar(x=f_years.index, y=f_years["company"]))
    return fig