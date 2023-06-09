# CSC_498_Scripting
A project where we get to implement some ethical hacking and hack through some of the websites given to us using python

# Report

# Introduction
For this assignment, we had to write a Python script that would search a target website's subdomains, directories, and files. The script's objective is to expose hidden links that could point to vulnerable sites. The destination website's URL should be passed as an argument when running the script from the terminal. Two text files containing subdomains and directories were given to us, and we were told to parse the HTML code using regular expressions rather than third-party tools like BeautifulSoup.

# Implementation
The script is designed to take a URL argument and perform the following tasks:<br>
<ol>
<li>Discover subdomains by reading the provided text file and testing them against the target URL.</li>
<li>Discover directories by reading the provided text file and testing them against the target URL.</li>
<li>Fetch and parse the HTML content of the target website to find unique file links.</li>
</ol>

Below is a step-by-step explanation of the implemented code:<br>

<ol>
  <li>Importing required libraries: The code imports necessary libraries, such as urllib.request, urllib.error, sys, requests, and re.
</li>
  <li>Checking and storing the URL argument: The code checks if the URL is provided as an argument, stores it in a variable, and then proceeds with the rest of the script.
</li>
  <li>Defining testing_subdomains() function: This function reads the subdomains from the provided text file and tests them against the target URL. If a valid subdomain is found, it is added to the subdomains_output list. The results are then saved to the subdomains_output.bat file.
</li>
  <li>Defining fetch_HTML_files() function: This function sends an HTTP request to the target URL and decodes the response content. It then uses the re.findall() function to extract all href attributes containing file links. The extracted links are saved to the files_output.txt file.
</li>
  <li>Defining testing_dir() function: This function reads directories from the provided text file and tests them against the target URL. If a valid directory is found, it is added to the subdir_output list. The results are then saved to the dics_output file.
</li>
  <li>Executing functions: The code calls testing_subdomains(), fetch_HTML_files(), and testing_dir() functions with the target URL as an argument.</li>
</ol>

# Challenges

<ol>
<li>Handling various types of URL formats and schemes.
</li>
<li>Avoiding infinite loops caused by recursive links on the website.
</li>
<li>Handling website redirects, cookies, and sessions.
</li>
<li>Dealing with websites that use JavaScript to load content or build URLs dynamically.
</li>
<li>Managing performance and resource usage when scanning large websites.
</li>
<li>Handling different types of encoding and decoding errors while parsing HTML content.
</li>
<li>Respecting website's robots.txt rules and rate limiting.
</li>
</ol>

# Conclusion

The used Python script efficiently locates subdomains, directories, and files on a target website by using text files that have been supplied and regular expressions to parse HTML. It is simpler to analyze and find potential vulnerabilities in the web application because the script saves the results in separate output files.


