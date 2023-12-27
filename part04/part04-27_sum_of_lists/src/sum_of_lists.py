# Write your solution here

def list_sum(integers1: list, integers2: list) -> list:
    des_list = []
    for i in range(len(integers1)):
        total = integers1[i] + integers2[i]
        des_list.append(total)
    return des_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
