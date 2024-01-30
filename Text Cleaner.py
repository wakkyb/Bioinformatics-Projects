# Step 1: Take input from user
user_input = input("Enter some text: ")

# Step 2: Delete lines containing numbers
lines_without_numbers = [line for line in user_input.split('\n') if not any(char.isdigit() for char in line)]

# Step 3: Delete lines with text "logo"
lines_without_logo = [line for line in lines_without_numbers if "logo" not in line.lower()]

# Step 4: Delete lines with text "@"
lines_without_at = [line for line in lines_without_logo if "@" not in line]

# Step 5: Output the rest of the text
result = '\n'.join(lines_without_at)
print(result)
