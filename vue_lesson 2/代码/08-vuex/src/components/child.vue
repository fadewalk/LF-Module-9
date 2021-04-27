<template>
	<div>
		<p>{{myCount}}</p>
	</div>
</template>

<script>
export default {

  name: 'child',

  data() {
    return {

    };
  },
  computed:{
  	myCount(){
  		return this.$store.state.count;
  	}
  }
};
</script>

<style lang="css" scoped>
</style>
