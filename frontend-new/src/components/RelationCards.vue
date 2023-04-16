<template>
	<div class="content">
		<section class="info-col">
			<div class="card-container">
				<img class="image" :src="imageURL1">
			</div>
			<div class="card-container">
				<img class="image" :src="imageURL2">
			</div>
		</section>
	</div>
</template>

<script>
export default {
  name: 'RelationCards',
  props: {
    imageURL1: {
      type: String,
      required: true,
    },
    imageURL2: {
      type: String,
      required: true,
    },
  },
}
</script>
  
<style>
	.card-container {
		text-align: center;
		/*background-color: red;*/
		display: flex;
		justify-content: center;
	}

	.image {
		
		border-radius: 5%;
		max-width: 100%;
    	max-height: 70vh;
		filter: drop-shadow(10px 10px 4px #494747);
		
	}
</style>  