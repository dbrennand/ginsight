# ginsight
A tiny wrapper for Google's PageSpeed Insight API.

## Updates
* 1/01/19: Added support for all parameters to API endpoint. These include:
    1. catagory: Defaults to Nonetype if not provided.
    2. strategy: Defaults to string "Desktop".
    3. utm_campaign: Defaults to Nonetype if not provided.
    4. utm_source: Defaults to Nonetype if not provided.

## Dependencies
* Requests
```
pipenv install
```

## Example Usage
```python
    insight = g_insight("Insert Key Here.")
    # Providing the only required parameter.
    print(insight.check_website("https://google.com"))
    # Using other params.
    print(insight.check_website("https://google.com", catagory="performance", strategy="mobile", utm_campaign="g_insight", utm_source="g_insight"))
```

## Authors -- Contributors
* **Daniel Brennand** - *Author* - [Dextroz](https://github.com/Dextroz)

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) for details.