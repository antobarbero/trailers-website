$(document).ready(function(){
  $("#search-trailers").submit(function(e){
    e.preventDefault();
    var q = $("#id_key_words").val();

    $.ajax({
      dataType: 'json',
      url: $(this).attr('action') + '?q=' + q,
      type: $(this).attr('method'),
      data: {},
      success: function(json){
        console.log(json)
      }
    });
  })
})
