# Social Media User Analysis

This project provides analysis for 1,000,000+ fully synthetic user profiles. The goal is to investigate how lifestyle factors (stress, exercise, sleep) correlate with social media consumption patterns (Reels, Feed, Stories).

## Keys

* Higher perceived stress → increased daily active minutes & more reels/stories consumption
* Lower self-reported happiness → longer sessions & higher feed/reels time
* Younger age → significantly higher reels watched, posts created, follower growth
* More exercise & better sleep → slightly higher happiness & lower compulsive usage

## Results

On the graphic, we can see that stress has a strong influence on the daily active minutes and reels/stories consumption. More stress — more active minutes and Instagram consumption.

![Stress Analysis](./instagram_analysis_plots/correlation_between_stress_and_instagram_activity.png)

On the scatter plot, we can see the strong relation between stress and instagram using.

![Stress Analysis](./instagram_analysis_plots/relationship_perceived_stress_score_vs_daily_active_minutes_instagram.png)

![Stress Analysis](./instagram_analysis_plots/relationship_perceived_stress_score_vs_reels_watched_per_day.png)

![Stress Analysis](./instagram_analysis_plots/relationship_perceived_stress_score_vs_stories_viewed_per_day.png)

Correlation between happiness and reels/feed time negative and equal approximiet -0.2. So unhappy people spend more time on Instagram and vice versa.

![Stress Analysis](./instagram_analysis_plots/correlation_between_happiness_and_times_on_feed_reels.png)

![Stress Analysis](./instagram_analysis_plots/relationship_self_reported_happiness_vs_time_on_feed_per_day.png)

![Stress Analysis](./instagram_analysis_plots/relationship_self_reported_happiness_vs_time_on_reels_per_day.png)

Age influences on posts created count negative and don't influence on followers count.

![Stress Analysis](./instagram_analysis_plots/correlation_between_age_and_posts_created_followers.png)

![Stress Analysis](./instagram_analysis_plots/relationship_age_vs_posts_created_per_week.png)

![Stress Analysis](./instagram_analysis_plots/relationship_age_vs_followers_count.png)

Healthy lifestyle (more exercises/better sleep) doesn't influence on happiness and Instagram usage because correlation almost 0 (0.001...).

![Stress Analysis](./instagram_analysis_plots/correlation_between_healthy_lifestyle_and_happiness_lower_compulsive_usage.png)

![Stress Analysis](./instagram_analysis_plots/relationship_exercise_hours_per_week_vs_self_reported_happiness.png)

![Stress Analysis](./instagram_analysis_plots/relationship_exercise_hours_per_week_vs_time_on_feed_per_day.png)

![Stress Analysis](./instagram_analysis_plots/relationship_exercise_hours_per_week_vs_time_on_explore_per_day.png)

![Stress Analysis](./instagram_analysis_plots/relationship_sleep_hours_per_night_vs_self_reported_happiness.png)

![Stress Analysis](./instagram_analysis_plots/relationship_sleep_hours_per_night_vs_time_on_feed_per_day.png)

![Stress Analysis](./instagram_analysis_plots/relationship_sleep_hours_per_night_vs_time_on_explore_per_day.png)

## How to Run

Clone the repository:
```bash
    git clone https://github.com/Nikita-Titarenko/instagram-analysis.git
```

Install dependencies:
```bash
    pip install pandas seaborn matplotlib kagglehub
```

Run
```bash
    python main.py
```