import requests
from bs4 import BeautifulSoup
from array import array
import urllib.request
from urllib.request import urlretrieve
import wget

def manga_downloader():
        global manga_name
        manga_name = input("Enter manga name(all lower-case):")
        a = manga_name.replace(' ', '-')
        url = 'http://www.mangaeden.com/en/en-manga/'
        urlnew = url + str(a)
        chapter_latest(urlnew)
        global chapter
        chapter = input("Enter what chapter you want to download:")
        urlold = urlnew + '/' + str(chapter) + '/'
        urlfinal = urlold + '/35/'
        source_code = requests.get(urlfinal)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for img_name in soup.findAll('img', {'id': 'mainImg'}):
                last = img_name.get('alt')
        print(last)
        global b
        b = int(input("Enter the page number shown above "))
        global i
        i = b + 2
        str(i)
        page = 1
        for page in range(1, i):
                urlfinall = urlold + str(page) + '/'
                jpg_downloader(urlfinall)

def jpg_downloader(link):
        source_code = requests.get(link)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for jpg in soup.findAll('img', {'id': 'mainImg'}):
                global reallink
                reallink = jpg.get('src')
                global reallink2
                reallink2 = 'https:' + reallink
                wget.download(reallink2)
                print(reallink2)


def mangareader():
        manga_name = input("Enter manga name(all small letter):")
        a = manga_name.replace(' ', '-')
        url = 'http://www.mangaeden.com/en/en-manga/'
        urlnew = url + str(a)
        chapter_latest(urlnew)
        chapter = input("Enter what chapter you want to read:")
        urlold = urlnew + '/' + str(chapter) + '/'
        urlfinal = urlold + '/35/'
        source_code = requests.get(urlfinal)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for img_name in soup.findAll('img', {'id': 'mainImg'}):
                last = img_name.get('alt')
                print (last)
        b = int(input("Enter the page number shown above:"))
        i = b + 2
        str(i)
        page = 1
        print("Here is the list of each page of the chapter you want to read")
        for page in range(1, i):
                urlfinal = urlold + str(page) + '/'
                print(urlfinal)

def latest_manga():
        url = "http://www.mangaeden.com/eng/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for jiu in soup.find_all('ul', {'class': 'thumbNews'}):
                for bla in soup.find_all('li', {'class': "topMangaHome fetch243489 toUnveil hotTopMangaHome"}):
                        print(soup.find('a')[href])


def begin():
        print("1. Check the latest manga this week")
        print("2. Download Manga")
        print("3. Read Manga online by giving you link")
        option=input("Enter the option that you prefer:")
        if (option==str(1)):
                latest_manga()
                ac=input("Do you want to use the software again?(y/n)")
                if ac ==str("y"):
                        begin()
                else:
                        return
        elif (option==str(2)):
                manga_downloader()
                ac=input("Do you want to use the software again?(y/n)")
                if ac ==str("y"):
                        begin()
                else:
                        return
        elif (option==str(3)):
                mangareader()
                ac=input("Do you want to use the software again?(y/n)")
                if ac ==str("y"):
                        begin()
                else:
                        return
        else:
                print ("You put the wrong command.")
                begin()

def chapter_latest(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        num=input("Enter how many latest chapter you want to see:")
        for abc in range (0,int(num)):
                for lat_chap in soup.find('b'):
                        print(soup.find_all('b')[abc].text)


begin()