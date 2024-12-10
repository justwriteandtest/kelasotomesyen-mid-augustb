from selenium import webdriver
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument("--disable-auto-maximize-for-tests")

driver = webdriver.Chrome(options = chromeOptions)
driver.minimize_window()

# Waktu untuk menunggu halaman selesai dimuat sebelum menampilkan title (dalam detik / seconds) 
pageLoadWaitTime = 2

urlList = [
    'https://tiket.com', # Cloudflare Challenges
    'https://tokopedia.com',
    'https://orangsiber.com',
    'https://idejongkok.com',
    'https://kelasotomesyen.com',
]

for url in urlList:
    driver.get(url)
    sleep(pageLoadWaitTime)
    print(f"{url} - {driver.title}")

driver.quit()