from bs4 import BeautifulSoup
import requests
import lxml.html
def fetch_results(escaped_search_term):
    language_code = "en"
    google_url = 'https://www.google.com/search?q={}&hl={}'.format(escaped_search_term,language_code)
    response = requests.get(google_url)
    return response
def fetch_results_bing(term):
    bing_url = 'https://www.bing.com/search?q='+term
    response = requests.get(bing_url)
    return response, bing_url


if __name__ == '__main__':
    se = int(input("please enter favourable search engine : \n 1. Google\n 2. Bing \n"))
    escaped_search_term = input('Search term must be a string : ')
    if se == 1:
        html = fetch_results(escaped_search_term)
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
    else:
        html, url = fetch_results_bing(escaped_search_term)
        doc = lxml.html.fromstring(html.content)
        results = doc.xpath('//li[@class="b_algo"]/h2/a[1]/@href')
        print()
        print("#####################################################################")
        print("searching for :", escaped_search_term, "at :", url)
        print("#####################################################################")
        print()
        for i in results:
            print(i, "\n")
        print()
        print()
        print("#####################################################################")
        print("returned", len(results), "results")
        print("#####################################################################")
