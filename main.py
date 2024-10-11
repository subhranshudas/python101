import requests



def greet(name):
    return f"Hello, {name}! Welcome to Python 101!"

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        joke = response.json()
        return f"Setup: {joke['setup']}\n\nPunchline: {joke['punchline']}"
    except requests.RequestException as e:
        print(f"an error occurred: {e}")
        return "Couldn't fetch a joke right now!"
    except (KeyError, ValueError) as e:
        print(f"error parsing: {e}")
        return "Received response but could not parse!"

def main():
    name = input("What's your name? ")
    greeting = greet(name)
    print(greeting)

    print("\nHere's a joke:")
    joke = get_random_joke()
    print(joke)


if __name__ == "__main__":
    main()