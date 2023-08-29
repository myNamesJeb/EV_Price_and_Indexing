import pandas as pd

def load_csv():
    df = pd.read_csv("/Users/beans/Documents/EVDB/EVdata.csv")
    # Remove dollar signs and commas, then convert 'Price' to float
    df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)
    return df

def best_matches(df, query):
    matches = df[df['Make/Model'].str.contains(query, case=False)]
    return matches

def isnotnan(row):
    if pd.isna(row['Tax Credit']):
        return 'N/A'
    else:
        return row['Tax Credit']

def main():
    df = load_csv()
    
    while True:
        print("\nOptions:")
        print("1: All matches")
        print("2: All data for best match")
        print("3: Price of best match")
        print("4: Tax Credit of best match")
        print("5: Range of best match")
        print("6: Battery Capacity of best match")
        print("7: All models sorted by price (highest to lowest) with Tax Credit")
        print("8: Exit")
        print("9: EM Tax Rebate")
        
        choice = input("Enter your choice: ")
        
        if choice == '8':
            print("Exiting. Have a great day!")
            break

        if choice != '7':
            query = input("Enter the Make/Model you're looking for: ")
        
        if choice == '1':
            print(f"All matches for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.to_string())
        elif choice == '2':
            print(f"All data for best match for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.iloc[0].to_string())
        elif choice == '3':
            print(f"Price of best match for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.iloc[0]['Price'])
        elif choice == '4':
            print(f"Tax Credit of best match for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.iloc[0]['Tax Credit'])
        elif choice == '5':
            print(f"Range of best match for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.iloc[0]['Range'])
        elif choice == '6':
            print(f"Battery Capacity of best match for {query}:")
            matches = best_matches(df, query)
            if matches.empty:
                print("No match found.")
            else:
                print(matches.iloc[0]['Battery Capacity'])
        elif choice == '7':
            sorted_df = df.sort_values(by='Price', ascending=False)
            print("All models sorted by price (highest to lowest) with Tax Credit:")
            for index, row in sorted_df.iterrows():
                print(f"{row['Make/Model']} - Price: {row['Price']} - Tax Credit: {isnotnan(row)}")
        elif choice == "9":
            matches = best_matches(df, query)
            if matches.empty:
                print('no matches...................... this is akward...')
            else:
                print(matches)
        else:
            print("Invalid choice. Quitting")
            quit()

if __name__ == "__main__":
    main()
