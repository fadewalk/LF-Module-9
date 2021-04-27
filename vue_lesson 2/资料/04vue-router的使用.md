#### 前端路由的实现原理

​	详情请结合代码观看

​	vue+vue-router  主要来做单页面应用（Single Page Application）

#### 为什么我们要做单页面应用？

	
	（1）传统的开发方式 url改变后，立马发送请求，响应整个页面，有可能资源过多，传统开发会让前端的页面出现 “白屏” 用户体验不好
	
	（2）SPA 单页面应用 ： 锚点值的改变后，不会立刻发送请求，而是在某个合适的时机，发送ajax请求，局部改变页面中的数据
	
	页面不立刻跳转用户体验好
#### vue-router集成

	它是vue中核心插件
1. 下载vue-router   

   ```javascript
   npm init --yes
   npm install vue-router --save
   ```

   - 引入vue-router的模块  默认会抛出一个VueRouter对象 另外还有两个全局的组件router-link 和router-view

2. Vue.use(VueRouter)

3. 创建路由对象
    		
   ​		


	var router = new VueRouter({
	
	// 配置路由对象
	
	routes:[
	{
		path:'/login',
		name:'login',
		component:Login
	},
	{
		path:'/register',
		name:'register',
		component:Register
	}
	]
	
	});
	
	4.路由对象挂载到vue实例化对象中
	
	var App = {
			template:`
				<div>
					<!--router-link默认会被渲染成a标签 to属性默认会被渲染成href属性-->
					<router-link :to="{name:'login'}">登录页面</router-link>
					<router-link :to="{name:'register'}">注册页面</router-link>
			
					<!--路由组件的出口-->
	
					<router-view></router-view>
	
				</div>
			`
		};
	
		new Vue({
			el:'#app',
			components:{
				App
			},
			//挂载
			router,
			template:`<App />`
		});

#### 命名路由 

给当前的配置路由信息对象设置name:'login'属性

:to = "{name:'login'}"

#### 路由范式

   (1)xxxx.html#/user/1
        配置路由对象中  
    

        	 {
        	 	path:'/user/:id',
        	 	component:User
        	 }
    
        	 <router-link :to = "{name:'user',params:{id:1}}"></router-link>
   (2)xxxx.html#/user?userId = 1

   	{
   		path:'/user'
   	}
   	 <router-link :to = "{name:'user',query:{id:1}}"></router-link>

	在组件内部通过this.$route 获取路由信息对象

#### 嵌套路由

	一个router-view 嵌套另外一个router-view
#### 动态路由匹配

```javascript
let User = {
  template: '<div>User</div>'
}

let router = new VueRouter({
  routes: [
    // 动态路径参数 以冒号开头
    { path: '/user/:id', component: User }
  ]
})
```

现在呢，像 `/user/foo` 和 `/user/bar` 都将映射到相同的路由。

一个“路径参数”使用冒号 `:` 标记。当匹配到一个路由时，参数值会被设置到 `this.$route.params`，可以在每个组件内使用。于是，我们可以更新 `User` 的模板，输出当前用户的 ID：

```html
let User = {
  template: '<div>User {{ $route.params.id }}</div>'
}
```

