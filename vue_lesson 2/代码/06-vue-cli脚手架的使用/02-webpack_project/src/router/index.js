// 整个路由的配置文件

import Vue from 'vue'
import VueRouter from 'vue-router'
// alias   @
// /Users/majinju/Desktop/vue_lesson/代码/06-vue-cli脚手架的使用/02-webpack_project/src
import Home from '@/components/Home/Home'
import FreeCourse from '@/components/FreeCourse/FreeCourse'

// 让vue使用此插件
Vue.use(VueRouter);

// Vue.protoype.$router = VueRoute

var router = new VueRouter({
	routes:[
		{
			path:'/',
			name:'Home',
			component:Home
		},
		{
			path:'/free',
			name:'FreeCourse',
			component:FreeCourse
		}

	]
})
export default router;