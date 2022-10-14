<template>
  <li>
    <v-row class="mt-2">
      <v-col cols="1">
        <v-row class="author" justify="center" @click="enterProfile">
          <v-card
            class="portrait img"
            :img="author.image"
            height="40"
            width="40"
          ></v-card>
          <div id="username">
            <p>{{ author.username }}</p>
          </div>
        </v-row>
      </v-col>
      <v-col cols="10" class="contentCol">


        <v-row
          v-if="content.length > 200 && lessContent"
          justify="left"
          class="content mb-2 ml-5 mr-5"
          >{{ cutContent }}
          <span class="loadMoreLess" @click="togglePostLength()">... view more</span>
        </v-row>


        <v-row
          v-else-if="content.length > 200 && !lessContent"
          justify="left"
          class="content mb-1 ml-5 mr-5"
          >{{ content }} <span class="loadMoreLess" @click="togglePostLength()">... view less</span>
        </v-row>


        <v-row
          v-else
          justify="left"
          class="content mb-1 ml-5 mr-5"
          >{{ content }}
        </v-row>


        



      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="1">
        <v-row>
          <p>
            {{ created }}
          </p>
        </v-row>
      </v-col>
    </v-row>
    <v-divider v-if="!last"></v-divider>
  </li>
</template>

<script>
export default {
  props: ['id', 'author-id', 'content', 'created', 'last'],
  data() {
    return {
      author: '',
      cutContent: '',
      lessContent: true,
    };
  },
  computed: {
  },
  methods: {
    enterProfile() {
      this.$router.push({ path: `/users/${this.author.id}` });
    },
    togglePostLength() {
      this.lessContent = !this.lessContent
      console.log(this.lessContent)
    }
  },
  created() {
    this.author = this.$store.getters['users/getUserInfo'](this.authorId);
    this.cutContent = this.content.slice(0, 454);
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
  margin-top: 0px;
}

.loadMoreLess {
  color: $primaryColor;
  font-weight: bold;
  padding-left: 1px;
  cursor: pointer;
  // font-size: 20px;
}

// .contentCol {
//   position: relative;
// }

// .content {
//   position: absolute;
//   bottom: 0%;
//   left: 0%;
//   right: 0%;
// }
</style>
