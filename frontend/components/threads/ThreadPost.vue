<template>
  <li>
    <v-row class="mt-1">
      <v-col cols="1">
        <v-row class="pb-3 author" justify="center" @click="enterProfile">
          <v-card
            class="portrait ml-5 mr-2 img"
            :img="author.image"
            height="40"
            width="40"
          ></v-card>
          <div id="username">
            <p>{{ author.username }}</p>
          </div>
        </v-row>
      </v-col>
      <v-col cols="9">
        <v-row justify="left ml-5">{{ content }}</v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="2">
        <v-row justify="left">
          <p>
            {{ created }}
          </p>
        </v-row>
      </v-col>
    </v-row>
    <v-divider></v-divider>
  </li>
</template>

<script>
export default {
  props: ['id', 'author-id', 'content', 'created'],
  data() {
    return {
      image: 'https://placekitten.com/600/600',
      author: '',
    };
  },
  methods: {
    enterProfile() {
      this.$router.push({ path: `/users/${this.author.id}` });
    },
  },
  created() {
    this.author = this.$store.getters['users/getAuthorCred'](
      this.authorId
    )
  },
};
</script>

<style lang="scss" scoped>
li {
  min-height: 100px;
  margin-left: 5px;
}
.author {
  cursor: pointer;
}
</style>
