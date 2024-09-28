from selectolax.parser import HTMLParser

TAG = "3am"

def parse(html_content=""):
    parser = HTMLParser(html_content)
    
    posts = parser.css('.post')

    d = []


    for post in posts:

        tds = post.css('.post-title.f_left')

        company_name = tds[0].text()

        d.append({
            "company_name": company_name,
            "data_size": None,
            "tag": TAG
        })

    
    return d