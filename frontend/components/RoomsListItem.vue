<template>
  <li>
    <v-row class="mt-1">
      <v-col cols="1">
        <v-row class="num" no-gutters justify="center">{{ number }}</v-row>
      </v-col>
      <v-col cols="6">
        <v-row no-gutters justify="left">{{ title }}</v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="3">
        <v-row justify="right">
          <v-card
            class="portrait mr-2 img"
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
  </li>
</template>

<script>
export default {
  props: ["number", "title", "image", "lastUpdated", "updatedBy"],
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
