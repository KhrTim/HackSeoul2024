def process_category(category):
    print(f"Received category: {category}")
    if category == "basketball":
        return "https://www.coupang.com/vp/products/105909624?itemId=509026658&vendorItemId=4305497855&pickType=COU_PICK&q=%EB%86%8D%EA%B5%AC%EA%B3%B5&itemsCount=36&searchId=7e38fc90ebfb439f81349da18a8849c2&rank=1"
    elif category == "Skin care":
        return "https://www.coupang.com/vp/products/1414809213?itemId=2779751047&vendorItemId=5484609359&sourceType=CATEGORY&categoryId=486148&isAddedCart="
    elif category == "Man":
        return "https://www.coupang.com/vp/products/5291011072?itemId=7607262414&vendorItemId=81735052457&q=%EB%82%A8%EC%9E%90%EC%98%B7&itemsCount=36&searchId=95d888e621424a67bdbe9ef681bc1aa8&rank=19&isAddedCart="
    elif category == "Mouse":
        return "https://www.coupang.com/vp/products/8145067451?itemId=19848126302&vendorItemId=70778258892&pickType=COU_PICK&q=%EB%A7%88%EC%9A%B0%EC%8A%A4&itemsCount=36&searchId=c102d3773d894c31871b1201498c685d&rank=1&isAddedCart="
    return None

def search_query(searchQuery):
    # 검색어 처리 로직
    print(f"Processing search query: {searchQuery}")
    
    # 여기서는 예시로 검색어를 그대로 반환합니다.
    return f"Search Query: {searchQuery} processed."