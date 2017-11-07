jQuery.fn.showModal = function(selector) {
  if (!selector) {
    return $(this);
  }
  jQuery(selector).fadeIn("fast");
  jQuery("body").addClass("no-scoll");
  return $(this);
};
jQuery.fn.hideModal = function() {
  jQuery(".modal:visible").fadeOut("fast");
  jQuery("body").removeClass("no-scoll");
  return $(this);
};
jQuery(document).ready(function($) {
  $(document).on("scroll", function(event) {
    if ($(".modal:visible").length) {
      event.preventDefault();
    }
    if ($(this).scrollTop() > 380) {
      $("nav.top")
        .removeClass("top")
        .hide()
        .addClass("scrolled")
        .slideDown("400");
    } else {
      $.when($("nav.scrolled").slideUp("fast")).done(function() {
        $(this)
          .removeClass("scrolled")
          .addClass("top")
          .fadeIn();
      });
    }
  });
  $(".close-button")
    .parent()
    .on("click", function(event) {
      event.preventDefault();
      $(this).hideModal();
    });
});
