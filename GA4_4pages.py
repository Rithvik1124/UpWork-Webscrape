from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

driver = webdriver.Chrome()

links = []
texts = []
df = pd.DataFrame(columns=['Job', 'Title', 'Link', 'Content', 'Country', 'City', 'Fixed Rate','Hourly Rate'])


# links={'Marketing Strategy':'marketing%20strategy','Digital Marketing':'digital%20marketing','Facebook':'Facebook','Meta':'Meta','TikTok':'Tik%20Tok','Google':'Google','GA4':'GA4','Universal Analytics':'Universal%20Analytics','GA3':'GA3','Retention':'retention','G.Analytics':'Google%20analytics','G.Tag Mng':'Google%20tag%20Manager','GTM':'GTM','B2B':'b2b','D2C':'d2c','B2C':'b2c','PPC':'PPC','Pay-Per-Clk':'Pay%20per%20click','Advertising':'advertising','Instagram':'Instagram'}


def page1():
    global df
    ga4_links = []
    platform_column = []
    title_l = []
    country_l = []
    city_l = []
    hr_rate_l = []
    fix_rate_l = []
    content_l = []

    try:
        driver.get("https://www.upwork.com/nx/jobs/search/?q=ga4&sort=recency&page=1")
        try:
            element = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            driver.execute_script("arguments[0].click();", element)
        except Exception:
            pass
        wait = WebDriverWait(driver, 25)
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="up-n-link"]')))
        ga4_links += [element.get_attribute('href') for element in elements]
        try:
            for link in range(0, len(ga4_links)):
                
                driver.get(ga4_links[link])
                title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h4[class="m-0"]')))
                content = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p[class="text-body-sm"]')))
                li_element = driver.find_element(By.CSS_SELECTOR, 'span[class="text-light-on-muted"]')
                try:
                    country = li_element.find_element(By.TAG_NAME,'strong').text
                except Exception:
                    country="N/A"
                try:
                    city = li_element.find_element(By.CLASS_NAME, 'nowrap').text
                except Exception:
                    city="N/A"
                
                try:
                    hr_rate = driver.find_element(By.CSS_SELECTOR, 'div[class="d-flex"]').text
                    hr_rate_l.append(hr_rate)
                    fix_rate_l.append("N/A")
                except Exception:
                    fix_rate = driver.find_element(By.CSS_SELECTOR, 'p[class="m-0"]').text
                    fix_rate_l.append(fix_rate)
                    hr_rate_l.append("N/A")
                        
                        
                        
                        
                        
                
                    
                title_l.append(title.text)
                content_l.append(content.text)
                country_l.append(country)
                city_l.append(city)
            
                    

        except Exception as ex:
            print(ex)

    except Exception as ex:

        print(ex)
        print("Reached the last page.")

    for i in range(len(ga4_links)):
        platform_column.append('GA4')
    print("HR\n",hr_rate_l)
    print("Fix\n",fix_rate_l)
    print(ga4_links)


    df_temp = pd.DataFrame(
        {'Job': platform_column, 'Title': title_l, 'Link': ga4_links, 'Content': content_l, 'Country': country_l,
         'City': city_l, 'Fixed Rate': fix_rate_l,'Hourly Rate': hr_rate_l})
    df = df.append(df_temp, ignore_index=False)
    page2()
    


def page2():
    global df
    ga4_links = []
    platform_column = []
    title_l = []
    country_l = []
    city_l = []
    hr_rate_l = []
    fix_rate_l = []
    content_l = []

    try:
        driver.get("https://www.upwork.com/nx/jobs/search/?q=ga4&sort=recency&page=2")
        try:
            element = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            driver.execute_script("arguments[0].click();", element)
        except Exception:
            pass
        wait = WebDriverWait(driver, 25)
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="up-n-link"]')))
        ga4_links += [element.get_attribute('href') for element in elements]
        try:
            for link in range(0, len(ga4_links)):
                
                driver.get(ga4_links[link])
                title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h4[class="m-0"]')))
                content = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p[class="text-body-sm"]')))
                li_element = driver.find_element(By.CSS_SELECTOR, 'span[class="text-light-on-muted"]')
                try:
                    country = li_element.find_element(By.TAG_NAME,'strong').text
                except Exception:
                    country="N/A"
                try:
                    city = li_element.find_element(By.CLASS_NAME, 'nowrap').text
                except Exception:
                    city="N/A"
                
                try:
                    hr_rate = driver.find_element(By.CSS_SELECTOR, 'div[class="d-flex"]').text
                    hr_rate_l.append(hr_rate)
                    fix_rate_l.append("N/A")
                except Exception:
                    fix_rate = driver.find_element(By.CSS_SELECTOR, 'p[class="m-0"]').text
                    fix_rate_l.append(fix_rate)
                    hr_rate_l.append("N/A")
                        
                        
                        
                        
                        
                
                    
                title_l.append(title.text)
                content_l.append(content.text)
                country_l.append(country)
                city_l.append(city)
            
                    

        except Exception as ex:
            print(ex)

    except Exception as ex:

        print(ex)
        print("Reached the last page.")

    for i in range(len(ga4_links)):
        platform_column.append('GA4')
    print("HR\n",hr_rate_l)
    print("Fix\n",fix_rate_l)
    print(ga4_links)


    df_temp = pd.DataFrame(
        {'Job': platform_column, 'Title': title_l, 'Link': ga4_links, 'Content': content_l, 'Country': country_l,
         'City': city_l, 'Fixed Rate': fix_rate_l,'Hourly Rate': hr_rate_l})
    df = df.append(df_temp, ignore_index=False)
    page3()
    


def page3():
    global df
    ga4_links = []
    platform_column = []
    title_l = []
    country_l = []
    city_l = []
    hr_rate_l = []
    fix_rate_l = []
    content_l = []

    try:
        driver.get("https://www.upwork.com/nx/jobs/search/?q=ga4&sort=recency&page=3")
        try:
            element = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            driver.execute_script("arguments[0].click();", element)
        except Exception:
            pass
        wait = WebDriverWait(driver, 25)
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="up-n-link"]')))
        ga4_links += [element.get_attribute('href') for element in elements]
        try:
            for link in range(0, len(ga4_links)):
                
                driver.get(ga4_links[link])
                title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h4[class="m-0"]')))
                content = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p[class="text-body-sm"]')))
                li_element = driver.find_element(By.CSS_SELECTOR, 'span[class="text-light-on-muted"]')
                try:
                    country = li_element.find_element(By.TAG_NAME,'strong').text
                except Exception:
                    country="N/A"
                try:
                    city = li_element.find_element(By.CLASS_NAME, 'nowrap').text
                except Exception:
                    city="N/A"
                
                try:
                    hr_rate = driver.find_element(By.CSS_SELECTOR, 'div[class="d-flex"]').text
                    hr_rate_l.append(hr_rate)
                    fix_rate_l.append("N/A")
                except Exception:
                    fix_rate = driver.find_element(By.CSS_SELECTOR, 'p[class="m-0"]').text
                    fix_rate_l.append(fix_rate)
                    hr_rate_l.append("N/A")
                        
                        
                        
                        
                        
                
                    
                title_l.append(title.text)
                content_l.append(content.text)
                country_l.append(country)
                city_l.append(city)
            
                    

        except Exception as ex:
            print(ex)

    except Exception as ex:

        print(ex)
        print("Reached the last page.")

    for i in range(len(ga4_links)):
        platform_column.append('GA4')
    print("HR\n",hr_rate_l)
    print("Fix\n",fix_rate_l)
    print(ga4_links)


    df_temp = pd.DataFrame(
        {'Job': platform_column, 'Title': title_l, 'Link': ga4_links, 'Content': content_l, 'Country': country_l,
         'City': city_l, 'Fixed Rate': fix_rate_l,'Hourly Rate': hr_rate_l})
    df = df.append(df_temp, ignore_index=False)
    page4()
    


def page4():
    global df
    ga4_links = []
    platform_column = []
    title_l = []
    country_l = []
    city_l = []
    hr_rate_l = []
    fix_rate_l = []
    content_l = []

    try:
        driver.get("https://www.upwork.com/nx/jobs/search/?q=ga4&sort=recency&page=4")
        try:
            element = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            driver.execute_script("arguments[0].click();", element)
        except Exception:
            pass
        wait = WebDriverWait(driver, 25)
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[class="up-n-link"]')))
        ga4_links += [element.get_attribute('href') for element in elements]
        try:
            for link in range(0, len(ga4_links)):
                
                driver.get(ga4_links[link])
                title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h4[class="m-0"]')))
                content = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p[class="text-body-sm"]')))
                li_element = driver.find_element(By.CSS_SELECTOR, 'span[class="text-light-on-muted"]')
                try:
                    country = li_element.find_element(By.TAG_NAME,'strong').text
                except Exception:
                    country="N/A"
                try:
                    city = li_element.find_element(By.CLASS_NAME, 'nowrap').text
                except Exception:
                    city="N/A"
                
                try:
                    hr_rate = driver.find_element(By.CSS_SELECTOR, 'div[class="d-flex"]').text
                    hr_rate_l.append(hr_rate)
                    fix_rate_l.append("N/A")
                except Exception:
                    fix_rate = driver.find_element(By.CSS_SELECTOR, 'p[class="m-0"]').text
                    fix_rate_l.append(fix_rate)
                    hr_rate_l.append("N/A")
                        
                        
                        
                        
                        
                
                    
                title_l.append(title.text)
                content_l.append(content.text)
                country_l.append(country)
                city_l.append(city)
            
                    

        except Exception as ex:
            print(ex)

    except Exception as ex:

        print(ex)
        print("Reached the last page.")

    for i in range(len(ga4_links)):
        platform_column.append('GA4')
    print("HR\n",hr_rate_l)
    print("Fix\n",fix_rate_l)
    print(ga4_links)


    df_temp = pd.DataFrame(
        {'Job': platform_column, 'Title': title_l, 'Link': ga4_links, 'Content': content_l, 'Country': country_l,
         'City': city_l, 'Fixed Rate': fix_rate_l,'Hourly Rate': hr_rate_l})
    df = df.append(df_temp, ignore_index=False)
    end()
    


def end():
    global df
    df.to_csv('ga4_scrap.csv',index=False, encoding='utf-8')
    print(df)
    driver.quit()


if __name__ == '__main__':
    page1()


