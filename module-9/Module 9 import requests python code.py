import requests
import json

response = requests.get('https://swapi.dev/api/people/1')
print(response.status_code)

print("\n-- Unformatted Response --")
print(response.text)

print("\n--- Formatted Response ---")
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())