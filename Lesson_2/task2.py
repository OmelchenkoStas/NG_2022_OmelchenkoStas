list = input().split(",")
print ("List: ", list)
list_without_duplicates = []
for i in list:
  if i not in list_without_duplicates:
    list_without_duplicates.append(i)

print ("list without duplicates: ", list_without_duplicates)