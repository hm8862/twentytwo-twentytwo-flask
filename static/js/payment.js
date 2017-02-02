
$(function() {
  var $form = $('#payment-form');
  $form.submit(function(event) {

    // Disable the submit button to prevent repeated clicks:
    $form.find('.submit').prop('disabled', true);

    // Request a token from Stripe:
    Stripe.card.createToken($form, stripeResponseHandler);

    // Prevent the form from being submitted:
    return false;
  });
});

function stripeResponseHandler(status, response) {
  // Grab the form:
  var $form = $('#payment-form');

    var $card_number = $('#card_number').val().length;
    var $exp_month = $('#exp_month').val().length;
    var $exp_year = $('#exp_year').val().length;
    var $cvc = $('#cvc').val().length;
    console.log($card_number, $exp_month, $exp_year, $cvc);
    if ($card_number == 0 || $exp_month == 0 || isNaN($exp_month) || $exp_year == 0 || isNaN($exp_year) || $cvc == 0) {
      $form.get(0).submit();
    }

  if (response.error) { // Problem!

    // Show the errors on the form:
    $form.find('.payment-errors').text(response.error.message);
    $form.find('.submit').prop('disabled', false); // Re-enable submission

  } else { // Token was created!

    // Get the token ID:
    var token = response.id;

    // Insert the token ID into the form so it gets submitted to the server:
    $form.append($('<input type="hidden" name="stripeToken">').val(token));

    // Submit the form:
    $form.get(0).submit();
  }
};