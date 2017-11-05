jQuery(document).ready(function($) {
    $(document).on('scroll', function () {
        if($(this).scrollTop() > 380) {
            $('nav.top').removeClass('top').hide().addClass('scrolled').slideDown('400')
        } else {
            $.when($('nav.scrolled').slideUp('fast')).done(function () {
                $(this).removeClass('scrolled').addClass('top').fadeIn();
            });
        }
    })
});
