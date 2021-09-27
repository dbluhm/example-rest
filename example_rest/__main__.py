# Here are our imports
import fastapi

app = fastapi.FastAPI()

# This populates a list, so we can test our GET and DELETE functions,
# without having to submit a bunch of POST requests first
quotes = [
    "You were the chosen one!",
    "It was said that you would destroy the Sith, not join them!",
    "Bring balance to the force, not leave it in darkness!",
    "I HATE YOU!!",
    "You were my brother Anakin!",
    "I loved you!",
]


# Give us something at the root
@app.get("/")
async def root():
    return {"message": "Hello There!"}


# Return the full list
@app.get("/list/")
async def read_list():
    return quotes


# Return a list item by index
@app.get("/list/{item_id}")
async def read_item(item_id: int):
    if item_id >= len(quotes) or item_id < 0:
        return {"Sorry, that item doesn't exist!"}

    return {"Item " + str(item_id): quotes[item_id]}


# Delete an item from the list by a supplied index
@app.get("/delete/{item_id}")
async def del_item(item_id: int):
    if quotes[item_id] is not None:
        quotes.pop(item_id)
    return


# and lastly, append an item to the end of the list
@app.post("/append/")
async def post_item(quote: str):
    quotes.append(quote)
    return
