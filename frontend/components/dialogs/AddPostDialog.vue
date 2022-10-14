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
          :counter="999"
          required
        ></v-textarea>

        <v-container class="mt-8 justify-center d-flex buttons">
          <v-btn
            color="primary"
            :small="buttonSize"
            class="mr-4"
            @click="closeDialog"
          >
            Close
          </v-btn>
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
  emits: ['close-dialog'],
  data() {
    return {
      valid: true,
      post: '',
      postRules: [
        (v) => !!v || 'Message is required',
        (v) =>
          (v && v.length <= 999) || 'Message must be less than 999 characters',
      ],
      data: false,
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
          post: this.post,
        };
        this.$emit('save-data', formData);
      }
    },
    closeDialog() {
      this.valid = true;
      this.post = '';
      this.$refs.form.resetValidation();
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
