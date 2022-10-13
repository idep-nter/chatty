<template>
  <div>
    <v-row class="mt-12 mainRow d-flex justify-center">
      <v-col md="8" sm="7">
        <v-card max-width="1400" height="650" class="pa-2 itemCard">
          <v-container class="d-flex justify-center mb-5"
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
          <thread-post
            v-for="post in posts"
            :key="post.id"
            :id="post.id"
            :author-id="post.author"
            :content="post.content"
            :created="post.created"
          >
          </thread-post>
        </v-card>
        <v-pagination
          id="pagination"
          class="mt-8"
          color="primary"
        ></v-pagination>
      </v-col>

      <v-container class="justify-center d-flex">
        <v-btn class="mr-5" color="primary">Refresh</v-btn>
        <v-dialog persistent v-model="addPostDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary">Add post</v-btn>
          </template>
          <add-post-dialog
            @close-dialog="addPostDialog = false"
          ></add-post-dialog>
        </v-dialog>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import InfoDialog from '~/components/dialogs/InfoDialog.vue'
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
  created() {
    this.id = this.$route.params.id;
    this.thread = this.$store.getters['threads/getThreadById'](this.id);
    this.posts = this.$store.getters['posts/getPosts'](this.id);
  },
};
</script>

<style lang="scss" scoped>
h1 {
  color: $primaryColor;
}

li {
  list-style-type: none;
}
</style>
