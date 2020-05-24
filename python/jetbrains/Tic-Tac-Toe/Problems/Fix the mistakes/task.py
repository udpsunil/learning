text = input()
words = text.split()
url_list = []
url = []
for word in words:
    if (
        word.casefold().startswith('https://')
        or word.casefold().startswith('http://')
        or word.casefold().startswith('www.')
    ):
        url_list.append(word)
for url in url_list:
    print(url)

