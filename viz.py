import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

def key_dist(raw_df):
    # create 3x3 grid of subplots
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))

    # Add the main title
    fig.suptitle("keyword distribution", fontsize=15)
    # plot histogram in each subplot using Seaborn
    sns.countplot(x="category", data=raw_df)
    plt.savefig('./figs/keyword_distribution.jpeg')
    plt.show()

def Word_cloud(Keywords):
    stopwords = set(STOPWORDS) 
    comment_words = '' 

    # iterate through the csv file 
    for val in Keywords: 

        # typecaste each val to string 
        val = str(val) 

        # split the value 
        tokens = val.split() 

        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 

        comment_words += " ".join(tokens)+" "


    wordcloud = WordCloud(width = 1000, height = 600, 
                    background_color ='white', 
                    stopwords = stopwords, 
                    min_font_size = 10).generate(comment_words) 


    # plot the WordCloud image                        
    plt.figure(figsize = (10, 6), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.title("Keywords Word Cloud")
    plt.savefig('./figs/Keywords_Word_Cloud.jpeg')  
    plt.show() 
    
def plot_my_rank(raw_df,title):
    
    # create some data to plot
    reliance_df=raw_df[raw_df['domain']=='Reliance']['rank']
    croma_df=raw_df[raw_df['domain']=='croma']['rank']
    vijaysales_df=raw_df[raw_df['domain']=='vijaysales']['rank']
    amazon_df=raw_df[raw_df['domain']=='amazon']['rank']
    flipkart_df=raw_df[raw_df['domain']=='flipkart']['rank']
    top_rank_df=raw_df[raw_df['rank'].isin([1,2,3,4,5])]


    # create 3x3 grid of subplots
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(20, 10))

    # Add the main title
    fig.suptitle(title, fontsize=15)
    # plot histogram in each subplot using Seaborn
    sns.histplot(data=reliance_df, ax=axs[0, 0], bins=20)
    axs[0, 0].set_title("Reliance Rank distribution")

    sns.histplot(data=croma_df, ax=axs[0, 1], bins=20)
    axs[0, 1].set_title("Croma Rank distribution")

    sns.histplot(data=vijaysales_df, ax=axs[0, 2], bins=20)
    axs[0, 2].set_title("Vijaysales Rank distribution")

    sns.histplot(data=amazon_df, ax=axs[1, 0], bins=20)
    axs[1, 0].set_title("Amazon Rank distribution")

    sns.histplot(data=flipkart_df, ax=axs[1, 1], bins=20)
    axs[1, 1].set_title("Flipkart Rank distribution")

    # Generate a color palette using seaborn
    colors = sns.color_palette('pastel', n_colors=5)
    # turn off the last subplot in the bottom row
    top_rank_df.domain.value_counts().plot.pie(colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.legend(title='Domains', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title('Distribution for all keywords', fontsize=14)
    axs[1, 2].set_title("Top Five")
    # axs[1, 2].axis('off')
    # plt.savefig(f'./figs/{title}.jpeg')
    plt.tight_layout()
    plt.savefig(f'./figs/{title}.jpeg')
    plt.show()