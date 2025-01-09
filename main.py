from code import *

### ask user for pubchem article id and save it as a string
# pmid = 123
pmid = "28546431"
# pmid = input("Enter the PubMed article ID of choice: ")

### retrive the entry
entry = get_pmid_entry(pmid)

### if article exists:
if entry:
    print("Successfully retrieved entry from PMID:", pmid)
    ## extract the abstract fprom the article
    abstract = extract_abstract(entry)
    ## get annotations
    get_annotations(abstract, pmid)
### otherwise,
else:
    print("Failed to retrieve entry from PMID:", pmid)
