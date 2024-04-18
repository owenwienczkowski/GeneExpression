# First, install GEOparse using pip if you haven't already
# pip install GEOparse

import GEOparse

# Define the GPL ID for which you want to retrieve the data
gpl_id = 'GPL570'

# Function to retrieve all GSM and GSE for a given GPL
def retrieve_gsm_gse(gpl_id):
    # Get the GEO platform object
    gpl = GEOparse.get_GEO(geo=gpl_id, destdir="./")

    # Retrieve all GSM entries related to the platform
    gsms = gpl.gsms.keys()
    print(f"Total GSM entries for {gpl_id}: {len(gsms)}")
    for gsm_id in gsms:
        print(f"GSM: {gsm_id}")

    # Retrieve all GSE entries related to the platform
    gses = gpl.gses.keys()
    print(f"Total GSE entries for {gpl_id}: {len(gses)}")
    for gse_id in gses:
        print(f"GSE: {gse_id}")

# Call the function with the GPL ID
retrieve_gsm_gse(gpl_id)
