# CSC_498_Scripting
A project where we get to implement some ethical hacking and hack through some of the websites given to us using python

# Report
For this assignment, we had to write a Python script that would search a target website's subdomains, directories, and files. The script's objective is to expose hidden links that could point to vulnerable sites. The destination website's URL should be passed as an argument when running the script from the terminal. Two text files containing subdomains and directories were given to us, and we were told to parse the HTML code using regular expressions rather than third-party tools like BeautifulSoup.

# Implementation
The script is designed to take a URL argument and perform the following tasks:<br>
<ol>
<li>Discover subdomains by reading the provided text file and testing them against the target URL.</li>
<li>Discover directories by reading the provided text file and testing them against the target URL.</li>
<li>Fetch and parse the HTML content of the target website to find unique file links.</li>
</ol>
