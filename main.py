from Googlenews import GoogleNews
googlenews =GoogleNews()
googlenews=GoogleNews(preiod='7d')
googlenews.search('World')
result=googlenews.result()
for x in result :
  print("-"*50)
  print("Title--",x['title'])
  print("Date/Time--",x['date'])
  print("Description--",x['desc'])
  print("link--",x['link'])
