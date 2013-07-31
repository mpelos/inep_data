jQuery(function($) {
  $(".schools").select2({
    minimumInputLength: 3,

    ajax: {
      url: "/schools",
      dataType: 'json',

      data: function (term) {
        return { name: term };
      },

      results: function (data, page) {
        return { results: data.schools };
      }
    }
  }).on("select2-selecting", function(event) {
    $.getJSON("/schools/" + event.val, function(data) {
      drawHistogram(data.school, data.city);
    });
  });

  $("select.schools").change(function() {
    var code = this.value;

    $.getJSON("/schools/" + code, function(data) {
      drawHistogram(data.school, data.city);
    });
  });
});
