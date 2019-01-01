try:
    import requests
except ImportError as err:
    print(f"Failed to import required modules {err}")


class g_insight(object):

    def __init__(self, api_key):
        self.api_key = f"{api_key}"
        self.endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    def send_request(self, params: dict):
        """Makes the request to the Google Insight API.
        Params:
            params: dict: Request params for API request.
        Returns:
            resp: The API JSON response.
            error: Occurs if request fails. resp.raise_for_status() is invoked.
        """
        try:
            resp = requests.get(self.endpoint, params=params)
            if ((resp.status_code) == (requests.codes.ok)):
                return resp.json()
            else:
                resp.raise_for_status()
        except requests.exceptions.TooManyRedirects:
            print("Request exceeded the acceptable number of redirects.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.HTTPError as err:
            print(f"The following HTTPError occured {err}")

    def check_website(self, url: str, catagory: str = None, strategy: str = "desktop", utm_campaign: str = None, utm_source: str = None):
        """Check website function.
        Params:
            More Info [1]: https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed#parameters
            url: string: The URL to query.
            catagory: string: "A Lighthouse category to run; if none are given, only Performance category will be run.[1]"
            strategy: string: Default is Desktop per API. Can be either str: desktop or mobile.
            utm_campaign: string: Campaign name for analytics.
            utm_source: string: Campaign source for analytics. 
        Returns:
            resp.json() from send_request()
        """
        # Valid catagory options.
        catagory_options = ["accessibility",
                            "best-practices", "performance", "pwa", "seo"]
        # Valid Strategy options.
        strategy_options = ["desktop", "mobile"]
        # Init params dict.
        params = {}
        # Add key param.
        params["key"] = self.api_key
        # Add url param.
        params["url"] = url
        # If not none and in acceptable catagory_options, add to params dict.
        if (catagory is not None) and (catagory in catagory_options):
            params["catagory"] = catagory
        # Check if different and in valid strategy_options. Defaults to desktop.
        if strategy in strategy_options:
            params["strategy"] = strategy
        # If not None, add to params dict.
        if utm_campaign is not None:
            params["utm_campaign"] = utm_campaign
        # If not None, add to params dict.
        if utm_source is not None:
            params["utm_source"] = utm_source
        return self.send_request(params)


# Example Usage.
if __name__ == "__main__":
    insight = g_insight("Insert Key Here.")
    # Providing the only required parameter.
    print(insight.check_website("https://google.com"))
    # Using other params.
    print(insight.check_website("https://google.com", catagory="performance", strategy="mobile", utm_campaign="g_insight", utm_source="g_insight"))
