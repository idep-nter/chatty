<template>
  <li>
    <v-row class="mt-1" @click="enterUserProfile">
      <v-col cols="1">
        <v-row class="num justify-center" no-gutters>{{ number }}</v-row>
      </v-col>
      <v-col cols="5" class="justify-center">
        <v-row>
          <v-card
            class="portrait ml-5 mr-2 img"
            :img="user.image"
            height="40"
            width="40"
          ></v-card>
          <p class="mt-3 ml-2">{{ user.username }}</p>
        </v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="1" class="mr-5">
        <v-row>
          <v-icon class="mb-1 mr-2" color="green" medium> mdi-account </v-icon>
          <p class="justify-left mt-3" no-gutters>Online</p>
        </v-row>
      </v-col>
      <!-- <v-col cols="1" class="mr-5">
        <v-row>
          <v-icon class="mb-1 mr-2" color="red" medium> mdi-account </v-icon>
          <p class="justify-left mt-3" no-gutters>Offline</p>
        </v-row>
      </v-col> -->
    </v-row>
  </li>
</template>

<script>
export default {
  props: ['id', 'number'],
  data() {
    return {
      user: '',
    };
  },
  computed: {},
  methods: {
    enterUserProfile() {
      this.$router.push({ path: `/users/${this.id}` });
    },
  },
  created() {
    this.user = this.$store.getters['users/getUserInfo'](this.id);
  },
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
// .icon {
//   padding-right: 0px;
// }
</style>
