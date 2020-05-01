
import pdb
import pprint

f = open("../data/My Clippings.txt", mode= "r", encoding="utf-8-sig")
#f = open('file', mode='r', encoding='utf-8-sig')

count = 0

results = []
data = []

#pdb.set_trace()

note = False
for line in f:
  line = line.strip("\ufeff")
  count += 1
  #if count == 200: break

  if line.strip() == "": continue

  if line[:7] == "=======":
    if note:
      results[-1].append[data[1]]
      results[-1].append(data[2])
      note = False
      data = []
      continue
    else:
      results.append(data)
      data = []
      continue

  if line[:10] == "- Your Note": note = True

  data.append(line.rstrip())

pp = pprint.PrettyPrinter()
#pp.pprint(results)
for r in results:
  if len(r) > 3:
    print(r)
  #print(r[1])
#print(results[1])
#print(results[1][0] == "Thank You for Smoking: A Novel (Buckley, Christopher)")
#pdb.set_trace()







'''
  
  
  print(line[:14])




  if line.strip() == "": continue

  if line == "==========":
    results.append(data)
    data = []

  if line[:15] == "- Your Highligt": data.append


  data.append(line)
  
'''


"""
  
  Title/Author 
  Empty 
  Location
  Highlight 
  Note 
  Break = "=========="
  
  """