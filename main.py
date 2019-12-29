from bs4 import BeautifulSoup
import urllib.request
import random
import string


url_base = 'https://prnt.sc/'

def get_html():
    global url_last3
    url_last3 = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(3)))
    req = str(url_base + url_first3 + url_last3)
    html = urllib.request.urlopen(req).read()
    return html

def main():
    count = input('Сколько скачать картинок, черный треугольник? ')
    pic_count = int(count)
    global url_first3
    url_first3 = input('Введи 3 символа: ')
    print('OK! я закгружу ' + count + ' картинки "' + url_first3 + '" приступим!')

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for counter in range(pic_count):
        html = get_html()
        soup = BeautifulSoup(html, 'html.parser')
        picture_url = soup.find(id='screenshot-image')['src']
        urllib.request.urlretrieve(picture_url, picture_url[40:])
        count = counter + 1
        print (str(count) + '   [' + str(url_first3) + str(url_last3) + '] - [' + picture_url + '] - DONE!')


if __name__ == '__main__':
    main()
