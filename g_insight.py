try:
    import requests
except ImportError as err:
    print(f"Failed to import required modules {err}")

class g_insight(object):
    
    def __init__(self, api_key):
        self.api_key = f"&key={api_key}"
        self.endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    def send_request(self, _url):
        try:
            json_resp = requests.get(f"{self.endpoint}{_url}{self.api_key}").json()
            return json_resp
        except requests.exceptions.TooManyRedirects:
            print("Request exceeded the acceptable number of redirects.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.HTTPError as err:
            print(f"The following HTTPError occured {err}")
    
    def check_website(self, url):
        url = f"?url={url}"
        return self.send_request(url)

# Example Usage.
if __name__ == "__main__":
    insight = g_insight("Insert API Key Here.")
    print(insight.check_website("https://google.com"))
    
    
