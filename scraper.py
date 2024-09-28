import httpx
import os
import json
from concurrent.futures import ProcessPoolExecutor, as_completed

import parsers 

def fetch_and_parse(url_obj, proxies):
    tag = url_obj['tag']
    url = url_obj['url']
    
    resp_text = None

    with httpx.Client(proxies=proxies) as client:
        response = client.get(url)
        if response.status_code == 200:
            resp_text = response.text
        else:
            print(f"Failed to access the site {url}, status code: {response.status_code}")
            return None

    if resp_text:
        data = parsers.parse(tag, resp_text)
        return data

    return None


def fetch_data_parallel(urls, proxies):
    results = []
    
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(fetch_and_parse, url_obj, proxies) for url_obj in urls]
        
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                results.extend(result)

    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    return results

if __name__ == "__main__":
    
    proxies = {
        "http://": "socks5://127.0.0.1:9150",
        "https://": "socks5://127.0.0.1:9150"
    }
    
    urls = [
        {
            "url":'http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/',
            "tag":parsers.TAGS.omega
        },
        {
            "url":'http://threeamkelxicjsaf2czjyz2lc4q3ngqkxhhlexyfcp2o6raw4rphyad.onion/',
            "tag":parsers.TAGS.threeam
        },
        {
            "url":'http://2c7nd54guzi6xhjyqrj5kdkrq2ngm2u3e6oy4nfhn3wm3r54ul2utiqd.onion/',
            "tag":parsers.TAGS.danon
        },
    ]

    
    data = fetch_data_parallel(urls, proxies)
    print("Data updated!")
