# ### import necesary packages
# import requests

# ### function to extract annotations from abstract as a JSON file
# def get_annotations(abstract, pmid):
# 	"""
#     Extracts annotations from the abstract of a specified PubMed article
#     and saves the results as a JSON file named after the PMID.

#     Arguments:
#         abstract (str): The abstract of the PubMed article.
#         pmid (str): The PubMed ID to be used in naming the output file.

#     """

# 	## get annotations
# 	results = gilda.annotate(abstract)

# 	# convert the results to JSON (if it's not already in JSON format)
# 	results_json = json.dumps(results, indent=4)

# 	# Ssve the results to a json file named as the PubMed ID
# 	filename = f"{pmid}.json"
# 	with open(filename, 'w') as json_file:
# 		json_file.write(results_json)

# 	print(f"Results have been saved to {filename}")



### import necessary packages
import requests
import json

### function to extract annotations from abstract as a JSON file
def annotate(abstract, pmid):
	"""
    Extracts annotations from the abstract of a specified PubMed article
    using the Gilda web service and saves the results as a JSON file named 
    after the PMID.

    Arguments:
        abstract (str): The abstract of the PubMed article.
        pmid (str): The PubMed ID to be used in naming the output file.

    """

	## URL to use the annotate endpoint
	url = "https://grounding.indra.bio/annotate"
	## extract annotations from abstract
	res = requests.post(url, json={'text': abstract})
	## store as a json object
	results = res.json()

	## save results as <PMID>.json file
	filename = f"{pmid}.json"
	with open(filename, 'w') as file:
		json.dump(results, file)

	print(f"Results have been saved to {pmid}.json")
	## return a json file of results
	return res.json()


