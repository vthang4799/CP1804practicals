def main():
  for num in range(20):
    if num % 2 != 0:
      print(num)
  for i in range(0, 110, 10):
      print(i, end=' ')
  for j in range(20, 0, -1):
      print(j, end=' ')
  number_of_lines = int(input("Enter the number: "))
  for num in range(1, number_of_lines+1):
    print("*" * num)
if __name__ == '__main__':
    main()