from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='templates/assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    
    # 여기서 검색 결과를 처리할 수 있습니다.
    results = [
        f'Result 1 for "{query}"',
        f'Result 2 for "{query}"',
        f'Result 3 for "{query}"'
    ]
    
    # 결과를 JSON 형식으로 반환
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
