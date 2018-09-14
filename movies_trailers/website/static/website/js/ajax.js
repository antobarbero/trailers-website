$(document).ready(function(){
  $("#search-trailers").submit(function(e){
    e.preventDefault();
    var q = $("#id_key_words").val();
    document.getElementById('result-container').innerHTML = '<p align="center" class="showcase-text lead mb-0">Loading ...</p>';
    $.ajax({
      dataType: 'json',
      url: $(this).attr('action') + '?q=' + q,
      type: $(this).attr('method'),
      data: {},
      success: function(json){
        if (json.length) {
          document.getElementById('result-container').innerHTML = '';
          json.forEach((movie) => {
            document.getElementById('result-container').innerHTML += renderItem(movie.Title, movie.Year, movie.trailers);
          });
        }
        else {
          document.getElementById('result-container').innerHTML = '<p align="center" class="showcase-text lead mb-0">No movies found!</p>';
        }
      }
    });
  })
});

function renderItem(title, year, trailers) {
  var html = '<div class="row no-gutters"><div class="col-lg-12 showcase-text"><h2>' + title + ' (' + year + ')' + '</h2></div>';

  trailers.forEach ((trailer) => {
    html += '<div class="col-lg-12 text-white showcase-img" align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/' + trailer + '"></iframe></div>';
  });

  if (trailers.length === 0) {
    html += '<div class="col-lg-12 showcase-text" align="center">No trailer found.</div>';
  }
  html += '</div><hr>';

  return html;
}