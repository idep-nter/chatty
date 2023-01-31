<template>
  <li>
    <v-row class="mt-1" @click="enterThread">
      <v-col cols="1">
        <v-row class="num justify-center" no-gutters>{{ number }}</v-row>
      </v-col>
      <!-- <v-divider vertical 
      ></v-divider> -->
      <v-col cols="8">
        <v-row no-gutters class="justify-left">{{ title }}</v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="3" class="pl-0 pr-0">
        <v-row class="justify-rigth" v-if="lastPost">
          <!-- <v-divider vertical 
      ></v-divider> -->
          <v-card
            class="portrait ml-5 mr-2 img"
            :img="image"
            height="40"
            width="40"
          ></v-card>
          <p class="mr-10">
            Last updated
            <i>{{ lastUpdated }}</i>
            <br />
            by
            <i>{{ updatedBy }}</i>
          </p>
        </v-row>
        <v-row v-else></v-row>
      </v-col>
    </v-row>

    <!-- <v-divider></v-divider> -->
  </li>
</template>

<script>
import { formatDate } from '~/helperFunctions';

export default {
  props: ['id', 'number', 'title'],
  data() {
    return {
      lastPost: '',
    }
  },
  computed: {
    lastUpdated() {
      return formatDate(this.lastPost.updatedAt)
    },
    updatedBy() {
      return this.$store.getters['users/getUserInfo'](this.lastPost.author).username;
    },
    image() {
      return this.$store.getters['users/getUserInfo'](this.lastPost.author).image
    }
  },
  methods: {
    enterThread() {
      this.$router.push({ path: `/threads/${this.id}` });
    },
  },
  created() {
    this.lastPost = this.$store.getters['threads/getThreadPosts'](String(this.id))[0]
  }
};
</script>

<style lang="scss" scoped>
.num {
  font-weight: bold;
}
.img {
  margin-top: 5px;
}
li {
  height: 50px;
}
li:hover {
  background-color: $secondaryColor;
  cursor: pointer;
}
</style>
