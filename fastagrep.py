import sys

FASTA_ID_START='>'            #indicator that a line contains name or desc of a genome

def fastagreper(file_in, file_out, keyword):
    with open(file_in, "r") as file0, open(file_out, "w") as file1:
        write_flag=False
        for line in file0:
            if FASTA_ID_START in line:
                write_flag = keyword in line
            if write_flag:
                file1.write(line)

def print_error_args():
    print(f"Invalid arguments provided.")
    print(f'Example: \tpython3 fastagrep.py input_file.fasta output_file.fasta keyword')
    return 0

def main():
    # Check if valid arguments are provided
    if len(sys.argv) != 4:
        return print_error_args()

    file_in  = sys.argv[1]
    file_out = sys.argv[2]
    keyword  = sys.argv[3]
    if not file_in.endswith(".fasta") or not file_out.endswith(".fasta"):
        return print_error_args()
    
    print(f"Fasta Grep")
    print(f"Reading sequences from: {file_in}")
    print(f"Writing selected sequences to: {file_out}")
    print(f"Key for selecting sequences: {keyword}")

    fastagreper(file_in, file_out, keyword)
    
    print(f"Fasta Grep: Complete")
    return 1

if __name__ == "__main__":
        main()