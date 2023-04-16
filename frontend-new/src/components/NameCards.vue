<template>
	<div class="content">
		<section class="info-col">
			<div class="name-container">
				<h3>If you like the {{ type1 }}...</h3>
			</div>
			<div class="name-container">
				<h1>{{ name1 }}</h1>
			</div>
			<div class="name-container">
				<h3>You might like the {{ type2 }}...</h3>
			</div>
			<div class="name-container">
				<h1>{{ name2 }}</h1>
			</div>
		</section>
	</div>
</template>

<script>
export default {
  name: 'NameCards',
  props: {
    name1: {
      type: String,
      required: true,
    },
    name2: {
      type: String,
      required: true,
    },
	type1: {
      type: String,
      required: true,
    },
    type2: {
      type: String,
      required: true,
    },
  },
}
</script>
  
<style>
	.name-container {
		text-align: center;
	}
</style>  