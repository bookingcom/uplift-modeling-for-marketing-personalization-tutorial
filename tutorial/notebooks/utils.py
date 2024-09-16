import pandas as pd
from pandas import DataFrame

booking_colors = {
    'dark blue': '#003580',
    'light blue': '#009FE3',
    'yellow': '#FEBA02',
    'dark grey': '#666666',
    'light grey': '#F2F6FA',
}

booking_palletes = {
    'sequential_5' : [
        '#99C9FF',
        '#3394FF',
        '#006CE4',
        '#004899',
        '#003066'
    ],
    'sequential_10':[
        '#99C9FF',
        '#6BB1FF',
        '#3E99FF',
        '#2286F6',
        '#0B74EA',
        '#0064D3',
        '#0054B2',
        '#004593',
        '#003A7C',
        '#003066'
    ],
    'divergent': [
        '#006CE4',
        '#0091EA',
        '#00ACC1',
        '#00C853',
        '#FFD600',
        '#FFB700',
        '#F56700',
        '#D4111E'
    ],
    'qualitative': [
        '#006CE4',
        '#D4111E',
        '#FFB700',
        '#00C853',
        '#9C27B0',
        '#00ACC1',
        '#6200EA',
        '#F56700',
        '#0091EA',
        '#FFD600'
    ]
}


def create_feature_cumulative_buckets(features_df: DataFrame, number_of_buckets: int, feature: str) -> DataFrame:
    """Creates a DataFrame with cumulative counts of a specified feature across a given number of score buckets.

    Args:
        features_df (DataFrame): The input DataFrame containing the data to be processed.
        number_of_buckets (int): The number of buckets to divide the score into.
        feature (str): The name of the feature/column to analyze.

    Returns:
        DataFrame: A DataFrame containing the cumulative counts of the specified feature across the buckets.
                  The DataFrame includes columns for the feature, bucket, count, and cumulative count.
    """
    
    # Create buckets for the score column
    features_df['score_bucket'] = pd.cut(features_df['score'], bins=number_of_buckets, labels=False)

    # Group by bucket and feature, then count occurrences
    grouped_df = (
        features_df.groupby(["score_bucket", feature])
        .size()
        .reset_index(name="count")
        .sort_values(["score_bucket", feature])
    )

    # Get unique values for the feature and buckets
    unique_feature_values = features_df[feature].unique()
    unique_bucket_values = features_df['score_bucket'].unique()

    # Generate all possible combinations of feature values and buckets
    all_combinations = pd.MultiIndex.from_product(
        [unique_feature_values, unique_bucket_values], 
        names=[feature, 'score_bucket']
    )

    # Create a DataFrame from the combinations
    all_combinations_df = pd.DataFrame(index=all_combinations).reset_index()

    # Merge the combinations with the grouped counts
    merged_df = pd.merge(
        all_combinations_df, grouped_df, 
        on=[feature, 'score_bucket'], 
        how='left'
    )

    # Replace NaN values in the count column with 0
    merged_df["count"] = merged_df["count"].fillna(0)

    # Sort by bucket and feature for clarity
    merged_df = merged_df.sort_values(["score_bucket", feature])

    # Calculate the cumulative count for each feature across buckets
    merged_df['cum_count'] = merged_df.groupby(feature)['count'].cumsum()

    return merged_df.reset_index(drop=True)