<!--  组件结构 html
	 业务逻辑 js
	 组件样式 css
 -->
 <template>
 	<!-- 一定是闭合标签 -->
 	<div class="app">
	
 		<h3>{{msg}}</h3>
 		<ul>
 			<li>1</li>
 			<li>2</li>
 			<li>3</li>
 			<li>4</li>
 			<li>5</li>
 		</ul>
 		<Header />
 	</div>
 	
 </template>
 <script>
 import Header from './Header.vue'
 	export default{
 		data(){
 			return {
 				msg:'学习单页组件'
 			}
 		},
 		methods:{

 		},
 		computed:{

 		},
 		components:{
 			Header
 		}
 	}
 </script>
 <!-- scoped 它表示只对当前组件的样式起作用 -->
 <style scoped>
 /*全局的*/
 h3{
 	color: yellow;
 }
 	
 </style>