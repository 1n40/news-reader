pip install googlenews

x=input("News you want to search ?")
y=input("The time period you want it to be in")
from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(period=y)
googlenews.search(x)
result=googlenews.result(sort=True)
for x in result :
  print("-"*50)
  print("Title--      ",x['title'])
  print("Date/Time--  ",x['date'])
  print("Description--",x['desc'])
  print("link--       ",x['link'])
