# 1.
# import re
#
# text = """
# Hello my name is Nikita
# age 26
# live in Torzhok city
# Apples
# Orange
# Elephant
# """
#
# pattern = r'\b[aeiouAEIOU][a-zA-Z]*[^aeiouAEIOU\s]\b'
#
# matches = re.findall(pattern, text)
#
# print(matches)


# 2.
# import re
# text = "https://www.example.com, ftp://ftp.example.com, http://another-example.com/page, httdp://subdomain.example.com/path/to/page.html, https://hostiq.ua/blog/what-is-url/"
# url_regex = r'(https?|ftp)://[^\s/$.?#]+\S*'
# matches = re.finditer(url_regex, text)
# for match in matches:
#     url = match.group(0)
#     print(url)

# 3.

# import re
#
# text = """
#         Пример текста
#         С большими
#         Буквами, урааа!!!
#        """
# regex = r'\b[A-ЯЁ][а-яё]*\b'
# matches = re.findall(regex, text)
# print(matches)


# 4.

# import re
#
# text = "Hello,book,letter,ori"
#
# regex = r'\b\w*(\w)\w*\1\w*\b'
#
# matches = re.findall(regex, text)
#
# print(matches)
