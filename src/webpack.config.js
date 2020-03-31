const path = require('path');

module.exports = {
  entry: {
    frontpage: './app/features/frontpage/main.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, './app/static')
  }
};