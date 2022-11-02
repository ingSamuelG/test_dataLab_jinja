from jinja2 import Environment, PackageLoader, select_autoescape
import requests
from const import CATS_FACTS_API_URL

def getCatFacts():
    response = requests.get(CATS_FACTS_API_URL)
    factsJson = response.json()["data"]
    onlyFacts = []
    for facts in factsJson:
        onlyFacts.append(facts["fact"])
    
    return onlyFacts

env = Environment(
    loader=PackageLoader("request"),
    autoescape=select_autoescape()
)

template = env.get_template("catFacts.html")
facts = getCatFacts()
htmlRender = template.render(facts =facts)

print(htmlRender)