<template>
  <div class="hello">
      <h2>{{myCount}}</h2>
      <Child />
      <button @click ='asyncHandler'>同步修改</button>
      <button @click ='change'>异步修改</button>
  </div>
</template>

<script>
import Child from './child'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed:{
    myCount(){
      return this.$store.state.count;
    }
  },
  components:{
    Child
  },
  methods:{
    change(){
      
      this.$store.dispatch('addCount',3)
    },
    asyncHandler(){
      this.$store.dispatch('asyncHandler',1);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
