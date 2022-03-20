# Import libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Global Constants
WIKI_TABLE_URL = [
    "https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(A%E2%80%93C)",
    "https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(D%E2%80%93I)",
    "https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(J%E2%80%93P)",
    "https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(Q%E2%80%93Z)"
]
TABLE_CLASS = "wikitable"
SUCCESS_RESPONSE = 200

class WebScrapping(object):
    """Class for extracting data from URLs"""

    @staticmethod
    def success_resp(status_code):
        """Checks if the response code was successful.

        :param status_code int: Status code to check
        :return:

        """
        status = True if status_code == SUCCESS_RESPONSE else False
        return status

    def get_web_table_as_df(self, url, table_class=None):
        """Extract data from website and return it as dataframe.

        :param url str: URL where table will be extracted
        :param table_class str: HTML class for table in URL
        :returns: Web table as a dataframe
        :rtype: pandas.Dataframe

        """
        if table_class is None:
            table_class = TABLE_CLASS
        df = pd.DataFrame()
        response = requests.get(url)
        if self.success_resp(response.status_code):
            web_table = BeautifulSoup(response.text, 'html.parser').find('table', {'class': table_class})
            df = pd.DataFrame(pd.read_html(str(web_table))[0])
        return df
