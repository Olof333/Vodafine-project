import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def main():
    input_df = pd.read_csv("vodafone-subset_20K.csv")
    statistics_df = pd.read_excel("all stats.xlsx").drop("Age", axis=1)

    apps_stat_dict = {
        "fb_count": "Facebook",
        "intagram_count": "Instagram",
        "telegram_count": "Telegram",
        "youtube_count": "YouTube",
        "steam_count": "Steam",
        "snapchat_count": "Snapchat",
        "twitter_count": "Twitter",
        "netflix_count": "Netflix",
        "dropbox_count": "Dropbox",
        "linkedin_count": "Linkedin",
        "itunes_count": "Itunes",
        "skype_count": "Skype",
        "tinder_count": "Tinder",
        "badoo_count": "Badoo",
        "whatsapp_count": "Whatsapp",
        "tumblr_count": "Trumblr",
        "uber_count": "Uber",
        "twitch_count": "Twitch",
    }

    for num, row in input_df.iterrows():
        total_variance = np.array([1 / 101] * 101)
        total_stat = []
        for name, value in row.iteritems():
            if name in apps_stat_dict and value >= 1:
                statistics = statistics_df[apps_stat_dict[name]].values / 100
                t_prod = total_variance * statistics
                total_variance = t_prod / np.sum(t_prod)
                total_stat.append(name)

        if total_stat:
            max_val = np.max(total_variance)
            amount = np.count_nonzero(total_variance == max_val)
            values = sorted(np.argpartition(total_variance, -amount)[-amount:])     #returns indexies (faster func)

            print(
                f"For row {num} the estimated age is in {{{', '.join([str(v) for v in values])}}}",
                f"with probability of {np.round(max_val*len(values)*100, 2)}% ({np.round(max_val*100, 2)}% for each)",
                # f"with {len(total_stat)} statistics used: {', '.join(total_stat)}",
                f"with {len(total_stat)} statistics used",
            )
            plt.bar(np.arange(101), total_variance)
            plt.show()
        else:
            print(f"Could not tell anything about row {num} :c")


if __name__ == "__main__":
    main()
