<template>
	<nav class="content">
		<router-link to="/top">Top Rated</router-link>	
		<router-link to="/new">New</router-link>	
		<router-link to="/seen">Most Viewed</router-link>
		<router-link to="/">Random</router-link>	
		
		<div class="nav-right">
			<router-link to="/calories">Create</router-link>
		</div>
		
	</nav>
</template>
  
<style>

/* TOP LEFT */
nav a {
	
	font-size: 18px;
	text-decoration: none;
	text-align: center;
	color: #333333;
	position: relative;
	margin-right: 17px;
}

a:hover {
	border-bottom: 1px solid;
}

nav {
	padding-top: 10px;
	height: 55px;
	/*display: flex;*/
	justify-content: left;
	align-items: center;
	overflow: hidden;
}

/* RIGHT SIDE */
.nav-right {
  float: right;
}

</style>  