function getRandomColor() {
  // Tạo giá trị ngẫu nhiên cho ba thành phần màu: đỏ, xanh lá cây và xanh dương
  var red = Math.floor(Math.random() * 256);
  var green = Math.floor(Math.random() * 256);
  var blue = Math.floor(Math.random() * 256);

  // Tạo chuỗi màu trong định dạng hex (#RRGGBB)
  var color = "#" + red.toString(16) + green.toString(16) + blue.toString(16);

  return color;
}