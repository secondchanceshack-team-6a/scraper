#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "usage: ./ext.sh <county> <id>\neg: ./ext.sh montgomery 1243241234"
    exit 1
fi

DATA_START='ctl00%24ctl00%24cphContent%24scrtab=ctl00%24ctl00%24cphContent%24upnltabhead%7Cctl00%24ctl00%24cphContent%24cphTabbedBar%24ultab&__EVENTTARGET=ctl00%24ctl00%24cphContent%24cphTabbedBar%24ultab&__EVENTARGUMENT=1&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJNzkzODc0MjI4D2QWAmYPZBYCZg9kFgICAw9kFgQCFQ9kFgICAQ9kFgICBQ8WAh4HVmlzaWJsZWhkAhkPZBYCAgMPZBYCZg9kFgQCAQ9kFgICAQ8QZA8WB2YCAQICAgMCBAIFAgYWBxAFB0dlbmVyYWwFB2dlbmVyYWxnEAUHQ2hhcmdlcwUHY2hhcmdlc2cQBQlBdHRvcm5leXMFCWF0dG9ybmV5c2cQBQlEb2N1bWVudHMFCWRvY3VtZW50c2cQBQhIZWFyaW5ncwUIaGVhcmluZ3NnEAUFQm9uZHMFBWJvbmRzZxAFBEZlZXMFBGZlZXNnFgBkAgMPZBYYAgEPDxYCHwBnZBYGAgEPPCsACgEADxYGHgxEYXRhU291cmNlSUQFCWRzR2VuZXJhbB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudAIBZBYCZg9kFgZmDw8WAh8AaGRkAgEPZBYCZg9kFgZmDxUCMVN0YXRlIE9mIFRlbm5lc3NlZSB2cyBDaHJpc3RvcGhlciBDaGFybGVzIEFhbmVydWQRNjNDQzEtMjAxNy1DUi04MjFkAgEPZBYCZg8VARtDaHJpc3RvcGhlciBDaGFybGVzIEFhbmVydWRkAgIPFQsJRGVmZW5kYW50C0p1bCAwNiAyMDE3BSQwLjAwAAQwLjAwDFJvc3MgSCBIaWNrcwtKYW4gMDIgMjAxOAhEaXNwb3NlZAALU2VwIDAxIDIwMTcETm9uZWQCAg8PFgIfAGhkZAIDDw8WBB4EVGV4dGUeC05hdmlnYXRlVXJsZWRkAgUPDxYCHwQFH01vbnRnb21lcnkgQ291bnR5IENpcmN1aXQgQ291cnRkZAIDD2QWAgIBDzwrAAoAZAIFD2QWAgIBDzwrAA0AZAIHD2QWAgIBDzwrAA0AZAIJD2QWAgIBDzwrAA0AZAILD2QWAgIBDzwrAA0AZAIND2QWAgIBDzwrAA0AZAIPD2QWAgIBDzwrAA0AZAIRD2QWAgIBDzwrAA0AZAITD2QWAgIBDzwrAA0AZAIVD2QWAgIBDzwrAA0AZAIXDw9kDxAWAWYWARYIHgROYW1lBQdQYXJ0eUlEHgRUeXBlCylcU3lzdGVtLlR5cGVDb2RlLCBtc2NvcmxpYiwgVmVyc2lvbj0yLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkSHgxEZWZhdWx0VmFsdWUFJEREQUFGNjhDLTc1MzYtNDdGQS1CRjkyLTc1QzUyQzM0MzNCMh4OUGFyYW1ldGVyVmFsdWVkFgECA2RkGAwFLmN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRmcm1kZXRhaWwPFCsAB2RkZGRkFgACAWQFM2N0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRncmlkcnVsZWRvY2tldA9nZAUxY3RsMDAkY3RsMDAkY3BoQ29udGVudCRjcGhGb3JtRGV0YWlsJGdyaWRwbXRhZ3JlZQ9nZAUtY3RsMDAkY3RsMDAkY3BoQ29udGVudCRjcGhGb3JtRGV0YWlsJGdyaWRmZWVzD2dkBTJjdGwwMCRjdGwwMCRjcGhDb250ZW50JGNwaEZvcm1EZXRhaWwkZ3JpZGRvY3VtZW50cw9nZAUyY3RsMDAkY3RsMDAkY3BoQ29udGVudCRjcGhGb3JtRGV0YWlsJGdyaWRhdHRvcm5leXMPZ2QFLmN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRncmlkYm9uZHMPZ2QFMWN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRmcm1wYXJ0eWluZm8PZ2QFMWN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRncmlkaGVhcmluZ3MPZ2QFMGN0bDAwJGN0bDAwJGNwaENvbnRlbnQkY3BoRm9ybURldGFpbCRncmlkY2hhcmdlcw9nZAUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFHWN0bDAwJGN0bDAwJGxvZ3N0YXRoZWFkJGN0bDAxBR1jdGwwMCRjdGwwMCRsb2dzdGF0aGVhZCRjdGwwMwUxY3RsMDAkY3RsMDAkY3BoQ29udGVudCRjcGhGb3JtRGV0YWlsJGdyaWRhZGRwYXJ0eQ9nZNvbNePNVkdRq%2Bb162nSC9Wi1UpA&__VIEWSTATEGENERATOR=20D8A3C2&__EVENTVALIDATION=%2FwEWDQLkw7ioCwLt6cx1Areo4tIDAvSDr4EPAq%2BT4UECz5agrAwC0JagrAwC0ZagrAwC0pagrAwC05agrAwC1JagrAwC1ZagrAwC07azlQyJiIUAW6G5BwYrsBaobyx4U3JwYw%3D%3D&ctl00%24ctl00%24ddlCourt=fc048db5&txtpayamt=&__ASYNCPOST=true&'

curl "https://$1.tncrtinfo.com/crCaseForm.aspx?id=$2" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://montgomery.tncrtinfo.com/crCaseForm.aspx?id=DDAAF68C-7536-47FA-BF92-75C52C3433B2' -H 'X-MicrosoftAjax: Delta=true' -H 'Cache-Control: no-cache' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' -H 'Connection: keep-alive' -H 'Cookie: pubinqcrt=selcrt=fc048db5' --data "$DATA_START"
