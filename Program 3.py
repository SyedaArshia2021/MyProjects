import json   
       
# Data to be written   
dict ={"fruit": "mango", "colour": "yellow", "type": "Alphonso"}   
       
# Converting to json    
json_op = json.dumps(dict, indent = 4)   
print(json_op)  
