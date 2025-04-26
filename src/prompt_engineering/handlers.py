# import google.generativeai as genai
# from src.config import load_config
# from src.rag.knowledge_base import SEOKnowledgeBase
# from src.prompt_engineering.templates import (
#     TITLE_ANALYSIS_TEMPLATE,
#     DESCRIPTION_ANALYSIS_TEMPLATE,
#     TAGS_ANALYSIS_TEMPLATE,
#     COMBINED_WITH_RAG_TEMPLATE
# )

# config = load_config()
# genai.configure(api_key=config.get('GEMINI_API_KEY'))

# def handle_title_analysis(title, use_rag=True):
#     """Handle title analysis with prompt engineering."""
#     if not title:
#         return "<p>No title provided for analysis.</p>"
    
#     if use_rag:
#         # Get relevant knowledge from the RAG system
#         knowledge_base = SEOKnowledgeBase()
#         relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO title optimization: {title}")
#         knowledge_text = "\n\n".join(relevant_knowledge)
        
#         # Create a combined prompt with RAG knowledge
#         prompt = COMBINED_WITH_RAG_TEMPLATE.format(
#             title=title,
#             description="",
#             tags="",
#             knowledge=knowledge_text
#         )
#     else:
#         # Use standard prompt template
#         prompt = TITLE_ANALYSIS_TEMPLATE.format(title=title)
    
#     # Updated Gemini API call
#     try:
#         response = genai.generate_text(prompt=prompt)
#         return response
#     except Exception as e:
#         # Fallback to rule-based analysis in case of API issues
#         print(f"Gemini API error: {e}")
#         return generate_basic_title_analysis(title)

# def handle_description_analysis(description, use_rag=True):
#     """Handle description analysis with prompt engineering."""
#     if not description:
#         return "<p>No description provided for analysis.</p>"
    
#     if use_rag:
#         # Get relevant knowledge from the RAG system
#         knowledge_base = SEOKnowledgeBase()
#         relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO description optimization")
#         knowledge_text = "\n\n".join(relevant_knowledge)
        
#         # Create a combined prompt with RAG knowledge
#         prompt = COMBINED_WITH_RAG_TEMPLATE.format(
#             title="",
#             description=description,
#             tags="",
#             knowledge=knowledge_text
#         )
#     else:
#         # Use standard prompt template
#         prompt = DESCRIPTION_ANALYSIS_TEMPLATE.format(description=description)
    
#     # Updated Gemini API call
#     try:
#         response = genai.generate_text(prompt=prompt)
#         return response
#     except Exception as e:
#         # Fallback to rule-based analysis in case of API issues
#         print(f"Gemini API error: {e}")
#         return generate_basic_description_analysis(description)

# def handle_tags_analysis(tags, use_rag=True):
#     """Handle tags analysis with prompt engineering."""
#     if not tags or len(tags) == 0:
#         return "<p>No tags provided for analysis.</p>"
    
#     # Convert tags list to string
#     tags_string = ", ".join(tags)
    
#     if use_rag:
#         # Get relevant knowledge from the RAG system
#         knowledge_base = SEOKnowledgeBase()
#         relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO tags optimization")
#         knowledge_text = "\n\n".join(relevant_knowledge)
        
#         # Create a combined prompt with RAG knowledge
#         prompt = COMBINED_WITH_RAG_TEMPLATE.format(
#             title="",
#             description="",
#             tags=tags_string,
#             knowledge=knowledge_text
#         )
#     else:
#         # Use standard prompt template
#         prompt = TAGS_ANALYSIS_TEMPLATE.format(tags=tags_string)
    
#     # Updated Gemini API call
#     try:
#         response = genai.generate_text(prompt=prompt)
#         return response
#     except Exception as e:
#         # Fallback to rule-based analysis in case of API issues
#         print(f"Gemini API error: {e}")
#         return generate_basic_tags_analysis(tags)

# # Basic rule-based analysis functions as fallbacks
# def generate_basic_title_analysis(title):
#     """Generate basic title analysis if API fails."""
#     analysis = "<h3>Title Analysis</h3>"
    
#     if not title:
#         return analysis + "<p>No title provided for analysis.</p>"
    
#     # Length analysis
#     if len(title) < 30:
#         analysis += "<p>Your title is too short. YouTube recommends titles between 60-70 characters.</p>"
#     elif len(title) > 70:
#         analysis += "<p>Your title is too long. YouTube truncates titles in search results after 70 characters.</p>"
#     else:
#         analysis += "<p>Your title length is good (between 30-70 characters).</p>"
    
#     # Keywords analysis
#     if title.lower() == title:
#         analysis += "<p>Consider capitalizing important words in your title for better visibility.</p>"
    
#     # General recommendations
#     analysis += """
#     <h4>General Recommendations:</h4>
#     <ul>
#         <li>Place important keywords at the beginning of your title</li>
#         <li>Consider using numbers (e.g., "5 Ways to...") to increase click-through rates</li>
#         <li>Create curiosity without using clickbait tactics</li>
#         <li>Make sure your title accurately reflects your video content</li>
#     </ul>
#     """
    
#     return analysis

# def generate_basic_description_analysis(description):
#     """Generate basic description analysis if API fails."""
#     analysis = "<h3>Description Analysis</h3>"
    
#     if not description:
#         return analysis + "<p>No description provided for analysis.</p>"
    
#     # Length analysis
#     word_count = len(description.split())
#     if word_count < 100:
#         analysis += "<p>Your description is quite short. YouTube recommends comprehensive descriptions of 200+ words.</p>"
#     else:
#         analysis += "<p>Your description length is good.</p>"
    
#     # First paragraph analysis
#     paragraphs = description.split("\n\n")
#     if paragraphs and len(paragraphs[0].split()) < 15:
#         analysis += "<p>Consider making your first paragraph more descriptive as it's visible before 'Show more'.</p>"
    
#     # Links analysis
#     if "http" in description:
#         analysis += "<p>Good job including links in your description.</p>"
#     else:
#         analysis += "<p>Consider adding relevant links to enhance your description.</p>"
    
#     # General recommendations
#     analysis += """
#     <h4>General Recommendations:</h4>
#     <ul>
#         <li>Include your main keywords in the first 1-2 sentences</li>
#         <li>Add timestamps if your video has distinct sections</li>
#         <li>Include calls-to-action (subscribe, like, comment)</li>
#         <li>Use relevant hashtags (3-5) at the end of your description</li>
#         <li>Structure your description with paragraphs for better readability</li>
#     </ul>
#     """
    
#     return analysis

# def generate_basic_tags_analysis(tags):
#     """Generate basic tags analysis if API fails."""
#     analysis = "<h3>Tags Analysis</h3>"
    
#     if not tags or len(tags) == 0:
#         return analysis + "<p>No tags provided for analysis.</p>"
    
#     # Number of tags analysis
#     if len(tags) < 8:
#         analysis += "<p>You have too few tags. YouTube recommends using 10-15 relevant tags.</p>"
#     elif len(tags) > 15:
#         analysis += "<p>You have many tags. Focus on the most relevant 10-15 tags for better results.</p>"
#     else:
#         analysis += "<p>Your tag count is good (between 8-15 tags).</p>"
    
#     # Tag length analysis
#     short_tags = sum(1 for tag in tags if len(tag.split()) == 1)
#     if short_tags > len(tags) / 2:
#         analysis += "<p>Most of your tags are single words. Consider using more multi-word phrases that viewers might search for.</p>"
    
#     # General recommendations
#     analysis += """
#     <h4>General Recommendations:</h4>
#     <ul>
#         <li>Start with your most important keyword as the first tag</li>
#         <li>Use a mix of broad and specific tags</li>
#         <li>Include exact phrases from your title in your tags</li>
#         <li>Add variations of your main keywords (singular/plural forms)</li>
#         <li>Research competitors' tags for ideas</li>
#     </ul>
#     """
    
#     return analysis

import google.generativeai as genai
from src.config import load_config
from src.rag.knowledge_base import SEOKnowledgeBase
from src.prompt_engineering.templates import (
    TITLE_ANALYSIS_TEMPLATE,
    DESCRIPTION_ANALYSIS_TEMPLATE,
    TAGS_ANALYSIS_TEMPLATE,
    COMBINED_WITH_RAG_TEMPLATE
)

config = load_config()
api_key = config.get('GEMINI_API_KEY')
if not api_key:
    print("WARNING: No Gemini API key found in configuration")
else:
    genai.configure(api_key=api_key)

# Define the fallback functions first so they're available in the handler functions
def generate_basic_title_analysis(title):
    """Generate basic title analysis if API fails."""
    analysis = "<h3>Title Analysis</h3>"
    
    if not title:
        return analysis + "<p>No title provided for analysis.</p>"
    
    words = title.split()
    
    # Length analysis
    if len(title) < 30:
        analysis += f"<p>Your title <strong>\"{title}\"</strong> is too short at {len(title)} characters. YouTube recommends titles between 60-70 characters.</p>"
        analysis += f"<p>Consider expanding it to include more relevant keywords. For example: \"{title} - Detailed Tutorial Guide 2025\"</p>"
    elif len(title) > 70:
        analysis += f"<p>Your title <strong>\"{title}\"</strong> is too long at {len(title)} characters. YouTube truncates titles in search results after 70 characters.</p>"
        analysis += f"<p>Consider shortening it to ensure important keywords are visible. For example: \"{' '.join(words[:6])}...\"</p>"
    else:
        analysis += f"<p>Your title <strong>\"{title}\"</strong> has a good length at {len(title)} characters.</p>"
    
    # Keywords analysis
    if title.lower() == title:
        analysis += f"<p>Consider capitalizing important words in your title for better visibility. For example: \"{title.title()}\"</p>"
    
    # Keyword positioning
    if len(words) > 4:
        analysis += f"<p>Consider repositioning important keywords to the beginning. For example: \"{' '.join(words[2:5])} - {' '.join(words[:2])} {' '.join(words[5:])}\"</p>"
    
    # General recommendations
    analysis += """
    <h4>Suggested Title Improvements:</h4>
    <ul>
        <li>Add numbers or years to create urgency (e.g., "Top 5" or "2025 Guide")</li>
        <li>Use emotional triggers like "Amazing" or "Ultimate" if appropriate</li>
        <li>Create a clear value proposition in your title that tells viewers what they'll gain</li>
    </ul>
    """
    
    return analysis

def generate_basic_description_analysis(description):
    """Generate basic description analysis if API fails."""
    analysis = "<h3>Description Analysis</h3>"
    
    if not description:
        return analysis + "<p>No description provided for analysis.</p>"
    
    # Length analysis
    word_count = len(description.split())
    if word_count < 100:
        analysis += f"<p>Your description is quite short at {word_count} words. YouTube recommends comprehensive descriptions of 200+ words.</p>"
        analysis += "<p>Consider adding more content about your video topic, including relevant keywords.</p>"
    else:
        analysis += f"<p>Your description has a good length at {word_count} words.</p>"
    
    # First paragraph analysis
    paragraphs = description.split("\n\n")
    if paragraphs and len(paragraphs[0].split()) < 15:
        analysis += f"<p>Your first paragraph is only {len(paragraphs[0].split())} words. Consider making it more descriptive and keyword-rich as it's visible before 'Show more'.</p>"
        analysis += f"<p>Try expanding it to include main keywords and a clear description of the video content.</p>"
    
    # Links analysis
    if "http" in description:
        analysis += "<p>Good job including links in your description. Make sure they're relevant to your content.</p>"
    else:
        analysis += "<p>Consider adding relevant links to enhance your description. Include your social media, related videos, or resources mentioned.</p>"
    
    # Hashtag analysis
    if "#" in description:
        hashtag_count = sum(1 for word in description.split() if word.startswith('#'))
        if hashtag_count > 5:
            analysis += f"<p>You have {hashtag_count} hashtags, which may be excessive. YouTube recommends 3-5 relevant hashtags.</p>"
        else:
            analysis += f"<p>Good job using {hashtag_count} hashtags. Make sure they're relevant to your content.</p>"
    else:
        analysis += "<p>Consider adding 3-5 relevant hashtags at the end of your description to improve discoverability.</p>"
        analysis += "<p>Suggested hashtags based on your content: #YouTubeTips #ContentCreation #VideoOptimization</p>"
    
    # Timestamp analysis
    if ":" in description and any(word[0].isdigit() for word in description.split()):
        analysis += "<p>Good job including timestamps in your description. They improve user experience and SEO.</p>"
    else:
        analysis += "<p>Consider adding timestamps if your video has distinct sections. For example:</p>"
        analysis += "<p>0:00 Introduction<br>1:30 Main Topic<br>5:45 Conclusion</p>"
    
    return analysis

def generate_basic_tags_analysis(tags):
    """Generate basic tags analysis if API fails."""
    analysis = "<h3>Tags Analysis</h3>"
    
    if not tags or len(tags) == 0:
        return analysis + "<p>No tags provided for analysis.</p>"
    
    # Number of tags analysis
    if len(tags) < 8:
        analysis += f"<p>You only have {len(tags)} tags, which is too few. YouTube recommends using 10-15 relevant tags.</p>"
        analysis += "<p>Consider adding more specific and related tags to improve discoverability.</p>"
    elif len(tags) > 15:
        analysis += f"<p>You have {len(tags)} tags, which is quite many. Focus on the most relevant 10-15 tags for better results.</p>"
        analysis += "<p>Consider removing less relevant tags to focus on your core keywords.</p>"
    else:
        analysis += f"<p>Your tag count is good at {len(tags)} tags.</p>"
    
    # Tag length analysis
    short_tags = sum(1 for tag in tags if len(tag.split()) == 1)
    if short_tags > len(tags) / 2:
        analysis += f"<p>{short_tags} of your {len(tags)} tags are single words. Consider using more multi-word phrases that viewers might search for.</p>"
    
    # Suggest improvements
    analysis += """
    <h4>Suggested Tag Improvements:</h4>
    <p>Based on your current tags, here are specific tags you should consider adding:</p>
    <ul>
        <li>"youtube optimization guide"</li>
        <li>"increase video views"</li>
        <li>"youtube algorithm tips"</li>
        <li>"youtube seo strategy"</li>
        <li>"grow youtube channel"</li>
        <li>"video ranking tips"</li>
        <li>"youtube content creator"</li>
    </ul>
    
    <p>Consider structuring your tags in this order:</p>
    <ol>
        <li>Your most specific, targeted keyword phrase</li>
        <li>Variations of your main keyword</li>
        <li>Broader category tags</li>
        <li>Brand-related tags (your channel name, etc.)</li>
    </ol>
    """
    
    return analysis

# Handler functions that use the fallback functions above
def handle_title_analysis(title, use_rag=True):
    """Handle title analysis with prompt engineering."""
    if not title:
        return "<p>No title provided for analysis.</p>"
    
    if use_rag:
        try:
            # Get relevant knowledge from the RAG system
            knowledge_base = SEOKnowledgeBase()
            relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO title optimization: {title}")
            knowledge_text = "\n\n".join(relevant_knowledge)
            
            # Create a combined prompt with RAG knowledge - more specific request
            prompt = f"""
            You are a YouTube SEO expert tasked with analyzing and improving this video title.
            
            TITLE: "{title}"
            
            Based on YouTube SEO best practices and this knowledge:
            {knowledge_text}
            
            Provide a detailed, specific analysis and 3-5 concrete suggestions to improve this exact title.
            
            Your response MUST include:
            1. At least 2-3 specific rewritten title examples that would perform better
            2. Specific keywords that should be added, removed, or repositioned
            3. Explanation of why these changes would improve performance
            
            Be extremely specific to this title - do not give generic advice.
            Format your response as HTML.
            """
            
            # Get model generation - using the specific model
            print("Calling Gemini API for title analysis...")
            model = genai.GenerativeModel('gemini-1.5-pro-002')  # Updated model name
            response = model.generate_content(prompt)
            
            print("API response received successfully")
            return response.text
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            # Fall back to rule-based analysis
            return generate_basic_title_analysis(title)
    else:
        # Use standard prompt template without RAG
        return generate_basic_title_analysis(title)

def handle_description_analysis(description, use_rag=True):
    """Handle description analysis with prompt engineering."""
    if not description:
        return "<p>No description provided for analysis.</p>"
    
    if use_rag:
        try:
            # Get relevant knowledge from the RAG system
            knowledge_base = SEOKnowledgeBase()
            relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO description optimization")
            knowledge_text = "\n\n".join(relevant_knowledge)
            
            # Create a combined prompt with RAG knowledge - more specific request
            prompt = f"""
            You are a YouTube SEO expert tasked with analyzing and improving this video description.
            
            DESCRIPTION:
            "{description}"
            
            Based on YouTube SEO best practices and this knowledge:
            {knowledge_text}
            
            Provide a detailed, specific analysis and 3-5 concrete suggestions to improve this exact description.
            
            Your response MUST include:
            1. Specific examples of text that should be added, rewritten, or repositioned
            2. Identification of missing elements (timestamps, links, calls to action, etc.)
            3. Suggestions for specific hashtags that would work well with this content
            
            Be extremely specific to this description - do not give generic advice.
            Format your response as HTML.
            """
            
            # Get model generation - using the specific model
            print("Calling Gemini API for description analysis...")
            model = genai.GenerativeModel('gemini-1.5-pro-002')  # Updated model name
            response = model.generate_content(prompt)
            
            print("API response received successfully")
            return response.text
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            # Fall back to rule-based analysis
            return generate_basic_description_analysis(description)
    else:
        # Use standard prompt template without RAG
        return generate_basic_description_analysis(description)

def handle_tags_analysis(tags, use_rag=True):
    """Handle tags analysis with prompt engineering."""
    if not tags or len(tags) == 0:
        return "<p>No tags provided for analysis.</p>"
    
    # Convert tags list to string
    tags_string = ", ".join(tags)
    
    if use_rag:
        try:
            # Get relevant knowledge from the RAG system
            knowledge_base = SEOKnowledgeBase()
            relevant_knowledge = knowledge_base.get_relevant_knowledge(f"YouTube SEO tags optimization")
            knowledge_text = "\n\n".join(relevant_knowledge)
            
            # Create a combined prompt with RAG knowledge - more specific request
            prompt = f"""
            You are a YouTube SEO expert tasked with analyzing and improving these video tags.
            
            TAGS: {tags_string}
            
            Based on YouTube SEO best practices and this knowledge:
            {knowledge_text}
            
            Provide a detailed, specific analysis and suggestions to improve these exact tags.
            
            Your response MUST include:
            1. A list of 10-15 specific optimized tags that would perform better, based on these existing tags
            2. An explanation of why these tags would be more effective
            3. Identification of any redundant or ineffective tags
            
            Be extremely specific - do not give generic advice.
            Format your response as HTML.
            """
            
            # Get model generation - using the specific model
            print("Calling Gemini API for tags analysis...")
            model = genai.GenerativeModel('gemini-1.5-pro-002')  # Updated model name
            response = model.generate_content(prompt)
            
            print("API response received successfully")
            return response.text
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            # Fall back to rule-based analysis
            return generate_basic_tags_analysis(tags)
    else:
        # Use standard prompt template without RAG
        return generate_basic_tags_analysis(tags)