<template>
  <RelationCards :imageURL1="media1.imageURL" :imageURL2="media2.imageURL"></RelationCards>
  <NameCards :name1="media1.name" :name2="media2.name" :type1="media1.type" :type2="media2.type"></NameCards>
  <ButtonSelect @refreshed="refreshMedia"></ButtonSelect>
</template>   

<script>
// @ is an alias to /src
import RelationCards from '@/components/RelationCards.vue';
import NameCards from '@/components/NameCards.vue';
import ButtonSelect from '@/components/ButtonSelect.vue';
import axios from "axios";

export default {
  name: 'HomeView',
  data() {
    return {
      media1: {},
      media2: {}
    }
  },
  methods: {
    refreshMedia() {
      console.log("this is a sign")
      axios.get('http://127.0.0.1:8000/rand')
      .then(response => {
        this.media1 = response.data
      }, error => {
        console.log(error);
      });

    axios.get('http://127.0.0.1:8000/rand')
      .then(response => {
        this.media2 = response.data
      }, error => {
        console.log(error);
      });
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/rand')
      .then(response => {
        this.media1 = response.data
      }, error => {
        console.log(error);
      });

    axios.get('http://127.0.0.1:8000/rand')
      .then(response => {
        this.media2 = response.data
      }, error => {
        console.log(error);
      });
  },
  components: {
    ButtonSelect,
    RelationCards,
    NameCards
}
}
</script>
