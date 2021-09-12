def main():
  file1 = open('input.txt', 'r')
  lines = file1.readlines()
  #print(lines)
  numbers = lines[0]
  #print(numbers)
  print(part1(numbers))

def part1(originalInput):
  sum = 0
  length = len(originalInput)
  for index in range(0,length):
    if (originalInput[index] == originalInput[(index+1)%length]):
      sum += int(originalInput[index])
  return sum

if __name__ == "__main__":
    main()
