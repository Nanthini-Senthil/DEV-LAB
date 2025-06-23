import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings

# Optional: Hide future warnings (only if desired)
warnings.simplefilter(action='ignore', category=FutureWarning)

# Sample dataset simulating chat messages
data = {
    'User': ['Anna', 'Ben', 'Anna', 'Diana', 'Ben'],
    'Message': [
        'Hey, are we still on for tonight?', 
        'Yes, let me confirm the time.', 
        'Cool, let me know.', 
        'The notes from the meeting are attached.', 
        'Reminder: team sync at 3 PM.'
    ],
    'Timestamp': ['2024-06-01 09:15', '2024-06-01 09:30', '2024-06-01 10:00', '2024-06-02 14:00', '2024-06-03 08:45'],
    'Topic': ['Plans', 'Confirmation', 'Follow-up', 'Meeting Notes', 'Reminder']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Add message length column
df['MessageLength'] = df['Message'].apply(len)

# 📊 Basic info
print("\n📊 DataFrame Info:")
print(df.info())

print("\n📝 Preview Data:")
print(df.head())

# 📈 Count of messages per user (fixed to avoid FutureWarning)
plt.figure(figsize=(6, 4))
sns.countplot(x='User', hue='User', data=df, palette='Set1', legend=False)
plt.title('Messages Sent by Each User')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 📊 Average message length by user
plt.figure(figsize=(6, 4))
df.groupby('User')['MessageLength'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Message Length per User')
plt.ylabel('Characters')
plt.tight_layout()
plt.show()

# 📆 Messages over time
plt.figure(figsize=(6, 4))
df.set_index('Timestamp').resample('D').size().plot(marker='o', color='green')
plt.title('Messages Over Time')
plt.ylabel('Number of Messages')
plt.tight_layout()
plt.show()

# ☁️ Word cloud from topics
text = ' '.join(df['Topic'])
wordcloud = WordCloud(background_color='white').generate(text)
plt.figure(figsize=(6, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Topic Word Cloud')
plt.tight_layout()
plt.show()
