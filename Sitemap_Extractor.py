# %%
import re

# %%
def extract_sitemap(input_file_path, regex_pattern, output_file_path):
    # Read the content of the input file
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Apply the regex pattern to extract URLs
    matches = re.findall(regex_pattern, content)
    
    # Write the matched URLs to the output file
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(matches))
    
    return output_file_path




# %%
regex_pattern_studierenwerk=r"https:\/\/www\.studierendenwerk-muenchen-oberbayern\.de?/[a-zA-Z0-9\-\/]+"
regex_pattern_thRo=r"https:\/\/www\.th-rosenheim\.de?/[a-zA-Z0-9\-\/]+"

studierenwerk_raw='studierenwerk_raw.txt'
thRo_raw='thRo_raw_xml.txt'

studierenwerk_sitemap='studierenwerk_sitemap.txt'
thRo_sitemap='thRo_sitemap.txt'

# %%

studierenwerk_sitemap=extract_sitemap(studierenwerk_raw,regex_pattern_studierenwerk,studierenwerk_sitemap)
thRo_sitemap=extract_sitemap(thRo_raw,regex_pattern_thRo,thRo_sitemap)
