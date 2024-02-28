$(document).ready(() => {
  $('INPUT#language_code').click(() => {
    $('DIV#hello').empty();
    const code = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + code,
      type: 'GET',
      success: (data) => {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
