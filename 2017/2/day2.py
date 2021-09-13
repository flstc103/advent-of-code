def main():
  lines = readinput('input.txt')
  values = processInput(lines)
  print(part1(values))
  print(part2(values))

def readinput(filename):
  file1 = open(filename, 'r')
  return file1.readlines()

def processInput(lines):
  values = []
  for line in lines:
    row = line.rsplit("\t")
    row = [int(x) for x in row]
    values.append(row)
  return values

def part1(values):
  checksum = 0
  for row in values:
    checksum += max(row)-min(row)
  return checksum

def part2(values):
  checksum = 0
  for row in values:
    row.sort()
    row.reverse()
    for i in range(0,(len(row)-1)):
      for j in range(i+1,len(row)):
        div=row[i]/row[j]
        if div==int(div):
          checksum += int(div)
  return checksum
  
if __name__ == "__main__":
    main()

