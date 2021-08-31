
console.log("Javascript Connected!");
// Controller
$(function() {
  $('a#maju').bind('click', function() {
    $.getJSON('/maju',
        function(data) {
      //do nothing

    });
return false;
});
});


$(function() {
  $('a#kanan').bind('click', function() {
    $.getJSON('/kanan',
    function(data) {
  //do nothing
  
});
return false;
});
});

$(function() {
  $('a#kiri').bind('click', function() {
    $.getJSON('/kiri',
    function(data) {
  //do nothing
 
});
return false;
});
});


$(function() {
  $('a#mundur').bind('click', function() {
    $.getJSON('/mundur',
    function(data) {
  //do nothing

});
return false;
});
});

$(function() {
  $('a#berhenti').bind('click', function() {
    $.getJSON('/berhenti',
    function(data) {
  //do nothing

});
return false;
});
});
