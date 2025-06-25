import yaml
def get_yaml_data(yaml_file):
    with open(yaml_file, 'r',encoding="UTF-8") as file:
        file_data = file.read()

        data = yaml.load(file_data,Loader=yaml.SafeLoader)
        return data