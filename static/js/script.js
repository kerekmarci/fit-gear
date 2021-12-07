/*
This code from:
https://templatemo.com/tm-559-zay-shop
*/

$(document).ready(function () {

    // Accordion
    var all_panels = $('.templatemo-accordion > li > ul').hide();

    $('.templatemo-accordion > li > a').click(function () {
        var target = $(this).next();
        if (!target.hasClass('active')) {
            all_panels.removeClass('active').slideUp();
            target.addClass('active').slideDown();
        }
        return false;
    });
    // End accordion
});

/* Auto-close message alerts */
setTimeout(function () {
    $('#message').fadeOut('slow');
}, 4000);