from flask import Flask, render_template, request, jsonify
from src.youtube.api import get_video_metadata
from src.analysis.title import analyze_title
from src.analysis.description import analyze_description
from src.analysis.tags import analyze_tags
from src.config import load_config

app = Flask(__name__)
config = load_config()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    if 'youtube_url' in data:
        # Process YouTube URL
        url = data['youtube_url']
        metadata = get_video_metadata(url)
        
        if not metadata:
            return jsonify({'error': 'Failed to fetch video metadata'}), 400
            
        title = metadata.get('title', '')
        description = metadata.get('description', '')
        tags = metadata.get('tags', [])
    else:
        # Process manual input
        title = data.get('title', '')
        description = data.get('description', '')
        tags = data.get('tags', [])
    
    # Analyze content
    title_analysis = analyze_title(title)
    description_analysis = analyze_description(description)
    tags_analysis = analyze_tags(tags)
    
    return jsonify({
        'title_analysis': title_analysis,
        'description_analysis': description_analysis,
        'tags_analysis': tags_analysis
    })

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=config.get('DEBUG', True))