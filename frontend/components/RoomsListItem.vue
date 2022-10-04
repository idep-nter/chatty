<template>
  <li>
    <v-row class="mt-1" @click="enterRoom">
      <v-col cols="1">
        <v-row class="num" no-gutters justify="center">{{ number }}</v-row>
      </v-col>
      <!-- <v-divider vertical 
      ></v-divider> -->
      <v-col cols="6">
        <v-row no-gutters justify="left">{{ title }}</v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="3">
        <v-row justify="right">
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
      </v-col>
    </v-row>
    <!-- <v-divider></v-divider> -->
  </li>
</template>

<script>
export default {
  props: ['id', 'number', 'title', 'image', 'lastUpdated', 'updatedBy'],
  methods: {
    enterRoom() {
      this.$router.push({ path: `/rooms/${this.id}` });
    }
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
