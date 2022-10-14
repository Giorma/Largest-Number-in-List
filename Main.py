List = []

List_Size = int(input("Enter number of elements in list: "))

for i in range(1, List_Size + 1):
    elements_in_list = float(input("Enter element: "))
    List.append(elements_in_list)

print("Largest element is: ", max(List))
