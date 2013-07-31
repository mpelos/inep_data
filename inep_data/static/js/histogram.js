var drawHistogram = function(school, city) {
  $('.histogram').highcharts({
    chart: {
      type: 'line',
      marginRight: 130,
      marginBottom: 80
    },

    title: {
      text: 'HISTOGRAMA DE ' + school.name + " (" + city.name + ")",
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

    yAxis: {
      title: {
        text: ''
      }
    },

    tooltip: {
      valueSuffix: '%'
    },

    legend: {
      y: 0
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
