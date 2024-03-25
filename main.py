{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing required libraries to retrieve, filter, and save data:\n",
    "\n",
    "import requests\n",
    "import json\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieving the records from the the API.\n",
    "def get_records():\n",
    "    url = \"https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus\"\n",
    "    response = requests.get(url)\n",
    "    if response.status_code == 200:\n",
    "        return response.json()\n",
    "    else:\n",
    "        return None\n",
    "\n",
    "#Filtering records based on theh creation date\n",
    "def filter_records(records):\n",
    "    filtered_records = [record for record in records if float(record.get('createdAt', 0)) >= 1640995200]\n",
    "\n",
    "#Counting the number of filtered records.\n",
    "def count_records(records):\n",
    "    return len(records)\n",
    "\n",
    "#Saving filtered records to a JSON file\n",
    "def save_records_to_file(records, filename):\n",
    "    with open(filename, 'w') as file:\n",
    "        json.dump(records, file, indent=4) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total filtered records: 200\n"
     ]
    }
   ],
   "source": [
    "# Main function for executionn:\n",
    "\n",
    "def main():\n",
    "    # Retrieving the records from the API\n",
    "    records = get_records()\n",
    "    if records:\n",
    "        # Filtering records based on creation date (Which is on or after Jan 1 2022)\n",
    "        filtered_records = filter_records(records)\n",
    "        \n",
    "        # Counting the number of filtered records\n",
    "        count = count_records(filtered_records)\n",
    "        \n",
    "        # Saving filtered records to a file\n",
    "        save_records_to_file(filtered_records, 'filtered_records.json')\n",
    "        \n",
    "        # Prining total number of filtered records\n",
    "        print(f\"Total filtered records: {count}\")\n",
    "    else:\n",
    "        print(\"Failed to retrieve records from the API.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
