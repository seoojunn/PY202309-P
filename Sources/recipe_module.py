from soynlp.tokenizer import MaxScoreTokenizer
from collections import Counter
import numpy as np

def preprocess_text(text):
    tokenizer = MaxScoreTokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens

def calculate_similarity(user_profile, recipes):
    # 텍스트 전처리 및 토큰화
    user_tokens = preprocess_text(user_profile)
    recipe_tokens_list = [preprocess_text(recipe) for recipe in recipes]

    # 사용자 프로필과 레시피의 단어 빈도 계산
    user_counter = Counter(user_tokens)

    similarities = []
    for recipe_tokens in recipe_tokens_list:
        # 레시피 블록을 토큰화하고 사용자 프로필과의 유사도 계산
        intersection = sum((user_counter & Counter(recipe_tokens)).values())
        union = sum((user_counter | Counter(recipe_tokens)).values())
        similarity = intersection / union if union != 0 else 0
        similarities.append(similarity)

    # 유사도에 따라 레시피를 정렬
    sorted_recipe_indices = np.argsort(similarities)[::-1]

    return sorted_recipe_indices
#상위3개 레시피 출력
def display_top_n_recipes(sorted_indices, recipes, n=3):
    for i in range(n):
        idx = sorted_indices[i]
        recipe = recipes[idx]
        print(f"\n레시피 {i + 1}:\n{recipe}")
