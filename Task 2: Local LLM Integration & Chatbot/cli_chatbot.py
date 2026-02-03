import requests

API_URL = "http://127.0.0.1:8000/get_recipe"

print("Welcome to Recipe Chatbot! Enter your ingredients (comma separated). Type 'exit' to quit.")

while True:
    user_input = input("Ingredients: ")
    if user_input.lower() == "exit":
        break
    ingredients = [i.strip() for i in user_input.split(",")]
    response = requests.post(API_URL, json={"ingredients": ingredients}).json()
    if "recipe" in response:
        print(f"Recipe: {response['recipe']}")
        print(f"Steps: {response['steps']}\n")
    else:
        print(response["message"], "\n")
