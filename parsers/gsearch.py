from search_engine_parser.core.engines.google import Search as GoogleSearch

gsearch = GoogleSearch()

def get_query_in_google(query: dict) -> dict:
    """ Return result with keys
    ini index - dict of numbers result
    "titles" - list titles
    "links" - list links
    "descriptions" - list descriptions
    """
    return gsearch.search(
        query['q'], 1, url="google.ru", hl='ru',
        as_sitesearch=query['as_sitesearch'])


if __name__ == '__main__':
    from pprint import pprint
    query = {}
    query['q'] = 'Курс UX дизайнер'
    query['as_sitesearch'] = 'netology.ru'
    gresults = get_query_in_google(query)
    pprint(gresults)

    # print first title from google search
    print(gresults["titles"][0])
    # print 10th link from yahoo search
    print(gresults["links"][9])
    # print 6th description from bing search
    print(gresults["descriptions"][5])

    # print first result containing links, descriptions and title
    print(gresults[0])