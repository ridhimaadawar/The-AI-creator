document.addEventListener('DOMContentLoaded', () => {
 const form = document.getElementById('articleForm');
 form.addEventListener('submit', async (event) => {
 event.preventDefault();
 const topic = document.getElementById('topic').value;
 try {
 const response = await fetch('/get_articles', {
 method: 'POST',
 headers: {
 'Content-Type': 'application/json',
 },
 body: JSON.stringify({ topic: topic }),
 });
 if (!response.ok) {
 throw new Error('Network response was not ok');
 }
 const articles = await response.json();
 console.log('Articles:', articles);
 // Update the HTML content
 const articlesList = document.getElementById('articles');
 articlesList.innerHTML = ''; // Clear existing content
 articles.forEach(article => {
 const listItem = document.createElement('li');
 const link = document.createElement('a');
 link.href = article.link;
 link.textContent = article.title;
 listItem.appendChild(link);
 articlesList.appendChild(listItem);
 articlesList.appendChild(document.createElement('br'));
 });
 } catch (error) {
 console.error('Error:', error);
 }
 });
