#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, strVal):
    if (isinstance(strVal, str)):
      self._value = strVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    strVal = self.value
    if(strVal[len(strVal) - 1] == "."):
      return True
    else:
      return False
    
  def is_question(self):
    strVal = self.value
    if(strVal[len(strVal) - 1] == "?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    strVal = self.value
    if(strVal[len(strVal) - 1] == "!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    sentences = re.split(r'[.?!]', self.value)
    #print(sentences)
    true_sentences = [string for string in sentences if string]
    #print(true_sentences)
    return len(true_sentences)

#complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
#complex_string.count_sentences()