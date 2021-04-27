//自带nodejs环境  cmd规范
// module.exports = {}
// var a = require('./webpack.config.js')

// nodejs中内容模块
var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
// html-webpack-plugin
// 如果在项目中配置了webpack.config.js 那么在终端中直接输入webpack,默认识别webpack.config.js项目配置文件
module.exports = {
	// 入口
	entry:{
		"main":'./src/main.js'
	},
	// 出口
	output:{
		path:path.resolve('./dist'),//相对转绝对
		filename:'./bundle.js'
	},
	// 模块中的loader  loader加载器 它能对css、json png jpg mp3 mp4 es6的js代码
	module:{
		loaders:[
			{
				test:/\.css$/,
				loader:'style-loader!css-loader'

			},
			{
				test:/\.vue$/,
				loader:'vue-loader'

			}
		]
	},
	watch:true,
	// 插件
	plugins:[
		new HtmlWebpackPlugin({
			template:'./index.html',//参照物
		})
	]



}
