from ingredient_module import IngredientModule as im

try:
    file_name ="ingredient.txt"
    ingredient_module = im()
    ingredient_list = im.load_ingredients_from_file(file_name)
    while True:
        print("\n레시피 추천 프로그램")
        print("1. 재료 추가")
        print("2. 재료 목록 표시")
        print("3. 종료")
        choice = input("선택: ") 
        if choice == '1':
            ingredient = input("재료를 입력하세요: ")
            im.add_ingredient(ingredient_list, ingredient) 
            print("재료가 추가되었습니다.") 
        elif choice == '2':
            im.display_ingredient(ingredient_list)
        elif choice == '3': 
            im.save_ingredients_to_file(ingredient_list, file_name)
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")