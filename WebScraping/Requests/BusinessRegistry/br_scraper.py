import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
global headers
global base_url
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
    }
base_url = 'https://business.egov.mv'


def base_link(search_param):
    global start_time
    start_time = datetime.now().strftime("%d-%m-%y %I:%M:%S")
    company_details = {}
    search_url = base_url+"/BusinessRegistry/SearchBusinessRegistry"
    data = {"query": search_param}
    response = requests.post(search_url, headers=headers, data=data)
    if response.status_code == 200:
        soup = bs(response.content, "html.parser")
        try:
            company_name = soup.find("div", {"class" : "feature_home"}).span.text.strip()
            if company_name.lower().replace(" ","") == search_param.lower().replace(" ", ""):
                company_link = soup.find("div", {"class" : "feature_home"}).a["href"]
                company_details = {
                                    "name" :company_name,
                                    "link" :company_link
                                }                
        except AttributeError:
            pass
    return company_details


def company_details(company_name):
    global company_url
    company_details = base_link(company_name)
    if len(company_details)>0 and len(company_details["link"]) != 0:
        company_url = base_url+company_details["link"]
        response = requests.get(company_url, headers=headers)
        if response.status_code == 200:
            company_soup = bs(response.content, "html.parser")
        return company_soup


def main(company_name, each_code,  otp_dict):
    csoup = company_details(company_name)
    if csoup:
        try:
            name_soup = csoup.find("div", {"class":'parallax-content-2'})
            otp_dict['OWCODE'].append(each_code)
            name_split = name_soup.find("div", {'class':'col-md-8'}).h1.text.split('|')
            otp_dict['FullName'].append(name_split[0])
            otp_dict['Register Number'].append(name_split[-1])
            otp_dict['URL'].append(company_url) 
        except:
            otp_dict['FullName'].append('')
            otp_dict['Register Number'].append('')
            otp_dict['URL'].append('')

        try:
            otp_dict['FullAddress'].append(name_soup.find("div", {'class':'col-md-8'}).text.strip().split('\n')[-1])
            address = name_soup.find("div", {'class':'col-md-8'}).text.strip().split('\n')[-1]
            split_address = address.split(',')
            for i in  range(len(split_address)):
                try:
                    otp_dict["RoomFloorBuilding1"].append(split_address[i])
                except:
                    otp_dict["RoomFloorBuilding1"].append('')
                    break
                try:    
                    otp_dict["StreetNumber"].append(split_address[i+1])
                except:
                    otp_dict["StreetNumber"].append('')
                    break
                try:    
                    otp_dict["TownName"].append(split_address[i+2])
                except:
                    otp_dict["TownName"].append('')
                    break
                
                if len(split_address)>4:
                    try:    
                        otp_dict['Street'].append(split_address[i+3].replace("'", ''))
                    except:
                        otp_dict["Street"].append('')
                        break
                else:
                    otp_dict["Street"].append('')

                try:    
                    otp_dict['CountryName'].append(split_address[-1])
                except:
                    otp_dict["CountryName"].append('')
                    break
                break
            
        except:
            otp_dict['FullAddress'].append('')
            otp_dict["StreetNumber"].append('')
            otp_dict["Street"].append('')
            otp_dict["TownName"].append('')
            otp_dict["CountryName"].append('')

        try:
            otp_dict['CompanyStatus'].append(name_soup.find("div", {'class':'col-md-4'}).text.strip().split('\n')[0].split("|")[-1].strip())
        except:
            otp_dict['CompanyStatus'].append('')

        people_details = csoup.find("div", {"class":'col-lg-12 add_bottom_15'})
        ptitles = people_details.findAll('div','form_title')
        psteps = people_details.findAll('div','step')

        if len(ptitles) == len(psteps):
            for each_range in range(len(ptitles)):

                if each_range == 0:
                    try:
                        otp_dict['Personnel1'].append(', '.join(ptitles[each_range].text.strip().split('\n')[::-1]))
                    except:
                        otp_dict['Personnel1'].append("")
                    otp_dict['Personnel1 contact'].append('')
                    md_step = psteps[each_range].text.strip()

                if each_range == 1:
                    if 'board of directors' in ptitles[each_range].text.strip().lower():
                        try:
                            bod_details = pd.read_html("<html>"+str(psteps[each_range])+"</html>")[0]
                        except:
                            bod_details = pd.DataFrame(np.nan, index=range(1,9), columns = ['Name', "Appointed Date"])
                        for i, j in  zip(range(0,8), range(1,9)):
                            try:
                                otp_dict[f"Board of Director: Name {j}"].append(bod_details.loc[i,'Name'])
                            except:
                                try:
                                    otp_dict[f"Board of Directors: Name {j}"].append(bod_details.loc[i,'Name'])
                                except:
                                    try:
                                        otp_dict[f"Board of Director: Name {j}"].append('')
                                    except:
                                        otp_dict[f"Board of Directors: Name {j}"].append("")
                            
                            try:
                                otp_dict[f"Appointed Date.{j}"].append(bod_details.loc[i,'Appointed Date'])
                            except:
                                otp_dict[f"Appointed Date.{j}"].append("")

                if each_range == 2:
                    if 'shareholders' in ptitles[each_range].text.strip().lower():
                        try:
                            shdr_details = pd.read_html("<html>"+str(psteps[each_range])+"</html>")[0]
                        except:
                            shdr_details = pd.DataFrame(np.nan, index=range(1,9), columns = ['Name', "Join Date"])
                        for k, l  in  zip(range(0,8), range(1,9)):
                            try:
                                otp_dict[f"Shareholder Info {l}"].append(shdr_details.loc[k, "Name"])
                            except:
                                otp_dict[f"Shareholder Info {l}"].append("")
                            try:                            
                                otp_dict[f"Shareholders Join Date {l}"].append(shdr_details.loc[k, "Join Date"])
                            except:
                                otp_dict[f"Shareholders Join Date {l}"].append("")

                if each_range == 3:
                    if 'Business Names'.lower() in ptitles[each_range].text.strip().lower():
                        try:
                            bns_details = pd.read_html("<html>"+str(psteps[each_range].table)+"</html>")[0]
                        except:
                            bns_details =pd.DataFrame(np.nan, index=range(1,18), columns = ['Name', 'Number', "Status", "Issued Date", "Expiry Date"])

                        for m, n in  zip(range(0,18), range(1,19)):
                            try:
                                otp_dict[f"Business Names{n}"].append(bns_details.loc[m, "Name"])
                            except :
                                otp_dict[f"Business Names{n}"].append("")
                            try:
                                otp_dict[f"Business Number.{n}"].append(bns_details.loc[m, "Number"])
                            except:
                                otp_dict[f"Business Number.{n}"].append("")
                            try:
                                otp_dict[f"Business Status.{n}"].append(bns_details.loc[m, "Status"])
                            except:
                                otp_dict[f"Business Status.{n}"].append("")
                            try:
                                otp_dict[f"Business Issued Date.{n}"].append(bns_details.loc[m, "Issued Date"])
                            except:
                                otp_dict[f"Business Issued Date.{n}"].append("")
                            try:
                                otp_dict[f"BusinessExpiry Date.{n}"].append(bns_details.loc[m, "Expiry Date"])
                            except:
                                otp_dict[f"BusinessExpiry Date.{n}"].append("")
            otp_dict["Start Time"].append(start_time)            
            otp_dict["End Time"].append(datetime.now().strftime("%d-%m-%y %I:%M:%S"))                              
    else:
        otp_dict['OWCODE'].append(each_code)
        otp_dict['FullName'].append(company_name)
        for each_col in otp_dict.keys():
            if each_col not in ['FullName', 'OWCODE']:
                otp_dict[each_col].append("") 
        print(f'Company : {company_name.upper()} is not available')
    return otp_dict


if __name__ == "__main__":
    output = pd.read_excel("./WebScraping/Requests/BusinessRegistry/Output_format.xlsx") 
    otp_cols = output.columns.tolist()
    otp_dict = dict.fromkeys(otp_cols,[])
    otp_dict = {k:[] for k in otp_cols}
    input = pd.read_excel("./WebScraping/Requests/BusinessRegistry/Input.xlsx")
    for each_comp, each_code in zip(input['FullName'], input['OWCODE']):
        otp_dict = main(each_comp, each_code, otp_dict)
    pd.DataFrame(dict([(k,pd.Series(v)) for k,v in otp_dict.items()])).to_excel('./WebScraping/Requests/BusinessRegistry/final_output.xlsx', index=False)