    @property
    def my_value(self):
        """The value property"""
        return self._my_value
  
    @my_value.setter
    def my_value(self, strVal):
        """my_value must be a string"""
    if isinstance(strVal, str):
      self._my_value = strVal
    else:
      print("The value must be a string.")