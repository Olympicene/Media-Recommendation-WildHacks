<template>
	<RelationCards :imageURL1="media1.imageURL" :imageURL2="media2.imageURL"></RelationCards>
	<NameCards :name1="media1.name" :name2="media2.name" :type1="media1.type" :type2="media2.type"></NameCards>
	<ButtonSelect @refreshed="refreshMedia" @upvoted="upvotePair" @downvoted="downvotePair"></ButtonSelect>
</template>

<script>
// @ is an alias to /src
import RelationCards from '@/components/RelationCards.vue';
import NameCards from '@/components/NameCards.vue';
import ButtonSelect from '@/components/ButtonSelect.vue';
import axios from "axios";

export default {
  name: 'New',
  data() {
    return {
      media1: {},
      media2: {}
    }
  },
  methods: {
    refreshMedia() {
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
    upvotePair() {
      axios.post('http://127.0.0.1:8000/upvote/', {
        rowID1: this.media1.rowid,
        rowID2: this.media2.rowid
      })
      .then(response => {
        console.log(response.data)
      }, error => {
        console.log(error);
      });
      this.refreshMedia()
    },
    downvotePair() {
      axios.post('http://127.0.0.1:8000/downvote/', {
        rowID1: this.media1.rowid,
        rowID2: this.media2.rowid
      })
      .then(response => {
        console.log(response.data)
      }, error => {
        console.log(error);
      });
      this.refreshMedia()
    }
  },
  created() {
    this.refreshMedia()
  },
  components: {
    ButtonSelect,
    RelationCards,
    NameCards
}
}
</script>