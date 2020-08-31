#!/usr/local/bin/python3
#

# pip instll wkhtmltopdf
# pip install pdfkit
# pip install BeautifulSoup4

import requests
import sys

import pdfkit

from bs4 import BeautifulSoup

usr = 'merle.scheffer'
pwd = '18.09.2008'

url_login = "http://vertretungsplan.thg-moodle.de/login.php"
url_plan = 'http://vertretungsplan.thg-moodle.de/vertretungsplan.php'


#
# Haptprogramm
#
def main():
    pdfkit.from_file("data.html", 'data.pdf')

#
# Python Start: Aufruf des Hauptprogrammes
#
if __name__ == '__main__':
   main()
