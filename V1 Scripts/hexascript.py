import re

def decode_hex_string(hex_string):
    # Use the 'unicode_escape' decoding to turn hex into readable characters
    return hex_string.encode('utf-8').decode('unicode_escape')

def filter_and_decode_hex(input_text):
    # Regex to find hexadecimal sequences (e.g. \x64) within the text
    hex_pattern = r"(\\x[0-9a-fA-F]{2})+"
    
    # Function to decode the hex sequences and replace them in the text
    decoded_text = re.sub(hex_pattern, lambda x: decode_hex_string(x.group()), input_text)
    
    return decoded_text

def process_file(input_filename):
    # Read the input file
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Filter and decode hex strings in the content
    decoded_content = filter_and_decode_hex(content)

    # Write the decoded content back into the same file (overwrite) using UTF-8 encoding
    with open(input_filename, 'w', encoding='utf-8') as file:
        file.write(decoded_content)

    print(f"Decoded content has been saved to {input_filename}")

# Example usage
input_filename = r'WarCommander.js'  # Replace with your actual file path
process_file(input_filename)
