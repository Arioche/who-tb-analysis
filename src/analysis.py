
import pandas as pd
import matplotlib.pyplot as plt

def top_countries(
        country_tb,
        n=10
):

    return (
        country_tb
        .groupby("CountryName")["rr_mdr_tb_cases"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

def yearly_trend(
        country_tb
    ):

    return(
        country_tb.groupby("year")["rr_mdr_tb_cases"]
        .sum()
        .sort_index()
    )
    

def plot_yearly_trend(country_tb):

    trend = yearly_trend(country_tb)

    plt.figure(figsize=(10, 6))
    trend.plot(marker='o')
    plt.title("Yearly Trend of RR/MDR TB Cases")
    plt.xlabel("Year")
    plt.ylabel("Number of Cases")
    plt.grid(True)

    plt.show()




def country_trend(country_tb, country_name):

    country_df = country_tb[
        country_tb["CountryName"] == country_name
    ]

    if country_df.empty:
        raise ValueError(
            f"{country_name} not found"
        )

    return yearly_trend(country_df)


def plot_country_trend(
    country_tb,
    country_name
):

    trend = country_trend(
        country_tb,
        country_name
    )

    plt.figure(figsize=(10, 6))

    trend.plot(marker="o")

    plt.title(
        f"RR/MDR-TB Cases in {country_name}"
    )

    plt.xlabel("Year")
    plt.ylabel("Cases")

    plt.grid(True)

    plt.show()


def top_countries_by_year(
    country_tb,
    year,
    n=10
):

    return (
        country_tb[country_tb["year"] == year]
        .groupby("CountryName")["rr_mdr_tb_cases"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
