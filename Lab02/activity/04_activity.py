import re

pattern = r'^[A-Za-z_$][A-Za-z]' 

namingConvention= input("Enter Java naming convention : ")


if re.match(pattern,namingConvention):
    print("Java naming convention passed")
else:    
    print("Java naming convention failed")