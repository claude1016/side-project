from bs4 import  BeautifulSoup  as bf
import re
import requests
import pandas as pd


def main(url):      #娛樂
  domain = 'https://www.setn.com'
  three = requests.get(url).text
  three=bf(three, 'html.parser')
  title=three.find('h3',{'class','view-li-title'}).find('a',{'class':'gt'}).text
  text=three.find('h3',{'class','view-li-title'}).find('a',{'class':'gt'})['href']
  text_1=requests.get(domain+text)
  text_1=bf(text_1.text,'html.parser')
  text_1=text_1.find('div',{'class':'Content2'}).text
  text_1=re.sub('（圖／\w*）','',text_1)
  title_content=(title,text_1)
  return   list(title_content)
def main_1(url):  #政治 #社會 #國際 #運動
  domain = 'https://www.setn.com'
  three = requests.get(url).text
  three = bf(three, 'html.parser')
  title=three.find('h3', {'class', 'view-li-title'}).find('a', {'class': 'gt'}).text
  text = three.find('h3', {'class', 'view-li-title'}).find('a', {'class': 'gt'})['href']
  text_1 = requests.get(domain + text)
  text_1 = bf(text_1.text, 'html.parser')
  text_1 = text_1.find('div', {'id':'Content1'}).text
  text_1 = re.sub('（圖／\w*）', '', text_1)
  title_content = (title, text_1)
  return  list(title_content)
#def main_2(url):


if __name__ == '__main__':
   type = ['娛樂', '政治', '社會', '國際', '運動']
   title_content = []
   title_content.append(main('https://www.setn.com/ViewAll.aspx?PageGroupID=8'))
   title_content.append(main_1('https://www.setn.com/ViewAll.aspx?PageGroupID=6'))
   title_content.append(main_1('https://www.setn.com/ViewAll.aspx?PageGroupID=41'))
   title_content.append(main_1('https://www.setn.com/ViewAll.aspx?PageGroupID=5'))
   title_content.append(main_1('https://www.setn.com/ViewAll.aspx?PageGroupID=34'))


   df=pd.DataFrame(title_content,columns=['標題','內容'])
   df.insert(0,'類別',type)  #選定位置，插入一欄
   print(df.values[0])

   df.to_excel('C:/Users/Claude/Desktop/NKUST/side project/三立新聞(爬蟲).xlsx')