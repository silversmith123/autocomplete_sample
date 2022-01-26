<!-- Some component.vue -->
<template>
  <VueSimpleSuggest
    ref="suggest"
    v-model="chosen"
    :min-length="0"
    :debounce="150"
    :list="simpleSuggestionList"
    display-attribute="text"
    @suggestion-click="onSuggestClick"
>
<!-- Filter by input text to only show the matching results -->
    <div slot="misc-item-above" slot-scope="{ suggestions, query }">
      <div class="misc-item">
        <span>You're searching for {{ query }}.</span>
      </div>
      <div class="misc-item">
        <span>{{ suggestions.length }} suggestions are shown...</span>
      </div>
      <hr>
    </div>
    <div slot="suggestion-item" slot-scope="{ suggestion }">
        <img :src="suggestion.img" width="30px"/>
        <span>{{ suggestion.text }}</span>
    </div>
  </VueSimpleSuggest>
</template>

<script>
  import VueSimpleSuggest from 'vue-simple-suggest'
  import 'vue-simple-suggest/dist/styles.css' // Optional CSS

  export default {
    components: {
      VueSimpleSuggest
    },
    data() {
      return {
        chosen: ''
      }
    },
    methods: {
      simpleSuggestionList() {
        const qs = new URLSearchParams;
        qs.append('text', this.$refs.suggest.text);
        return fetch(`http://3.113.171.65/suggest?${qs}`, { method: 'GET', mode: "cors"})
          .then(response => response.json());
      },
      onSuggestClick (suggest) {
        //トラッキングもこの位置を想定
        location = 'https://www.google.com/search?q=' + encodeURI(suggest.text);
      }
    }
  }
</script>
