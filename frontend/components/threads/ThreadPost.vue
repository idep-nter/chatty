<template>
  <li>
    <v-row class="mt-3 mb-3">
      <v-col cols="1">
        <div class="author mb-3 mt-1" @click="enterProfile">
          <v-row class="justify-center">
            <v-card :img="author.image" height="40" width="40"></v-card>
          </v-row>
          <v-row id="username" class="justify-center">
            <p>{{ author.username }}</p>
          </v-row>
        </div>
      </v-col>
      <v-col cols="10" class="contentCol">
        <v-row
          v-if="content.length > 454 && lessContent"
          class="ml-5 mr-5 justify-left"
          >{{ cutContent }}
          <span class="loadMoreLess" @click="togglePostLength()"
            >... view more</span
          >
        </v-row>

        <v-row
          v-else-if="content.length > 454 && !lessContent"
          class="ml-5 mr-5 justify-left"
          >{{ content }}
          <span class="loadMoreLess" @click="togglePostLength()"
            >... view less</span
          >
        </v-row>

        <v-row v-else class="justify-left content mb-3 ml-5 mr-5"
          >{{ content }}
        </v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="1" class="mb-5">
        <v-row>
          <p>
            {{ date }}
          </p>
        </v-row>
        <v-row class="mt-0">
          <p>
            {{ time }}
          </p>
        </v-row>
      </v-col>
    </v-row>
    <v-divider v-if="!last"></v-divider>
  </li>
</template>

<script>
import { formatPostDate } from '~/helperFunctions';
export default {
  props: ['id', 'author-id', 'content', 'created', 'last'],
  data() {
    return {
      author: '',
      cutContent: '',
      lessContent: true,
      date: '',
      time: '',
    };
  },
  computed: {},
  methods: {
    enterProfile() {
      this.$router.push({ path: `/users/${this.author.id}` });
    },
    togglePostLength() {
      this.lessContent = !this.lessContent;
    },
  },
  created() {
    this.author = this.$store.getters['users/getUserInfo'](this.authorId);
    this.cutContent = this.content.slice(0, 454);
    this.date = formatPostDate(this.created).split(" ")[0];
    this.time = formatPostDate(this.created).split(" ")[1];
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
.contentCol {
  // padding-top: 0px;
  position: relative;
}

</style>
