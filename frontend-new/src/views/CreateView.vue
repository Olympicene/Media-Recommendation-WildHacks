<template>
  <body>
  <center>
    <h1><tt> Media Requests </tt></h1>
    <div class="boxed">
      <h2><tt> Name </tt></h2>
      <input type="text" id="Textbox" name="Name">
      <h2><tt> Media Type </tt></h2>
      <input type="text" id="Textbox" name="Type">
      <h2><tt> Pictures of Media </tt></h2>
      <input type="text" id="Textbox" name="Pics">
    </div>
  </center>
  </body>
</template>

<style>
  #Textbox {
    border-radius: 10px;
    border: 1px solid #73AD21;
    width: 200px;
    height: 50px;
  }

  .boxed {
    border: 1px solid black;
    padding: 10px;
    width: 300px;
    padding-bottom: 50px;
  }

  h1 {
    text-align: center;
  }

  h2 {
    text-align: center;
  }

  body {
    background-color: #EADDCA;
  }
</style>
