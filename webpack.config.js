const path = require('path');

module.exports = {
  entry: './wagtail_multiple_chooser_panel/static_src/main.js',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.svg$/,
        use: ['@svgr/webpack'],
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: ['file-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  externals: {
    /* These are provided by Wagtail */
    'react': 'React',
    'react-dom': 'ReactDOM',
    'gettext': 'gettext',
    'jquery': 'jQuery',
  },
  output: {
    path: path.resolve(
      __dirname,
      'wagtail_multiple_chooser_panel/static/wagtail_multiple_chooser_panel/js'
    ),
    filename: 'wagtail-multiple-chooser-panel.js'
  },
};
