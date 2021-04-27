<template>
	<div>
		
		<h3>{{att}}</h3>
	</div>
</template>

<script>
export default {

  name: 'Header',

  data() {
    return {
    	att:"alex"
    };
  },
};
</script>

<style scoped>
h3{
	color: green;
}

</style>
