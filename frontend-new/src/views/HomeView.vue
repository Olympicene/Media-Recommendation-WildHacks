<template>
  <RelationCards></RelationCards>
  <ButtonSelect></ButtonSelect>
</template>   

<script>
// @ is an alias to /src
import RelationCards from '@/components/RelationCards.vue';
import ButtonSelect from '@/components/ButtonSelect.vue';

export default {
  name: 'HomeView',
  components: {
      ButtonSelect,
      RelationCards
}
}
</script>
