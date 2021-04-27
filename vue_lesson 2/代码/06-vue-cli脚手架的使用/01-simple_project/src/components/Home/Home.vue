<template>
	<div class ="home">
		我是首页====={{text}}
        <Header />

		<button @click ='addHandler' >触发</button>
	</div>
</template>

<script>
export default {

  name: 'Home',
  methods:{
  	addHandler(){
  		this.$emit('add','哈哈哈')
  	}
  },
  data() {
    return {

    };
  },
  props:['text']
};
</script>

<style lang="css" scoped>
</style>
