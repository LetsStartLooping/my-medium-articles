import pandas as pd
import inspect

# Gives the list of parameters passed in the init method of a class
def get_init_params(class_name):
    method_params = inspect.signature(class_name.__init__).parameters
    param_names = [p for p in method_params if p != 'self']

    return param_names

class ObjectDB:

    # This method can be used to convert a single DataFrame row to a single Class object
    @classmethod
    def init_pandas(cls, data):
        item = cls(*tuple(data))
        return item
    
    # Convert a DF with multiple rows to list of class objects
    @classmethod
    def init_pandas_list(cls, data):
        data.fillna("", inplace=True)
        items = [cls(*tuple(row)) for index, row in data.iterrows()]
        return items

    # Convert a list of class objects to DF
    @classmethod
    def df(cls, items):
        cls_df = pd.DataFrame([item for item in items])
        cls_df.columns = get_init_params(cls)
        
        return cls_df
    
    def __iter__(self):
        list_vars = [self.__dict__[var] for var in get_init_params(self)]
        return iter(list_vars)
    


