import pandas as pd

def main():
    try:
        # Load dataset
        df = pd.read_csv("data.csv")

        print("\n===== DATASET INFO =====")
        df.info()

        print("\n===== FIRST 5 ROWS =====")
        print(df.head())

        print("\n===== STATISTICAL SUMMARY =====")
        print(df.describe())

        print("\n===== MISSING VALUES =====")
        print(df.isnull().sum())

        # Data Cleaning
        df = df.dropna()
        df = df.drop_duplicates()

        print("\n===== CORRELATION MATRIX =====")
        print(df.corr(numeric_only=True))

        # Save cleaned dataset
        df.to_csv("cleaned_data.csv", index=False)

        print("\n✔ Analysis Completed Successfully")
        print("✔ Cleaned file saved as cleaned_data.csv")

    except FileNotFoundError:
        print("❌ Error: data.csv file not found.")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()