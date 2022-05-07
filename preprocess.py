import re
from typing import List

def remove_space_start_end(text:str):
  return text.strip()

def lowercase(text:str):
  return text.lower()

def only_alphabets(text:str):
  text = re.sub('[^a-zA-Z]',' ',text) 
  text = re.sub(' (rd|th|st) '," ", text)
  return text

def remove_multiple_space(text:str):
  return " ".join(text.split())

def preprocess(texts:List[str]):
  for text in texts:
    text = str(text)
    text = remove_space_start_end(text)
    text = lowercase(text)
    text = only_alphabets(text)
    text = remove_multiple_space(text)
  return texts