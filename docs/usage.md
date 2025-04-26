# YouTube SEO Helper - Usage Guide

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google API key (for YouTube Data API)
- Gemini API key (optional, for enhanced analysis)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-seo-helper.git
   cd youtube-seo-helper
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file with your API keys:

bash
Copy
Edit
YOUTUBE_API_KEY=your_youtube_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
DEBUG=True
Run the application:

bash
Copy
Edit
python app.py
Open your browser and navigate to:

arduino
Copy
Edit
http://localhost:5000
Using the Application
Analyzing a YouTube Video
On the home page, select the "YouTube URL" tab.

Enter a valid YouTube video URL in the input field.

Click "Analyze".

Review the analysis results for title, description, and tags.

Analyzing Content Before Publishing
On the home page, select the "Title & Description" tab.

Enter your planned video title.

Enter your planned video description.

Enter your planned tags (comma-separated).

Click "Analyze".

Review the analysis results for title, description, and tags.

Understanding the Results
Title Analysis
The title analysis provides:

Evaluation of current title length and optimization

Keyword placement recommendations

Click-through rate improvement suggestions

Actionable recommendations for improving your title

Example recommendations:

Add numbers to increase click-through rates (e.g., "5 Ways to...")

Move important keywords to the beginning of the title

Create curiosity without using clickbait tactics

Description Analysis
The description analysis provides:

Evaluation of the first few lines (visible before "Show more")

Keyword density and placement

Overall description structure

Suggestions for timestamps, links, and calls-to-action

Example recommendations:

Make the first paragraph more descriptive and keyword-rich

Add timestamps for longer videos to improve user experience

Include calls-to-action (subscribe, like, comment)

Tags Analysis
The tags analysis provides:

Evaluation of tag quantity and quality

Mix of broad and specific tags

Relevance to content

Suggestions for additional or modified tags

Example recommendations:

Use more multi-word phrases that viewers might search for

Include variations of your main keywords

Structure tags with most specific ones first

Best Practices
Titles
Keep titles between 60-70 characters

Place important keywords at the beginning

Create curiosity without being clickbait

Use numbers when appropriate (e.g., "10 Ways to...")

Descriptions
Make the first 2-3 lines count (visible before "Show more")

Write at least 200-300 words for the full description

Include your main keyword in the first paragraph

Use timestamps for longer videos

Add relevant links and calls-to-action

Tags
Use 10-15 tags for optimal reach

Include a mix of specific and broad tags

Start with your most important keyword

Include variations of your main keywords