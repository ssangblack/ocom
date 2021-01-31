import webbrowser
import datetime
hour = int(input('hour : '))
minute = int(input('minute : '))
url = str(input('url : '))
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
while True:
    now = str(datetime.datetime.now())
    h = int(now[11:13])
    m = int(now[14:16])
    if h == hour and m == minute :
        webbrowser.get(chrome_path).open(url)
        break
