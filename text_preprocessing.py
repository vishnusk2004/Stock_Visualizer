import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)

    # Handle missing values
    df.fillna('N/A', inplace=True)

    # Normalize text data
    df['Name'] = df['Name'].str.upper()

    # Save cleaned data
    df.to_csv('cleaned_stock_data.csv', index=False)
    print("Cleaned data saved to cleaned_stock_data.csv")

def main():
    clean_data('stock_data.csv')

if __name__ == '__main__':
    main()
