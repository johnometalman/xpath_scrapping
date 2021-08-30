import requests 
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//div[@class = "col mb-4"]/div/h2/a/@href'
XPATH_TITTLE = '//div[@class = "mb-auto"]/h2/a/text()'
XPATH_SUMMARY = '//div[@class = "lead"]/p/text()'
XPATH_BODY = '//div[@class = "html-content"]/p[not(class)]/text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices) 


        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)





def run():
    parse_home()

if __name__ == "__main__":
    run()