from selectolax.parser import HTMLParser

TAG = "omega"

def parse(html_content=""):
    parser = HTMLParser(html_content)
    
    tr_rows = parser.css('.trow')

    d = []

    for tr in tr_rows:

        tds = tr.css('td')

        if len(tds) >= 3:
            
            company_name = tds[0].text()  
            data_size = tds[3].text() 
            
            r = {
                "company_name": company_name,
                "data_size": data_size,
                "tag": TAG
            }

            d.append(r)
    
    return d