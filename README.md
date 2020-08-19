# Web-Scout
Check availability of various online products using python and web scraping

## Dependencies
- notify_run
- selenium
- bs4
- lxml

## Steps
- pip install required packages
- setup a [notify run](https://notify.run/) web page to send alerts to
- subscribe to notify-run web page via browser to get alerts when using phone or computer
- set bat file shortcut (opens minimized) to run in task scheduler at defined time interval
- notifications will recurringly be pushed notify-run web page page

## Notes
- amazon check uses selenium chromedriver
- repfitness check only needs bs4
