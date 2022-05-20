favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("\nThe following languages have been mentioned.")
for language in sorted(set(favorite_languages.values())):
    print(language.title())