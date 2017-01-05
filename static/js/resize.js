$(window).on('resize', function() {

    // get current dimensions
    var $top = $('#top-padding');
    var $bottom = $("#bottom-padding")
    var currentWidth = window.innerWidth
    var currentHeight = window.innerHeight
    var aspectRatio = 1.0 * 16 / 9

    // calculate required padding height
    var divHeight = (currentHeight - (currentWidth / aspectRatio)) / 2
   	
    // set div height
    $top.css("height", divHeight.toString() + "px" )
    $bottom.css("height", divHeight.toString() + "px")
}).trigger('resize');

