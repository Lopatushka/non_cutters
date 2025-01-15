def process_file(file_path):
    """
    Reads a file Non-cutters from SnapGene and processes its content into a set of non-cutter resticteses.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.read().split()  # Read all lines and split into words
            lines = lines[3:]  # Skip the first three elements
            lines = {line[:-1] for line in lines}  # Remove trailing commas and convert to a set
        return lines
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return set()

def main(file_paths):
    """
    Reads non-cutter sequences from multiple files and finds their intersection.
    """
    # List to hold sets of non-cutter sequences
    content_sets = [process_file(file_path) for file_path in file_paths]

    # Filter out empty sets if any files were missing
    content_sets = [s for s in content_sets if s]

    if not content_sets:
        print("No valid data to process.")
        return

    # Perform intersection on all sets
    result = set.intersection(*content_sets)

    # Print the result
    if result:
        print(f"List of non-cutters for all files: {', '.join(sorted(result))}")
    else:
        print("No common non-cutters found across all files.")

if __name__ == "__main__":
    file_list = ['pMal_non_cutters.txt', 'pCMV-3Tag-1A_non_cutters.txt', 'pAcUW51_non_cutters.txt']
    main(file_list)


'''def main():
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
    main()'''