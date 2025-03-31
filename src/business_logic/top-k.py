import pandas as pd
import heapq

def load_data(filepath='/merged_dataframe.csv'):
    df = pd.read_csv(filepath)
    df = df.dropna(subset=['ratingsCount', 'review/score'])
    return df

def calculate_popularity(row, metric='ratingsCount'):
    #Calculate popularity score for a book.
    #Options: 'ratingsCount', 'weighted' (ratingsCount * review/score), or custom.
    if metric == 'ratingsCount':
        return row['ratingsCount']
    elif metric == 'weighted':
        return row['ratingsCount'] * row['review/score']
    else:
        raise ValueError(f"Unknown metric: {metric}")

def get_top_k_books(df, k=10, metric='ratingsCount'):
    heap = []
    for _, row in df.iterrows():
        score = calculate_popularity(row, metric)
        book_info = {
            'Title': row['Title'],
            'score': score,
            'ratingsCount': row['ratingsCount'],
            'review/score': row['review/score']
            # more rows if wanted
        }
        if len(heap) < k:
            heapq.heappush(heap, (score, book_info))
        else:
            heapq.heappushpop(heap, (score, book_info))
    # highest score first
    return [book for (score, book) in sorted(heap, reverse=True)]

def top_k_books(k=10, metric='ratingsCount', filepath='Task2/merged_dataframe.csv'):
    df = load_data(filepath)
    return get_top_k_books(df, k, metric)

# Test
#if __name__ == '__main__':
    top_5 = top_k_books(k=5, metric='weighted')
    for book in top_5:
        print(f"Title: {book['Title']}, Popularity Score: {book['score']}")