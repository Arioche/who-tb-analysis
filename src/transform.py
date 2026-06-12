import pandas as pd


def create_tb_dataset(tb_raw):

    tb = tb_raw[
        [
            "SpatialDim",
            "ParentLocation",
            "TimeDim",
            "NumericValue"
        ]
    ].copy()

    tb.columns = [
        "country_code",
        "region",
        "year",
        "rr_mdr_tb_cases"
    ]

    return tb


def create_region_lookup(region_raw):

    region_lookup = region_raw[
        [
            "CountryCode",
            "CountryName",
            "RegionCode",
            "RegionName"
        ]
    ].copy()

    return region_lookup


def join_country_names(tb, region_lookup):

    country_tb = tb.merge(
        region_lookup,
        left_on="country_code",
        right_on="CountryCode",
        how="left",
        validate="many_to_one"
    )

    return country_tb


def keep_countries_only(country_tb):

    country_tb = country_tb[
        country_tb["CountryName"].notna()
    ].copy()

    return country_tb


def create_country_dataset(tb_raw, region_raw):

    tb = create_tb_dataset(tb_raw)

    region_lookup = create_region_lookup(
        region_raw
    )

    country_tb = join_country_names(
        tb,
        region_lookup
    )

    country_tb = keep_countries_only(
        country_tb
    )

    return country_tb