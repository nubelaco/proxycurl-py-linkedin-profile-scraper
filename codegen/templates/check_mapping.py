import json

with open("linkedin_mapping.json", "r") as f:
    linkedin_mapping: dict[str, dict[str, str]] = json.load(f)


endpoints = []
for command in linkedin_mapping:
    endpoints.append(linkedin_mapping.get(command).get("endpoint"))

print(len(endpoints))

with open("api_mapping.json", "r") as f:
    api_mapping: dict[str, dict[str, object]] = json.load(f)

api_mapping_endpoints = [
    endpoint
    for endpoint in api_mapping.get("endpoint")
]

print(len(api_mapping_endpoints))

for endpoint in api_mapping_endpoints:
    if endpoint not in endpoints:
        print(endpoint)
