# import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class Plot():
    def __init__(self, df):
        self.df = df

    def overall_bc(self, year):
        # year count
        df_year = self.df.groupby("year").count()
        # total number of registers per year
        f_years = df_year[df_year.index>=year] # filter unwanted years

        fig = go.Figure()
        fig.add_trace(go.Bar(x=f_years.index, y=f_years["company"]))
       
        return fig


    # dataframe of only top10 industries
    def stack_bc(self, top):
        top_indus = list(self.df["industry"].value_counts().keys()[1:top+1]) # top n
        df_top_indus = self.df[self.df["industry"].isin(top_indus)] # if inndustry * is in * top


        # group data by year and by industry
        g_year_comp = df_top_indus.groupby(["year", "industry"]) # group
        years  = list(set([year_indus_tuple[0] for year_indus_tuple in list(g_year_comp.groups.keys())])) # extraxt years
        industries  = list(set([year_indus_tuple[1] for year_indus_tuple in list(g_year_comp.groups.keys())])) # extraxt industries

        # a dict to store the count of each industry for each year. e.g: {"Others":[10, 20, 30]}, the value referes to first, second and third year's counts.
        indus_yearCount = {i:[] for i in industries}

        for indus in industries:
            for year in years:
                try:
                    count = g_year_comp.get_group((year, indus)).count()["company"] # count of the companies per year per industry

                    indus_yearCount[indus].append(count)
                except Exception as e:
                    indus_yearCount[indus].append(0)


        # plot
        fig = go.Figure()
        for indux, countList in indus_yearCount.items():
            fig.add_trace(go.Bar(name=indux, x=years, y=countList)) # add trace of each group


        # Change the bar mode
        fig.update_layout(
            title=f'New Registers per Year for Top {top} Industries',
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Number of new registers',
                titlefont_size=16,
                tickfont_size=14,
            ),
            xaxis=dict(
                title='Year',
                titlefont_size=16,
                tickfont_size=14,
            ),
            legend=dict(
                x=1,
                y=1,
        #         bgcolor='rgba(255, 255, 255, 0)',
        #         bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode="stack"
        )

        return fig

    def search_tb(self, term):
        def lookFor(row, term):
            if term.lower() in row["company"].lower():
                return row.name
        results = self.df.apply(lookFor, axis=1, args=(term,))
        df = self.df.loc[results.dropna().index]

        tableDF = df.reset_index(drop=False)

        h_values = tableDF.columns.tolist()
        c_values = [tableDF[h] for h in h_values]
        h_values = [f"<b>{h}</b>" for h in h_values] # bold headers

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=h_values,
                fill_color='#3b3b3b',
                line_color="black",
                align='left', font=dict(color='white', size=11)),
            cells=dict(
                values=c_values,
                line_color="black",
                align='left', font=dict(color='black', size=11))
            )
        ])
        fig.update_layout(
            title=f'new title',
            # autosize=False,
            # width=500,
            # height=500,
            margin=dict(l=10, r=10, b=5, t=100, pad=0),
            )
        return fig

