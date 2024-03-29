function getRandomColor() {
  // Tạo giá trị ngẫu nhiên cho ba thành phần màu: đỏ, xanh lá cây và xanh dương
  var red = Math.floor(Math.random() * 256);
  var green = Math.floor(Math.random() * 256);
  var blue = Math.floor(Math.random() * 256);

  // Tạo chuỗi màu trong định dạng hex (#RRGGBB)
  var color = "#" + red.toString(16) + green.toString(16) + blue.toString(16);

  return color;
}

function myChart(type, labels, values){
const ctx = document.getElementById('myChart');
    new Chart(ctx, {
      type: type,
      data: {
        labels: labels,
        datasets: [{
          label: 'Count Course',
          data: values,
          borderWidth: 1,
          backgroundColor: [
            getRandomColor(),
            getRandomColor(),
            getRandomColor()
          ],
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
}