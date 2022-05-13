from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os 
import getpass
import pathlib
import sys 
import pickle
chrome_options = Options()
chrome_options.add_argument("--headless")

def entry():
    global driver
    global url
    global folder
    folder = "C:" + os.path.sep + "Users"+ os.path.sep + getpass.getuser() + os.path.sep + "Desktop"+ os.path.sep+ "Stamp_stocks" 
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
    os.chdir(folder)
    path = ("WebScraping\Selenium\chromedriver.exe") #Adjust you path and check webdriver compatibility with chrome browser
    url = 'https://registration.telangana.gov.in/stampStockPosition.htm'
    driver = Chrome(path) # , options = chrome_options)
    driver.get(url)

    

def options():
    output = {}
    xps = {'district' : '//*[@id="districtCode"]', 'category':'//*[@id="category"]', 'denomination' : '//*[@id="denomination"]'}
    for k in xps:
        x = driver.find_element_by_xpath(xps[k])
        options = [i for i in x.find_elements_by_tag_name("option")]
        var = [element.get_attribute("text")  for element in options if element.get_attribute("text") != "Select..."]
        output[k] = var
    return(output)


def scraping(output):
    data = {}
    for a in output['district']:
        data[a] = {}
        for b in output['category']:
            data[a].update({b:[]})
            for c in output['denomination']:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="districtCode"]'))).send_keys(a)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="category"]'))).send_keys(b)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="denomination"]'))).send_keys(c) 
                try:
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stampStockRegister"]/div[3]/button[1]'))).click()                    
                except sys.exc_info()[0]:
                    driver.refresh()
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="districtCode"]'))).send_keys(a)
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="category"]'))).send_keys(b)
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="denomination"]'))).send_keys(c)
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stampStockRegister"]/div[3]/button[1]'))).click()                    
                xk = pd.read_html(driver.page_source)[0]
                if '------------ No Stamp Stock Found------------' in xk.values:
                    with open(folder + "\\"+ 'No_stamps_stocks_data1.txt','a') as f:
                        f.write(a + "_" + ('_').join(b.split(" ")) +"_"+str(c))
                        f.write("\n")
                    # data[a][b].append([c,'No Stamp Stock Found'])
                else:
                    xk.columns = [xk.columns[i][0] for i in range(len(xk.columns))]
                    xk = xk.iloc[:-1,:-1]
                    xk.drop(['Sl.No'], axis = 1, inplace = True)
                    # data[a][b].append([c,xk])
                    xk.to_csv(a + "_" + ('_').join(b.split(" ")) +"_"+str(c)+".csv", encoding = 'utf-8')
                driver.get(url)
    return(data)




entry()
output = options()
data = scraping(output)

with open(r"stampstock_data.pickle", "wb") as output_file:
    pickle.dump(data, output_file)

"""

# =============================================================================
# dump
# =============================================================================

#pickle loading code
#=========================================================
with open("your_path\dict_data.pickle", 'rb') as f:
    data = pickle.load(f)
print(data)
#=========================================================

# def local_save(data):
#     folder = "C:" + os.path.sep + "Users"+ os.path.sep + getpass.getuser() + os.path.sep + "Desktop"+ os.path.sep+ "Stamp_stocks" 
#     pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
#     for m in data.keys():
#         for i in data[m]:
#             for j in data[m][i]:
#                 try:
#                     if 'No Stamp Stock Found' in j:
#                         pass
#                 except ValueError:
#                     # print(m+"_"+('_').join(i.split(" "))+"_"+str(j[0])+".csv")
#                     j[1].to_csv(m+"_"+('_').join(i.split(" "))+"_"+str(j[0])+".csv", encoding = 'utf-8')
#                     # print('\n')
#     print("DataFrames are Locally Saved in your current working directory")
    
"""
