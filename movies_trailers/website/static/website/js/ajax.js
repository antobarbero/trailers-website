$(document).ready(function(){
  $("#search-trailers").submit(function(e){
    e.preventDefault();
    var q = $("#id_key_words").val();
    document.getElementById('result-container').innerHTML = '<center>Loading ...</center>';
    $.ajax({
      dataType: 'json',
      url: $(this).attr('action') + '?q=' + q,
      type: $(this).attr('method'),
      data: {},
      success: function(json){
        document.getElementById('result-container').innerHTML = '';
        json.forEach((movie) => {
            document.getElementById('result-container').innerHTML += renderItem(movie.Title, movie.trailers);
        });
      }
    });
  })
});

function renderItem(title, trailers) {
  var html = '<div class="row no-gutters"><div class="col-lg-12 showcase-text"><h2>' + title + '</h2></div>';

  trailers.forEach ((trailer) => {
    html += '<div class="col-lg-12 text-white showcase-img" align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/' + trailer + '"></iframe></div>';
  });

  if (trailers.length === 0) {
    html += '<div class="col-lg-12 showcase-text" align="center">No trailer found.</div>';
  }
  html += '</div><hr>';

  return html;
}