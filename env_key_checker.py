import os

# Load the .env.example file
with open('.env.example') as example_file:
    example_keys = set(line.split('=')[0].strip() for line in example_file if '=' in line)

# Load the .env file
with open('.env') as env_file:
    env_keys = set(line.split('=')[0].strip() for line in env_file if '=' in line)

# Find missing keys
missing_keys = example_keys - env_keys

# Output the results
if missing_keys:
    print('Missing keys in .env:', missing_keys)
else:
    print('All keys are present in .env.')
