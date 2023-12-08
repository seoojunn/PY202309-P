from ingredient_module import IngredientModule as im
from recipe_module import calculate_similarity, display_top_n_recipes
import numpy as np  # NumPy 모듈 임포트 추가

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# 사용자 프로필 및 레시피 파일 경로
user_profile_path = 'ingredient.txt'
recipe_file_path = 'food_info.txt'

# 사용자 프로필 및 레시피 파일 내용 가져오기
user_profile = ''
ingredient_list = []

try:
    file_name = "ingredient.txt"
    ingredient_module = im()
    ingredient_list = im.load_ingredients_from_file(file_name)
    while True:
        print("\n레시피 추천 프로그램")
        print("1. 재료 추가")
        print("2. 재료 수정")
        print("3. 재료 제거")
        print("4. 재료 목록 표시")
        print("5. 종료")
        choice = input("선택: ")
        if choice == '1':
            ingredient = input("재료를 입력하세요: ")
            im.add_ingredient(ingredient_list, ingredient)
            print("재료가 추가되었습니다.")
        elif choice == '2':
            index = int(input("수정할 재료의 인덱스를 입력하세요(1번부터 입력): ")) - 1
            new_ingredient = input("새로운 재료를 입력하세요: ")
            im.modify_ingredient(ingredient_list, index, new_ingredient)
        elif choice == '3':
            index = int(input("제거할 재료의 인덱스를 입력하세요(1번부터 입력): ")) - 1
            im.remove_ingredient(ingredient_list, index)
        elif choice == '4':
            im.display_ingredient(ingredient_list)
        elif choice == '5':
            im.save_ingredients_to_file(ingredient_list, file_name)
            print("프로그램을 종료합니다.")
            user_profile = ' '.join(ingredient_list)
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

recipes = read_text_file(recipe_file_path).split('\n\n')
sorted_recipe_indices = calculate_similarity(user_profile, recipes)
display_top_n_recipes(sorted_recipe_indices, recipes, n=3)

satisfied = input("만족하시나요? (y/n): ")

while satisfied.lower() != 'y':
    current_top_indices = sorted_recipe_indices[:3]

    # 다음으로 추천될 레시피 중에서 현재 상위 3개의 인덱스를 제외한 인덱스들
    next_top_indices = []
    for idx in sorted_recipe_indices:
        if idx not in current_top_indices:
            next_top_indices.append(idx)

        # 상위 3개를 모두 찾았으면 반복 종료
        if len(next_top_indices) == 3:
            break
    display_top_n_recipes(next_top_indices, recipes, n=3)
    satisfied = input("만족하시나요? (y/n): ")
