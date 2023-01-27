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
      <h1>Edit Profile</h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          :counter="20"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="firstName"
          :rules="nameRules"
          :counter="30"
          label="First name"
          required
        ></v-text-field>

        <v-text-field
          v-model="lastName"
          :rules="nameRules"
          :counter="30"
          label="Last name"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          v-model="image"
          :rules="imageRules"
          label="Image URL"
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
          :value="enteredPassword"
          label="Current password"
          :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          @input="(_) => (password = _)"
        ></v-text-field>

        <v-container>
          <v-container class="mt-8 justify-center d-flex">
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
  emits: ['close-dialog'],
  props: ['user-info'],
  data() {
    return {
      valid: true,
      value: true,
      enteredPassword: '',
      loadedPassword: this.userInfo.password,
      username: this.userInfo.username,
      usernameRules: [
        (v) => !!v || 'Username is required!',
        (v) =>
          (v && v.length <= 20) || 'Username must be less than 20 characters!',
      ],
      firstName: this.userInfo.firstName,
      lastName: this.userInfo.lastName,
      nameRules: [
        (v) => !!v || 'Name is required!',
        (v) => (v && v.length <= 30) || 'Name must be less than 30 characters!',
      ],
      image: this.userInfo.image,
      imageRules: [
        (v) =>
          /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)/.test(
            v
          ) || 'Must be a valid URL',
      ],
      email: this.userInfo.email,
      emailRules: [
        (v) => !!v || 'E-mail is required!',
        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid!',
      ],
      aboutme: this.userInfo.aboutme,
      aboutmeRules: [
        (v) =>
          (v && v.length <= 200) || 'Name must be less than 200 characters',
      ],
      errorMessage: '',
    };
  },
  methods: {
    submitForm() {
      if (
        this.$refs.form.validate() 
        // && this.enteredPassword === this.loadedPassword
      ) {
        const formData = {
          id: this.userInfo.id,
          password: this.userInfo.password,
          username: this.username,
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          image: this.image,
          aboutme: this.aboutme,
        };
        this.$store.dispatch('users/editUser', formData);

        if (this.showError) {
        this.errorMessage = 'Failed to update profile info! Check input data.';
        return;
      }
      }
    },
    closeDialog() {
      this.valid = true;
      this.$refs.form.resetValidation();
      this.enteredPassword = '';
      this.loadedPassword = this.userInfo.password;
      this.username = this.userInfo.username;
      this.email = this.userInfo.email;
      this.image = this.userInfo.image;
      this.aboutme = this.userInfo.aboutme;
      this.$emit('close-dialog');
    },
  },
  created() {
    console.log(this.userInfo)
    console.log(this.userInfo.password)
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
