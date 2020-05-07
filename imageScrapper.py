from bs4 import BeautifulSoup
from requests import get
import os
from time import sleep
from shutil import make_archive,rmtree
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options 

def get_link(searchVar):
    #parsing
    searchVar = '%20'.join(searchVar.strip().split(' '))
    link = "https://www.flickr.com/search/?text="+searchVar
    return link


def get_images(title):
    try:
        link = get_link(title)
    
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        driver = Chrome(chrome_options=chrome_options)
        driver.get(link)
    
        for i in range(1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

        sleep(5)

        bsObj = BeautifulSoup(driver.page_source,"html.parser")
   
    
        linkToMain = bsObj.find_all("div",{"class":"photo-list-photo-view"})
        images=[]
    
        for i in linkToMain:
            style = i.attrs["style"]
            url = style.find("url(")
            style = style[url+5:-3]
            images.append("https:"+style)
    
        print(len(images),images,sep='\n')

        driver.close()

        return images
    except:
        return 1



# def download(images):
#     if('images' not in os.listdir()):
#         os.mkdir("images")
#     for i in range(len(images)):
#         with open(f"images/{i}.{images[i].split('.')[-1]}",'bw') as img:
#             img.write(get(images[i]).content)
#     print("DONE DOWNLOADING!!!!!")  

#     # zipfile = make_archive('images','zip','images')
#     # print("done zipping")
#     # rmtree("images")

if __name__ == "__main__":
    topic = input("enter something : ")
    get_images(topic)
