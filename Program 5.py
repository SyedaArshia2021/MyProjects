def count_words(filename):
   with open(filename) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("example_file.txt"))
