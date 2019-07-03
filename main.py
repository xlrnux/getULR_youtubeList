import platform
from selenium import webdriver

# 4K Downloader : http://www.4kdownload.com/
# 4K Downloader 스마트모드를 이용하여 클립으로만 다운로드 할 수 있게 재생목록 URL 을 따옴.
# TARGET_URL 에 재생목록이 있는 동영상 주소를 넣어줌
# 실행하면 console 에 재생목록의 주소가 전부 출력
# 해당 주소들을 전부다 복사
# 4K Downloader 옵션에서 스마트모드 키고 링크복사를 누름
# 재생목록이 아닌 클립으로 다운로드를 시키면 끝!
# 저작권은 지키세요!
######################################
TARGET_URL = ""
######################################
OS = str(platform.system())
if OS == "Windows":
    driver = webdriver.Chrome('./chromedriver.exe')
elif OS == "Linux":
    driver = webdriver.Chrome('/usr/bin/chromedriver')
else:
    print("this program only support Linux and Windows")
    exit(100)

driver.implicitly_wait(3)  # 암묵적으로 3초 기다린다
driver.get(TARGET_URL)
driver.implicitly_wait(2)

urls = driver.find_elements_by_id("wc-endpoint")

for _url in urls:
    strings = _url.get_property("href")
    print(strings)
