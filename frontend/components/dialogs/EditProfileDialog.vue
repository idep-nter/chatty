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
      <h1>
        Edit Profile
      </h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="username"
          :rules="usrModeRules"
          :counter="showCounter"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="name"
          :rules="nameRules"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-textarea
          v-model="aboutme"
          label="About me"
          :rules="aboutmeRules"
          :counter="200"
          required
        ></v-textarea>

        <v-text-field
          autocomplete="current-password"
          :value="password"
          label="Current password"
          :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          :rules="pswModeRules"
          @input="(_) => (password = _)"
        ></v-text-field>


        <v-container>
          <v-container class="mt-8 justify-center d-flex">
            <v-btn
              color="primary"
              :small="buttonSize"
              :disabled="!valid"
              class="mr-4"
              @click="submitForm"
            >
              Edit
            </v-btn>
          </v-container>

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
          thread: this.thread,
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
