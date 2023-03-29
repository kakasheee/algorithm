#컴퓨터공학과_20234029_황서빈
import urllib.request
import time

while True:
    print("현재 $ 환율을 알려드리겠습니다.")
    page = urllib.request.urlopen('https://www.google.com/finance/quote/USD-KRW?sa=X&ved=2ahUKEwj44-D8-__9AhUYaN4KHUQ0Bx8QmY0JegQIBhAd')
    text = page.read().decode('utf8')
    where = text.find('fxKbKc">')
    start_of_dallor = where + 8
    end_of_dallor = start_of_dallor + 10
    price = text[start_of_dallor: end_of_dallor]
    print("1 $ =",price)
    print("컴퓨터공학과_20234029_황서빈")
    time.sleep(10)
