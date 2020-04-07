from seleniumwire import webdriver
import webbrowser
import time
import json

ii=1

driver = webdriver.Chrome("/PATH/chromedriver")

driver.get("https://www.supermercato24.it/")
driver.find_element_by_link_text("ACCETTO").click()
driver.find_element_by_link_text("Fai la spesa").click()
time.sleep(7)
driver.find_element_by_xpath("//input[@type='email']").send_keys("xxxxxx@xxxxx.it")
driver.find_element_by_xpath("//input[@type='password']").send_keys("INSERT_PW")
driver.find_element_by_xpath("//input[@value='Accedi']").click()

driver.get('https://www.supermercato24.it/s#/locations/11243/stores/4494/checkout')

while(ii==1):
    endpoint_orari = "https://api.supermercato24.it/sm/api/v3/locations/11243/stores/4494/availability?funnel=CHECKOUT"
    try:
        trigger_status_update()
    except:
        driver.refresh()

    request = driver.wait_for_request(endpoint_orari)
    j = json.loads(request.response.body)
    del driver.requests
    
    try:
        j['error']
        print(j['error'])
        time.sleep(40)
    except:
        ii=0
webbrowser.open('https://www.youtube.com/watch?v=Kp3mx6OEeZk')
