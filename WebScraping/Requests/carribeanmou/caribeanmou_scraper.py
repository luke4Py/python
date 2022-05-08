import requests
import json
import pandas as pd
import re
import numpy as np

#CURRENT DETENTIONS

cr_det_url = 'https://caribbeanmou.org/content/inspection-detention-data'
try:
    cr_det_data = pd.read_html(cr_det_url)
except:
    print('Issue with current Detentions link')

if len(cr_det_data)>0:
    cr_final_data = cr_det_data[0]
else:
    print("cr_det_data might be empty, confirm and check with UI")


#DETENTIONS
det_url = 'https://caribbeanmou.org/views/ajax'
data_list = []
page_num = 20
new_page_num = 2
count = 0
for i in range(0,page_num):
    if i < new_page_num :
        payload = {
        "page": i,
        "view_name": "detention_list",
        "view_display_id": "page_1",
        "view_args": "",
        "view_path": "node/99",
        "view_base_path": "detention-demo",
        "view_dom_id": "1",
        "pager_element": "0",
        "js": "true"
        }
        response = requests.post(det_url, headers = {"user-agent" :'Chrome'}, data = payload)
        response.status_code
        x = json.loads(response.content)[2]
        if count == 0:
            page_num_details = re.findall("Go to page\s*\d", x['data'])
            new_page_num = max([int(re.findall('\d+', each_page)[-1]) for each_page in page_num_details])
        data_list.append(pd.read_html(x['data'])[0])
        count+=1
    else:
        break

final_det_data = data_list[0].append(data_list[1:])
final_det_data.reset_index(drop=True, inplace = True)

viewdef_idx = np.where(final_det_data["Deficiency"].str.count('VIEW DEFICIENCIES >>') == 1.0)

def_data_list = []
for each_inspec in final_det_data.loc[viewdef_idx, "Inspection ID"]:
    def_url = f"https://caribbeanmou.org/deficiency-data/{int(each_inspec)}"
    def_data_list.append(pd.read_html(def_url)[1])
base_def_data = def_data_list[0].append(def_data_list[1:])
dummy_data = pd.DataFrame(np.nan, columns =['Inspection ID',	'Deficiency Code',	'Deficiency Description',	'Action Taken'], index=range(len(final_det_data)))
dummy_data.loc[pd.Index(viewdef_idx[0].tolist()),:] = base_def_data.set_index(pd.Index(viewdef_idx[0].tolist()))
final_det_data.merge(dummy_data, on=dummy_data.index, how='left')
final_detention_data = pd.concat([final_det_data, dummy_data], axis=1)



#INSPECTIONS
det_url = 'https://caribbeanmou.org/views/ajax'
insp_data_list = []
insp_page_num = 20
insp_new_page_num = 2
insp_count = 0
for i in range(0,insp_page_num):
    if i < insp_new_page_num :
        payload = {
        "page": i,
        "view_name": "Inspection_List_Updated",
        "view_display_id": "page_2",
        "view_args": "",
        "view_path": "node/99",
        "view_base_path": "inspection-data",
        "view_dom_id": "1",
        "pager_element": "0",
        "js": "true"
        }
        response = requests.post(det_url, headers = {"user-agent" :'Chrome'}, data = payload)
        response.status_code
        x = json.loads(response.content)[2]
        if insp_count == 0:
            insp_page_num_details = re.findall("Go to page\s*\d", x['data'])
            insp_new_page_num = max([int(re.findall('\d+', each_page)[-1]) for each_page in insp_page_num_details])
        insp_data_list.append(pd.read_html(x['data'])[0])
        insp_count+=1
    else:
        break


final_insp_data = insp_data_list[0].append(insp_data_list[1:])
final_insp_data.reset_index(drop=True, inplace = True)

viewinspdef_idx = np.where(final_insp_data["Deficiency"].str.count('VIEW DEFICIENCIES >>') == 1.0)
insp_def_list = []
failed_idx = []
for each_inspec, idx in zip(final_insp_data.loc[viewinspdef_idx, "Inspection ID"], viewinspdef_idx[0].tolist()):
    print(idx)
    try:
        def_url = f"https://caribbeanmou.org/deficiency-data/{int(each_inspec)}"
        insp_def_list.append(pd.read_html(def_url)[1])
    except:
        failed_idx.append(idx)
        print(f'{each_inspec} Shaip status not updated')
failed_idx = {322, 324, 325}
viewinspdef_idx = set(viewinspdef_idx[0])-set(failed_idx)
base_insp_data = insp_def_list[0].append(insp_def_list[1:])
dummy_insp_data = pd.DataFrame(np.nan, columns =['Inspection ID',	'Deficiency Code',	'Deficiency Description',	'Action Taken'], index=range(len(final_insp_data)))
dummy_insp_data.loc[pd.Index(list(viewinspdef_idx)),:] = base_insp_data.set_index(pd.Index(list(viewinspdef_idx)))
final_insp_data = pd.concat([final_insp_data, dummy_insp_data], axis=1)

# final_insp_data.to_excel("Inspections.xlsx")

with pd.ExcelWriter('caribbeanmou.xlsx',mode='ab') as writer: 
    cr_final_data.to_excel(writer, sheet_name='current dententions') 
    final_detention_data.to_excel(writer,sheet_name='Detentions')
    final_insp_data.to_excel(writer,sheet_name='Inspections')