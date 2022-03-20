# Import libraries
import numpy as np
import pandas as pd
import pycountry
from webscrapping import WebScrapping, WIKI_TABLE_URL

class DfHandler(object):
    """Class for handling Pandas dataframes"""

    def __init__(self):
        self.df_database = None

    @staticmethod
    def get_country_from_iso(iso):
        """Get country information from ISO code.

        :param iso str: Country ISO code
        :returns: Databased formatted object with country information
        :rtype: pycountry.db.Country

        """
        return pycountry.countries.get(alpha_3=iso)

    @staticmethod
    def get_country_diff_lang(country_name):
        """Get dataframe with country name in different languages.

        :param country_name str: Country name
        :returns: Dataframe with country name in different languages
        :rtype: pandas.Dataframe

        """
        df_web = WebScrapping()
        # Loop through the URL list
        for url in WIKI_TABLE_URL:
            df = df_web.get_web_table_as_df(url)
            # Attempt to find the country
            if not df.empty:
                df = df[df[0].eq(country_name)]
            # Country found
            if not df.empty:
                break
        return df

    @staticmethod
    def get_matching_names (df_diff_lang, countries_list):
        """Get dataframe with matching names in different languages.

        :param df_diff_lang pandas.Dataframe: Dataframe with country name in different languages
        :param countries_list list: Country name
        :returns: List with country name matches
        :rtype: list

        """
        # Rearrange dataframe for looping
        df_diff_lang = pd.concat([df_diff_lang[0], df_diff_lang[1].str.split(',', expand=True)], axis=1)
        df_diff_lang.columns = np.arange(len(df_diff_lang.columns))
        diff_lang_list = df_diff_lang.values.astype(str)[0]
        # Fill a list with matching names
        resp = [c for c in countries_list for d in diff_lang_list if c in d]
        return resp
