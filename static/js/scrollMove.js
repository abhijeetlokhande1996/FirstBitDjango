function scrollMove(ele, frame, step) {
  var step = step || 1;
  var $item = $(ele).children();
  var w = 0;
  iLen = $item.length;
  for (let i = 0; i < iLen; i++) {
    const element = $item[i];
    w += element.clientWidth + Math.random() * 100;
  }

  $(ele).html($(ele).html() + $(ele).html());

  var $items = $(ele);

  var temp = 0;
  function move() {
    if (temp > w) {
      temp = 0;
    } else {
      temp = temp + step;
    }
    
    $items.scrollLeft(temp);
  }

  setInterval(move, 1000 / frame);
}
