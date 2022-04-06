import requests
from colorama import init, Fore, Back, Style
import os
os.system('cls')
init()
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Limited Blacklister")

check = True

def program():
    keyworderror = f"{Back.RED}{Fore.BLACK}[ERROR]{Back.BLACK}{Fore.WHITE} Keyword not found"
    keyword = ""
    keyword = str(input(f"{Back.BLUE}{Fore.BLACK}[INPUT]{Fore.WHITE}{Back.BLACK} Enter keyword: "))
    if keyword == "":
        print(f"{Back.RED}{Fore.BLACK}[ERROR]{Back.BLACK} Keyword not found")
        program()
    print(f"{Back.YELLOW}{Fore.BLACK}[PROCESSING]{Back.BLACK}{Fore.WHITE} Grabbing all IDS linked to keyword ")
    global check
    response = requests.get(
        f"https://catalog.roblox.com/v1/search/items?category=Collectibles&keyword={keyword}&limit=120&subcategory=Collectibles"
    )
    # e.g.
    # [{'id': 321570597, 'itemType': 'Asset'},
    #  {'id': 57603998, 'itemType': 'Asset'},
    try:
        ids_and_item_types = response.json()["data"]
    except:
        print(keyworderror)
    # e.g.
    # [321570597, 56935215, 57603998, 16641209, 108829742, 57038857]
    try:   
        just_the_ids = [datum["id"] for datum in ids_and_item_types]
    except:
        print(keyworderror)
        program()
    # e.g.
    # ['321570597', '56935215', '57603998', '16641209', '108829742', '57038857']
    ids_as_strings_instead_of_numbers = [str(id_) for id_ in just_the_ids]
    final = ", ".join(ids_as_strings_instead_of_numbers)
    if not final and check == True :
        check = False
        print(keyworderror)
        check = True
        program()
    elif check == True:
        check = False
        with open(f'Results/{keyword}.txt', 'w') as f:
            f.write(final)
        length = len(final)
        print(f"{Back.GREEN}{Fore.WHITE}[SUCCESS]{Fore.WHITE}{Back.BLACK}{Fore.GREEN} Saved{Fore.WHITE} {final} {Fore.GREEN}to: Results/{keyword}.txt")
        print(f"{Back.BLACK}{Fore.WHITE}-----------------------")
        check = True
        program()
program()

