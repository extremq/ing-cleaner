import pandas as pd


def clean_transactions(input_file: str, output_file: str):
    # Read input file
    df = pd.read_excel(input_file, engine='xlrd')

    # Take subset of data starting from row 3 and use that as columns
    df.columns = df.iloc[3]
    df = df[4:]

    # Cut off the last 3 rows
    df = df[:-3]

    # Make Debit and Credit strings
    df['Debit'] = df['Debit'].astype(str)
    df['Credit'] = df['Credit'].astype(str)

    # Convert NaN to 0
    df['Debit'] = df['Debit'].replace('nan', 0)
    df['Credit'] = df['Credit'].replace('nan', 0)

    # Format date column and convert to string
    df['Data'] = pd.to_datetime(df['Data'], format='%Y%m%d')
    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

    # Write to xlsx
    df.to_excel(output_file, index=False)

    print("Done, saved to", output_file)
