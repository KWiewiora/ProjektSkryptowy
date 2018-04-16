import facebook
import urllib3
import requests

token = 'EAACEdEose0cBAFFQqW6HCmzkaPnPmz3whglZAwN3c7CGqzAgGUf94pfBxbjpecEskTmqi9W3ag1jggJNOjAvv20fqsEvsWOrNARQdmwPuCG4enhJCL3vG1yXjvfZCsz8vXc6gFKEr2FTpiu5ZAUwpKQgtZAndTZBqW6jjbMcTGZCUKPEIB6CRgr421wHheOZAUZD'
graph = facebook.GraphAPI(access_token=token, version = '2.12')
post = graph.get_object(id="564534550592133", fields="name")

print (post['name'])
