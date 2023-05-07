def finance(code):
    driver = webdriver.Chrome()
    driver.get(f"https://finance.daum.net/quotes/A{code}#current/quote")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    time_ = soup.select('div > div > table > tbody > tr > td > span.time')
    num_ = soup.select('div > div > table > tbody > tr > td > span.num')

    box1 = []
    for i in time_[10:]: 
        box1.append(i.text) 

    box2 = []
    for i in num_[103:167:7]: 
        box2.append(int(i.text.replace(',',''))) 
    
    for i, j in zip(box1, box2): 
        print(i, j)
    
    time.sleep(3)
    driver.close()
