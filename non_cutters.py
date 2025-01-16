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
        print(f"Error: File {file_path} not found and will not be processed.")
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
        print(f"List of non-cutter restriction enzymes: {', '.join(sorted(result))}")
    else:
        print("No common non-cutters found across all files.")

if __name__ == "__main__":
    file_list = ['./files/insertion.txt', './files/pcDNA3.1_myc_His.txt', './files/pAcUW51_non_cutters.txt']
    main(file_list)