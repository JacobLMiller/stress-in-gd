import opencitingpy

def metaToDict(M):
    entry = {
        'id': M.author[0].split(",")[0] + M.year + M.source_title.replace(" ", ""),
        'title': M.title,
        'booktitle': M.source_title, 
        'doi': M.doi, 
        'citation_count': M.citation_count,
        'keywords': "None"
    }
    return entry

client = opencitingpy.client.Client()

roots = ['10.1007/978-3-540-31843-9_25', '10.1109/TVCG.2008.85', '10.1111/cgf.13187']
seen  = set(roots)

citations = list()
for depth in range(3):

    metadata = list()
    for paper in roots:
        print(paper)
        try: 
            metadata.append(client.get_metadata(paper)[0])
        except:
            citations.append({'id': "unknown", "doi": paper})
    citations.extend(metaToDict(M) for M in metadata)

    roots = list()
    for M in metadata:
        for paper in M.citation:
            if paper and paper not in seen:
                seen.add(paper)
                roots.append(paper)


    import json 
    with open("webcrawl-data.json", 'w') as fdata:
        json.dump(citations, fdata, indent=4)