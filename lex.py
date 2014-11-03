with open('sample.c') as f:
   data = f.read()

data = data.split('\n')

for i in range(len(data)):
   data[i] = data[i].strip()

while '' in data:
   data.remove('')

print(data)   
