

url = "https://localhost:8080/ctg/job/test/job/test1/90/"
process = url.split('/')[0:-2]
result = ('/').join(process)
print(result)