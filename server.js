const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

// 静的ファイルを提供
app.use(express.static(path.join(__dirname, 'public')));

// ルートURLにアクセスした時にcamera.htmlを表示
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'camera.html'));
});

app.listen(PORT, () => {
  console.log(`サーバーが起動しました: http://localhost:${PORT}`);
}); 