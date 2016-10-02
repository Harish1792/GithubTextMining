import string
import unicodedata


data = "hi,hello how are you?"
text_nopunc=data.translate(string.maketrans("",""), string.punctuation)
print text_nopunc