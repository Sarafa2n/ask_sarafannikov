jQuery(function ($) {
  "use strict";

  const $formErrors = $('.form__errors');

  $('#js-btn-logout').on('click', function (event) {
    event.preventDefault();
    $.get('/api/logout',
        function (data) {
            if(data.status === 'success')
                location.replace('/');
        });
  });


  $(window).load(function() {
    $("body").removeClass("preload");
  });


  const $formLogin = $('.js-form-signin');

  $formLogin.on('submit', function (event) {
    event.preventDefault();
    let $target = $(event.target);
    let url = $target.attr("action");
    $.post(url, $formLogin.serialize(),
        function(data){
      if (data.status === 'auth'){
        $('.form__errors').text(data.errors.username);
      }
      if (data.status === 'invalid'){
        if (data.errors.password) {
          $formErrors.text(data.errors.password);
        }
        if (data.errors.username){
          $formErrors.text(data.errors.username);
        }
        if (data.errors.__all__){
          $formErrors.text(data.errors.__all__);
        }
      }
      if (data.status === 'success'){
        document.location.replace("/");
      }
    });
  });


});