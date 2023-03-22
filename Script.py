import urllib.request
import urllib.error
import sys
import requests
import re

if len(sys.argv) < 2:
    print("Please provide the url")
else: 
    first_arg = sys.argv[1]
    print("First arguemnt"+first_arg)


def testing_subdomains(target_url):
    subdomains_output = []
    with open("./subdomains_dictionary.bat") as file:
        for line in file:
            subdomain = line.strip()
            if subdomain[len(subdomain)-1] == ".":
                continue
            domain = subdomain + "." + target_url
            url = "http://" + domain
            print(domain)
            try:
                response = urllib.request.urlopen(url)
            except urllib.error.URLError:
                continue
            if response.code == 200:
                subdomains_output.append(domain)

    with open("./subdomains_output.bat", "w") as output_file:
        for domain in subdomains_output:
            output_file.write(domain + "\n")

    return subdomains_output

url = "testphp.vulnweb.com"

# print(testing_subdomains(url))

def fetch_HTML_files(target_url):
    try:
        response = requests.get("http://" + target_url)
        links = re.findall('href="(.*?)"', response.content.decode('utf-8'))
        with open("./files_output.txt", "a") as files_output_file:
            for link in links:
                files_output_file.write(link + "\n")
        return links
    except requests.exceptions.ConnectionError:
        return "No such domain"
print(fetch_HTML_files(url))

# def testing_dir(target_url):
#     subdomains_output = []
#     with open("./subdomains_dictionary.bat") as file:
#         for line in file:
#             subdomain = line.strip()
#             if subdomain[len(subdomain)-1] == ".":
#                 continue
#             domain = subdomain + "." + target_url
#             url = "http://" + domain
#             print(domain)
#             try:
#                 response = urllib.request.urlopen(url)
#             except urllib.error.URLError:
#                 continue
#             if response.code == 200:
#                 subdomains_output.append(domain)

#     with open("./subdomains_output.bat", "w") as output_file:
#         for domain in subdomains_output:
#             output_file.write(domain + "\n")

#     return subdomains_output

url = "testphp.vulnweb.com"
