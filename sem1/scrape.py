from bs4 import BeautifulSoup
import requests
import csv

csv_header = ['index', 'comment', 'score']


header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
with open('douban_comment_1.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)
    
    for i in range(10):
        start = i * 20
        url = 'https://movie.douban.com/subject/35183042/comments?percent_type=h&start={}&limit=20&status=P&sort=new_score'.format(start)
        request = requests.get(url=url, headers=header)
        besoup = BeautifulSoup(request.text, features="lxml")
        short_comment = besoup.select('span[class=short]')
        info = besoup.select('span[class=comment-info]')
        time = besoup.select('span[class=comment-time]')
        for j, (short_comment_, info_) in enumerate(zip(short_comment, info)):
            text = short_comment_.text.replace('\n','')
            score = info_.select('span[title]')[0].get('title')
            print(text, score)
            writer.writerow([(i*20)+j, text, score])
        
        
