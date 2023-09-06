from langchain.tools import BaseTool
from typing import Any, List
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()
api_key = os.environ.get("NEYNAR_SQL_API_KEY")

class AddressesToFidTool(BaseTool):
    name = "Addresses to Farcaster ID"
    description = '''
    As soon as you find an address for an entity or list of addresses, you must use this tool next to get the associated FIDs.
    You will need the FID to do the next step, finding content created by this FID.
    '''

    def _run(self, addresses: List[str]):
        url = 'https://data.hubs.neynar.com/api/queries/12/results'
        params = {'api_key': api_key}
        payload = {
            "max_age": 1800,
            "parameters": {
                "addresses": ",".join(x.strip().lower() for x in addresses)
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, params=params, headers=headers, json=payload).json()
        if "query_result" not in list(response.keys()):
            if "job" not in list(response.keys()):
                raise ValueError("Error while trying to find matches. Is your API key valid?")
            else:
                time.sleep(1)
                response = requests.post(url, params=params, headers=headers, json=payload).json()
                if "query_result" not in list(response.keys()):
                    raise ValueError("Error while trying to find matches. Is your API key valid?")
                
        rows = response["query_result"]["data"]["rows"]
        result = {}
        for row in rows:
            for addr in row["verified_addresses"]:
                if addr.lower() in addresses:
                    result[addr.lower()] = {
                        "username": row["fname"],
                        "fid": row["fid"]
                    }
        return result

    def _arun(self, task: Any):
        raise NotImplementedError("This tool does not support async")

# curl -X POST 'https://data.hubs.neynar.com/api/queries/12/results?api_key=asdfjka' -d '{"max_age": 1800, "parameters": {"address": "0x0916c04994849c676ab2667ce5bbdf7ccc94310a"}}'