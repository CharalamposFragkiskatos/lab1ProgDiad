import requests  # εισαγωγή της βιβλιοθήκης
import datetime


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break



try:
    #url = input("Give a URL\n")
    url = "http://facebook.com/"
    r= requests.get(url)
    # Ερώτημα 1
    '''
    for key in r.headers:
        print('{'+"'"+key +"'"+ " : " + "'"+r.headers[key] +"'"+"}")

    # Ερώτημα 2
    '''
    if "server" in r.headers.keys():
        print("Server software:" + r.headers["server"])
    for cookie in r.cookies:
        print("Cookie "+ cookie.name, end = ' expires ' )
        print(datetime.datetime.fromtimestamp(int(cookie.expires)).strftime('%Y-%m-%d %H:%M:%S')) 
except:
    print("Incorrect URL. Try again...\n")
    


