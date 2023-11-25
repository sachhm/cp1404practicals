"""
CP1404/CP5632 Practical
Wiki
"""
import wikipedia

try:
    user_input = input("Enter a page title or search phrase: ")
    while user_input != "":
        user_page = wikipedia.page(user_input, auto_suggest=False)
        print(f"Title: {user_page.title}")
        print(f"URL: {user_page.url}")
        print(f"Summary: {user_page.summary}")
        user_input = input("Enter a page title or search phrase: ")
except wikipedia.exceptions.DisambiguationError as disambiguation_error:
    print(f"{user_input} yields multiple potential choices:")
    print(disambiguation_error.options)
