# 1 Nested List Challenge

scores = [('Alice', 85), ('Bob', 72), ('Charlie', 91)]

# Find min score
min_score = min(scores, key = lambda x: x[1])

# Keep only students with score higher than min
scores = [score for score in scores if score[1] > min_score[1]]

# Find second min score
sec_min_score = min(scores, key= lambda x: x[1])

# Keep only students with second min score
scores = [score for score in scores if score[1] == sec_min_score[1]]

# Sort students alphabetically
scores.sort(key= lambda x: x[0])

for score in scores:
    print(score[0])


