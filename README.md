# Stress in GD
This repository is a work in progress to keep track of graph drawing and network visualization papers which utilize the stress metric.

# SurVis - Visual Literature Browser

![Screenshot](/doc/survis.png)

SurVis is a flexible online browser to present and analyze scientific literature. The system is made for authors of survey articles, theses, or books who want to share their references in a user-friendly way. All you need to start is a bib file and a list of keywords for your papers.

Test SurVis with a reference literature database: http://dynamicgraphs.fbeck.com

## How To Use SurVis for Your Literature Collection

Dowload the latest SurVis release or fork this repository.

To start SurVis, open 'src/index.html' in your browser.

The bibliography data is stored in 'bib/references.bib' in BibTeX format.

Supplemental data is contained in 'src/data/':
* 'tag_categories.js': list of special tag categories; they can be used as a prefix for the tags and appear, for instance, 'a:b' refers to tag 'b' in tag category 'a'
* 'authorized_tags.js': tags that are defined through a description (highlighted in SurVis, description appears as a tooltip)
* 'search_stopwords.js': a list of stopwords used to exclude terms from search queries
* 'papers_pdf' (optional): PDF files of the papers, please use the BibTeX id as a file name
* 'papers_img' (optional): PNG thumbnails for the papers, please use the BibTeX id as a file name

Please do not edit the files in 'src/data/generated/' because they are created automatically. 

After completing your changes, just run 'update_data.py' with Python 3. Reload SurVis in the browser to see the changed bibliography. The script will continue to check for updates on the bib file until you stop it.

If the edit mode is activated, BibTeX entries can be modified in the browser, but are not stored in the 'bib' directory. To make those changes persistent, use 'download BibTex' in SurVis and copy the BibTeX data to your bib file in the 'bib' directory. You can also use the features to save and load the data from local storage of the browser; be careful, however, these features are still experimental.

Further properties of SurVis, such as the title of the page, can be modified in the file 'src/properties.js'. For the publication of your literature collection, you should usually deactivate the edit mode in the properties ('editable = false;').

Enjoy SurVis and send feedback if you like.

## Learn more

We've published a paper about SurVis at VAST 2015 - please reference it if you use or want to refer to SurVis in one of your publications. 

Beck, Fabian; Koch, Sebastian; Weiskopf, Daniel: Visual Analysis and Dissemination of Scientific Literature Collections with SurVis. In: IEEE Transactions on Visualization and Computer Graphics (2015).

* DOI: http://dx.doi.org/10.1109/TVCG.2015.2467757
* Preview video: https://vimeo.com/136206061 