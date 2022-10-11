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
      <h1>Create Thread</h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="name"
          :rules="nameRules"
          :counter="15"
          label="Title"
          required
        ></v-text-field>

        <v-text-field
          v-model="description"
          :rules="descriptionRules"
          label="Description"
          :counter="50"
        ></v-text-field>

        <v-container class="mt-8 justify-center d-flex buttons">
          <v-btn
            color="primary"
            :small="buttonSize"
            :disabled="!valid"
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
  emits: ['close-dialog', 'save-data'],
  data() {
    return {
      valid: true,
      name: '',
      nameRules: [
        (v) => !!v || 'Name is required',
        (v) => (v && v.length <= 20) || 'Name must be less than 20 characters',
      ],
      description: '',
      descriptionRules: [
        (v) =>
          (v && v.length <= 200) || 'Name must be less than 200 characters',
      ],
    };
  },
  methods: {
    submitForm() {
      // if (this.$refs.form.validate()) {
      //   const formData = {
      //     name: this.name,
      //     description: this.description,
      //   };
      //   this.$emit("save-data", formData);
      // }
    },
    closeDialog() {
      this.$emit('close-dialog');
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
