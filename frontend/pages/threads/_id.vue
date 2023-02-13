<template>
  <v-container class="mt-12 mainRow d-flex justify-center">
    <v-card
      width="1200"
      min-height="819"
      max-height="auto"
      class="pa-2 mb-3 itemCard"
    >
      <v-container class="d-flex justify-center pb-0"
        ><h1>{{ thread.name }}</h1>
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
            :info="thread"
          ></info-dialog>
        </v-dialog>
      </v-container>
      <v-container class="d-flex justify-center pt-0">
        <v-chip-group>
          <v-chip v-for="tag in tags" :key="tag.id">
            {{ tag.name }}
          </v-chip>
        </v-chip-group>
      </v-container>

      <v-container class="justify-center d-flex mb-5">
        <v-btn @click="refresh()" class="mr-5" color="primary">Refresh</v-btn>
        <v-btn
          v-if="posts.length > 3"
          @click="scrollToElement()"
          color="primary"
          >Add post</v-btn
        >
      </v-container>

      <v-container v-if="posts.length > 0" class="pb-0">
        <thread-post
          v-for="(post, index) in posts"
          :key="post.id"
          :id="post.id"
          :author-id="post.author"
          :content="post.content"
          :created="post.createdAt"
          :last="lastIndexCheck(index)"
        >
        </thread-post>

        <v-container class="mt-5 pt-0">
          <v-pagination color="primary"></v-pagination>
        </v-container>
      </v-container>
      <v-container v-else class="d-flex justify-center noPosts">
        <h2>No posts yet!</h2>
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
        <v-container class="d-flex justify-center pb-12 pt-0">
          <v-btn color="primary" @click="submitForm()" :disabled="!loggedIn||!post" 
            >Submit</v-btn
          >
        </v-container>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import InfoDialog from '~/components/dialogs/InfoDialog.vue';
import ThreadPost from '~/components/threads/ThreadPost.vue';

export default {
  components: { ThreadPost, InfoDialog },
  data() {
    return {
      infoDialog: false,
      addPostDialog: false,
      id: '',
      thread: '',
      posts: [],
      tags: [],
      valid: true,
      post: '',
      postRules: [
      (v) => {
          if (v.length > 999)  {
            return 'You must enter a first name.'
          }  
          return true
        },
      ],
    };
  },
  computed: {
    loggedIn() {
      return this.$store.getters['auth/loggedIn'];
    },
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
    async submitForm() {
      if (this.$refs.form.validate()) {
        const formData = {
          thread: this.id,
          post: this.post,
        };
        await this.$store.dispatch('threads/addPost', formData);

        await this.$store.dispatch('users/loadUserId');
        const id = this.$store.getters['users/getUserId'];
        const author = this.$store.getters['users/getUserInfo'](id);
        await this.$store.dispatch('users/addPostCount', author);
        
        await this.$store.dispatch('threads/loadPosts');
        this.refresh()
      }
    },
    refresh() {
      this.posts = this.$store.getters['threads/getThreadPosts'](this.id);
      this.post = ''
    }
  },
  created() {
    this.id = this.$route.params.id;
    this.thread = this.$store.getters['threads/getThreadById'](this.id);
    this.posts = this.$store.getters['threads/getThreadPosts'](this.id);
    this.tags = this.$store.getters['threads/getThreadTags'](this.thread.tags);
  },
};
</script>

<style lang="scss" scoped>
.noPosts {
  align-items: center;
  height: 20%;
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
