# 18.05

# 1.
# import re
# texts = "А вот и я тут"
# texts2 = "вторая строка"
# texts3 = "треТья строка"
# texts4 = [texts, texts2, texts3]
# pattern = r'(?i)^[aeiouаеиоуэыюя].*[bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ]$'
# for text in texts4:
#  if re.fullmatch(pattern, text):
#    print(text)

# 2.
# import re
#
# text1 = "https://www.example.com"
# text2 = "ftp://ftp.example.com"
# text3 = "http://another-example.com/page"
# text4 = "httdp://subdomain.example.com/path/to/page.html"
# text5 = "https://hostiq.ua/blog/what-is-url/"
# url_regex = r'(https?|ftp)://[^\s/$.?#]+\S*'
# texts = [text1, text2, text3, text4, text5]
#
# for text in texts:
#     if re.fullmatch(url_regex, text):
#         print(text)

# 3.

# import re
# text = "Первая строка"
# text2 = "вторая строка"
# text3 = "треТья строка"
#
# regex = r'(?m)^(.*[А-ЯA-Z].*)$'
# matches = re.fullmatch(regex, text)
# if matches:
#     print(matches.group().strip())






# 4.

# import re
#
# text = "new world"
# text2 = "book it's strong"
# text3 = "My name is skrillex"
# text4 = "letter"
# texts = [text, text2, text3, text4]
# pattern = r'\b(\w*(\w)\2\w*)\b'
#
# for t in texts:
#     if re.search(pattern, t):
#         print(t)

