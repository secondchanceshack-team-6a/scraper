import urllib3
from bs4 import BeautifulSoup

url = "https://montgomery.tncrtinfo.com/crCaseList.aspx"
data = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "/wEPDwULLTE0ODU1MDYxNDkPZBYCZg9kFgJmD2QWAgIDD2QWBAIVD2QWAgIBD2QWAgIFDxYCHgdWaXNpYmxlaGQCGQ9kFgQCBQ9kFgICAQ8PFgIfAGdkFgICBQ8PFgIeBFRleHQFC1BhZ2UgMSBvZiA3ZGQCBw9kFgQCAQ8PFgIfAGhkZAIFDw9kDxAWBWYCAQICAgMCBBYFFggeBE5hbWUFDlBhcnR5Rmlyc3ROYW1lHgRUeXBlCylcU3lzdGVtLlR5cGVDb2RlLCBtc2NvcmxpYiwgVmVyc2lvbj0yLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkSHgxEZWZhdWx0VmFsdWVlHg5QYXJhbWV0ZXJWYWx1ZWQWCB8CBQ1QYXJ0eUxhc3ROYW1lHwMLKwQSHwQFAkFBHwVkFggfAgURUGFydHlCdXNpbmVzc05hbWUfAwsrBBIfBGUfBWQWCB8CBQhQYWdlU2l6ZR8DCysEBx8EBQIyMB8FZBYIHwIFClBhZ2VOdW1iZXIfAwsrBAkfBAUBMR8FZBYFAgMCAwIDAgMCA2RkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRjdGwwMCRsb2dzdGF0aGVhZCRjdGwwMQUdY3RsMDAkY3RsMDAkbG9nc3RhdGhlYWQkY3RsMDMFMmN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoU2VhcmNoUmVzdWx0cyRncmlkU2VhcmNoDzwrAAoBCAIBZIxjwonTdFGQsBeFZiVaQSithISI",
    "__VIEWSTATEGENERATOR": "822659F4",
    "__EVENTVALIDATION": "/wEWIAKe/uKEDALt6cx1Areo4tIDAvSDr4EPAq+T4UECptqivQgC9emh/wQC4aeB0QMC+cWkkwcCiarL8g4CmJWIxQUC9+WzmAwC6sCXqg0C6sCDtAsC6sCfKQLqwIuzDgLqwMepDwLqwLOzDQLqwM+oAgLqwLsyAq/+i7wJAq/+98UHAq/+s7wIAq/+n8YGAq/+u7sLAq/+p8UJAq/+47sKAq/+z8UIAq/+67oNAq/+18QLAuDgn6MNAuDgi60LAW5Xcf4Y+BajzlMgFYYX8nKJQaA=",
    "ctl00$ctl00$ddlCourt": "fc048db5",
    "ctl00$ctl00$cphContent$cphSelectionCriteria$txtPartyFirstName": "",
    "ctl00$ctl00$cphContent$cphSelectionCriteria$txtPartyLastName": "AA",
    "ctl00$ctl00$cphContent$cphSelectionCriteria$txtPartyBusinessName": "",
    "ctl00$ctl00$cphContent$cphContentPaging$hfpg": "1",
    "ctl00$ctl00$cphContent$cphContentPaging$hfmx": "7",
    "ctl00$ctl00$cphContent$cphContentPaging$nextpage": "Next >",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl02$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl03$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl04$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl05$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl06$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl07$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl08$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl09$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl10$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl11$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl12$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl13$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl14$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl15$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl16$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl17$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl18$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl19$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl20$hfrc": "124",
    "ctl00$ctl00$cphContent$cphSearchResults$gridSearch$ctl21$hfrc": "124",
}

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Origin": "https://montgomery.tncrtinfo.com",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 7 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
}

http = urllib3.PoolManager()
r = http.request('POST', url, headers=headers, fields=data)
soup = BeautifulSoup(r.data, 'html.parser')
print(soup.find('table'))
