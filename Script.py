import urllib.request
import urllib.error
import sys

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
            if subdomain == "":
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

print(testing_subdomains(url))
print(urllib.request.urlopen("https://" + url))
