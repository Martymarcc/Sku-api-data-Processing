#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Importing required Libraries
import requests
import json
import time


# In[11]:


API_URL = "https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus"

# Retreiving records from API
def get_records():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve records from the API.")
        return None

#Filtering records to include only those created after Jan 1, 2022 
def filter_records(records):
    filtered_records = []
    for record in records:
        created_at_str = record.get("createdAt", "0")
        try:
            # Convert string to float and then to int to handle fractional seconds
            created_at = int(float(created_at_str))
            # Convert Unix timestamp to datetime
            created_date = time.gmtime(created_at)
            # Check if the record was created on or after Jan 1, 2022
            if created_date.tm_year >= 2022:
                filtered_records.append(record)
        except ValueError:
            print(f"Invalid createdAt value for record: {record}")
    return filtered_records

#Counting the # of filtered records
def count_records(records):
    return len(records)

#Saving file to a json file
def save_records_to_file(records, filename="filtered_records.json"):
    with open(filename, "w") as file:
        json.dump(records, file)
    print(f"Filtered records saved to {filename}")


# In[12]:


# Main function to retreieve, filter, count, and save records.
def main():
    records = get_records()
    if records:
        filtered_records = filter_records(records)
        count = count_records(filtered_records)
        print(f"Number of filtered records: {count}")
        save_records_to_file(filtered_records)


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




