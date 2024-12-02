
import re

def filter_urls(input_file_path, regex_pattern, output_file_path):
    # Read the content of the input file
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Apply the regex pattern to extract URLs
    matches = re.findall(regex_pattern, content)
    
    # Write the matched URLs to the output file
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(matches))
    
    return output_file_path


