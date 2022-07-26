import requests

from constants import ENDPOINT_FILTER_BY_NAME

filter_name = ENDPOINT_FILTER_BY_NAME+'Es'

response = requests.get(filter_name)
response_json = response.json()

company_size = len(response_json['body']['results'])

if company_size < 1:
    print("No companies found", company_size)

elif company_size < 5:
    print("Normal number of companies found", company_size)

elif company_size > 4:
    print("Many companies found", company_size)
