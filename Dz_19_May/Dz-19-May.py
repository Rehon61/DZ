# 1.

# import re
#
# log_string = "2024-05-12 12:34:56 [INFO] Доброе утро!"
#
# pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
#
# matches = re.match(pattern, log_string)
#
# if matches:
#     date = matches.group(1)
#     time = matches.group(2)
#     log_level = matches.group(3)
#     message = matches.group(4)
#
#     print("Date:", date)
#     print("Time:", time)
#     print("Log Level:", log_level)
#     print("Message:", message)


# 2.
# import re
#
# def is_valid_password(password):
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#     if re.match(pattern, password):
#         return True
#     else:
#         return False
#
#
# password1 = "Password1@"
# password2 = "weakpassword"
# print(is_valid_password(password1))
# print(is_valid_password(password2))

# 3.
# import re
#
# def extract_table_data(html_string):
#     pattern = r'<table>(?:(?!<table>).)*?<tr>(?:(?!<tr>|</tr>).)*?<td>(?:(?!<td>|</td>).)*?([\w\s]+)(?:(?!<td>|</td>).)*?</td>(?:(?!<tr>|</tr>).)*?<td>(?:(?!<td>|</td>).)*?([\w\s]+)(?:(?!<td>|</td>).)*?</td>.*?</tr>(?:(?!<tr>|</table>).)*?</table>'
#     matches = re.findall(pattern, html_string, re.DOTALL)
#     return matches
#
# html_table = "<table><tr><td>Ку</td><td>Ку2</td></tr></table>"
# data = extract_table_data(html_table)
# print(data)


# 4.
# import re
#
#
# def extract_links(text):
#     link_pattern = r'(https?://\S+)|www\.\S+|([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})|([a-zA-Z]:\\\S+)'
#     matches = re.findall(link_pattern, text)
#
#     websites = [match[0] for match in matches if match[0]]
#     emails = [match[1] for match in matches if match[1]]
#     files = [match[2] for match in matches if match[2]]
#
#     result = {
#         "Ссылки": websites,
#         "Почты": emails,
#         "Файлы": files
#     }
#
#     return result
#
#
# text = "Вот почта на которую надо отправить example@mail.com тут будет находиться нужный файл C:\\Documents\\example.docx, так же прилагаю ссылку на сайт https://example.com"
# result = extract_links(text)
# print(result)








