<template>
  <v-card>
    <v-container>
      <h2>Description</h2>
        <p>{{ info.description }}</p>
      <v-container class="mt-8 justify-center d-flex buttons">
        <v-btn color="primary" class="mr-4" @click="closeDialog"> Close </v-btn>
      </v-container>
    </v-container>
  </v-card>
</template>

<script>
export default {
  emits: ['close-dialog'],
  props: ['info'],
  data() {
    return {};
  },
  methods: {
    closeDialog() {
      this.$emit('close-dialog');
    },
  },
  computed: {
    buttonSize() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          return true;
        default:
          return false;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
h2 {
  text-align: center;
  margin-bottom: 10px;
  color: $primaryColor;
}
p {
  color: $primaryColor;
  text-align: center;
}
/* Smartphones */
/* @media (max-width: 767px) {
  .formCard {
    margin-top: 0px !important;
  }
  .buttons {
    padding-bottom: 50px !important;
  }
} */
</style>
