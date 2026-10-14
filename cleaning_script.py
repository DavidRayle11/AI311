import re 
import string

##
#This file is meant to be the preprocessing file that will
#make the text uniform, remove URLs, HTML tags, punctuation, and numbers
#clean the extra spaces that are within the every email
## 

def clean_text(text):
    text = text.lower() #lowercase 
    text = re.sub(r"http\S+|www\S+", "", text) #url removal
    text = re.sub(r"<.*?>", "", text) #http removal
    text = re.sub(f" [{string.punctuation}]", "", text) #punctuation removal
    text = re.sub(r"\d+", "", text) #number removal
    text = text.strip() #remove spaces 
    return text

df["Cleaned_text"] = df["Email Text"].apply(clean_text)

print(df[["Email Text", "Cleaned_text"]].head())