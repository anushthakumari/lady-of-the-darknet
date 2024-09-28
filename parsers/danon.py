from selectolax.parser import HTMLParser

TAG = "danon"

def parse(html_content=""):
    parser = HTMLParser(html_content)
    
    posts = parser.css('.card-bodys')

    d = []

    for post in posts:

        tds = post.css('.card-title')

        company_name = tds[0].text()

        d.append({
            "company_name": company_name,
            "data_size": None,
            "tag": TAG
        })

    
    return d