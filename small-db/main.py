import yaml

class SmallDB():

    def __init__(self, file_path):
        self.file_path = file_path
        self.yaml_data = self.read_data()

    def read_data(self):
        # Try reading YAML file, if not exist then return an empty Dictionary
        try:
            with open(self.file_path, 'r') as yaml_file:
                data = yaml.load(yaml_file, Loader=yaml.FullLoader)
            return data if data is not None else {}
        except FileNotFoundError:
            print("YAML file not found")
            return {}
        
    def save_data(self):

        # Update YAML file with the latest data
        with open(self.file_path, 'w') as yaml_file:
            yaml.dump(self.yaml_data, yaml_file, default_flow_style=False)
        
    def insert_entry(self, key, value):

        # Read latest data from the file
        self.yaml_data = self.read_data()

        # Add new Values to existing Data
        self.yaml_data[key] = value

        # Update file with new Data
        self.save_data()
    
    def read_entry(self, key):
        if key in self.yaml_data:
            return self.yaml_data[key] 
        else:
            print(f"Key '{key}' not found.")
            return None

    def update_entry(self, key, value):
        # Read latest data from the file
        self.yaml_data = self.read_data()

        if key in self.yaml_data:
            self.yaml_data[key] = value
            self.save_data()
        else:
            print(f"Key '{key}' not found.")

    def delete_entry(self, key):
        # Read latest data from the file
        self.yaml_data = self.read_data()
        
        if key in self.yaml_data:
            del self.yaml_data[key]
            self.save_data()
        else:
            print(f"Key '{key}' not found.")

if __name__ == '__main__':

    file_path = 'test.yaml'
    my_small_db = SmallDB(file_path=file_path)

    my_small_db.insert_entry("api_call_ineterval_mins", 5)

    # my_small_db.insert_entry("api_calls_count", {"2023-10-07": 10})
    
    # # Read Existing List into a Python Dictionary
    # api_calls_count = my_small_db.read_entry("api_calls_count")

    # # Add new Entries
    # api_calls_count["2023-10-06"] = 20
    # api_calls_count["2023-10-05"] = 5

    # # Modify Count for Existing Entry for 2023-10-07
    # api_calls_count["2023-10-07"] = 50

    # # Then update the YAML File with the updated list
    # my_small_db.insert_entry("api_calls_count", api_calls_count)

    # my_small_db.delete_entry('api_call_ineterval_mins')
