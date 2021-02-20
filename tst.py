import subprocess
import os, sys
import requests


user = 'ak'
password = 'ak'

# pipeline script to validate 

# def call_jenkins():
#     params = {'jenkinsfile':'Jenkinsfile'}
#     res = requests.post('http://localhost:8080/pipeline-model-converter/validate', auth=(user, password), params=params ) 
#     print(res.text)

#     print(res.content)
def jen():
        
    file1 = 'Jenkinsfile'

    v = os.popen("curl -u ak:ak -X POST -F 'jenkinsfile=<Jenkinsfile' http://localhost:8080/pipeline-model-converter/validate")
    print(v)
    for values in v:
        print(values)
jen()
