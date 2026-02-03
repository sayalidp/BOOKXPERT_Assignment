from fastapi import FastAPI
from pydantic import BaseModel
import json
from typing import List

# Load recipes
with open("recipes.json", "r") as f:
    recipes = json.load(f)

app = FastAPI()

class Query(BaseModel):
    ingredients: List[str]

def find_recipe(user_ingredients):
    matches = []
    for recipe in recipes:
        common = set(user_ingredients).intersection(set(recipe["ingredients"]))
        score = len(common) / len(recipe["ingredients"]) * 100
        if score > 0:
            matches.append((recipe, score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[0][0] if matches else None

@app.post("/get_recipe")
def get_recipe(query: Query):
    recipe = find_recipe([i.lower() for i in query.ingredients])
    if recipe:
        return {"recipe": recipe["name"], "steps": recipe["steps"]}
    else:
        return {"message": "No matching recipe found."}

@app.get("/")
def root():
    return {"message": "Welcome to Recipe Chatbot API. Use /get_recipe to get recipes."}
