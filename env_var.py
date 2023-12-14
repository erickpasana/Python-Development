import requests
import os

'[Environment]::SetEnvironmentVariable("sheety_Username", "Erick88", "User")'
sheety_end_point = 'https://api.sheety.co/b17d3c0b422c3d51ecc6636c25073af5/walks/workouts'
google_sheet_code = 'https://docs.google.com/spreadsheets/d/1w3mCLW2K49ViPLnCx6MPLsQcGYHeOzlwgAgIWNgvc5Y/edit#gid=248757316'

# env_var_command = $env:var_name='value'

APP_ID = 'f5fb5329'
API_KEY = '17c8a9516aa3fa34abc7d1945dc7abfe'
# sheety_Username = 'Erick88'
# sheety_pwd = 'GGnhC7@xDBtjb7^U'
prefix = 'sheeety_'
# APP_ID = os.environ.get('sheety_APP_ID')
# API_KEY = os.environ.get('sheety_API_KEY')

env_var_dict = {
    'APP_ID': APP_ID,
    'API_KEY': API_KEY
}
print(env_var_dict)
for key, value in env_var_dict.items():
    var_name = f"{prefix}{key}"
    env_var = f"{var_name}={value}"
    # os.environ[var_name]=value
    print(env_var)


# print(env_var_dict.items())

