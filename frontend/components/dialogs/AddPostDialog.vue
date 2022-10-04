<template>
  <v-card>
    <v-container>
      <v-alert
        dense
        outlined
        type="error"
        v-if="errorMessage"
        class="justify-center mx-auto mt-15 logAlert"
        max-width="500"
      >
        {{ errorMessage }}
      </v-alert>
      <h1>Add a post</h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-textarea
          v-model="post"
          :rules="postRules"
          :counter="200"
          required
        ></v-textarea>

        <v-container class="mt-8 justify-center d-flex buttons">
          <v-btn
            color="primary"
            :small="buttonSize"
            :disabled="!valid"
            class="mr-4"
            @click="submitForm"
          >
            Submit
          </v-btn>
        </v-container>
      </v-form>
    </v-container>
  </v-card>
</template>

<script>
export default {
  // emits: ['input-check'],
  data() {
    return {
      valid: true,
      post: "",
      postRules: [
        (v) => !!v || "Message is required",
        (v) => (v && v.length <= 200) || "Message must be less than 200 characters",
      ],
      // hasData: false,
    };
  },
  // watch: {
  //   post(value) {
  //     if (this.post) {
  //       this.$emit('input-check', true);
  //     } else {
  //       this.$emit('input-check', false);
  //     }
  //   },
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        const formData = {
          id: this.id,
          author: this.name,
          room: this.room,
          content: this.post,
          created: this.created,
        };
        this.$emit("save-data", formData);
      }
    },
  },
  // computed: {
  //   buttonSize() {
  //     switch (this.$vuetify.breakpoint.name) {
  //       case 'xs':
  //         return true;
  //       default:
  //         return false;
  //     }
  //   },
  // },
};
</script>

<style lang="scss" scoped>
h1 {
  display: flex;
  justify-content: center;
  color: $primaryColor;
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
