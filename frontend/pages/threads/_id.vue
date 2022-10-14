<template>
  <v-container class="mt-12 mainRow d-flex justify-center">
    <v-card
      max-width="1400"
      min-height="819"
      max-height="auto"
      class="pa-2 mb-3 itemCard"
    >
      <v-container class="d-flex justify-center"
        ><h1>{{ thread.title }}</h1>
        <v-dialog persistent v-model="infoDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              v-bind="attrs"
              v-on="on"
              class="ml-3"
              v-if="thread.description"
            >
              mdi-information-outline
            </v-icon>
          </template>
          <info-dialog
            @close-dialog="infoDialog = false"
            :info="thread.description"
          ></info-dialog>
        </v-dialog>
      </v-container>

      <v-container class="justify-center d-flex ml-1 mb-5">
        <v-btn class="mr-5" color="primary">Refresh</v-btn>
        <v-btn @click="scrollToElement()" color="primary">Add post</v-btn>
      </v-container>

      <v-container v-if="posts">
        <thread-post
          v-for="(post, index) in posts"
          :key="post.id"
          :id="post.id"
          :author-id="post.author"
          :content="post.content"
          :created="post.created"
          :last="lastIndexCheck(index)"
        >
        </thread-post>
      </v-container>
      <v-container
        id="noPosts"
        v-if="posts.length === 0"
        class="d-flex justify-center"
      >
        <h2>No posts yet!</h2>
      </v-container>

      <v-container class="mt-5">
        <v-pagination color="primary"></v-pagination>
      </v-container>

      <v-form ref="form" v-model="valid" lazy-validation class="">
        <v-container class="mt-10">
          <v-textarea
            ref="addPost"
            class="textarea"
            outlined
            justify="center"
            style="width: 700px"
            v-model="post"
            :rules="postRules"
            :counter="999"
            required
            height="250"
            placeholder="Write a post here..."
            no-resize
          ></v-textarea>
        </v-container>
        <v-container class="d-flex justify-center pb-12">
          <v-btn color="primary">Add post</v-btn>
        </v-container>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import InfoDialog from '~/components/dialogs/InfoDialog.vue';
import AddPostDialog from '~/components/dialogs/AddPostDialog.vue';
import ThreadPost from '~/components/threads/ThreadPost.vue';

export default {
  components: { AddPostDialog, ThreadPost, InfoDialog },
  data() {
    return {
      infoDialog: false,
      addPostDialog: false,
      id: '',
      thread: '',
      posts: [],
    };
  },
  computed: {
    //   getLastIndex(index) {
    //     const lastIndex = arr.length - 1
    //     return index === lastIndex ? true : false
    //   }
  },
  methods: {
    lastIndexCheck(index) {
      const lastIndex = this.posts.length - 1;
      if (index === lastIndex || (index % 9 === 0 && index != 0)) {
        return true;
      } else {
        return false;
      }
    },
    scrollToElement() {
      this.$refs.addPost.$el.scrollIntoView({ behavior: 'smooth' });
    },
  },
  created() {
    this.id = this.$route.params.id;
    this.thread = this.$store.getters['threads/getThreadById'](this.id);
    this.posts = this.$store.getters['posts/getPosts'](this.id);
  },
};
</script>

<style lang="scss" scoped>
#noPosts {
  align-items: center;
  height: 60%;
}
h1 {
  color: $primaryColor;
}

li {
  list-style-type: none;
}

.textarea {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
