// main.js是整个项目的入口启动文件

// 导入npm下载的模块
import Vue from 'vue'
// 导入自己编写的模块  
// 不同在于 如果是npm下载的 from '名称'  自己编写的模块  from '路径引入'
import App from './App.vue'


// 1.引入全局的组件
import Header from './components/Common/Header.vue'
// 2.注册全局组件
Vue.component(Header.name,Header);




new Vue({
  el: '#app',
  // DOM直接渲染  
  // appendChild()
  render: h => h(App)
})
