
"""
Requirements:
Fetch Data: 
Write a Python script to perform an HTTP GET request to fetch JSON data from a public API (example URL: https://jsonplaceholder.typicode.com/todos).


Process Data with Conditional List Comprehension:
Extract titles from the JSON data, but only include those that contain a specific string (e.g., 'qui').
Implement this using list comprehension.


Display Results with f-Strings:
Format and print the filtered titles using f-strings.
Ensure that each printed title is a string.


Type Checking:
Demonstrate checking whether one of the extracted titles is of type int.

"""

import requests

example_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url = example_url)
response.raise_for_status()

data = response.json()
filter_string = "qui"

filtered_data = [title for title in data if filter_string in title["title"]]

number = 0
for i in filtered_data:
    if type(i["title"]) == str:
        number = number +1
        print(f'Title #{number} is: {i["title"]}')
    else:
        print("Title is not a string")

print(type(filtered_data[0]["title"]) == int)