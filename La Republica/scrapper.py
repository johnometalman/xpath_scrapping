import requests 
import lxml.html as html



url = 'https://www.larepublica.co/'

xpath_article = '//div[@class="V_Title"]/text-fill/a/@href'
#xpath_tittle = '//div[@class="mb-auto"]/h2/span/text()'
#xpath_summary = '//div[@class="lead"]/p/text()'
#xpath_body = '//div[@class="html-content"]/p[not(@class)]/text()'

def parse_home():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(xpath_article)
            print(links_to_notices) 


        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()