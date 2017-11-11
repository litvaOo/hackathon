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
  $("#full-page").fullpage({
    parallax: true,
    parallaxOptions: {
      type: "reveal",
      percentage: 62,
      property: "translate"
    },
    onLeave: function(index, nextIndex, direction) {
      if (index === 1) {
        $("nav.top")
          .hide()
          .removeClass("top")
          .slideDown("fast");
      }
      if (nextIndex === 1) {
        $.when($("nav").slideUp("fast")).then(function() {
          $(this)
            .addClass("top")
            .fadeIn("fast");
        });
      }
    }
  });
  $(".close-button")
    .parent()
    .on("click", function(event) {
      event.preventDefault();
      $(this).hideModal();
    });
});
