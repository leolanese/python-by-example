def main():

# iterate using a function and a sentinel until end of line ''
  with open("./testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
      print(line)
      
if __name__ == "__main__":
    main()      
      
