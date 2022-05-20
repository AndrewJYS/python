import pprint

people = {'Ford': {'Occupation': 'Researcher', 'Gender': 'Male',
                   'Home Planet': 'Betelgeuse Seven', 'Name': 'Ford Prefect'},
          'Trillian': {'Occupation': 'Mathematician', 'Gender':'Female',
                       'Home Planet': 'Earth', 'Name': 'Tricia McMillan'},
          'Robot': {'Occupation': 'Paranoid Android', 'Gender': 'Unknown',
                    'Home Planet': 'Unknown', 'Name': 'Marvin'},
          'Arthur': {'Occupation': 'Sandwich-Maker','Gender': 'Male',
                     'Home Planet': 'Earth', 'Name': 'Arthur Dent'}}

pprint.pprint(people)