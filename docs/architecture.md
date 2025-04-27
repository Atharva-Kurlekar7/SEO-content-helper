# SEO-CONTENT-HELPER - System Architecture

## Overview

YouTube SEO Helper is a web application that helps content creators optimize their videos for better search visibility and engagement. The system implements sophisticated generative AI components to provide actionable SEO recommendations based on YouTube best practices.

## Architecture Diagram

![SEO-CONTENT-HELPER](./SEO_helper_architecture_diag.svg)

## Component Description

### Web Interface
- **URL Input**: Accepts YouTube video URLs for analysis
- **Manual Input**: Allows direct input of titles, descriptions, and tags
- **Results Display**: Shows analysis results and recommendations

### Flask Backend
- **YouTube API Integration**: Retrieves video metadata from YouTube
- **Analysis Processing**: Coordinates the analysis workflow
- **Response Handling**: Prepares analysis results for display

### Core Components

#### Prompt Engineering
- **Prompt Templates**: Specialized templates for analyzing titles, descriptions, and tags
- **Context Management**: Integrates context from RAG system into prompts
- **Error Handling**: Graceful fallback to rule-based analysis when API fails

#### Retrieval-Augmented Generation (RAG)
- **Knowledge Base**: Contains YouTube SEO best practices
- **Vector Retrieval**: Finds relevant knowledge for specific content
- **Document Chunking**: Splits knowledge base into manageable chunks

## Data Flow

1. **Input Collection**: User provides a YouTube URL or manual content
2. **Data Extraction**: System extracts metadata from YouTube or uses manual input
3. **Knowledge Retrieval**: RAG system retrieves relevant SEO knowledge
4. **Prompt Generation**: System creates tailored prompts with context
5. **Analysis Generation**: LLM or rule-based system generates detailed analysis
6. **Result Presentation**: System displays the results to the user

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **YouTube Integration**: YouTube Data API v3
- **SEO Analysis**: Google Gemini API / Rule-based fallback
- **RAG Implementation**: Vector similarity search
- **Data Storage**: Markdown files for knowledge base