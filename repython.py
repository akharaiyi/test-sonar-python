import sys, os
import re


values = "please  SONAR ANALYSIS call me when https://sonar.fmr.com/sonar/dashbaord you SONAR ScaN ctgsonarcustomgate  ctgsonarquality() please call me"
run_sonar = "https://localhost.fmr.com   SonarQube Server please check your lol"
prog = re.findall(r'sonar_\w+',  values, flags=re.I) # collect all values 
prog1 = re.findall(r'sonar[\s]+\w+', values , flags=re.I)
prog2 = re.findall(r'ctgsonar\w+\(\)', values, flags=re.I) 

# try https
prog4 = re.findall(r'https:\/\/sonar.fmr.com\/', values, flags=re.I)

final_sonar = prog + prog1 + prog2 + prog4
print(final_sonar)

def check_str():
    try:
        for val in final_sonar:
            if val in  values:
                if 'https://localhost' in run_sonar or 'SonarQube Server' in run_sonar: #define too string.
                    print('yes')
                    print('great job SUCCESS')
                else:
                    print('Please ran the sonar stage')
                    sys.exit(-1)
    except Exception as e:
        print(f'error {e}')                
             


def main():
    check_str() 




if __name__ == "__main__":   
    main()
   
