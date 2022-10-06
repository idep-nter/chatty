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
      name: "",
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      description: "",
      descriptionRules: [
        (v) =>
          (v && v.length <= 200) || "Name must be less than 200 characters",
      ],
      hasData: false,
    };
  },
  // watch: {
  //   name(value) {
  //     if (this.name) {
  //       this.$emit('input-check', true);
  //     } else {
  //       this.$emit('input-check', false);
  //     }
  //   },
  //   description(value) {
  //     if (this.description) {
  //       this.$emit('input-check', true);
  //     } else {
  //       this.$emit('input-check', false);
  //     }
  //   },
  // },
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        const category = this.categories.find(
          (cat) => cat.name === this.category
        );
        const formData = {
          id: this.id,
          name: this.name,
          category: category.id,
          image: this.image,
          price: this.price,
          important: this.important,
          link: this.link,
          description: this.description,
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
