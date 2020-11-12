# import
from requests import get
import json
import pathlib
import os

def get_data(endpoint):
    print(endpoint)
    response = get(endpoint, timeout=20)
    if response.status_code >= 400:
        print(response.status_code)
        print(f"Request failed: { response.text }")
    return response.json()

if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()

    with open( root / "data/AA3_stops_street.json", 'r+') as filehandle:
        data = json.load(filehandle)
        new_data = get_data("https://data.police.uk/api/crimes-street/stops-street?lat=51.9042&lng=-2.10141")
        filehandle.seek(0)
        json.dump(new_data, filehandle, indent=4)

    with open( root / "data/AA3_all_crime.json", 'r+') as filehandle:
        data = json.load(filehandle)
        new_data = get_data("https://data.police.uk/api/crimes-street/all-crime?lat=51.9042&lng=-2.10141")
        filehandle.seek(0)
        json.dump(new_data, filehandle, indent=4)