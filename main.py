import kagglehub
import pandas as pd
import os
from visuals import build_corr, build_lmplot

def main():
    output_dir = "instagram_analysis_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    path = kagglehub.dataset_download("rockyt07/social-media-user-analysis")
    file_path = os.path.join(path, "instagram_usage_lifestyle.csv")
    df = pd.read_csv(file_path)
    df = df.sample(n=50000, random_state=10)

    print(df.head())
    print(df.count())

    build_corr(
        df, 
        [
            'perceived_stress_score', 
            'daily_active_minutes_instagram', 
            'reels_watched_per_day', 
            'stories_viewed_per_day'
        ],
        [
            'stress', 
            'active minutes', 
            'reels consumption', 
            'stories consumption'
        ],
        'Correlation between stress and Instagram activity',
        output_dir
    )
    build_lmplot(
        df, 
        ['perceived_stress_score'], 
        [
            'daily_active_minutes_instagram', 
            'reels_watched_per_day', 
            'stories_viewed_per_day'
        ],
        output_dir
    )

    build_corr(
        df, 
        [
            'self_reported_happiness', 
            'time_on_feed_per_day', 
            'time_on_reels_per_day'
        ],
        ['happiness', 'feeds time', 'reels time'],
        'Correlation between happiness and times on feed_reels',
        output_dir
    )
    build_lmplot(
        df, 
        ['self_reported_happiness'], 
        [
            'time_on_feed_per_day', 
            'time_on_reels_per_day'
        ],
        output_dir
    )

    build_corr(
        df, 
        [
            'age', 
            'posts_created_per_week', 
            'followers_count'
        ],
        ['age', 'posts created', 'followers'],
        'Correlation between age and posts created_followers',
        output_dir
    )
    build_lmplot(
        df,
        ['age'], 
        [
            'posts_created_per_week', 
            'followers_count'
        ],
        output_dir
    )

    build_corr(
        df, 
        [
            'exercise_hours_per_week', 
            'sleep_hours_per_night', 
            'self_reported_happiness',
            'time_on_feed_per_day',
            'time_on_explore_per_day'
        ],
        ['exercise', 'sleep', 'happiness', 'feed', 'explore'],
        'Correlation between healthy lifestyle and happiness_lower compulsive usage',
        output_dir
    )
    build_lmplot(
        df, 
        ['exercise_hours_per_week', 'sleep_hours_per_night'], 
        [
            'self_reported_happiness', 
            'time_on_feed_per_day',
            'time_on_explore_per_day'
        ],
        output_dir
    )

if __name__ == "__main__":
    main()