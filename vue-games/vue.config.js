module.exports = {
  publicPath: 'https://play2learn-6e8de4778938.herokuapp.com/static/dist', // The base URL where your app will be deployed
  outputDir: '../static/dist', // The path for where files will be output when the app is built
  indexPath: '../../templates/_base_vue.html', // The path for the generated index file

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true,
      },
    },
  },
};

// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
