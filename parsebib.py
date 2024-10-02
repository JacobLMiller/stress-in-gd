import re


pattern = r'@(\w+)\{((?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*)\}'

with open('bib/references.bib','r') as fdata:
    text = fdata.read()

import bibtexparser
bibs = bibtexparser.parse_string(text)
import json 
# json.dumps(bibs.entries_dict,indent=4)

for name,entry in bibs.entries_dict.items():
    print(entry)

with open("webcrawl-data.json", 'r') as fdata:
    data = json.load(fdata)

print(len(data))

import requests

def get_doi_bibtex(doi):
    base_url = f"https://doi.org/{doi}"
    headers = {
        "Accept": "application/citeproc+json"
    }
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        return response.text.strip()
    else:
        print(response.status_code)
        print(response.text)
        return None
    
def jsonToEntry(data):
    try: 
        obj = {
            "id": data["author"][0]["family"] + str(data["published"]["date-parts"][0][0]),
            "title": data["title"],
            "booktitle": data["container-title"], 
            "doi": data["DOI"],   
            "citation_count": data["is-referenced-by-count"], 
            "keywords": "None"
        }
        return obj
    except: 
        return None

import tqdm
import time
new_data = list()
for entry in tqdm.tqdm(data):
    if entry['id'] == "unknown":
        doiData = get_doi_bibtex(entry['doi'])
        if not doiData: continue 
        doiData = json.loads(doiData)
        
        with open("test.json", 'w') as fdata:
            json.dump(doiData,fdata,indent=4)

        newEntry = jsonToEntry(doiData)
        if newEntry:
            new_data.append(newEntry)
        time.sleep(0.1)


data = [e for e in data if e['id'] != "unknown"]
data.extend(new_data)

with open("updated-crawl.json", 'w') as fdata:
    json.dump(data,fdata,indent=4)


