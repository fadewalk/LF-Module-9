<template>
  <!-- 组件的页面结构 -->
  <div id="app">
    <Header />
  <h3>{{msg}}</h3>  
    <div v-html = 'title'></div>
    <ul>
      <!-- key绑定key的时候 如果数据中有id 就绑定id，没有id 绑定index -->
      <li v-for = '(item,index) in datas' :key = 'index'>
        {{ item }}
      </li>
    </ul>

    <Home  :text = 'text' @add = 'addHandler'/>

  </div>
</template>

<script>
//导入
import Home from './components/Home/Home.vue'

// 组件内部的业务逻辑
export default {
  name: 'app',
  data () {
    return {
      msg: '我们来学习vue-cli脚手架项目',
      title:"<h3>alex</h3>",
      datas:['抽烟','喝酒','烫头'],
      text:"我是父组件的内容"
    }
  },
  components:{
    Home
  },
  methods:{
    addHandler(data){
      console.log(data);
    }
  }
}
</script>

<style>
/*组件的样式*/
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
