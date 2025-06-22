from flask import Flask, render_template, request, jsonify
from papertrial import get_scholarly_articles, write_introduction, write_conclusion
app = Flask(_name_)
@app.route('/', methods=['GET', 'POST'])
def index():
 if request.method == 'POST':
 topic = request.form['topic']
 articles = get_sample_articles(topic) # Use sample articles for demo
 introduction = write_introduction(topic, articles)
 conclusion = write_conclusion(topic)
 return render_template('index.html', topic=topic, articles=articles,
 introduction=introduction, conclusion=conclusion)
 else:
 # Display the form for GET requests
 return render_template('index.html')
@app.route('/get_articles', methods=['POST'])
def get_articles():
 if request.is_json:
 data = request.get_json()
 topic = data.get('topic')
 articles = get_scholarly_articles(topic)
 return jsonify(articles)
 else:
 return jsonify({'error': 'Unsupported Media Type'}), 415
def get_sample_articles(topic):
 """Provides a sample list of articles for demonstration purposes."""
 articles = [
 {'title': 'Sample Article Title 1', 'link': 'https://example.com/article1'},
 {'title': 'Sample Article Title 2', 'link': 'https://example.com/article2'},
 {'title': 'Sample Article Title 3', 'link': 'https://example.com/article3'}
 ]
 return articles[:2] # Return only the first two articles
if _name_ == '_main_':
 app.run(debug=True)
