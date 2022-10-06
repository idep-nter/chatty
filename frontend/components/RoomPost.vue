<template>
  <li>
    <v-row class="mt-1">
      <v-col cols="1">
        <v-row class="pb-3" justify="center">
          <v-card
            class="portrait ml-5 mr-2 img"
            :img="image"
            height="40"
            width="40"
          ></v-card>
          <div id="author">
            <p>{{ author }}</p>
          </div>
        </v-row>
      </v-col>
      <v-col cols="9">
        <v-row justify="left">{{ content }}</v-row>
      </v-col>
      <v-spacer></v-spacer>

      <v-col cols="2">
        <v-row justify="left">
          <p>
            {{ created }}
          </p>
        </v-row>
      </v-col>
    </v-row>
    <v-divider></v-divider>
  </li>
</template>

<script>
export default {
  props: ['id', 'author', 'content', 'created'],
  data() {
    return {
      image: 'https://placekitten.com/600/600',
    };
  },
};
</script>

<style lang="scss" scoped>
li {
  min-height: 100px;
}

#author {
  margin-left: 10px;
}
</style>
