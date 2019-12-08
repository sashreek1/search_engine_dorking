from bs4 import BeautifulSoup
import requests
import lxml.html
escaped_search_term = input('Search term must be a string : ')
number_results = int(input("number of required results : "))
def fetch_results(escaped_search_term,number_results):
    language_code = "en"
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results,language_code)
    response = requests.get(google_url)
    return response


if __name__ == '__main__':
    html = fetch_results(escaped_search_term,number_results)
    doc = lxml.html.fromstring(html.content)
    results = doc.xpath('//div[@class="BNeawe UPmit AP7Wnd"]/text()')
    print()
    print("#####################################################################")
    print("searching for :", escaped_search_term)
    print("#####################################################################")
    print()
    for i in results:
        print(i)
    print()
    print()
    print("#####################################################################")
    print("returned", len(results),"results")
    print("#####################################################################")