import sys
import time


start = time.time()

class Disease:
    def __init__(self, nome, genes, percentage = 0):
        self.name = name
        self.genes = genes
        self.percentage = percentage



def fillIndexes(pattern, pattern_size, indexes):
  size = 0
  i = 1
  if len(indexes) == 0:
    1+1
  else:
    indexes[0] = 0
  while i < pattern_size:
    if pattern[i] == pattern[size]:
      indexes[i] = size + 1
      size += 1
      i += 1
    else:
      if size != 0:
        size = indexes[size - 1]
      else:
        indexes[i] = 0
        i += 1


def KMP(pattern, text, sub):
  text_size = len(text)
  pattern_size = len(pattern)
  indexes = [0] * pattern_size
  fillIndexes(pattern, pattern_size, indexes)
  i = 0
  j = 0
  count = j
  sum = 0
  while i < text_size and j<pattern_size:
    if pattern[j] == text[i]:
      i += 1
      j += 1
      count += 1   
    else:
      if j != 0:
        j = indexes[j-1]

        if count>sub-1:    
          sum += count
          pattern = pattern[count:]
          pattern_size = len(pattern)
          indexes = [0] * pattern_size
          fillIndexes(pattern, pattern_size, indexes)
          j = 0

        count = j
      else:
        i += 1
    if j == pattern_size or i == text_size:
      if count>sub-1:
        sum += count
        pattern = pattern[count:]
        pattern_size = len(pattern)
        indexes = [0] * pattern_size
        fillIndexes(pattern, pattern_size, indexes)
  return sum


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].percentage >= R[j].percentage:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


output = sys.argv[2]
input = sys.argv[1]

with open(input, 'r') as file:
  sub = int(file.readline().strip())
  DNA = file.readline().strip()
  num_disease = int(file.readline().strip())
  genes = []
  diseases = []
  for x in range(num_disease):
    info_disease = file.readline().split()
    genes = info_disease[2:]
    disease  = Disease(info_doencas[0],genes)
    genes = []
    diseases.append(disease)
  result = []

result_genes = 0
for x in range(len(diseases)):
  for y in range(len(diseases[x].genes)):

    if KMP(diseases[x].genes[y],DNA,sub)/len(diseases[x].genes[y])*100 >= 90:

      result_genes += 1
    doencas[x].percentage = round(result_genes/(len(diseases[x].genes))*100)
  result_genes = 0


merge_sort(diseases)

with open(output, 'w') as output_file:
  for diseases in diseases:
      output_file.write(f"{disease.name} -> {disease.percentage}%\n")

end = time.time()
time_passed = end - start
print("End of execution:", time_passed, "seconds")
