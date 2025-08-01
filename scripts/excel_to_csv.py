import os
import sys
from utils import get_input_path, convert_file


def main():
    """
    Converts an Excel file to CSV.
    """
    input_path = get_input_path("excel")

    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        sys.exit(1)

    if os.path.isdir(input_path):
        files = os.listdir(input_path)
        if not files:
            print(f"Error: No files found in {input_path}")
            sys.exit(1)
        input_file = os.path.join(input_path, files[0])
    else:
        input_file = input_path

    converted_data = convert_file(input_file, "excel-to-csv")

    if converted_data:
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + ".csv"
        output_path = os.path.join("data", "output", output_filename)
        with open(output_path, "w") as f:
            f.write(converted_data)
        print(f"Successfully converted {input_file} to {output_path}")


if __name__ == "__main__":
    main()
