$(document).ready(function() {

    $(".play").click(function() {
        $("#iframe1").show('1500');
    });
    $(".playlistbtn").click(function() {
        $("#myIframe2").show('1500');
    });
    $(".playProfile").click(function() {
        $("#iframe3").show('1500');
    });

    $(".editphoto").click(function() {
        $("#updateprof").show('1500');
    });
    $("#submit").click(function() {
        $("#updateprof").slideDown('2000');
    });


});