user_info=dict(
    name="Anas",
    age=21,
    fav_movies=['KGF','300']
)

# how to add data 
# user_info['fav_songs']=['song1','song2' ]
# print(user_info)

# pop method

# popped_item=user_info.pop('fav_songs')
# print(f"popped item is {popped_item}") 
# print(user_info)

# popitem method  (For Random Deletion)

# popped_item=user_info.popitem()  
# print(f"popped item is {popped_item}")
# print(user_info)

# update method

more_info={'State':'Punjab','Hobbies':['coding','reading','cricket']}
user_info.update(more_info)
print(user_info)