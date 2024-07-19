import requests
import sys

# Function to create a new PasteBin paste
def create_paste(title, body_text, expiration='1M', listed=False):
    # Replace 'your_pastebin_api_key' with your actual PasteBin API key
    PASTEBIN_API_KEY = 'z3dlNB3wtM5rm_5qY8-5M0hF5QnitGIs' # <-- Insert your PasteBin API key here
    pastebin_url = 'https://pastebin.com/api/api_post.php'
    paste_data = {
        'api_dev_key': PASTEBIN_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 1 if not listed else 0,
    }
    response = requests.post(pastebin_url, data=paste_data)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get information about a Pokémon from the PokéAPI
def get_pokemon_info(pokemon_name):
    pokemon_name = pokemon_name.strip().lower()
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(pokeapi_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - Pokémon '{pokemon_name}' not found.")
        return None

# Function to get the Pokémon name from command line arguments
def get_pokemon_name():
    if len(sys.argv) < 2:
        print("Error: Pokémon name not provided.")
        sys.exit(1)
    return sys.argv[1]

# Function to construct the paste title and body text
def construct_paste_content(pokemon_info):
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    title = f"{name}'s Abilities"
    body_text = '\n'.join(f"- {ability}" for ability in abilities)
    return title, body_text

# Main function
def main():
    pokemon_name = get_pokemon_name()
    print(f"Getting information for {pokemon_name}...")
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        title, body_text = construct_paste_content(pokemon_info)
        print("Posting new paste to PasteBin...")
        paste_url = create_paste(title, body_text)
        if paste_url:
            print(f"Success! Paste created: {paste_url}")
        else:
            print("Failed to create paste on PasteBin.")

if __name__ == "__main__":
    main()
