# Templates for analyzing YouTube content

TITLE_ANALYSIS_TEMPLATE = """
Analyze the following YouTube video title for SEO effectiveness:

TITLE: {title}

Based on YouTube SEO best practices, provide specific recommendations for improvement.
Consider:
1. Length (optimal is 60-70 characters)
2. Keyword placement (front-loading important keywords)
3. Click-worthiness (ability to attract clicks)
4. Clarity and conciseness
5. Emotional appeal or curiosity gap

Provide 3-5 actionable suggestions that would improve this title's SEO performance.
Format your response as HTML with paragraphs and bullet points.
"""

DESCRIPTION_ANALYSIS_TEMPLATE = """
Analyze the following YouTube video description for SEO effectiveness:

DESCRIPTION:
{description}

Based on YouTube SEO best practices, provide specific recommendations for improvement.
Consider:
1. First 2-3 lines visibility before "Show more" (critical area)
2. Keyword density and placement
3. Length (ideal is 200+ words)
4. Structure and readability
5. Use of timestamps, links, calls to action
6. Channel promotion elements

Provide 3-5 actionable suggestions that would improve this description's SEO performance.
Format your response as HTML with paragraphs and bullet points.
"""

TAGS_ANALYSIS_TEMPLATE = """
Analyze the following YouTube video tags for SEO effectiveness:

TAGS: {tags}

Based on YouTube SEO best practices, provide specific recommendations for improvement.
Consider:
1. Number of tags (10-15 is optimal)
2. Mix of broad and specific tags
3. Relevance to content
4. Inclusion of variations and long-tail keywords
5. Competitor tag analysis

Provide 3-5 actionable suggestions that would improve these tags' SEO performance.
Format your response as HTML with paragraphs and bullet points.
"""

COMBINED_WITH_RAG_TEMPLATE = """
Analyze the following YouTube video content for SEO effectiveness:

TITLE: {title}
DESCRIPTION: {description}
TAGS: {tags}

Here is additional knowledge about YouTube SEO best practices that may be relevant:

{knowledge}

Based on this information and YouTube SEO best practices, provide specific recommendations for improvement.
Consider all aspects of YouTube SEO optimization.

Provide 3-5 actionable suggestions for each section (title, description, and tags) that would improve this video's SEO performance.
Format your response as HTML with clear section headings, paragraphs and bullet points.
"""