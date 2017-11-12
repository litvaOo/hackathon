jQuery.fn.showModal = function(selector) {
  if (!selector) {
    return $(this);
  }
  jQuery(selector).fadeIn("fast");
  jQuery("body").addClass("no-scoll");
  if (jQuery("#full-page").length) {
    jQuery("#full-page").fullpage.setAllowScrolling(false);
  }
  return jQuery(this);
};

jQuery.fn.hideModal = function() {
  jQuery(".modal:visible").fadeOut("fast");
  jQuery("body").removeClass("no-scoll");
  if (jQuery("#full-page").length) {
    jQuery("#full-page").fullpage.setAllowScrolling(true);
  }
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
  $(".job-create-link").on("click", function(event) {
    event.preventDefault();
    $(this)
      .hideModal()
      .showModal("#modal-job-create");
  });
  $("form[name='login-form']").on("submit", function(event) {
    event.preventDefault();
    $.post("/api/v1/rest-auth/login/", {
      email: $(this)
        .find('input[name="email"]')
        .val(),
      password: $(this)
        .find('input[name="password"]')
        .val(),
      csrfmiddlewaretoken: $(this)
        .find('input[name="csrfmiddlewaretoken"]')
        .val()
    })
      .then(function(response) {
        window.location.reload();
      })
      .catch(function(error) {
        $("span.error-message").text(error.responseJSON.non_field_errors);
      });
  });
  // TODO
  // $("form[name='signup-form']").on("submit", function(event) {
  //   event.preventDefault();
  //   $.post("/api/v1/rest-auth/registration/", $(this).serialize())
  //     .then(function(response) {
  //       window.location.reload();
  //     })
  //     .catch(function(error) {
  //       $("span.error-message").text(error.responseJSON.non_field_errors);
  //     });
  // });
});

function initialize() {
  var options = {
    types: ["(cities)"]
  };

  var input = document.getElementById("id_location");
  var autocomplete = new google.maps.places.Autocomplete(input, options);
  google.maps.event.addListener(autocomplete, "place_changed", function() {
    var place = autocomplete.getPlace();
    $("#id_city").val(
      place.address_components.filter(r => r.types[0] === "locality")[0]
        .long_name
    );
    $("#id_country").val(
      place.address_components.filter(r => r.types[0] === "country")[0]
        .long_name
    );
  });
}

google.maps.event.addDomListener(window, "load", initialize);
