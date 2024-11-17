//base dir javascript program

//videos section
const video = document.getElementById('videos');
const videoLink = document.getElementById('videos_link');

//movies
const movies = document.getElementById('movies_links');
const moviesSubLinks = document.getElementById('movies_inner_links');

//series
const series = document.getElementById('series_links');
const seriesSubLinks = document.getElementById('series_inner_links');

//gerne
const genre = document.getElementById('genre_links');
const genreLink = document.getElementById('genre_inner_links');


//video listener
video.addEventListener('click' , () => {
videoLink.classList.toggle('videos-links_show');
videoLink.style.transition='left .6s ease'
})

//movies listener
movies.addEventListener('click' , () =>{
moviesSubLinks.classList.toggle('movies_inner_links_show');
})

//genre listener
genre.addEventListener('click' ,() =>{
   genreLink.classList.toggle('genre_links_show'); 
} )

// series listener
series.addEventListener('click' , ()=>{
    seriesSubLinks.classList.toggle('series_inner_links_show');
})
