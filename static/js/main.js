document.addEventListener('DOMContentLoaded', function() {
    // Tab switching functionality
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            const tabId = button.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Form submission for URL
    const urlForm = document.getElementById('url-form');
    urlForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const youtubeUrl = document.getElementById('youtube-url').value.trim();
        
        if (!youtubeUrl) {
            alert('Please enter a YouTube URL');
            return;
        }
        
        // Show loading state
        const submitBtn = urlForm.querySelector('.submit-btn');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Analyzing...';
        submitBtn.disabled = true;
        
        // Send request to server
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ youtube_url: youtubeUrl })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch video data');
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        })
        .catch(error => {
            alert('Error: ' + error.message);
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        });
    });
    
    // Form submission for manual input
    const manualForm = document.getElementById('manual-form');
    manualForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('video-title').value.trim();
        const description = document.getElementById('video-description').value.trim();
        const tagsInput = document.getElementById('video-tags').value.trim();
        const tags = tagsInput ? tagsInput.split(',').map(tag => tag.trim()) : [];
        
        if (!title && !description && tags.length === 0) {
            alert('Please enter at least one field (title, description, or tags)');
            return;
        }
        
        // Show loading state
        const submitBtn = manualForm.querySelector('.submit-btn');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Analyzing...';
        submitBtn.disabled = true;
        
        // Send request to server
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                title: title,
                description: description,
                tags: tags
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Analysis failed');
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        })
        .catch(error => {
            alert('Error: ' + error.message);
            submitBtn.textContent = originalBtnText;
            submitBtn.disabled = false;
        });
    });
    
    // Function to display results
    function displayResults(data) {
        const resultsContainer = document.getElementById('results-container');
        const resultsContent = resultsContainer.querySelector('.results-content');
        
        // Clear previous results
        resultsContent.innerHTML = '';
        
        // Create HTML for results
        let resultsHTML = '';
        
        // Title analysis
        if (data.title_analysis) {
            resultsHTML += `
                <div class="analysis-section">
                    <h3>Title Analysis</h3>
                    <div class="analysis-content">
                        ${data.title_analysis}
                    </div>
                </div>
            `;
        }
        
        // Description analysis
        if (data.description_analysis) {
            resultsHTML += `
                <div class="analysis-section">
                    <h3>Description Analysis</h3>
                    <div class="analysis-content">
                        ${data.description_analysis}
                    </div>
                </div>
            `;
        }
        
        // Tags analysis
        if (data.tags_analysis) {
            resultsHTML += `
                <div class="analysis-section">
                    <h3>Tags Analysis</h3>
                    <div class="analysis-content">
                        ${data.tags_analysis}
                    </div>
                </div>
            `;
        }
        
        // Add results to the page
        resultsContent.innerHTML = resultsHTML;
        resultsContainer.style.display = 'block';
        
        // Scroll to results
        resultsContainer.scrollIntoView({ behavior: 'smooth' });
    }
});
// Add animation to steps when page loads
document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.step');
    
    steps.forEach((step, index) => {
      setTimeout(() => {
        step.style.opacity = '0';
        step.style.transform = 'translateY(20px)';
        step.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        
        setTimeout(() => {
          step.style.opacity = '1';
          step.style.transform = 'translateY(0)';
        }, 200);
      }, index * 150);
    });
  });
  
  // Add loading animation for form submission
  document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
      form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        
        submitBtn.innerHTML = '<span class="loading-dots">Analyzing</span>';
        submitBtn.disabled = true;
        
        const loadingDots = document.querySelector('.loading-dots');
        let dotCount = 0;
        
        const interval = setInterval(() => {
          dotCount = (dotCount + 1) % 4;
          loadingDots.textContent = 'Analyzing' + '.'.repeat(dotCount);
        }, 300);
        
        // Reset after 30 seconds in case of an error
        setTimeout(() => {
          clearInterval(interval);
          submitBtn.textContent = originalText;
          submitBtn.disabled = false;
        }, 30000);
      });
    });
  });