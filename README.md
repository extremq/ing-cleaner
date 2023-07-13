# ing-cleaner

`ing-cleaner` is a Python script designed to clean ING transaction reports. This script specifically handles `.xls` Excel files, where it performs various cleaning operations, and outputs a cleaned `.xlsx` Excel file.

## Script Usage

To use this script, simply run it from the command line with the following command:

```
python ing-cleaner.py --input your_file.xls --output cleaned_file.xlsx
```

Replace `your_file.xls` with the name (and path, if not in the same directory) of the ING transaction report you want to clean, and replace `cleaned_file.xlsx` with the desired name (and path) for the output file.

The `--output` argument is optional; if not provided, the script will output to `output.xlsx` by default.

## Cleaning Operations

The cleaning process performed by this script includes the following steps:

- Reads the input file using pandas and the 'xlrd' engine.
- Sets the DataFrame's column names based on the third row of the file.
- Removes the first four rows and last three rows.
- Converts the 'Debit' and 'Credit' columns to string data type.
- Replaces any 'NaN' values in the 'Debit' and 'Credit' columns with 0.
- Formats the 'Data' column and converts it to a string in the format 'dd/mm/yyyy'.
- Writes the cleaned DataFrame to an Excel file.

## Requirements

This script requires Python 3 and the following Python libraries:

- pandas
- xlrd
- os

## Notes

This script assumes that the data in the Excel file is structured in a specific way, so it may not work correctly if the structure of your Excel file is different. Please adjust the code accordingly if your file's structure differs.

This is my configuration:
![image](https://github.com/extremq/ing-cleaner/assets/45830561/7080f98e-f85e-4e0d-a412-26382cace7b0)


## Final Thoughts

`ing-cleaner` makes cleaning ING transaction reports simple and automated. Remember to replace the input and output file names with your actual file paths and desired output paths/names. Always ensure you have a backup of your original files before performing any operations.
