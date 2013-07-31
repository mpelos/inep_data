var drawHistogram = function(school, city) {
  $('.histogram').highcharts({
    chart: {
      type: 'line',
      marginRight: 130,
      marginBottom: 25
    },

    title: {
      text: 'Histograma de' + school.name,
      x: -20 //center
    },

    subtitle: {
      text: 'fonte: INEP',
      x: -20
    },

    xAxis: {
      categories: ['0-99', '100-199', '200-299', '300-399', '400-499',
        '500-599', '600-699', '700-799', '800-899', '900-1000']
    },

    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      x: -10,
      y: 100,
      borderWidth: 0
    },

    series: [{
      name: school.name,
      data: school.relative_scores
    }, {
      name: city.name,
      data: city.relative_scores
    }]
  });
};

jQuery(function($) {
  $("select.schools").change(function() {
    var code = this.value;

    $.getJSON("/schools/" + code, function(data) {
      drawHistogram(data.school, data.city);
    });
  });
});
