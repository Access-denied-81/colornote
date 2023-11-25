
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  let isDrawing = false;
  let currentTool = 'pen';
  let currentColor = '#000000';
  let currentSize = 5;
  let title = document.getElementById("title");
  canvas.addEventListener('mousedown', startDrawing);
  canvas.addEventListener('mousemove', draw);
  canvas.addEventListener('mouseup', stopDrawing);
  canvas.addEventListener('mouseout', stopDrawing);

  // WebSocket connection to the server
  const wsScheme = window.location.protocol === "https:" ? "wss://" : "ws://";
  const wsPath = wsScheme + window.location.host + '/ws/drawing/';  // Replace this with your WebSocket path
  const ws = new WebSocket(wsPath);

  ws.onopen = function () {
    console.log('WebSocket connection established.');
  };

  ws.onerror = function (error) {
    console.error('WebSocket error:', error);
  };

  ws.onmessage = function (event) {
    const data = JSON.parse(event.data);
    drawOnCanvas(data);
  };

  function startDrawing(e) {
    isDrawing = true;
    draw(e);
  }

  function draw(e) {
    if (!isDrawing) return;
    ctx.beginPath();
    ctx.lineWidth = currentSize;
    ctx.lineCap = 'round';
    ctx.strokeStyle = currentColor;
    const x = e.clientX - canvas.getBoundingClientRect().left;
    const y = e.clientY - canvas.getBoundingClientRect().top;

    if (currentTool === 'pen') {
      ctx.globalCompositeOperation = 'source-over';
      ctx.moveTo(x, y);
      ctx.lineTo(x, y);
      ctx.stroke();
    } else if (currentTool === 'eraser') {
      ctx.globalCompositeOperation = 'destination-out';
      ctx.arc(x, y, currentSize / 2, 0, Math.PI * 2);
      ctx.fill();
    }

    // Send drawing data to the server via WebSocket
    const drawingData = {
      x: x,
      y: y,
      tool: currentTool,
      color: currentColor,
      size: currentSize
    };
    ws.send(JSON.stringify(drawingData));
  }

  function stopDrawing() {
    isDrawing = false;
  }

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Send a signal to the server to clear the canvas for other users
    const clearData = { clearCanvas: true };
    ws.send(JSON.stringify(clearData));
  }

  function selectTool() {
    currentTool = document.getElementById('tool').value;
  }

  function selectColor() {
    currentColor = document.getElementById('color').value;
  }

  function selectSize() {
    currentSize = document.getElementById('size').value;
  }

  function drawOnCanvas(data) {
    // Implement logic to draw on the canvas using received data
    // Example: draw a line or point based on data
    ctx.beginPath();
    ctx.lineWidth = data.size;
    ctx.lineCap = 'round';
    ctx.strokeStyle = data.color;

    if (data.tool === 'pen') {
      ctx.globalCompositeOperation = 'source-over';
      ctx.moveTo(data.x, data.y);
      ctx.lineTo(data.x, data.y);
      ctx.stroke();
    } else if (data.tool === 'eraser') {
      ctx.globalCompositeOperation = 'destination-out';
      ctx.arc(data.x, data.y, data.size / 2, 0, Math.PI * 2);
      ctx.fill();
    }
  }
