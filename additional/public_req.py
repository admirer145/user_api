import requests

def get_random_joke():


    url = "https://v2.jokeapi.dev/joke/Any?amount=5"
    # params = {
    #     "category": "Programming",
    #     "contains": "Python",
    #     "amount": 5,
    #     "lang": "en",
    #     "format": "json"
    # }

    # url = "https://official-joke-api.appspot.com/random_joke"
    
    response = requests.get(url)
    json_resp = response.json()
    jokes_list = json_resp["jokes"]
    first_joke = jokes_list[0]

    print(first_joke)
    
    # if response.status_code == 200:
    #     data = response.json()
    #     print(f"{data['setup']} - {data['punchline']}")
    # else:
    #     print(f"Failed to get joke. Status code: {response.status_code}")

# if __name__ == "__main__":
#     get_random_joke()


# https://official-joke-api.appspot.com/random_ten
# https://official-joke-api.appspot.com/jokes/{type}/random
# https://official-joke-api.appspot.com/jokes/{type}/10
# https://official-joke-api.appspot.com/jokes/15

# url = "https://v2.jokeapi.dev/joke/Any"
# params = {
#     "category": "Programming",
#     "contains": "Python",
#     "amount": 5,
#     "lang": "en",
#     "format": "json"
# }

get_random_joke()

# import requests

# username = "admirer145"
# url = f"https://api.github.com/users/{username}/repos"

# response = requests.get(url)

# for repo in response.json():
#     print(repo["name"], repo["html_url"])