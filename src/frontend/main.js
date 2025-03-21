document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('movie-search');
    const searchBtn = document.getElementById('search-btn');
    const loadingElement = document.getElementById('loading');
    const errorMessageElement = document.getElementById('error-message');
    const recommendationsContainer = document.getElementById('recommendations-container');
    const movieTitleElement = document.getElementById('movie-title');
    const recommendationsList = document.getElementById('recommendations-list');

    const API_URL = 'https://localhost:5000/api';

    async function getRecommendations(movieTitle) {
        showLoading();

        try {
            const response = await fetch(`${API_URL}/recommendations?title=${encodeURIComponent(movieTitle)}&top_n=10`);

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Failed to get recommendations');
            }

            const data = await response.json();
            displayRecommendations(data);
        } catch (error) {
            showError(error.message);
        }
    }

    function displayRecommendations(data){
        hideLoading();
        errorMessageElement.classList.add('hidden');

        movieTitleElement.textContent = data.movie;
        recommendationsList.innerHTML = '';
    }
})