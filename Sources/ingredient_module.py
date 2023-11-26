class IngredientModule:
    #재료 추가하는 함수 생성
    def add_ingredient(ingredient_list, ingredient): 
        ingredient_list.append(ingredient)
    #재료 보여주는 함수 생성
    def display_ingredient(ingredient_list):
        if not ingredient_list:
            print("재료 목록이 비어 있습니다.")
        else:
            print("재료 목록:")
            for i in range(len(ingredient_list)):
                ingredient = ingredient_list[i]
                print(f"{i+1}. {ingredient}")
    #재료를 파일에 저장하는 함수 생성
    def save_ingredients_to_file(ingredient_list, filename):
        write_fp = open(filename, 'w', encoding="utf8")
        for ingredient in ingredient_list:
            write_fp.write(ingredient+"\n")
        write_fp.close()
        print("재료가 파일에 저장되었습니다.")
    #재료를 읽어오는 함수    
    def load_ingredients_from_file(filename):
        try:
            ingredient_list = []
            read_fp = open(filename,'r', encoding="utf8")
            lines = read_fp.readlines()
            for line in lines:
                ingredient_list.append(line.strip())
            read_fp.close()
            return ingredient_list
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")