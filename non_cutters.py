def main():
    content_list = [] # list of sets
    for name in path_to_files:
        with open(name, 'r') as file:
            # Read lines and strip newline characters
            temp = file.read().split()
            temp = temp[3:]
            temp = [i[:-1] for i in temp] # delete commas
            temp = set(temp)
            content_list.append(temp)

    # for i in content_list:
    #     print(i)

    # Perform AND (intersection) on all sets in the listcle
    result = list(set.intersection(*content_list))

    # Print the result
    print(f'List of non-cutters for all files: {", ".join(result)}')

if __name__ == "__main__":
    path_to_files = ['pMal_non_cutters.txt', 'pCMV-3Tag-1A_non_cutters.txt', 'pAcUW51_non_cutters.txt']
    main()