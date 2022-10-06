<template>
  <div>
    <v-row class="mt-12 mainRow d-flex justify-center">
      <v-col md="8" sm="7">
        <v-card max-width="1400" height="650" class="pa-2 itemCard">
          <v-container class="d-flex justify-center mb-5"><h1>{{ room.title }}</h1></v-container>          
          <room-post
            v-for="post in posts"
            :key="post.id"
            :id="post.id"
            :author="post.author"
            :content="post.content"
            :created="post.created"
          >
          </room-post>
        </v-card>
        <v-pagination
          id="pagination"
          class="mt-8"
          color="primary"
        ></v-pagination>
      </v-col>

      <v-container class="justify-center d-flex">
        <v-btn class="mr-5" color="primary">Refresh</v-btn>
        <v-dialog v-model="addPostDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary">Add message</v-btn>
          </template>
          <add-post-dialog></add-post-dialog>
        </v-dialog>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import AddPostDialog from '~/components/dialogs/AddPostDialog.vue';
import RoomPost from '~/components/RoomPost.vue';

export default {
  components: { AddPostDialog, RoomPost },
  data() {
    return {
      addPostDialog: false,
      id: null,
      room: null,
      posts: [],
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.room = this.$store.getters['rooms/getRoomById'](this.id);
    this.posts = this.$store.getters['posts/getPosts'](this.id);
    console.log(this.posts)
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
