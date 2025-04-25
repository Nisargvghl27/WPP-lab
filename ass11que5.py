# Given a dataset of concerts, count the number of concerts per (artist, venue), per year
# month. Make the resulting table be a wide table - one row per year month with a column
# for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
# to determine which (artist, venue) pairs to include in the result.
import pandas as pd

df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

counts = (
    df
    .groupby(['year_month', 'artist', 'venue'])
    .size()
    .rename('concert_count')
)

all_months = pd.period_range(df['year_month'].min(),
                             df['year_month'].max(),
                             freq='M')
all_pairs = pd.MultiIndex.from_product(
    [artists, venues],
    names=['artist', 'venue']
)
full_index = pd.MultiIndex.from_product(
    [all_months, artists, venues],
    names=['year_month', 'artist', 'venue']
)

full_counts = counts.reindex(full_index, fill_value=0)

wide = (
    full_counts
    .reset_index()
    .pivot(index='year_month',
           columns=['artist','venue'],
           values='concert_count')
)
wide.columns = [f"{artist} @ {venue}" for artist, venue in wide.columns]
wide = wide.sort_index(axis=1)