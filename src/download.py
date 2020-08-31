#!/usr/local/bin/python
#

# apt-get install wkhtmltopdf
# pip install wkhtmltopdf
# pip install pdfkit
# pip install BeautifulSoup4

import sys
import requests
import pdfkit
from bs4 import BeautifulSoup

usr = 'Göstenmeier'
pwd = 'kT8BG39'

url_home  = "hhttps://enrichment.schleswig-holstein.de"
url_login = url_home + "/content/index.php"
url_browser = url_home + "/content/klKursBrowser.php"

def debug(line):
    '''
    Debug Messages
    '''
    print("DBG: %s" % line)

#
# Haptprogramm
#
def main():
    # Start a session so we can have persistant cookies
    session = requests.session()
    debug("session: %r" % session)

    # This is the form data that the page sends when logging in
    login_data = {
        'user': usr,
        'passwort': pwd,
        'submit': 'Anmelden',
    }
    debug("%-20s|%r" % ("login data", login_data))

    # Authenticate
    page = session.post(url_login, data=login_data)
    debug("%-20s|%s: %r" % ("login page", url_login, page))
    debug("%-20s|%r" % ("login page", page.text))

    # Try accessing a page that requires you to be logged in
    page = session.get(url_browser)
    debug("%-20s|%s: %r" % ("access page", url_plan, page))
    debug("%-20s|%r" % ("access page", page.text))

    # Parse page
    soup = BeautifulSoup(page.text, "html5lib")
    debug("%-20s|%r" % ("soup", soup))

    data = soup.find('div', attrs={'class': 'timetable'})
    debug("%-20s|%r" % ("data", data))

    with open("data.html", "w") as html:
        html.write(str(data))

    # pdfkit.from_file("data.html", 'data.pdf')

#
# Python Start: Aufruf des Hauptprogrammes
#
if __name__ == '__main__':
   main()
