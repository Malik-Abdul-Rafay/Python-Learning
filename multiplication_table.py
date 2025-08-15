try:
    table_num =  int(input("Enter Table Number: "))
    table_length =  int(input("Enter Table Number: "))

except RuntimeError as e:
    print(e)


for i in range(1, table_length + 1):
    print(f"{table_num} x {i} = {table_num * i}")