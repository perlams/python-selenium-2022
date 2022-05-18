DEFAULT_CONFIG = {
  "url": "https://laboratorio.qaminds.com/",
  "browser_name": "firefox",
  "path": "../../../drivers/geckodriver",
  "incognito": True,
  "headless": {
    "enabled": False,
    "resolution": {
      "width": 800,
      "height": 600
    }
  },
  "page_load": 5,
  "implicit_wait": 5,
  "explicit_waits": {
    "small": 3,
    "medium": 6,
    "large": 10
  }
}