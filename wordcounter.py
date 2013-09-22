import sys
import string

def word_position(filename):
  word_count = {}  
  input_file = open(filename, 'r')
  f = input_file.read()
  collection = list()
  terms = dict()
while True:
    try:
     i = f.index("<BODY>")+6
     j = f.index("</BODY>")
     collection.append(f[i:j])
     f = f[j+7:]
    except:
      break

  


  for doc in collection:
    doc_id = collection.index(doc)
    doc = doc.lower()

    for char in string.punctuation:
      doc = doc.replace(char,"")

    for char in "\n\t":
      doc = doc.replace(char," ")

    for token in doc.split(" "):
      if token == "": continue
      posting_list = terms.get(token,[])
      if not doc_id in posting_list:
        
        posting_list.append(doc_id)
        terms[token] = posting_list

  out_file = open('result.txt','w')
  for term in terms:
     out_file.write("[" + str(term)+"]" + str(terms[term])+"\n")
     
  input_file.close()  
  out_file.close()


def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordposition.py {-pos} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '-pos':
    word_position(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
