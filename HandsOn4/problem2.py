def eliminate_duplicates(input_list):
    position = 0
    unique_list = [input_list[position]]
    
    for index in range(len(input_list)):
        if input_list[index] != unique_list[-1]:
            unique_list.append(input_list[index])
            position += 1
    
    return unique_list

def main():
    list1 = [2, 2, 2]
    distinct_list1 = eliminate_duplicates(list1)
    print(distinct_list1)
    # Output: [2]
    
    list2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    distinct_list2 = eliminate_duplicates(list2)
    print(distinct_list2)
    # Output: [1, 2, 3, 4, 5]

if __name__ == '__main__':
    main()
