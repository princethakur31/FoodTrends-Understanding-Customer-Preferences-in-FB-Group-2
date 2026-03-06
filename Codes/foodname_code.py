
import pandas as pd
import re

# Load your CSV file
df = pd.read_csv('food_ip.csv')

# Comprehensive food keywords list
food_keywords = {
    'pizza', 'burger', 'cheeseburger', 'chicken burger', 'veggie burger', 'french fries', 'fries', 
    'hotdog', 'wrap', 'shawarma', 'sandwich', 'club sandwich',
    'biryani', 'chicken biryani', 'mutton biryani', 'veg biryani', 'pulao', 
    'veg pulao', 'chicken pulao', 'fried rice', 'jeera rice', 'lemon rice',
    'roti', 'chapati', 'naan', 'butter naan', 'garlic naan', 'paratha', 
    'aloo paratha', 'paneer paratha', 'kulcha',
    'dosa', 'masala dosa', 'idli', 'vada', 'medu vada', 'uttapam', 'pongal',
    'butter chicken', 'chicken tikka masala', 'chicken curry', 'mutton curry', 
    'fish curry', 'dal tadka', 'dal makhani', 'paneer', 'palak paneer',
    'tandoori chicken', 'chicken tikka', 'seekh kebab', 'tikka',
    'samosa', 'pakora', 'vada pav', 'pani puri', 'gol gappe', 'chaat', 
    'bhel puri', 'sev puri', 'dahi puri', 'aloo tikki',
    'noodles', 'chowmein', 'hakka noodles', 'manchurian', 'chilli chicken',
    'gulab jamun', 'rasgulla', 'rasmalai', 'jalebi', 'kulfi', 'ice cream', 'kheer'
}

def extract_food_items(post_text):
    if pd.isna(post_text):
        return None
    text_lower = str(post_text).lower()
    found_foods = []
    
    for food in food_keywords:
        if re.search(r'\b' + re.escape(food) + r'\b', text_lower):
            found_foods.append(food.title())
    
    return ', '.join(found_foods) if found_foods else None

# Extract food items from post_text column
df['food_items'] = df['post_text'].apply(extract_food_items)

# Save output CSV
df.to_csv('food_post.csv', index=False)

print("Food extraction complete! No food = NULL")
print("\nSample results:")
print(df[['post_text', 'food_items']].head(10))
