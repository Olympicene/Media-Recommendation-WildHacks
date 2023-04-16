<template>
	<div class="content button-container">
		<section>
			<div class = " col" @click="onUpvote">
				<button class = "upvote button">I disagree.</button>
			</div>
			<div class = "col" @click="onRefreshButton">
				<button class = "refresh button">IDK</button>
			</div>
			<div class = "col" @click="onDownvote">
				<button class = "downvote button">I agree!</button>
			</div>
		</section>
	</div>
</template>

<script>
export default {
  name: 'NameCards',
  methods: {
	onRefreshButton (event) {
		this.$emit('refreshed', 'someValue')
	},
	onDownvote (event) {
		this.$emit('downvoted', 'someValue')
	},
	onUpvote (event) {
		this.$emit('upvoted', 'someValue')
	}
  }
}
</script>

<style>
	.button-container {
		height: 50px;
		padding-bottom: 30px;
	}

	.button {
		padding: 20px 28px;
		display: block;
		width: 100%;
		border: none;
		font-size: 16px;
		cursor: pointer;
		text-align: center;	
	}

	.button:hover {
		background-color: #ddd;
		color: black;
	}

	.upvote {
		border-radius: 20px 0px 0px 20px;
		background-color: #adc1da;
		background-size: cover;
	}

	.downvote {
		border-radius: 0px 20px 20px 0px;
		background-color: #f99a9e	;
	}

	.refresh {
		background-color: #F9FCFB;
	}
	
	.col {
		float: left;
		width: 33.33%;
		margin-bottom: 10px;
	}
</style>  