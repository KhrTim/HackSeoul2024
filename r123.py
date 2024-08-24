def process_category(category):
    # 카테고리와 검색어에 대한 로직 처리
    
    # 콘솔에 출력하여 확인
    print(f"Received category: {category}")
    if f"{category}" == "basekball":
        return "https://www.coupang.com/vp/products/105909624?itemId=509026658&vendorItemId=4305497855&pickType=COU_PICK&q=%EB%86%8D%EA%B5%AC%EA%B3%B5&itemsCount=36&searchId=7e38fc90ebfb439f81349da18a8849c2&rank=1"
    # 처리 결과 반환
    return f"Category: {category}."

def search_query(searchQuery):
    # 검색어 처리 로직
    print(f"Processing search query: {searchQuery}")
    
    # 여기서는 예시로 검색어를 그대로 반환합니다.
    return f"Search Query: {searchQuery} processed."