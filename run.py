from flask import Flask, request, jsonify, render_template
import r123  # r123.py 파일을 임포트합니다.
app = Flask(__name__, static_folder='templates/assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/process_category', methods=['POST'])
def process_category():
    data = request.json
    category = data.get('category')

    if category:
        # 카테고리가 존재하면 해당 함수 호출
        result = r123.process_category(category)
    else:
        result = "No category provided"

    # 결과를 클라이언트에 반환
    return jsonify({'message': result})

@app.route('/process_search', methods=['POST'])
def process_search():
    data = request.json
    search_query = data.get('search')

    if search_query:
        # 검색어가 존재하면 해당 함수 호출
        result = r123.search_query(search_query)
    else:
        result = "No search query provided"

    # 결과를 클라이언트에 반환
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)
