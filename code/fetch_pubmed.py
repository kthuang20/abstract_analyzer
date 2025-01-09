### import necessary packages
from Bio import Entrez

### email 
Entrez.email = "katie.huang830@gmail.com"

### function to get the PubMed entry
def get_pmid_entry(pmid):
	"""
    Retrieves a PubMed article entry for a given PMID.

    Arguments:
        pmid (str): The PubMed ID of the article.

    Returns:
        dict: The parsed PubMed article entry.
        None: If the PMID is invalid or causes an error.
    """

	## if PMID exists,
	try:
		## retrieve the pubmed article
		handle = Entrez.efetch(db="pubmed", id=pmid, rettype="xml", retmode="text")
		## read in the entry
		entry = Entrez.read(handle)
		## close handle
		handle.close()

	## if PMID does not exist
	except Exception as e:
		print(f"An error occurred while retrieving PMID {pmid}: {e}")
		return None
	
	return entry

### function to extract only the abstract
def extract_abstract(entry):
	"""
    Extracts the abstract from PubMed article entry for a given PMID.

    Arguments:
        entry (dict): The parsed PubMed article entry.

    Returns:
        str: The abstract of article.
    """

	## extract the abstract
	abstract = entry['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText']
	## concantenate all parts
	abstract = " ".join(abstract)
	return abstract



