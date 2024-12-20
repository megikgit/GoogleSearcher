import requests
import fake_useragent
from bs4 import BeautifulSoup as BS
import colorama
import pyfiglet

def convert_to_str(li: list) -> str:
    string = ""
    for el in li:
        string += el
    
    return string

def parse_links(prompt: str, count: int) -> list:
    links = []
    
    prompt = prompt.split()
    
    # Converting
    for i, letter in enumerate(prompt):
        if letter == " ":
            prompt[i] = "%20"
    
    prompt = convert_to_str(prompt)
    
    # Main Link
    link = f"https://google.com/search?q={prompt}"
    
    # Get html syntax
    response = requests.get(link, headers={"User-Agent": fake_useragent.UserAgent().random})
    html = response.content
    
    # Get searchable content
    soup = BS(html, "lxml")
    
    # Get Elements
    elements = soup.find_all("a", limit=count)
    
    # Parse links
    for element in elements:
        try:
            if element["href"].find("https://") != -1:
                links.append(element["href"])
        except KeyError:
            print("Useless link found: No \"href\" attribute found.")
    
    return links

if __name__ == "__main__":
    print(colorama.Fore.LIGHTYELLOW_EX)
    pyfiglet.print_figlet("CONSOLE BROWSING")
    print(colorama.Fore.LIGHTCYAN_EX)
    pyfiglet.print_figlet("Prompt: ")
    prompt = input()
    try:
        print(colorama.Fore.RED)
        pyfiglet.print_figlet("Max links (Number): ")
        count = int(input())
    except ValueError:
        print("Don't enter text into number input")
        quit()
    links = parse_links(prompt, count)
    print(colorama.Fore.MAGENTA)
    for link in links:
        print(link)
        for x in range(50):
            print("-", end = "")
        print()
