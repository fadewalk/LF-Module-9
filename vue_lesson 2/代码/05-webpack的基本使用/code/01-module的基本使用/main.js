// 整个程序的入口

// 引入第三方的库  es6Module模块导入方法
import Vue from './vue.js'

//再导入
// import App from './App.js'

// 对象的解构
// import {num,num2,add} from './App.js'


import * as  object from './App.js'
console.log(object)


// console.log(num);
// console.log(num2);
// add(3,5)



new Vue({
	el:"#app",
	data(){
		return {

		}
	},
	components:{
		App:object.default
	},
	template:`<App />`
});