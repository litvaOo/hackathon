jQuery.fn.showModal = function(selector) {
  if (!selector) {
    return $(this);
  }
  jQuery(selector).fadeIn("fast");
  jQuery("body").addClass("no-scoll");
  jQuery("#full-page").fullpage.setAllowScrolling(false);
  return jQuery(this);
};

jQuery.fn.hideModal = function() {
  jQuery(".modal:visible").fadeOut("fast");
  jQuery("body").removeClass("no-scoll");
  jQuery("#full-page").fullpage.setAllowScrolling(true);
  return jQuery(this);
};

jQuery(document).ready(function($) {
  $("#full-page").fullpage({
    parallax: true,
    parallaxOptions: {
      type: "reveal",
      percentage: 62,
      property: "translate"
    },
    navigation: true,
    navigationPosition: "right",
    onLeave: function(index, nextIndex, direction) {
      if (index === 1) {
        $("nav.top")
          .hide()
          .removeClass("top")
          .slideDown("fast");
      }
      if (nextIndex === 1) {
        $("nav")
          .hide()
          .addClass("top")
          .fadeIn("400");
      }
    }
  });
  $(".close-button")
    .parent()
    .on("click", function(event) {
      event.preventDefault();
      $(this).hideModal();
    });
  $(".login-link").on("click", function(event) {
    event.preventDefault();
    $(this)
      .hideModal()
      .showModal("#modal-login");
  });
  $(".signup-link").on("click", function(event) {
    event.preventDefault();
    $(this)
      .hideModal()
      .showModal("#modal-signup");
  });
});
