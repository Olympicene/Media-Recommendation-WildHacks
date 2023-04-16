<template>
	<div class="content button-container">
		<section>
			<div class = " col">
				<button class = "upvote button">Downvote</button>
			</div>
			<div class = "col">
				<button class = "question button">IDK</button>
			</div>
			<div class = "col">
				<button class = "downvote button">Upvote</button>
			</div>
		</section>
	</div>
</template>

<style>
	.button-container {
		height: 50px;
		padding: 30px;
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
		background-image: url("../assets/up.png");
		background-size: cover;
	}

	.downvote {
		border-radius: 0px 20px 20px 0px;
		background-color: #f99a9e	;
	}

	.question {
		background-color: #F9FCFB;
	}
	
	.col {
		float: left;
		width: 33.33%;
		margin-bottom: 10px;
	}
</style>  