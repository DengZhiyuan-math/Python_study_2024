import pandas as pd
import glob


# Step 1: Collect Data from Excel Files
def collect_data_from_excel_files(file_pattern):
    all_files = glob.glob(file_pattern)
    df_list = [pd.read_excel(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df


# Step 2: Rearrange Data in Increasing Order
def rearrange_data_increasing_order(df):
    sorted_df = df.apply(lambda x: x.sort_values().values)
    return sorted_df


# Step 3: Calculate Variance and Mean
def calculate_variance_and_mean(df):
    variance = df.var()
    mean = df.mean()
    return variance, mean


# Main function to execute the steps
def main():
    file_pattern = 'path/to/excel/files/*.xlsx'  # Update this path
    df = collect_data_from_excel_files(file_pattern)
    sorted_df = rearrange_data_increasing_order(df)
    variance, mean = calculate_variance_and_mean(sorted_df)

    print("Sorted DataFrame:\n", sorted_df)
    print("Variance of each column:\n", variance)
    print("Mean of each column:\n", mean)


if __name__ == "__main__":
    main()