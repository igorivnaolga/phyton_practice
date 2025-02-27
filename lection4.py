# def filter_commas(text):
#     while ",," in text:
#         text = text.replace(",,", ",")
    
#     return text.strip(",")

# res = filter_commas("Hello,,,son , i'll visit you,,,, soon,,,,,,")
# print(res)

# import re
# def filter_commas_regex(text):
#     pattern = r",+"
#     return re.sub(pattern,",", text).strip(",")

# res = filter_commas_regex("Hello,,,son , i'll visit you,,,, soon,,,,,,")
# print(res)



# def encrypt(key, message):
#     message = message.upper()
#     res = ""
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     for letter in message:
#         if letter in alpha:
#             index = (alpha.index(letter) + key) % len(alpha)
#             res += alpha[index]
#         else:
#             res += letter
#     return res


# res = encrypt(3, "brute is a killerz!")
# # res = encrypt(-3, "EUXWH LV D NLOOHUC")
# print(res)


# def find_max_vowels_chain(text):
#     vowels = "aeiou"

#     for char in text:
#         if char.lower() not in vowels:
#             text = text.replace(char, ".")
    
#     print(text)
#     chains = text.split(".")
#     chains.sort(key=len)
#     max_chain = chains[-1]
#     return max_chain, len(max_chain)

# text = "To be or not to be this is the question"
# res = find_max_vowels_chain(text)
# print(res)


# cars = {
#     "Ford" : 2005,
#     "Mitsubishi" : 2000,
#     "BMW" : 2019,
#     "VW" : 2005,
# }

# names = cars.keys()
# print("|".join(names))

# print(cars.keys())


import re

# test_string = "asssd@gmail.com"
# pattern = "^ass.+com$"

# res= re.search(pattern, test_string)
# if res is not  None:
#     print("Match is found")


# def find_max_vowels_chain_regex(text):
#     pattern = r"[aeiou]+"
#     res = max(re.findall(pattern, text, flags=re.IGNORECASE))
#     print(res)

# text = "To be or not to be this is the question"
# find_max_vowels_chain_regex(text)



# sample_text = "Bot activity detected: 192.16.4.162, 69.168.21.11 looks suspicious"
# pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# res = re.findall(pattern, sample_text)
# print(res)


text = "People love Python"

print(re.match(r"Python", text))
print(re.search(r"Python", text))



def replace(x):
    return len(x.group()) * "*"

import re
text = " to be or not to be an idiot. Be a good coder!"
def replace_spam_words(text,spam_words):
    pattern = "|".join(spam_words)
    return re.sub(pattern, replace, text, flags=re.IGNORECASE)

res = replace_spam_words(text,["idiot","coder", "be"])
print(res)
