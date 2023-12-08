#만개의 레시피 크롤링 하는 법 서칭 https://otugi.tistory.com/393
import requests, json
from bs4 import BeautifulSoup

def food_info(name):
    url = f"https://www.10000recipe.com/recipe/list.html?q={name}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print("HTTP response error :", response.status_code)
        return
    
    food_list = soup.find_all(attrs={'class':'common_sp_link'})
    food_id = food_list[0]['href'].split('/')[-1]
    new_url = f'https://www.10000recipe.com/recipe/{food_id}'
    new_response = requests.get(new_url)
    if new_response.status_code == 200:
        html = new_response.text
        soup = BeautifulSoup(html, 'html.parser')
    else : 
        print("HTTP response error :", response.status_code)
        return
    
    food_info = soup.find(attrs={'type':'application/ld+json'})
    result = json.loads(food_info.text)
    ingredient = ','.join(result['recipeIngredient'])
    recipe = [result['recipeInstructions'][i]['text'] for i in range(len(result['recipeInstructions']))]
    for i in range(len(recipe)):
        recipe[i] = f'{i+1}. ' + recipe[i]
    
    res = {
        'name': name,
        'ingredients': ingredient,
        'recipe': recipe
    }

    return res

def save_to_file(result, filename="food_info.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n\n")  # 각 음식 결과 사이에 빈 줄 추가
        file.write(f"음식 이름: {result['name']}\n")
        file.write(f"재료: {result['ingredients']}\n")
        file.write("레시피:\n")
        for step in result['recipe']:
            file.write(f"{step}\n")

# 여러 음식에 대한 정보를 저장
foods_to_search = ["아보카도 간장와사비 계란밥", "새송이버섯버터굴소스볶음", "느타리버섯볶음","새송이버섯소고기볶음","순두부장","도토리묵김무침 ","떡 베이컨 간장조림","고추장 달걀조림"]

for food_name in foods_to_search:
    result = food_info(food_name)
    save_to_file(result)
