import requests 
import lxml.html as html
import os 
import datetime


url = 'https://www.larepublica.co/'

xpath_article = '//h2[@class= "headline"]/a/@href'
xpath_tittle = '//div[@class= "mb-auto"]/h2/span[1]/text()'
xpath_summary = '//div[@class="lead"]/p/text()'
xpath_body = '//div[@class="html-content"]/p[not(@class)]/text()'

def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                tittle = parsed.xpath(xpath_tittle)[0]
                tittle = tittle.replace('\"', '')
                summary = parsed.xpath(xpath_summary)[0]
                body = parsed.xpath(xpath_body)
            except IndexError:
                return

            with open(f'{today}/{tittle}.txt', 'w', encoding='utf-8') as f:
                f.write(tittle)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')

        else:
            raise ValueError(f'Error:{response.status_code}')

    except ValueError as ve:
        print(ve)




def parse_home():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(xpath_article)
            #print(links_to_notices) 

            today = datetime.date.today().strftime('%d-%m-%Y')

            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links_to_notices:
                parse_notice(link, today)

        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()